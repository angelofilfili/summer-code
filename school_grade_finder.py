scores = []

def asking_user(scores):
    counter = 0
    while True:
        score = input("Give a score between 0 and 100: ")
        if score.isdigit():
            int_score = int(score)
            if 0 <= int_score <= 100:
                scores.append(int_score)
                counter += 1
                print(counter)
                if counter == 5:
                    break
            else:
                print("Please give a number that is between 0 & 100.")
        else:
            print("Please give a NUMBER that is between 0 & 100.")

    return scores

def averages(scores):
    counter = 0
    total_scores = 0
    for score in scores:
        total_scores += score
        counter += 1
    average_score = total_scores / counter

    return average_score

def letter_grade(average_score):
    if average_score >= 90:
        return 'Your average score leaves with an A in the course! YOU PASS!!'
    elif 79 <= average_score <= 89:
        return 'Your average score leaves with an B in the course! YOU PASS!!'
    elif 69 <= average_score <= 78:
        return 'Your average score leaves with an C in the course! YOU PASS!!'
    elif 60 <= average_score <= 68:
        return 'Your average score leaves with an D in the course! YOU PASS!!'
    else:
        return 'Your average score leaves with an F in the course! YOU FAIL!!'
    
asking_user(scores)
average_score = averages(scores)
final_grade = letter_grade(average_score)

print(final_grade)






