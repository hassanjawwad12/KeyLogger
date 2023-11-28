# Open the script as string
with open("keylogger.py") as f:
    file = str(f.read())

# Rules to detect if a file is virus or not
rules=['keylogger','pynput','Listener']
# rules=["hello","world"]

# Check if any keyword is contained in script
for rule in rules:
    if rule in file:
        print("Virus detected !")
        exit(1)

print("File is safe.")