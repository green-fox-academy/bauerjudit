
import sys
import csv
import time
from datetime import datetime
from colors import red, green, yellow


csv_input = "todo.csv"


def open_list():

    input_file = open(csv_input, "r")
    lines = csv.reader(input_file, delimiter = "|")
    print("   Priority:    Description:   Status:    Deadline: ")
    for index, line in enumerate(lines):

        print(index+1, line[0:3])
    print()
    print()
    input_file.close()


def add_new_item():
    with open(csv_input, "a") as csvfile:
       todo_csv = csv.writer(csvfile, delimiter = "|", lineterminator="\n")
       status = "active"
       priority = input ("Choose a priority: H - High, M - Medium, L - Low: ").upper()
       if priority == "H":
            priority_mod = "High"
       elif priority == "M":
            priority_mod = "Medium"
       elif priority == "L":
            priority_mod = "Low"
       else:
            priority_mod = "Medium"

       description = input("Give the description: ")
       deadline = int(input("Please give the deadline | format:20150622: "))
       date = datetime.now().strftime('%d/%m/%Y %H:%M')
       data = [priority_mod, description, status, deadline, date]
       todo_csv.writerow(data)


def remove():
    text = open(csv_input, "r")
    lines = list(csv.reader(text, delimiter = "|"))
    open_list()
    user_input = int(input("Enter an index: "))
    new_list = list(lines)
    print()
    print("Are you sure? y/n: ")
    print(new_list[user_input-1])
    yes = input("")
    if  yes == "y":
        new_list.remove(new_list[user_input-1])
        with open(csv_input, "w") as csvfile:
            todo_csv = csv.writer(csvfile, delimiter = "|", lineterminator="\n")
            for line in todo_csv:
                todo_csv.writerow(line)
            print("\033c")
            print("Remove complete")
    elif yes == "n":
        print("Remove aborted")
    else:
        print("")
