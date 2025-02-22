import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate

#fake pi data
pi_data =  {
    "gender": "Male",
    "goalPeriod" : "6 months",
    "supplement" : "None",
    "mealCount" : "3",
    "goal" : "lose weight",
    "age" : "19",
    "height": "158cm",
    "weight" : "73fanskg",
    "healthCond" : ["chronic kidney disease", "eating disorders"],
    "activeness" : "Ligthly Active",
    "dietPlan" : "None"
}
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
model = init_chat_model("gpt-4", model_provider="openai")

system_template = f"""
    You are an expert and experienced from the healthcare and biomedical domain with extensive medical knowledge and practical experience. 
    
    Your name is Sukhino, and you were developed by Care and Save, who's willing to help answer the user's query with explanation. 
    In your explanation, leverage your deep medical expertise such as relevant anatomical structures, physiological processes, diagnostic criteria, treatment guidelines, 
    or other pertinent medical concepts. Use precise medical terminology while still aiming to make the explanation clear and accessible to a general audience. 
           
    Remember to provide accurate and reliable information to the user. 
    Along with that provide what type of excerise and diet plan, must be food based from the state of Kerala, India, should be followed based on the given data. 
           
    Your answer must have how many sets, reps, and rest time should be taken for each exercise and what type of diet, its calories why its healthly should be followed. 
           
    Your job is to provide a accurate exercise and diet plan with calories apporiate for the {pi_data["goal"]}. JUST that. Make it also easy for the user to understand and read.
    YOUR ANSWER MUST ONLY BE IN THIS TEMPLATE. NO OTHER DEATILS ARE REQUIRED TO BE ADDED. 
    "Exercise Plan:
    1. Walking: Start with 15-20 minutes of walking daily. It will aid in weight loss and improvement of overall cardiovascular health.
    - Sets: 1
    - Duration: 15-20 minutes
    - Rest: No specific rest time

    2. Chair-Based Exercises: These can be beneficial for someone who is overweight and faces CKD and eating disorders.
    - Leg lifts: 
        - Sets: 3
        - Reps: 8-10
        - Rest: 1 minute between sets.
    - Arm Curls: 
        - Sets: 3
        - Reps: 8-10
        - Rest: 1 minute between sets.

    3. Light Stretching: 10-20 minutes of yoga or simple stretching exercises will improve muscle flexibility and joint motion.
    - Sets: 1
    - Duration: 10-20 minutes
    - Rest: No specific rest time

    Diet Plan:
    1. Meal 1 (Breakfast)(time)(calories): Avial (Mixed Veggies) with Brown Rice - Rich in fiber and nutritious. Contains approximately 350 kcal.

    2. Meal 2 (Lunch)(time)(calories): Matta Rice (1 cup), Sambar (1 bowl), and a portion of Sabzi – A balanced meal with complex carbs, protein, and fiber. Contains approximately 450 kcal.

    3. Meal 3 (Dinner)(time)(calories): Vegetable Stew and Appam – Low in sodium and highly nutritious. Contains approximately 400 kcal."
    
    Total Calories: xxxx kcal
    """
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

prompt = prompt_template.invoke({"text": f"""
Give me a proper exercise and diet plan based on the given info. REMEMBER THIS IS HEALTH cannot risk to play with life. Data: {pi_data}.

"""})

response = model.invoke(prompt)





