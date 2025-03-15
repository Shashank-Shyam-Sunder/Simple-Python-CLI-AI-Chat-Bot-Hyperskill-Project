if __name__ == "__main__":
    # Implement the Python code using the `openai` library to create the assistant.
    # Start with a system prompt for the chat completion API.
    # Send a static message and receive a response from the API.
    # Show the chat completion message.
    # %%
    import os
    from dotenv import load_dotenv
    import openai

    # %% Just for debugging
    # Loading the OPENAI API KEY
    # Manually specify .env file location if needed
    # os.chdir("C:\Shashank_work\Python_Works\Simple Python CLI Chat\Simple Python CLI Chat\\task")
    # env_path = os.path.join(os.getcwd(), '.env')
    # load_dotenv(env_path)  # Load environment variables
    # api_key = os.environ.get("OPENAI_API_KEY")

    # %%
    # Without debugging it works well but not in python console
    load_dotenv()
    api_key = os.environ.get("OPENAI_API_KEY", None)

    if not api_key:
        # print("Missing API Key. Check your .env file.")
        raise KeyError("Missing API Key. Check your .env file.")


    # else:
    #     print(f"Debugging API Key: {api_key[:5]}...{api_key[-5:]}")  # ✅ Safe
    #
    # %% Creating a function to end the conversation
    def end_conversation(message):
        if message == "End Conversation":
            return None


    functions_list = [
        {
            "type": "function",
            "function": {
                "name": "end_conversation",
                "description": "End Conversation with the Chatbot",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message": {"type": "string", "description": "Message: End Conversation"},
                    },
                    "required": ["message"],
                },
            },
        }
    ]

    # %% Creating a simple Chat bot using OPENAI
    client = openai.OpenAI(api_key=api_key, base_url="https://litellm.aks-hs-prod.int.hyperskill.org/")


    def get_chat_completion(prompt_message, tools=None, tool_choice="auto"):
        return client.chat.completions.create(
            model="gpt-4o-mini",
            messages=prompt_message,
            temperature=0.8,
            tools=tools,
            tool_choice=tool_choice,
        )


    # Function to compute the tokens cost
    Model_cost = {"input_cost": 0.01 / 1000, "output_cost": 0.03 / 1000}


    #
    def calculate_tokes_cost(chat_completion_ai):
        input_tokens_cost = chat_completion_ai.usage.prompt_tokens * Model_cost["input_cost"]
        output_tokens_cost = chat_completion_ai.usage.completion_tokens * Model_cost["output_cost"]

        return input_tokens_cost + output_tokens_cost


    # Using while loop for continuous interaction with the user
    ###
    while True:
        # %%
        prompt = input("Enter a message: ")
        # prompt = "What is your training cutoff date?"
        # prompt = "What are you?"
        # prompt = "End Conversation"
        # print(f"You: {prompt}")
        messages = [{"role": "user", "content": prompt}]

        chat_completion = get_chat_completion(messages, tools=functions_list)
        gpt_response = chat_completion.choices[0].message.content
        # %%
        # tool_call = chat_completion.choices[0].message.tool_calls[0]
        if chat_completion.choices[0].message.tool_calls:
            print(chat_completion.choices[0].message.tool_calls[0].id)
            print(f"You: {prompt}")
            print(f"Assistant: {gpt_response}")

            total_tokens_cost = calculate_tokes_cost(chat_completion)
            print(f"Cost: ${total_tokens_cost}")
            break
        else:
            print(f"You: {prompt}")
            print(f"Assistant: {gpt_response}")

            total_tokens_cost = calculate_tokes_cost(chat_completion)
            print(f"Cost: ${total_tokens_cost}")

        # %%


