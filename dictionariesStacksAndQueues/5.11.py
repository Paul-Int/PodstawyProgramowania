import json
import os

filename = "voting.json"

# Read the contents of the json file (or create empty if missing)
if os.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as f:
        try:
            votes = json.load(f)
        except json.JSONDecodeError:
            votes = {}
else:
    votes = {}

# Vote for a person
person_name = input("Name of the person you are voting for: ").strip()

if person_name != "":
    if person_name in votes:
        votes[person_name] += 1
    else:
        votes[person_name] = 1

# Save voting data to json file
with open(filename, "w", encoding="utf-8") as f:
    json.dump(votes, f, ensure_ascii=False, indent=2)

print("Current results:", votes)