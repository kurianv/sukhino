import openai
from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import base64
from nutritionix import Nutritionix
import requests
 
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI()
nix = Nutritionix(app_id= os.getenv('NIX_APP_ID'), api_key= os.getenv('NIX_API_KEY'))

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def image_details(image_path):
    base64_image = encode_image(image_path)

    response = client.responses.create(
        model="gpt-4o",
        input=[
            {
                "role": "user",
                "content": [
                    { "type": "input_text", "text": """
                    You are a food scanner, that is required to scanning the image and identify the food in the image. Make sure you throughly look at what food is found and have the numbers to be accurate, in terms of the quantity of the food or the size of the dish. REMEMBER YOU ARE AN HEALTH EXPERT, YOUR NUMBERS MATTER AND ARE REQUIRED TO HELP PEOPLE. 
                    UNDER DESCRIPTION PROVIDE REASONING TO YOUR FINDING, AND ALSO THE NUMERICAL FINDING. serving_weight_grams must be in grams measurement and the value MUST JUST BE NUMERIC. calorie, total_food_cal AND total_calories must be null
                    IMPORTANT: RETURN THE RESPONSE **ONLY IN JSON FORMAT** AS SHOWN BELOW AND NO UNWANTED TEXT AS SUMMARY OR CONSULATION:
                    {
                        "food_name": [
                            {
                                "food_number": "1",
                                "name": "appam",
                                "serving_weight_grams" : 46
                                "calorie" : null
                                "total_food_cal" : null
                                "description": ""
                            }
                            {
                                "food_number": "2",
                                "name": "vegetable stew",
                                "serving_weight_grams" : 482
                                "calories" : null
                                "total_food_cal" : null
                                "description": ""
                            }
                        ],
                        "total_calories" : null
                    }
                    """ },
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{base64_image}",
                    },
                ],
            }
        ],
    )

    final = str(response.output_text).replace("```json", "").replace("```", "")
    json_response = json.loads(final)
    
    total = 0
    for i in range(len(json_response["food_name"])):
        cal, grams = calorieCounter(json_response["food_name"][i]["name"])
        count  = json_response["food_name"][i]["serving_weight_grams"]/grams
        json_response["food_name"][i]["calorie"] = cal
        json_response["food_name"][i]["total_food_cal"] = cal * count
        print("For", round(count), json_response["food_name"][i]["name"], ":", round(json_response["food_name"][i]["total_food_cal"]))
        total += round(json_response["food_name"][i]["total_food_cal"])
    
    json_response["total_calories"] = total
    print("totalcalories: ", total)

    print(json_response)
    
    with open(f"{image_path[:len(image_path)-4]}.json", "w", encoding="utf-8") as file:
        json.dump(json_response, file, indent=4)  
    

def calorieCounter(food):
    api_key = os.getenv('NIX_API_KEY')
    app_id = os.getenv('NIX_APP_ID')

    url = "https://trackapi.nutritionix.com/v2/natural/nutrients"
    headers = {
        "x-app-id": app_id,
        "x-app-key": api_key
    }
    
    query = {
        "query": food
    }
    response = requests.request('POST', url, headers=headers, data=query)    
    return response.json()["foods"][0]["nf_calories"], response.json()["foods"][0]["serving_weight_grams"]


image_details("appam.jpg")




