def generate_subject(email_text, client):
    system_prompt = """ 
    You are a very professional writer who gives headings to the emails. 
    Analyzer the emails carefully, understand the purpose and highlights of the email. And give a clear heading of no more than 20 words and no less than      8 words. Do add website's name like - <Website Name>: and then the subject line - to show which website's promotion email it is. If email is not     promotional then add no such thing.
    """

    user_prompt = f"""
    Here is the content of email - please provide me a heading/title for this as per the rules
    {email_text}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    return response.choices[0].message.content
