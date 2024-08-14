import json

with open("2015/day12/input.json") as file:
    data = json.load(file)
    
def sum_integers(data):
    
    sum = 0
    
    if isinstance(data, int):
        return data
    
    elif isinstance(data, list):
        for item in data:
            sum += sum_integers(item)
            
    elif isinstance(data, dict):
        for value in data.values():
            ##PART2
            # if value == "red":
            #     return 0
            sum += sum_integers(value)
    
    return sum

print(sum_integers(data))