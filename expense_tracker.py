import csv
import os
from datetime import date
from datetime import datetime
import json

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
        rows = list(reader)
        print(f"{'№':<4} {'date':<12} {'category':<15} {'sum($)':<10} {'description'}")
        print('-' * 60)
        for i, row in enumerate(rows):
            print(f"{i:<4} {row['date']:<12} {row['category']:<15} {row['sum($)']:<10} {row['description']}")
    return rows

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

# ------ DELETE / EDIT --------
def delete_expense():
    rows = show_expenses()
    try:
        index = int(input("Enter the number of the record to delete: "))
        if index < 0 or index >= len(rows):
            print("Invalid number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    deleted = rows.pop(index)
    print(f"Deleted: {deleted['date']} | {deleted['category']} | {deleted['sum($)']} | {deleted['description']}")

    with open(FILENAME, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(rows)

def edit_expense():
    rows = show_expenses()
    try:
        index = int(input("Enter the number of the record to edit: "))
        if index < 0 or index >= len(rows):
            print("Invalid number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    old = rows[index]
    print(f"Editing record: {old['date']} | {old['category']} | {old['sum($)']} | {old['description']}")

    new_date = input(f"New date [{old['date']}]: ").strip() or old['date']
    new_cat = input(f"New category [{old['category']}]: ").strip() or old['category']
    new_sum = input(f"New amount [{old['sum($)']}]: ").strip() or old['sum($)']
    new_desc = input(f"New description [{old['description']}]: ").strip() or old['description']

    rows[index] = {
        'date': new_date,
        'category': new_cat,
        'sum($)': new_sum,
        'description': new_desc
    }

    with open(FILENAME, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(rows)

    print("Record updated.")
# -----------------------------

# export to json
def export_to_json():
    try:

        with open(FILENAME, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            expenses = list(reader)
    
        with open('expenses.json', 'w', encoding='utf-8') as json_file:
            json.dump(expenses, json_file, ensure_ascii=False, indent=4)

        print('Exportet to "expenses.json"')
    except Exception as e:
        print(f'Error exporting to JSON: {e}')



# the main proccess 
def main():
    file_existence()
    while True:
        print('\n--- Expense Tracker ---')
        print('1. Add expense')
        print('2. Show all expenses')
        print('3. Show the sum of your expenses')
        print('4. Filter your expenses')
        print('5. Delete/edit expense')
        print('6. Export to JSON')
        print('7. Leave')
        choice = input('Choose the option: ')

        if choice == '7':
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
                choice2 = input('Only 1 or 2: ').strip()
                if choice2 == '1':
                    filter_by_category()
                elif choice2 == '2':
                    filter_by_date()
                else:
                    print('Try again.')
            elif choice == '5':
                choice3 = input('Delete or edit?(1 or 2): ').strip()
                if choice3 == '1':
                    delete_expense()
                elif choice3 == '2':
                    edit_expense()
            elif choice == '6':
                export_to_json()
            else:
                print('Try again.')
                continue

main()