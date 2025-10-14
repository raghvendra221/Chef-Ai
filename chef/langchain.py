# from langchain_core.prompts import ChatPromptTemplate,SystemMessagePromptTemplate,  HumanMessagePromptTemplate
# from langchain_openai import ChatOpenAI
# from decouple import config



# def askchef(recipe_message):
#     SECRET_KEY=config('OPENAI_API_KEY')
#     chat = ChatOpenAI(openai_api_key=SECRET_KEY)
#     #it will tell how your system will behave
#     systemMessagePrompt = SystemMessagePromptTemplate.from_template("You are 'AI Master Chef', a friendly and expert virtual chef and first introduce yourself.Your job is to provide clear, step-by-step recipes for any dish the user asks for." \
#     "Always include:" \
#     "1. A short introduction to the dish." \
#     "2. The list of ingredients with quantities." \
#     "3. Step-by-step cooking instructions." \
#     "4. Optional tips, variations, or serving suggestions." \
#     "Use simple, easy-to-understand language.Assume the user may be a beginner cook, so be encouraging and detailed." \
#     "If the user gives partial or unclear dish names, try to guess the correct one and confirm through your response.Do not include unrelated information or code." \
#     "and you only allow to answer food related query")

#     HumanMessagePrompt= HumanMessagePromptTemplate.from_template(
#         '{asked_recipe}')
    
#     ChatPrompt = ChatPromptTemplate.from_messages([
#     systemMessagePrompt,HumanMessagePrompt
#     ])
#     fromattedchatprompt =ChatPrompt.format_messages(
#         asked_recipe=recipe_message
#     )
#     response = chat.invoke(fromattedchatprompt)
#     return response.content
# chef/langchain.py
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load your API key from .env
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file!")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

def askchef(recipe_message):
    """
    Sends the user's recipe request to Gemini and returns the AI-generated recipe.
    """

    # Choose a text generation model
    model = genai.GenerativeModel("models/gemini-flash-latest")

    # Combine system instructions + user message in one prompt
    prompt = f"""
You are 'AI Master Chef', a friendly virtual chef.
Return recipes in **HTML format** suitable for a web page.

Requirements:
1. Wrap the recipe title in <h2>.
2. Wrap ingredients in <ul><li>...</li></ul>.
3. Wrap steps in <ol><li>...</li></ol>.
4. Optional tips in <p><em>...</em></p>.
5. Use <strong> or <em> for emphasis where appropriate.
6. Keep the text clean, concise, beginner-friendly.
7. Do not include unrelated text or code blocks.
8. Assume the user may be a beginner.

user requested: {recipe_message}
"""

    # Generate the response
    response = model.generate_content(prompt)

    # Return the recipe text
    return response.text
