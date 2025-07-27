import csv

FILENAME = "expenses.csv"

def valid_num(n):
    if n.isdigit():
        return True
    else:
        return False

def add_expense():
    date = input('Укажите дату: ')
    category = input('Укажите категорию: ')
    summ = float(input('Укажите сумму: '))
    desc = input('Укажите описание: ')
    with open(FILENAME, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, summ, desc])
    print('Расход добавлен!')

def show_expenses():
    print(open('expenses.csv').read())

def expenses_sum():
    total = 0
    with open('expenses.csv', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
                total += float(row['sum($)'])
    print(f'Сумма ваших расходов: {total}$')

while True:
    print('1. Добавить расход')
    print('2. Показать все расходы')
    print('3. Показать сумму расходов')
    print('4. Выйти')
    choice = input('Выберите опцию: ')

    if choice == '4':
        break
    else:
        if choice == '1':
            add_expense()
        if choice == '2':
            show_expenses()
        if choice == '3':
            expenses_sum()
            