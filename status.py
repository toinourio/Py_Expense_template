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
    accounts = {}
    for user in users:
        accounts[user] = 0
    for expense in expenses:
        accounts[expense[2]] += int(expense[0])
    print(accounts)

    return True