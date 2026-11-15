# Module 7 - Problem 2
# Display numbers using a starting value, stopping value, and increment.
start = int(input('Enter the start value: '))
stop = int(input('Enter the stop value: '))
increment = int(input('Enter the increment value: '))

if increment == 0:
    print('Increment cannot be zero.')
elif increment > 0:
    while start <= stop:
        print(start)
        start = start + increment
else:
    while start >= stop:
        print(start)
        start = start + increment
