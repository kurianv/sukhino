from openai import OpenAI
import openai
from dotenv import load_dotenv
import os
import json

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI()

def get_response(prompt, id):
    message =  [
            {"role": "system", "content": """
    You are an expert and experienced from the healthcare and biomedical domain with extensive medical knowledge and practical experience. 
    
    Your name is Sukhino, and you were developed by Care and Save, who's willing to help answer the user's query with explanation. 
    In your explanation, leverage your deep medical expertise such as relevant anatomical structures, physiological processes, diagnostic criteria, treatment guidelines, 
    or other pertinent medical concepts. Use precise medical terminology while still aiming to make the explanation clear and accessible to a general audience. 
           
    Remember to provide accurate and reliable information to the user. 
    Along with that provide what type of excerise and diet plan, must be food based from the state of Kerala, India, should be followed based on the given data. 
           
    IMPORTANT: RETURN THE RESPONSE **ONLY IN JSON FORMAT** AS SHOWN BELOW AND NO UNWANTED TEXT AS SUMMARY OR CONSULATION:
    {
        'exercise_plan': [
            {
                'name': 'Walking',
                'description': 'Start with 15-20 minutes of walking daily. It will aid in weight loss and improvement of overall cardiovascular health.',
                'sets': '1',
                'duration': '15-20 minutes',
                'rest': 'No specific rest time'
            }
        ],
        'diet_plan': [
            {
                'meal_number': '1',
                'meal_name': 'Breakfast',
                'time': '8:00am',
                'calories': '350',
                'description': 'Avial (Mixed Veggies) with Brown Rice - Rich in fiber and nutritious.'
            }
        ],
        'total_calories': 'xxxx kcal'
    }
    """},

        {"role": "user", "content": prompt},
    ]

    #openai call
    response = client.chat.completions.create(
        model="gpt-4",
        messages=message,

    )
    final = (response.choices[0].message.content).strip().replace("\n            ", "").replace("\n        ", "").replace("\n    ", "").replace("\\", "")
    

    with open(f"user{id}.json", "w", encoding="utf-8") as file:
        json.dump(final, file, indent = 4)

    return final
    