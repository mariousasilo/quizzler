import requests
import json


ENDPOINT = "https://opentdb.com/api.php"
NUM_OF_QUESTIONS = 10
parameters = {
    "amount": NUM_OF_QUESTIONS,
    "category": 18,
    "type": "boolean"
}


class QuestionsGenerator:

    def __init__(self):
        self.response = requests.get(url=ENDPOINT, params=parameters)
        self.questions_json = self.response.json()
        with open(file="data.json", mode="w") as file:
            json.dump(self.questions_json, file, indent=4)
