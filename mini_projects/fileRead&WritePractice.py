try:
    with open('testFile.txt') as file:  #can list name only cuz in same folder but if different then gotta list path
        print(file.read())
except FileNotFoundError:
    print("This file was not found :C")   

print(file.closed) #prints True because 'with open' closes automatically

txt_data = "I like pizza"

file_path = "output.txt"

with open(file_path, "w") as file: # w = write , x = also writes if file doesnt exist , a = append , r = read
    file.write(txt_data)
    print(f"txt file '{file_path}' was created") 

employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

try:
    with open(file_path, "w") as file:
        for employee in employees:
            file.write(employee + " ")
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")

import json 

employee_dict = {
    "name" : 'Spongebob',
    "age" : 30,
    "job" : "cook"
}

try:
    with open(file_path, "w") as file:
        json.dump(employee_dict, file, indent=4)
        print(f"json file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")

import csv

employee_list = [["Name", "Age", "Job"],
                 ["Spongebob", 30, "Cook"],
                 ["Patrick", 37, "Unemployed"],
                 ["Sandy", 27, "Scientist"]]

try:
    with open("csvfile.txt", "w", newline="") as file:
        writer = csv.writer(file)
        for row in employee_list:
            writer.writerow(row)
        print(f"csv file 'csvfile.txt' was created")
except FileExistsError:
    print("That file already exists!")





    


