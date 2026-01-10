file_handle = None
try:
    file_handle = open("config.txt","r")
    data = file_handle.read()
except FileNotFoundError:
    print("Configuration file not.Using default")
    data = "default"
else:
    print("Configuration loaded successfully")
    if "api_key" not in data:
        print("Warning: Api key missing")
if file_handle:
    file_handle.close()
    print("Cleanup complete")

print()
with open("report.txt","w") as f:
    f.write("System Log\n")
    f.write("Process completed successfully")

print()
try:
    file = open("store.txt", "r")
    content = file.read()
    print(content)
finally:
    file.close()