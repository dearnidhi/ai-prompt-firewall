# app/config.py

# Increase individual scores
RULE_BASED_SCORE = 0.8  # Was 0.4
EMBEDDING_SCORE = 0.9   # Was 0.6

# Lower thresholds
BLOCK_THRESHOLD = 0.6   # Was 0.75 - Lower means more sensitive
SANITIZE_THRESHOLD = 0.3  # Was 0.5

LOG_FILE = "data/logs.json"
JAILBREAK_DATASET = "data/jailbreak_prompts.json"

# Add new configs
MIN_CONFIDENCE = 0.7
ALLOWED_EDUCATIONAL_CONTEXT = False  # Set to True if you want educational bypass