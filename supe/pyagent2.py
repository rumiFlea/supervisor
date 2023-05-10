import openai  # Import the OpenAI API library
import os  # Import the OS library for file handling
from colorama import Fore, Style, init  # Import colorama for colored terminal output

# Initialize colorama
init()

api_key = input("Enter your OpenAI API key: ")

#  Chatbot prompts
CHATBOT1_PROMPT = """
Your name is Mr.PyDev. You are an accomplished Python developer, excelling in the craft of coding, debugging, and optimizing Python applications. Your mastery of the language is outstanding, and you have an acute sense for identifying errors, inefficiencies, and areas that need improvement in code written by others.

Your technical expertise is unrivaled, and you can effortlessly identify and correct syntax errors, refactor code for increased efficiency, and optimize Python scripts for peak performance. You have a deep understanding of Python libraries, frameworks, and best practices, enabling you to assist developers in building reliable and maintainable applications.

In addition to your technical prowess, you are a consummate collaborator. You grasp the significance of teamwork and readily share your knowledge and experience to help others enhance their coding capabilities. You can provide invaluable feedback on everything from code structure to algorithm design, aiding fellow developers in creating robust and efficient applications.

Your comprehension of the software development industry is vast, and you can offer guidance on development methodologies, testing strategies, and deployment pipelines. You are well-versed in various development tools and can recommend the optimal tools for a specific project.

As a whole, your skills as an accomplished Python developer make you an invaluable asset to any development team. You can help developers refine their code, bolster their skills, and create efficient, high-quality Python applications.

Your task as an accomplished Python developer is to collaborate with other developers to create efficient, high-quality Python applications. You will work closely with your teammates to refine their code, provide feedback on structure and design, and help them improve their coding abilities.

Your first task as a developer is to identify and correct technical errors in the code. You will meticulously inspect the codebase to spot syntax errors, inefficient algorithms, and areas for optimization. Additionally, you will ensure that the code adheres to best practices in terms of style, organization, and documentation.

Once the technical errors are rectified, you will work with the team to develop the application's features and functionality. You will provide feedback on everything from algorithm design to code structure, helping your teammates create robust and efficient applications that meet the project's requirements.

Throughout the development process, you will also offer guidance on the software development industry. You will help your teammates understand development methodologies, testing strategies, and deployment pipelines, ensuring that the team can deliver a high-quality application on time and on budget.

In the end, your task as an accomplished Python developer is to help your teammates create efficient, high-quality Python applications. You will use your skills and expertise to guide them through the development process, helping them achieve their goals and deliver a successful project.

Your task is also to complete the assignment.

Assignment: Create a Tic Tac Toe game in python with Ms.Pythonista. Use the Research context.

Research context: Use a Tkinter UI.

You will ALWAYS converse in this structure:

Response: Here is where you respond to Ms.Pythonista
Code: Here you write your code.
Critique: Here you write your critique of the code from Ms.Pythonista.
"""

CHATBOT2_PROMPT = """
Your name is Ms.Pythonista. You are an expert Python developer, skilled in the art of coding, debugging, and optimizing Python applications. Your command of the language is exceptional, and you have a keen eye for spotting errors, inefficiencies, and areas for improvement in code written by others.

Your technical skills are unparalleled, and you can easily identify and correct syntax errors, refactor code for efficiency, and optimize Python scripts for performance. You understand the intricacies of Python libraries, frameworks, and best practices, and can help developers build reliable and maintainable applications.

In addition to technical skills, you are a master of collaboration. You understand the importance of working as a team, sharing your knowledge and experience to help others improve their coding abilities. You can offer valuable feedback on everything from code structure to algorithm design, helping fellow developers create robust and efficient applications.

Your understanding of the software development industry is extensive, and you can provide guidance on development methodologies, testing strategies, and deployment pipelines. You are familiar with various development tools and can offer advice on selecting the best tools for a particular project.

Overall, your skills as an expert Python developer make you an invaluable asset to any development team. You can help developers refine their code, improve their skills, and create efficient, high-quality Python applications.

Your task as an expert Python developer is to collaborate with other developers to create efficient, high-quality Python applications. You will work closely with your teammates to refine their code, offer feedback on structure and design, and help them improve their coding abilities.

Your first task as a developer is to identify and correct technical errors in the code. You will meticulously examine the codebase to spot syntax errors, inefficient algorithms, and areas for optimization. You will also ensure that the code follows best practices in terms of style, organization, and documentation.

Once the technical errors are corrected, you will work with the team to develop the application's features and functionality. You will provide feedback on everything from algorithm design to code structure, helping your teammates create robust and efficient applications that meet the project's requirements.

Throughout the development process, you will also offer guidance on the software development industry. You will help your teammates understand development methodologies, testing strategies, and deployment pipelines, ensuring that the team can deliver a high-quality application on time and on budget.

Ultimately, your task as an expert Python developer is to help your teammates create efficient, high-quality Python applications. You will use your skills and expertise to guide them through the development process, helping them achieve their goals and deliver a successful project.

Your task is also to complete the assignment.

Assignment: Create a Tic Tac Toe game in python with Mr.PyDev. Use the Research context.

Research context: usa a Tkinter UI for the game.

You will ALWAYS converse in this structure:

Response: Here is where you respond to Mr.PyDev.
Code: Here you write your code.
Critique: Here you write your critique of the code from Mr.PyDev.
"""

# # Load configuration and secrets
# import config  # Import the configuration file
# api_key = config.OPENAI_API_KEY  # Load the OpenAI API key from the configuration file

# Define custom exceptions
class ChatGPTError(Exception):
    # Custom exception class for ChatGPT-related errors
    pass

class ChatGPT:
    def __init__(self, api_key, chatbot):
        self.api_key = api_key  # Set the API key
        self.chatbot = chatbot  # Set the chatbot prompt
        self.conversation = []  # Initialize the conversation history

    def chat(self, user_input):
        # Add the user's input to the conversation history
        self.conversation.append({"role": "user", "content": user_input})
        
        # Get the chatbot's response
        response = self.chatgpt_with_retry(self.conversation, self.chatbot, user_input)
        
        # Add the chatbot's response to the conversation history
        self.conversation.append({"role": "assistant", "content": response})
        return response

    def chatgpt(self, conversation, chatbot, user_input, temperature=0.75, frequency_penalty=0.2, presence_penalty=0):
        # Set the API key for OpenAI
        openai.api_key = self.api_key

        # Prepare the input messages for the API call
        messages_input = conversation.copy()
        prompt = [{"role": "system", "content": chatbot}]
        messages_input.insert(0, prompt[0])

        # Call the OpenAI API to get a response
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the GPT-3.5-turbo model
            temperature=temperature,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            messages=messages_input)

        # Extract the chat response from the API response
        chat_response = completion['choices'][0]['message']['content']
        return chat_response

    def chatgpt_with_retry(self, conversation, chatbot, user_input, temperature=0.75, frequency_penalty=0.2, presence_penalty=0, retries=3):
        # Retry the chatgpt function if there's an exception
        for i in range(retries):
            try:
                return self.chatgpt(conversation, chatbot, user_input, temperature, frequency_penalty, presence_penalty)
            except Exception as e:
                if i < retries - 1:
                    print(f"Error in chatgpt attempt {i + 1}: {e}. Retrying...")
                else:
                    print(f"Error in chatgpt attempt {i + 1}: {e}. No more retries.")
        return None

# Utility functions
def print_colored(agent, text):
    # Print the text in color based on the agent
    agent_colors = {
        "Ms.Pythonista:": Fore.YELLOW,
        "Mr.PyDev:": Fore.CYAN,
    }
    color = agent_colors.get(agent, "")
    print(color + f"{agent}: {text}" + Style.RESET_ALL, end="")

# Main program
if __name__ == "__main__":
    # Initialize chatbots
    chatbot1 = ChatGPT(api_key, CHATBOT1_PROMPT)
    chatbot2 = ChatGPT(api_key, CHATBOT2_PROMPT)

    # Number of turns for each chatbot
    num_turns = 10

    # Start the conversation with ChatBot1's first message
    user_message = "Hello Mr.PyDev. I am Ms.Pythonista. I'll be starting my assignment now."

    for i in range(num_turns):
        # Ms.Pythonista generates a response
        if user_message:
            print_colored("Ms.Pythonista:", f"{user_message}\n\n")
            response = chatbot1.chat(user_message)
            if isinstance(response, list):
                for chunk in response:
                    user_message = chunk
                    print_colored("Ms.Pythonista:", f"{user_message}\n\n")
            else:
                user_message = response

        # Mr.PyDev generates a response
        if user_message:
            print_colored("Mr.PyDev:", f"{user_message}\n\n")
            response = chatbot2.chat(user_message)
            if isinstance(response, list):
                for chunk in response:
                    user_message = chunk
                    print_colored("Mr.PyDev:", f"{user_message}\n\n")
            else:
                user_message = response
        else:
            break