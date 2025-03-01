from datetime import datetime

def add_expense(expense_list):
    '''
    Take Date, Category, Amount and Description as input 
    '''
    # To take input for date value if date format is wrong user will be prompted to provide value in correct format
    while True:
        date_inp = input("Enter date of the expense in format YYYY-MM-DD: ")
        try:
            date_inp_val = datetime.strptime(date_inp, "%Y-%m-%d").date()
            break # exit when valid value for date is given
        except ValueError:
            print("Invalid date format! Please enter in yyyy-mm-dd format.")

    # Add category of the expense
    category = input("Enter the category of the expense: ")
    
    # To take input for amount, if value is not in valid format prompt user to provide value in correct format
    while True:
        try:
            amount = float(input("Enter the amount: "))
            break # exit when valid amount value is given
        except ValueError:
            print("Enter valid value for amount")
    
    #Add description for the expenses    
    description = input("Enter description of expense: ")
    
    # Add details to a dictionary
    expense_entry_dict = {}    
    expense_entry_dict['date'] = date_inp_val
    expense_entry_dict['category'] = category
    expense_entry_dict['amount'] = amount
    expense_entry_dict['description'] = description
    
    # Add item to a list of expenses
    expense_list.append(expense_entry_dict)

def view_expenses(expense_list):
    '''
    Display details of expenses
    '''
    
    print("----- Expenses Detail is given below ---- ")
    for i in expense_list:
        missing_ctr = False
        
        # Check if value for any of the key is missing for an item
        for v in i.values():
            if v == '':
                missing_ctr = True
        # display expense detail for each item if no value for the key of item is missing 
        if missing_ctr == False:
            for k, v in i.items():
                print(k, ':', v, sep='')
        # skip the item if any of the value for the key of item is missing
        else:
            continue
        print("________________________")

def set_budget(monthly_budget):
    '''
    Take input from user to set the monthly budget
    '''
    monthly_budget = float(input("Enter your monthly budget: "))
    return monthly_budget

def total_expense(expense_list, monthly_budget):
    '''
    Display total expenses till date.
    Also, shows if total expenses are more than set monthly budget
    '''
    total_expense = 0.0
    # Sum up all the expenses for the month
    for expense_item in expense_list:
        total_expense += float(expense_item['amount'])
    
    # compare monthly expense with monthly budget
    if total_expense > monthly_budget:
        print("You have exceeded your budget")
    else:
        balance_amount = monthly_budget - total_expense
        print("You have {} left for the month".format(str(balance_amount)))

import csv

def save_expenses(expense_list):
    '''
    Save expenses to a file
    '''

    keys = expense_list[0].keys()

    # write items(dictionary) from expense_list to a file
    with open('expense.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(expense_list)

def load_expenses(expense_list):
    '''
    Load expense details to a list
    '''
    # read csv file to a list of dictionaries
    with open('expense.csv', 'r') as input_file:
        csv_reader = csv.DictReader(input_file)
        expense_list = [row for row in csv_reader]
        return expense_list


def menu():
    '''
    Display menu to the user
    '''
    print("Option 1: Add expense")
    print("Option 2: View expenses")
    print("Option 3: Track budget")
    print("Option 4: Save Expenses")
    print("Option 5: Exit")
    print("-------------------------")

def interactive_menu():
    '''
    Provide user with menu options.
    Allow user to Add, view and save expenses.
    '''
    menu()
    expense_list = []
    monthly_budget = 0.0
    expense_list = load_expenses(expense_list)
    while True:
        option_chosen = input("Enter an option: ")
        if option_chosen == '1':
            add_expense(expense_list)
        elif option_chosen == '2':
            view_expenses(expense_list)
        elif option_chosen == '3':
            monthly_budget = set_budget(monthly_budget)
            total_expense(expense_list,monthly_budget)
        elif option_chosen == '4':
            save_expenses(expense_list)
        elif option_chosen == '5':
            save_expenses(expense_list)
            break
        else:
            print("Invalid choice. Please try again!")

interactive_menu()
