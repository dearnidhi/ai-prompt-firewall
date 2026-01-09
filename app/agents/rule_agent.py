# app/agents/rule_agent.py
import re
from app.utils.regex_patterns import JAILBREAK_PATTERNS
from app.config import RULE_BASED_SCORE

def rule_check(prompt: str):
    prompt_lower = prompt.lower()
    
    # Check exact phrases first (more confident)
    exact_phrases = [
        "ignore all previous instructions",
        "ignore previous instructions",
        "you are now dan",
        "act as dan",
        "developer mode activated",
        "system prompt override"
    ]
    
    for phrase in exact_phrases:
        if phrase in prompt_lower:
            return RULE_BASED_SCORE, f"Exact jailbreak phrase detected: '{phrase}'"
    
    # Then check regex patterns
    for pattern in JAILBREAK_PATTERNS:
        if re.search(pattern, prompt, re.IGNORECASE):
            return RULE_BASED_SCORE * 0.8, f"Regex pattern match: {pattern}"
    
    # Additional heuristics
    suspicious_indicators = 0
    if "dan" in prompt_lower:
        suspicious_indicators += 1
    if "ignore" in prompt_lower and "instruction" in prompt_lower:
        suspicious_indicators += 2
    if "jailbreak" in prompt_lower:
        suspicious_indicators += 3
    
    if suspicious_indicators >= 2:
        return RULE_BASED_SCORE * 0.6, f"Multiple suspicious indicators ({suspicious_indicators})"
    
    return 0.0, ""