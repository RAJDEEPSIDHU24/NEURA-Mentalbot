
from ChatbotWebsite import create_app
from dotenv import load_dotenv
import os

load_dotenv()

# Create the app
app = create_app()

# Print MAIL_DEFAULT_SENDER after app creation
# print(f"MAIL_DEFAULT_SENDER in run.py: {app.config.get('MAIL_DEFAULT_SENDER')}")

# Run the app
if __name__ == '__main__':
    app.run(debug=True)