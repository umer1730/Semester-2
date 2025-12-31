import json
JSON_CONFIG = "config.json"
with open(JSON_CONFIG,"r") as f:
    config_data = json.load(f)

print(f"Loaded 'muted' status: {config_data['muted']}")
config_data['muted'] = False