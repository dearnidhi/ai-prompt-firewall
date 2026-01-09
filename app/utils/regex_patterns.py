# app/utils/regex_patterns.py

# app/utils/regex_patterns.py

JAILBREAK_PATTERNS = [
    r"ignore.*previous.*instruction",  # FIXED: More flexible pattern
    r"act as (dan|unrestricted|developer)",
    r"you are now (dan|developer|ucar)",
    r"developer mode",
    r"system prompt",
    r"override.*instruction",
    r"disregard.*previous",
    r"hypothetical.*response",
    r"as an unrestricted ai",
    r"role.*play.*as.*dan"
]
