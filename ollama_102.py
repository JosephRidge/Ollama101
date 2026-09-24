import ollama_101_utils as utils
from ollama import chat

# prompting section 
print("To exit please type 'exit'")
user_input = utils.getUserQuery(messages=utils.messages,machine_question_nudge = "Give me somthing to summarize...") 

while True:  
    if (user_input == "exit"):
        print("stopping...")
        break
    else: 
        print("running...")
        user_prompt = f"<YOU>: {user_input}"
        print(user_prompt) 
        print("summarizing...")
        response = utils.generateTextSummay(model=utils.MODEL, text = user_input)
        print('\n<MACHINE Thinker summary>: ')
        print(response)
        # for chunk in response:
        #     print(chunk.message.content, end='', flush=True)

        user_input = utils.getUserQuery(messages=utils.messages,machine_question_nudge = "Give me more to summarize...") 