def get_response(user_input: str, open_ai_client, chat_log) -> str:
    try:
        chat_log.append({
            "role": "user", 
            "content": user_input
        })
        output = open_ai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=chat_log
        )
        ai_reponse = output.choices[0].message.content
        chat_log.append({
            "role": "assistant", 
            "content": ai_reponse.strip("\n").strip()
        })
        return ai_reponse
    except Exception as e:
        print(e)
        return "Sorry, I encountered an error while processing your request. Please try again later."