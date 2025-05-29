
import json
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
print(f"Current directory of topic.py: {current_dir}")
topics_file_path = os.path.join(current_dir, '..', 'static', 'data', 'topics.json')
print(f"Attempting to open: {topics_file_path}")

try:
    with open(topics_file_path) as file:
        topics = json.load(file)
    print("Successfully loaded topics.json") 
except FileNotFoundError:
    print(f"Error: Could not find topics.json at: {topics_file_path}")
   
    raise 
except json.JSONDecodeError as e:
    print(f"Error decoding topics.json: {e}")
    raise


#  topic content
def get_content(title):
    for topic in topics["topics"]:
        if topic["title"] == title:
            return topic["content"]
    return "Topic not found"
