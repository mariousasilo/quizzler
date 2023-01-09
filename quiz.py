import json


class Quiz:

    def __init__(self):
        with open("data.json") as file:
            self.questions_dict = json.load(fp=file)
            self.questions_list = self.questions_dict["results"]
            self.questions_correct = []
            self.questions_wrong = []
