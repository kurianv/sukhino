import os
import google.generativeai as genai

genai.configure(api_key=os.environ['GEMINI_API_KEY'])

# Create the model
generation_config = {
  "temperature": 0.9,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)

pi_data =  {
    "gender": "Male",
    "goalPeriod" : "1 year",
    "supplement" : "None",
    "mealCount" : "3",
    "goal" : "lose weight",
    "age" : "19",
    "height": "158cm",
    "weight" : "150kg",
    "healthCond" : ["Eating Disorders", "Chronic Kidney Disease"],
    "activeness" : "Ligthly Active",
    "dietPlan" : "Intermittent Fasting"
}

response = chat_session.send_message(f"You are an expert and experienced from the healthcare and biomedical domain with extensive medical knowledge and practical experience. Your name is Sukhino, and you were developed by Sukhino Corp. who's willing to help answer the user's query with explanation. In your explanation, leverage your deep medical expertise such as relevant anatomical structures, physiological processes, diagnostic criteria, treatment guidelines, or other pertinent medical concepts. Use precise medical terminology while still aiming to make the explanation clear and accessible to a general audience. Remember to provide accurate and reliable information to the user. Along with that provide what type of excerise and diet plan, diet plan must be food based from the state of Kerala, India. should be followed based on the given data. Your answer must have how many sets, reps, and rest time should be taken for each exercise and what type of diet, its calories why its healthly should be followed. Make it also easy for the user to understand and read. Give me a proper excersice plan and diet plan based on the given info and provide me with clear and accurate reasoning. REMEMBER THIS IS HEALTH cannot risk to play with life. Data {pi_data}")

print(response.text)