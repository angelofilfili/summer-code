name = input("What is your name?")
age = int(input("How old are you?"))

while True:
    age2 = input("Did you already have a birthday this year? (yes/no)")
    if age2.lower() == "yes":
        year_born = 2026 - age
        break
    elif age2.lower() == "no":
        year_born = 2025 - age
        break
    else:
        print("Please answer with 'yes' or 'no'.")

age_in_10_years = age + 10
print(f"Hello, {name}! You were born in {year_born} and you'll be {age_in_10_years} years old in 10 years.")