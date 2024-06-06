from flask import Flask, request, jsonify, send_from_directory
import requests

app = Flask(__name__, static_url_path='', static_folder='.')

# Replace with your actual CLU endpoint and API key
CLU_ENDPOINT = 'https://mentalhealthlanguageresource.cognitiveservices.azure.com/language/:analyze-conversations?api-version=2022-05-01'
CLU_API_KEY = '80e4b8a9cd5e4ce9897ede1e793604d0'
LANGUAGE_SERVICE_ENDPOINT='https://mentalhealthlanguageresource.cognitiveservices.azure.com/'
LANGUAGE_SERVICE_API_KEY='80e4b8a9cd5e4ce9897ede1e793604d0'

@app.route('/')
def index():
    return send_from_directory('.', 'chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message').strip().lower()
    predefined_responses = {
        "hi": "Hello! How can I assist you today?",
        "hey": "Hey,what's up! How can I assist you today?",
        "I need help": "Sure,How can I assist you today?",
        "ok": "Alright. How can I help you further?",
        "thanks": "You're welcome! If you have any other questions, feel free to ask.",
        "no":"Ok,still if you'll any advice feel free to ask me any time.I'm always available for you",
        "no thanks": "You're welcome!",
        "thank you": "You're welcome! If you have any other questions, feel free to ask.I'm always available for you",
        "thanks for that": "You're welcome! If you have any other questions, feel free to ask.I'm always available for you"
    }
    
    if user_input in predefined_responses:
        return jsonify({"response": predefined_responses[user_input]})
    else:
        response = analyze_intent(user_input)
        return jsonify(response)
def analyze_intent(user_input):
    headers = {
        'Ocp-Apim-Subscription-Key': CLU_API_KEY,
        'Content-Type': 'application/json'
    }
    body = {
        "kind": "Conversation",
        "analysisInput": {
            "conversationItem": {
                "id": "1",
                "participantId": "1",
                "modality": "text",
                "text": user_input
            }
        },
        "parameters": {
            "projectName": "MentalHealthChatBotCLU",  # Replace with your actual project name
            "deploymentName": "MentalHealthChatBotCLU",  # Replace with your actual deployment name
            "stringIndexType": "Utf16CodeUnit"  # Use the valid enum value
        }
    }
    response = requests.post(CLU_ENDPOINT, headers=headers, json=body)
    
    # Print the status code and response content for debugging
    print(f"Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")

    if response.status_code != 200:
        return {"response": f"Error: Unable to process the request. Status Code: {response.status_code}, Response: {response.text}"}

    result = response.json()
    
    # Debugging: Print the full response
    print(result)
    
    # Check if 'result' is in the response
    if 'result' not in result:
        return {"response": "Error: Invalid response from the CLU service."}
    
    # Extract the top intent
    top_intent = result['result']['prediction']['topIntent']
    print(f"Top Intent: {top_intent}")  # Debugging: Print the top intent
    
    response_text = get_solution_from_qa_model(top_intent)

    # Define the advice for each intent
    advice_dict = {
        "Anxiety": "Here are a few strategies that might help with anxiety: practice deep breathing, engage in mindfulness meditation, and consider reaching out to a friend or therapist.",
        "Depression": "I'm sorry you're feeling this way. It might help to engage in activities you enjoy, even if they don't seem appealing right now. Physical exercise and talking to someone you trust can also make a big difference.",
        "Stress": "Stress can be overwhelming. Consider taking short breaks throughout your day, practicing time management techniques, and doing something you find relaxing.",
        "Crisis Support": "It sounds like you're in a crisis. It's important to talk to a professional immediately. Please reach out to a crisis hotline or seek emergency assistance.",
        "Diet and Nutrition": "Maintaining a balanced diet is crucial for your overall well-being. Consider incorporating more fruits, vegetables, whole grains, and lean proteins into your meals. Drinking plenty of water and limiting processed foods can also help.",
        "Exercise and Physical Activity": "Regular physical activity can significantly improve your mental and physical health. Aim for at least 30 minutes of moderate exercise most days of the week. Activities like walking, jogging, cycling, and yoga can be beneficial.",
        "General Support": "It's important to seek support when you need it. Reach out to friends, family, or support groups. Talking about your feelings and concerns can help alleviate stress and provide new perspectives.",
        "Loneliness": "Loneliness can be tough, but there are ways to cope. Try to stay connected with loved ones through calls, messages, or social media. Joining clubs, volunteering, or participating in community activities can also help you meet new people.",
        "Mindfulness and Meditation": "Practicing mindfulness and meditation can help reduce stress and improve focus. Set aside a few minutes each day to sit quietly, focus on your breath, and observe your thoughts without judgment.",
        "None": "It seems like you didn't specify an area of concern. Could you provide more details or let me know how I can assist you?",
        "Panic Attack": "During a panic attack, try to focus on your breathing. Take slow, deep breaths and count to four as you inhale and exhale. Grounding techniques, like focusing on your surroundings or holding an ice cube, can also help. If panic attacks persist, seek professional help.",
        "Positive Reinforcement": "Positive reinforcement can boost your motivation and self-esteem. Celebrate your achievements, no matter how small, and reward yourself for reaching your goals. Positive self-talk can also make a big difference.",
        "Relationship Issues": "Relationship issues can be challenging. Open and honest communication is key. Try to express your feelings calmly and listen to the other person's perspective. If needed, consider seeking help from a therapist or counselor.",
        "Seeking Professional Help": "Seeking professional help is a positive step towards improving your mental health. Therapists, counselors, and psychiatrists can provide valuable support and strategies for managing your concerns. Don't hesitate to reach out.",
        "Self-Esteem Issues": "Improving self-esteem takes time and effort. Focus on your strengths and achievements, practice self-compassion, and avoid comparing yourself to others. Setting small, achievable goals can also help build confidence.",
        "Sleep Issues": "Good sleep hygiene can improve your sleep quality. Try to maintain a consistent sleep schedule, create a relaxing bedtime routine, and limit screen time before bed. Avoid caffeine and heavy meals in the evening.",
        "Stress": "Stress can be managed with various techniques. Practice relaxation exercises like deep breathing or progressive muscle relaxation, take regular breaks, and engage in activities you enjoy. Prioritizing tasks and setting realistic goals can also help.",
        "Thanks Greetings": "You're welcome! If you have any other questions, feel free to ask.",
        "Wellness Tips": "For overall wellness, focus on a balanced lifestyle. Eat nutritious foods, stay physically active, get enough sleep, and take time for hobbies and relaxation. Staying connected with loved ones and seeking support when needed is also important."
    }


    advice = advice_dict.get(top_intent, "I'm not sure how to help with that. Can you provide more details?")
    
    return {"response": advice + " " + response_text}

def get_solution_from_qa_model(intent):
    headers = {
        'Ocp-Apim-Subscription-Key': LANGUAGE_SERVICE_API_KEY,
        'Content-Type': 'application/json'
    }
    body = {
        "question": intent,
        "top": 1
    }
    endpoint = 'https://mentalhealthlanguageresource.cognitiveservices.azure.com/language/:query-knowledgebases?projectName=MentalIllness&api-version=2021-10-01&deploymentName=production'
    response = requests.post(endpoint, headers=headers, json=body)
    result = response.json()

    if response.status_code != 200:
        print(f"Error: Unable to fetch solution from Language Service. Status Code: {response.status_code}, Response: {result}")
        return "I'm not sure how to help with that. Can you provide more details?"

    answers = result.get('answers', [])
    if answers and answers[0].get('confidenceScore', 0) > 0.5:
        return answers[0].get('answer')
    else:
        return "I'm not sure how to help with that. Can you provide more details?"

if __name__ == '__main__':
    app.run(debug=True,use_reloader=True,host='0.0.0.0',port=8000)
