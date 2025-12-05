import json
import random
import os

def load_random_text():

    base_dir=os.path.dirname(os.path.dirname(__file__))
    json_path=os.path.join(base_dir,"data","texts.json")

    with open(json_path,"r",encoding="utf-8") as f:
        data=json.load(f)


    return random.choice(data["texts"])

