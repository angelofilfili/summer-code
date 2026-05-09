
# w/o list comprehension
doubles = []
for x in range(1, 11):
    doubles.append(x * 2)


print(doubles)
# Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#list comprehension template :
# [expression for value in iterable if condition]

# Using list comprehension
doubles2 = [x * 2 for x in range(1,11)]
print(doubles2)
# Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

triples = [y * 3 for y in range(1, 11)]
squares = [z**2 for z in range(1, 11)]
print(triples)
# Output: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
print(squares)
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

fruits1 = ['apple', 'orange', 'banana', 'coconut']
fruits = [fruit.upper() for fruit in fruits1]
fruit_chars = [fruit[0] for fruit in fruits1]
print(fruits)
print(fruit_chars)

#conditions now

numbers = [1, -2, 3, -4, 5, -6, 8, -7]
positive_nums = [num for num in numbers if num >= 0]
print(positive_nums)

negative_nums = [num for num in numbers if num<= 0]
print(negative_nums)

even_nums = [num for num in numbers if num % 2 == 0]
print(even_nums)

odd_nums = [num for num in numbers if num % 2 == 1]
print(odd_nums)

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)



