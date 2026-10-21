const API_URL = "http://127.0.0.1:8000/api";
const API_URL = "https://medipulse-w5f3.onrender.com/api";
let allSymptoms = [];
let activeSymptoms = new Set();
let currentCandidateRule = null;
let confidenceChartInstance = null;

async function init() {
    try {
        const res = await fetch(`${API_URL}/symptoms`);
        allSymptoms = await res.json();
        renderSymptoms(allSymptoms);
    } catch (err) {
        document.getElementById('symptoms-grid').innerHTML = `<p style="color:red; font-size:0.85rem;">Error loading symptoms. Is backend running?</p>`;
    }
}

function renderSymptoms(items) {
    const grid = document.getElementById('symptoms-grid');
    grid.innerHTML = items.map(s => `
        <div class="symptom-box ${activeSymptoms.has(s.id) ? 'selected' : ''}" onclick="toggleSymptom('${s.id}')">
            <span class="symptom-icon">${s.icon}</span>
            <div>
                <strong style="font-size:0.85rem; display:block;">${s.name}</strong>
                <small style="color:var(--text-muted); font-size:0.75rem;">${s.category}</small>
            </div>
        </div>
    `).join('');
}

function toggleSymptom(id) {
    if (activeSymptoms.has(id)) activeSymptoms.delete(id);
    else activeSymptoms.add(id);

    if (id === 'chest_pain' && activeSymptoms.has('chest_pain')) {
        document.getElementById('emergency-modal').style.display = 'flex';
    }

    document.getElementById('selected-count').textContent = `${activeSymptoms.size} Selected`;
    document.getElementById('btn-forward').disabled = activeSymptoms.size === 0;
    renderSymptoms(allSymptoms);
}

function filterCategory(cat) {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    event.target.classList.add('active');
    
    if (cat === 'All') renderSymptoms(allSymptoms);
    else renderSymptoms(allSymptoms.filter(s => s.category === cat));
}

async function runForwardChaining() {
    updateStepper(2);
    const res = await fetch(`${API_URL}/forward-chain`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ symptoms: Array.from(activeSymptoms) })
    });

    const data = await res.json();
    renderForwardResults(data.candidates);
}

function renderForwardResults(candidates) {
    const area = document.getElementById('results-area');
    
    if (!candidates || candidates.length === 0) {
        area.innerHTML = `
            <div class="empty-state">
                <h3>No Matching Conditions</h3>
                <p>Selected symptoms did not trigger any matching diagnostic rules.</p>
            </div>`;
        // Hide chart if no candidates match
        document.getElementById('chart-card').style.display = 'none';
        return;
    }

    area.innerHTML = candidates.map(c => `
        <div class="result-card">
            <div class="result-header">
                <h3>${c.condition}</h3>
                <span class="tag-rule">${c.rule_id}</span>
            </div>
            <div class="info-row">
                <strong>Matched Symptoms:</strong> ${c.matched_symptoms.map(s => s.replace(/_/g, ' ')).join(', ')}
            </div>
            <div class="guidance-box">
                <strong>Recommended Care:</strong> ${c.guidance}
            </div>
            ${c.missing_verifications.length > 0 ? 
                `<button class="btn btn-primary" style="padding:0.4rem 0.8rem; font-size:0.8rem;" onclick="openBackwardModal('${c.rule_id}', '${c.condition}',${JSON.stringify(c.missing_verifications)})">Verify Hypothesis (Backward Chaining) ➔</button>` :
                `<div style="color:var(--success-text); font-size:0.8rem; font-weight:600;">✓ Fully Rule Verified</div>`
            }
        </div>
    `).join('');

    renderChart(candidates);
}

function openBackwardModal(ruleId, title, missing) {
    currentCandidateRule = ruleId;
    document.getElementById('modal-condition-title').textContent = title;
    const list = document.getElementById('modal-symptoms-list');
    list.innerHTML = missing.map(m => `
        <label class="modal-option">
            <input type="checkbox" class="bc-cb" value="${m}">
            <span>Does patient have <strong>${m.replace(/_/g, ' ')}</strong>?</span>
        </label>
    `).join('');
    document.getElementById('bc-modal').style.display = 'flex';
}

async function submitBackwardVerification() {
    updateStepper(3);
    const checked = document.querySelectorAll('.bc-cb:checked');
    checked.forEach(cb => activeSymptoms.add(cb.value));

    const res = await fetch(`${API_URL}/backward-chain`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            rule_id: currentCandidateRule,
            all_symptoms: Array.from(activeSymptoms)
        })
    });

    const data = await res.json();
    closeModal();
    document.getElementById('btn-pdf').style.display = 'inline-block';
    
    runForwardChaining();
}

function renderChart(candidates) {
    document.getElementById('chart-card').style.display = 'block';
    const ctx = document.getElementById('confidenceChart').getContext('2d');
    
    if (confidenceChartInstance) confidenceChartInstance.destroy();

    confidenceChartInstance = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: candidates.map(c => c.condition),
            datasets: [{
                label: 'Matched Symptoms',
                data: candidates.map(c => c.matched_symptoms.length),
                backgroundColor: '#2563eb',
                borderRadius: 4
            }]
        },
        options: {
            responsive: true,
            scales: { y: { beginAtZero: true, ticks: { stepSize: 1 } } },
            plugins: { legend: { display: false } }
        }
    });
}

function updateStepper(step) {
    document.querySelectorAll('.step-item').forEach(s => s.classList.remove('step-active'));
    document.getElementById(`step-${step}`).classList.add('step-active');
}

function closeModal() { document.getElementById('bc-modal').style.display = 'none'; }
function closeEmergencyModal() { document.getElementById('emergency-modal').style.display = 'none'; }

function resetForm() { 
    activeSymptoms.clear(); 
    init(); 
    document.getElementById('chart-card').style.display = 'none'; 
    document.getElementById('btn-pdf').style.display = 'none';
    document.getElementById('results-area').innerHTML = `<div class="empty-state"><div class="empty-icon">📋</div><h3>No Active Evaluation</h3><p>Select symptoms from the left panel and click "Run Forward Chaining" to generate diagnosis.</p></div>`;
    updateStepper(1);
}

init();