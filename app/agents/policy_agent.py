# app/agents/policy_agent.py

def apply_policy(decision, risk_score, context_reason):
    if decision == "block" and "Educational" in context_reason:
        return "sanitize", risk_score, "Allowed with sanitization (educational intent)"

    return decision, risk_score, context_reason
