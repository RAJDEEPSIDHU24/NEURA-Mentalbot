import cohere
import os
 # to get the responses i used cohere intergrated into this chatbot 

# SO i initialize the Cohere client with my API key from the environment variable 
co = cohere.Client(os.environ.get("COHERE_API_KEY"))
# cohere api key is needed  when we want to use its model or other ai services in our project 
def get_response(message, conversation_history=None):
    try:
        prompt = message
        if conversation_history:
            prompt = "\n".join(conversation_history) + "\nUser: " + message + "\nBot:"

        response = co.generate(
            model='command-light',  
            # there are different models of cohere like command r, command r+ , embed  command light is flexible and cheaper version
            #faster responses
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