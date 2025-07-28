import csv
import os
from datetime import date
from datetime import datetime

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
    date_input = input('Set the date(YYYY-MM-DD): ')
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

# ---------- FILTERS ---------- 
def filter_by_category():
    category_input = input('Enter the category to filter: ')
    found = False
    with open(FILENAME, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        print(f'{'date':<12} {'category':<15} {'sum($)':<10} {'description'}')
        print('-' * 50)
        for row in reader:
            if row['category'].strip().lower() == category_input.strip().lower():
                found = True
                print(f'{row['date']:<12} {row['category']:<15} {row['sum($)']:<10} {row['description']}')
    if not found:
        print('No records found for this category')

def filter_by_date():
    start_input = input('Enter start date (YYYY-MM-DD): ').strip()
    end_input = input('Enter end date (YYYY-MM-DD): ').strip()

    try:
        start_date = datetime.strptime(start_input, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_input, "%Y-%m-%d").date()
    except ValueError:
        print('Invalid date format. Use YYYY-MM-DD.')
        return
    
    if start_date > end_date:
        print('Start date must be before or equal to end date.')
        return
    
    found = False
    with open(FILENAME, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        print(f'\nExpenses from {start_date} to {end_date}')
        print(f'{'date':<12} {'category':<15} {'sum($)':<10} {'description'}')
        print('-' * 50)
        for row in reader:
            try:
                row_date = datetime.strptime(row['date'], '%Y-%m-%d').date()
            except ValueError:
                continue
            if start_date <= row_date <= end_date:
                found = True
                print(f'{row['date']:<12} {row['category']:<15} {row['sum($)']:<10} {row['description']}')
    if not found:
        print('No expenses found in this date range.')
# -----------------------------


# the main proccess 
def main():
    file_existence()
    while True:
        print('\n--- Expense Tracker ---')
        print('1. Add expense')
        print('2. Show all expenses')
        print('3. Show the sum of your expenses')
        print('4. Filter your expenses')
        print('5. Leave')
        choice = input('Choose the option: ')

        if choice == '5':
            break
        else:
            if choice == '1':
                add_expense()
            elif choice == '2':
                show_expenses()
            elif choice == '3':
                expenses_sum()
            elif choice == '4':
                print('Choose your filter(by category/by date)')
                choice2 = input('Only 1 or 2:')
                if choice2 == '1':
                    filter_by_category()
                elif choice2 == '2':
                    filter_by_date()
                else:
                    print('Try again.')
            else:
                print('Try again.')
                continue

main()