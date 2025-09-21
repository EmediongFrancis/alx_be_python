#!/usr/bin/python3

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

reminder = ""

match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task."
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task."
    case _:
        reminder = f"Reminder: Your task '{task}' has an undefined priority level."

if time_bound == "yes":
    reminder = f"Reminder: {reminder} that requires immediate attention today!"
else:
    if priority == "low":
        reminder = f"Note: {reminder}. Consider completing it when you have free time."
    else:
        reminder = f"Reminder: {reminder}. Consider completing it when you have free time."
print(reminder)