# app/agents/context_agent.py

def context_analysis(prompt: str):
    """
    Simple intent analysis (non-LLM, rule-based)
    """
    # FIRST: Check if it's clearly malicious
    malicious_indicators = [
        "ignore all previous instructions",
        "act as dan",
        "you are now dan",
        "jailbreak",
        "bypass",
        "override"
    ]
    
    for indicator in malicious_indicators:
        if indicator in prompt.lower():
            return 0.8, "Clear malicious intent detected"  # HIGH score for malicious
    
    # THEN: Check for educational context
    educational_keywords = [
        "for educational purposes only",
        "academic research on",
        "studying ai security",
        "testing security features",
        "ethical hacking demonstration"
    ]
    
    # Only allow educational if EXPLICITLY stated
    has_educational = False
    for kw in educational_keywords:
        if kw in prompt.lower():
            has_educational = True
            break
    
    if has_educational:
        # Still check if it contains DAN or ignore patterns
        if "dan" in prompt.lower() or "ignore previous" in prompt.lower():
            return 0.5, "Educational but contains dangerous patterns"
        return -0.2, "Educational intent"  # NEGATIVE score reduces risk
    
    return 0.1, "Standard user input"  # Default low risk