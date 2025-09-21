#!/usr/bin/python3

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match (priority, time_bound):
    case ("high", "yes"):
        print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    case ("high", "no"):
        print(f"Reminder: Your high-priority task '{task}' is not time-bound, but should be prioritized.")
    case ("medium", "yes"):
        print(f"Reminder: Your medium-priority task '{task}' is time-bound. Please plan accordingly.")
    case ("medium", "no"):
        print(f"Reminder: Your medium-priority task '{task}' is not time-bound. Address it when possible.")
    case ("low", "yes"):
        print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")
    case ("low", "no"):
        print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid input for priority or time-bound status. Please enter valid values.")