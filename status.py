from PyInquirer import prompt
import csv
from expense import get_users

def get_expenses():
    with open('expense_report.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        expenses = []
        for row in reader:
            expenses.append(row)
    return expenses

def show_status():
    expenses = get_expenses()
    users = get_users()[1]
    for user in users:
        print(user, expenses[0][-1])

    return True