import os
import csv
from pprint import pprint

def format_data(data: list) -> None:
    new_item = {
        "Name": data[1],
        "Email": data[2],
        "Phone Number": data[3],
        "Address": data[6],
        "Lat": data[9],
        "Lng": data[10]
    }

    return new_item

def food_bank_data(path: str) -> dict:

    fb_dict = {"food_banks": []}

    if os.path.isfile(path):
        with open(path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for line in reader:
                fb_dict["food_banks"].append(format_data(line))
    else:
        print("file does not exsist")
        return None
    
    return fb_dict


if __name__ == "__main__":
    pprint(food_bank_data("../data/foodbanks_ATLANTIC.csv"))