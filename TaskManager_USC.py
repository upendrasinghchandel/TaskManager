# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 21:14:28 2024

@author: Upendra
"""

import os
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user():
    username = input("Enter a new username: ")
    password = input("Enter a new password: ")
    with open("users.txt", "a") as file:
        file.write(f"{username}:{hash_password(password)}\n")
    print("Registration successful! Please log in.")

def authenticate_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    hashed_password = hash_password(password)
    with open("users.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(":")
            if username == stored_username and hashed_password == stored_password:
                print("Login successful!")
                return username
    print("Invalid username or password.")
    return None

def add_task(username):
    task = input("Enter a new task: ")
    with open(f"tasks_{username}.txt", "a") as file:
        file.write(f"{task}:Pending\n")
    print("Task added successfully!")

def view_tasks(username):
    if os.path.exists(f"tasks_{username}.txt"):
        with open(f"tasks_{username}.txt", "r") as file:
            tasks = file.readlines()
            if tasks:
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task.strip()}")
            else:
                print("No tasks found.")
    else:
        print("No tasks found.")

def mark_task_completed(username):
    view_tasks(username)
    task_number = int(input("Enter the task number to mark as completed: ")) - 1
    if os.path.exists(f"tasks_{username}.txt"):
        with open(f"tasks_{username}.txt", "r") as file:
            tasks = file.readlines()
        if 0 <= task_number < len(tasks):
            tasks[task_number] = tasks[task_number].replace("Pending", "Completed")
            with open(f"tasks_{username}.txt", "w") as file:
                file.writelines(tasks)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

def delete_task(username):
    view_tasks(username)
    task_number = int(input("Enter the task number to delete: ")) - 1
    if os.path.exists(f"tasks_{username}.txt"):
        with open(f"tasks_{username}.txt", "r") as file:
            tasks = file.readlines()
        if 0 <= task_number < len(tasks):
            del tasks[task_number]
            with open(f"tasks_{username}.txt", "w") as file:
                file.writelines(tasks)
            print("Task deleted.")
        else:
            print("Invalid task number.")

def main():
    while True:
        print("\nWelcome to the Task Manager!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            register_user()
        elif choice == "2":
            username = authenticate_user()
            if username:
                while True:
                    print("\nTask Manager Menu")
                    print("1. Add Task")
                    print("2. View Tasks")
                    print("3. Mark Task as Completed")
                    print("4. Delete Task")
                    print("5. Logout")
                    user_choice = input("Choose an option: ")
                    if user_choice == "1":
                        add_task(username)
                    elif user_choice == "2":
                        view_tasks(username)
                    elif user_choice == "3":
                        mark_task_completed(username)
                    elif user_choice == "4":
                        delete_task(username)
                    elif user_choice == "5":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid option, try again.")
        elif choice == "3":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
