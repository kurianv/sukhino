import openAiLLM as ai
#import embedding as emb

pi_data =  {
    "Name": "Kurian Vadakara",
    "id": "001",
    "gender": "Male",
    "goalPeriod" : "1 year",
    "supplement" : "None",
    "mealCount" : "3",
    "goal" : "lose weight",
    "age" : "19",
    "height": "158cm",
    "weight" : "73kg",
    "healthCond" : [],
    "activeness" : "Ligthly Active",
    "dietPlan" : "Intermittent Fasting"
}

response = ai.get_response(f"I want to gain muscle {pi_data}", pi_data["id"])
print(response)
#embed = emb.embedding(response)




