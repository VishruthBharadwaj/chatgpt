import openai

#OpenAI API key
openai.api_key = "Your Key"

# Define the questions
questions = [
    "Do you have formally defined criteria for notifying a client during an incident that might impact the security of their data or systems? What are your SLAs for notification?",
    "Is personal information transmitted, processed, stored, or disclosed to or retained by third parties? If yes, describe.",
    "Which cloud providers do you rely on?",
    "Please specify the primary data center location/region of the underlying cloud infrastructure used to host the service(s) as well as the backup location(s).",
    "Which of the following, if any, are performed as part of your monitoring process for the service:\n\n* Application Performance Monitoring (APM)\n\n* End User Monitoring (EUM)\n\n* Digital Experience Monitoring (DEM)"
]

# unavailability of data phrases
unavailable_phrases = [
    "Data not available",
    "I don't have access",
    "I don't process personal",
    "I don’t have access to personal data"
    "As an AI assistant, I don't transmit, process, or store personal information",
    "I don't have direct access",
    "I do not have direct access",
    "I do not have access"
]

# check for unavailability
def is_unavailable(content):
    for phrase in unavailable_phrases:
        if phrase in content:
            return True
    return False

# get answers using OpenAI
def get_answers(questions):
    answers = []

    for question in questions:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ]
        )
        
        assistant_message = response.choices[0].message
        assistant_message_content = assistant_message['content']
        
        if is_unavailable(assistant_message_content):
            answers.append("Data not available")
        else:
            answers.append(assistant_message_content)

    return answers


answers = get_answers(questions)

with open("answers_output.txt", "w") as file:
    for idx, (question, answer) in enumerate(zip(questions, answers)):
        file.write(f"Question {idx+1}: {question}\n ")
        file.write(f"Answer {idx+1}: {answer}\n\n")
