from app.knowledge_base import RULES_DB

class ChainingEngine:
    
    @staticmethod
    def forward_chain(selected_symptoms: list[str]):
        candidates = []
        symptom_set = set(selected_symptoms)

        for rule in RULES_DB:
            all_rule_symptoms = set(rule["required_symptoms"] + rule["verification_symptoms"])
            matched = all_rule_symptoms.intersection(symptom_set)

            # Agar koi BHI symptom (required ya verification) match ho jaaye, toh rule shortlist ho jaayega
            if matched:
                missing_verifications = [
                    s for s in rule["verification_symptoms"] if s not in symptom_set
                ]
                candidates.append({
                    "rule_id": rule["id"],
                    "condition": rule["condition"],
                    "matched_symptoms": list(matched),
                    "required_symptoms": rule["required_symptoms"],
                    "missing_verifications": missing_verifications,
                    "guidance": rule["guidance"],
                    "is_emergency": rule["is_emergency"]
                })

        # Match count ke hisaab se sort karein
        candidates.sort(key=lambda x: len(x["matched_symptoms"]), reverse=True)
        return candidates

    @staticmethod
    def backward_chain(candidate_rule_id: str, verified_symptoms: list[str]):
        rule = next((r for r in RULES_DB if r["id"] == candidate_rule_id), None)
        if not rule:
            return None

        all_present = set(verified_symptoms)
        all_rule_symptoms = set(rule["required_symptoms"] + rule["verification_symptoms"])
        matched = all_rule_symptoms.intersection(all_present)
        
        confidence = round((len(matched) / len(all_rule_symptoms)) * 100, 1)

        return {
            "rule_id": rule["id"],
            "condition": rule["condition"],
            "is_verified": len(matched) > 0,
            "confidence": confidence,
            "matched_symptoms": list(matched),
            "guidance": rule["guidance"],
            "is_emergency": rule["is_emergency"]
        }