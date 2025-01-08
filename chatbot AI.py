import datetime
import re
def get_current_time():
    return datetime.datetime.now().strftime("%H:%M:%S")
def get_current_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")
def calculate_math_expression(expression):
    try:
        result = eval(expression)
        return f"The result is {result}"
    except Exception as e:
        return "Sorry, I could not understand the math expression."
def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm doing great, thank you for asking!"
    elif "time" in user_input or "what time is it" in user_input:
        return f"The current time is {get_current_time()}."
    elif "date" in user_input or "what is the date" in user_input:
        return f"Today's date is {get_current_date()}."
    elif "weather" in user_input:
        return "I can't provide live weather updates, but it's always a good idea to check your favorite weather app!"
    elif "calculate" in user_input or "what is" in user_input or "plus" in user_input or "minus" in user_input or "times" in user_input or "divided by" in user_input:
        math_expression = re.sub(r"what is|calculate|is", "", user_input).strip()
        return calculate_math_expression(math_expression)
    elif "bye" in user_input or "goodbye" in user_input or "see you" in user_input:
        return "Goodbye! Have a wonderful day!"
    elif "help" in user_input:
        return "I can assist you with the current time, date, weather, or basic math calculations."
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! Let me know if you need anything else."
    else:
        return "Sorry, I didn't quite understand that. Can you please rephrase?"
def start_chat():
    print("Chatbot: Hi! I'm here to assist you. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if 'bye' in user_input.lower():
            print("Chatbot: Goodbye! Have a wonderful day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
start_chat()
