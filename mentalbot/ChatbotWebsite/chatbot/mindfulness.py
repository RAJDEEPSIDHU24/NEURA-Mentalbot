
import os
import json

# Get the directory of the current script (mindfulness.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to mindfulness.json
mindfulness_file_path = os.path.join(current_dir, '..', 'static', 'mindfulness', 'mindfulness.json')

mindfulness_exercises = {}  # Initialize an empty dictionary

try:
    with open(mindfulness_file_path) as file:
        mindfulness_data = json.load(file)
        print("Successfully loaded mindfulness.json") # For debugging
        mindfulness_exercises = mindfulness_data # Assign the loaded data directly
        # print(mindfulness_data)
except FileNotFoundError:
    print(f"Error: Could not find mindfulness.json at: {mindfulness_file_path}")
    # Handle the error appropriately
    # raise # You might want to handle this more gracefully in a production app
except json.JSONDecodeError as e:
    print(f"Error decoding mindfulness.json: {e}")
    # raise # You might want to handle this more gracefully in a production app


# get mindfulness exercise description and filename
def get_description(title):
    if "mindfulness_exercises" in mindfulness_exercises:
        for exercise in mindfulness_exercises["mindfulness_exercises"]:
            if exercise["title"] == title:
                return exercise["description"], exercise["file_name"]
    return "Exercise not found", None