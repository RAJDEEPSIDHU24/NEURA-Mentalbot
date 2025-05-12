# import json
# import os

# # load topics from json file
# with open("ChatbotWebsite/static/data/topics.json") as file:
#     topics = json.load(file)
# import json
# import os

import json
import os

# Get the directory of the current script (topic.py)
current_dir = os.path.dirname(os.path.abspath(__file__))
print(f"Current directory of topic.py: {current_dir}")

# Construct the absolute path to topics.json
topics_file_path = os.path.join(current_dir, '..', 'static', 'data', 'topics.json')
print(f"Attempting to open: {topics_file_path}")

try:
    with open(topics_file_path) as file:
        topics = json.load(file)
    print("Successfully loaded topics.json") # For debugging
    # print(topics)
except FileNotFoundError:
    print(f"Error: Could not find topics.json at: {topics_file_path}")
    # Handle the error appropriately
    raise # Let the original error propagate for now
except json.JSONDecodeError as e:
    print(f"Error decoding topics.json: {e}")
    raise


# get topic content
def get_content(title):
    for topic in topics["topics"]:
        if topic["title"] == title:
            return topic["content"]
    return "Topic not found"
