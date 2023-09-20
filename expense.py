from PyInquirer import prompt
import csv

def get_users():
    userchoices = []
    usercheckbox = []
    with open('users.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            userchoices.append(row[0])
            usercheckbox.append({'name': row[0]})
    return [usercheckbox, userchoices]



def new_expense(*args):
    users = get_users()

    expense_questions = [
        {
            "type":"input",
            "name":"amount",
            "message":"New Expense - Amount: ",
        },
        {
            "type":"input",
            "name":"label",
            "message":"New Expense - Label: ",
        },
        {
            "type":"list",
            "name":"spender",
            "message":"New Expense - Spender: ",
            "choices": users[1],
        },
        {
            "type":"checkbox",
            "name":"payback",
            "message":"New Expense - Payback: ",
            "choices": users[0],
        }
    ]

    infos = prompt(expense_questions)
    fieldnames = ['amount', 'label', 'spender', 'payback']
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    with open('expense_report.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(infos)
    print("Expense Added !")
    return True


