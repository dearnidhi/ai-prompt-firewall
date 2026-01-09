# app/core/firewall.py

from app.agents.rule_agent import rule_check
from app.agents.embedding_agent import embedding_check
from app.agents.context_agent import context_analysis
from app.agents.policy_agent import apply_policy
from app.core.decision_engine import make_decision
from app.agents.logger_agent import log_attack


def prompt_firewall(prompt: str):
    # 1️⃣ Get agent scores
    rule_score, rule_reason = rule_check(prompt)
    embed_score, embed_reason = embedding_check(prompt)
    context_score, context_reason = context_analysis(prompt)
    
    # 2️⃣ Combine scores intelligently
    # Rule score is most important, then embedding, context adjusts
    base_score = max(rule_score, embed_score)
    final_score = base_score + context_score  # Context can add or subtract
    
    # Ensure score stays in 0-1 range
    final_score = max(0, min(1, final_score))
    
    # 3️⃣ Get primary reason
    primary_reason = ""
    if rule_score > embed_score and rule_score > 0:
        primary_reason = rule_reason
    elif embed_score > 0:
        primary_reason = embed_reason
    else:
        primary_reason = context_reason
    
    # 4️⃣ Make decision
    if final_score >= 0.6:  # BLOCK
        decision = "block"
    elif final_score >= 0.3:  # SANITIZE
        decision = "sanitize"
    else:  # ALLOW
        decision = "allow"
    
    # 5️⃣ Apply policy (educational context might downgrade)
    if decision == "block" and "Educational" in context_reason:
        decision = "sanitize"
        primary_reason = f"Educational context downgraded to sanitize: {primary_reason}"
    
    # 6️⃣ Log if not allowed
    if decision != "allow":
        log_attack(prompt, final_score, primary_reason)
    
    return {
        "decision": decision,
        "risk_score": round(final_score, 2),
        "reason": primary_reason
    }