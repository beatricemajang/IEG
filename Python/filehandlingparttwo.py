import json

try:
    with open('Python/fruitsdictionary.json', 'r') as filehandler:
        data = json.load(filehandler)
        for product in data:
            print(product)
except Exception as e:
    print("Something went wrong:", e)