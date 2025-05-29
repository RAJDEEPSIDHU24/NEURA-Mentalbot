from ChatbotWebsite import create_app
from dotenv import load_dotenv
load_dotenv()

# Create the app
app = create_app()

# Run the app
if __name__ == '__main__':
    app.run()
