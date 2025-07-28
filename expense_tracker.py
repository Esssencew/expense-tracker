import csv
import os
from datetime import date

FILENAME = "expenses.csv"
HEADERS = ['date', 'category', 'sum($)', 'description']

# checking the existence of file
def file_existence():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(HEADERS)

# adding expense
def add_expense():
    date_input = input('Set the date(YY-MM-DD): ')
    date_total = date_input if date_input else date.today()
    category = input('Set the category: ')
    try:
        summ = float(input('Enter the amount: '))
    except ValueError:
        print('Put the number.')
        return
    desc = input('Enter the description: ')
    with open(FILENAME, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([date_total, category, summ, desc])
    print('Expense was added!')

# showing expenses
def show_expenses():
    with open(FILENAME, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        print(f'{'date':<12} {'category':<15} {'sum($)':<10} {'description'}')
        print('-' * 50)
        for row in reader:
            print(f'{row['date']:<12} {row['category']:<15} {row['sum($)']:<10} {row['description']}')

# counting the sum of expenses
def expenses_sum():
    total = 0
    with open('expenses.csv', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
                total += float(row['sum($)'])
    print(f'Sum of your amounts: {total}$')

# the main proccess 
def main():
    file_existence()
    while True:
        print('\n--- Expense Tracker ---')
        print('1. Add expense')
        print('2. Show all expenses')
        print('3. Show the sum of your expenses')
        print('4. Leave')
        choice = input('Choose the option: ')

        if choice == '4':
            break
        else:
            if choice == '1':
                add_expense()
            elif choice == '2':
                show_expenses()
            elif choice == '3':
                expenses_sum()
            else:
                print('Try again.')
                continue

main()