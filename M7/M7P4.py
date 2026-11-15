# Module 7 - Problem 4
# Calculate gross pay with time-and-a-half overtime after 40 hours.
count = 0
total_gross_pay = 0
answer = input('Do you want to enter an employee? (Yes/No): ')

while answer.lower() == 'yes':
    last_name = input('Enter employee last name: ')
    hours = float(input('Enter hours worked: '))
    rate = float(input('Enter hourly pay rate: '))

    if hours > 40:
        gross_pay = 40 * rate + (hours - 40) * rate * 1.5
    else:
        gross_pay = hours * rate

    print('Employee:', last_name, 'Gross pay: $' + format(gross_pay, '.2f'))
    total_gross_pay = total_gross_pay + gross_pay
    count = count + 1
    answer = input('Do you want to enter another employee? (Yes/No): ')

print('Number of employees:', count)
print('Total gross pay: $' + format(total_gross_pay, '.2f'))
