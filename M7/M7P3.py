# Module 7 - Problem 3
# Calculate each student's average exam score and count students.
count = 0
answer = input('Do you want to enter a student? (Yes/No): ')

while answer.lower() == 'yes':
    last_name = input('Enter student last name: ')
    exam1 = float(input('Enter first exam score: '))
    exam2 = float(input('Enter second exam score: '))
    average = (exam1 + exam2) / 2
    print('Student:', last_name, 'Average:', format(average, '.2f'))
    count = count + 1
    answer = input('Do you want to enter another student? (Yes/No): ')

print('Number of students:', count)
