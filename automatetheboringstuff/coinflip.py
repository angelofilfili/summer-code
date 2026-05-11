import random
for i in range(100):
    if random.randint(0,1) == 0:
        print('H', end=' ')
    else:
        print('T', end=" ")
    
print()

''' performs 100 coin flips with random module
uses end = ' ' to put the results all together on a single line.'''

print('cats', 'dogs', 'mice', sep=',') #prints them together seperated by a comma instead of a space
