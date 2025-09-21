#!/usr/bin/python3

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

message = ""

match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        print(f"Invalid priority level '{priority}' entered.")
        message = ""

if message:
    if time_bound == "yes":
        message += " that requires immediate attention today!"
        print(f"Reminder: {message}")
    else:
        if priority == "low":
            message += ". Consider completing it when you have free time."
            print(f"Note: {message}")
        else:
            message += ". Consider completing it when you have free time."
            print(f"Reminder: {message}")