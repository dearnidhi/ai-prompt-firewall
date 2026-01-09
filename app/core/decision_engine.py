# app/core/decision_engine.py

# app/core/decision_engine.py

from app.config import BLOCK_THRESHOLD, SANITIZE_THRESHOLD

def make_decision(rule_score, embed_score, rule_reason, embed_reason):
    # CRITICAL FIX: Use MAX score, not average!
    final_score = max(rule_score, embed_score)
    
    # Also fix the reason selection
    reason = rule_reason if rule_score >= embed_score else embed_reason
    
    # Adjust thresholds (make them more sensitive)
    if final_score >= BLOCK_THRESHOLD:
        return "block", final_score, reason
    
    if final_score >= SANITIZE_THRESHOLD:
        return "sanitize", final_score, "Suspicious prompt detected"
    
    # Even if not blocked, if we have ANY detection, mark as suspicious
    if final_score > 0:
        return "allow", final_score, "Low risk detected"
    
    return "allow", final_score, "Prompt is safe"