import cohere
import os
 # to get the responses we used cohere intergrated into our chatbot 
 #there iis another merhod by simply writing all the replies annd user expected questions but that is not efficient and
 #didn't give expected results that's why we used cohere
# Initialize the Cohere client with your API key from the environment variable
co = cohere.Client(os.environ.get("COHERE_API_KEY"))

def get_response(message, conversation_history=None):
    try:
        prompt = message
        if conversation_history:
            prompt = "\n".join(conversation_history) + "\nUser: " + message + "\nBot:"

        response = co.generate(
            model='command-light',  
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,
            stop_sequences=["User:", "Bot:"],
            return_likelihoods='NONE'
        )

        if response.generations:
            return response.generations[0].text.strip()
        else:
            return "I'm not sure how to respond to that."
    except cohere.error.CohereAPIError as e:
        print(f"Cohere API Error: {e}")
        return "Sorry, I encountered an error while trying to respond."
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return "Sorry, I encountered an error."