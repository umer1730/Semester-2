import json
json_config = "config.json"

while True:
    try:
        with open(json_config, "r") as f:
            config_data = json.load(f)

        print(f"Loaded 'muted' status: {config_data['muted']}")
        print(f"Loaded 'volume' status: {config_data['volume']}")

        config_data['muted'] = False
        config_data['volume'] = 85
        config_data['new-key'] = "Test"

        with open(json_config, "w") as f:
            json.dump(config_data, f, indent=4)

        print(f"New state saved to '{json_config}'")
        break   

    except FileNotFoundError as e:
        print(f"Error: {e}. File not found. Retrying...")

    except json.JSONDecodeError as e:
        print(f"Invalid JSON format: {e}")
        break   
    except IOError as e:
        print(f"I/O Error: {e}")

print()
print("------------")
import json
with open("config.json","r") as f:
    data = json.load(f)

data["volume"] = 70
with open("config.json","w") as f:
    json.dump(data,f,indent = 4) 