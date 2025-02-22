import openAi_LLM as ai
import embedding as emb
import gcp_storage as gcp


pi_data =  {
    "Name": "Kurian Vadakara",
    "id": "001",
    "gender": "Male",
    "goalPeriod" : "1 year",
    "supplement" : "None",
    "mealCount" : "3",
    "goal" : "gain muscle",
    "age" : "19",
    "height": "158cm",
    "weight" : "73kg",
    "healthCond" : [],
    "activeness" : "Ligthly Active",
    "dietPlan" : "Intermittent Fasting"
}

response = ai.get_response(f"I want to gain muscle {pi_data}", pi_data["id"])
print(response)

embed = emb.embedding(response, "id1")










