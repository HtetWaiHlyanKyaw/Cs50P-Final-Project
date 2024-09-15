from datetime import date, datetime
import pyfiglet
import csv
import os
from tabulate import tabulate
from tasks import Task
import re

commands = ["create", "delete", "quit", "help", "show"]

priorities = ["high", "low", "medium"]

tasks = []

"""create function is used to create a new task"""


def validate_create():
    while True:
        try:
            task = input("Task Name                    : ").strip()
            deadline = input("Deadline (YYYY-MM-DD)        : ").strip()
            datetime.strptime(deadline, "%Y-%m-%d")
            priority = input("Priority (low/medium/high)   : ").strip().lower()
            if not priority in priorities:
                raise ValueError
            confirmation = (
                input("Are you sure you want to create a new task? [yes/no] ")
                .strip()
                .lower()
            )
            return create(task, deadline, priority, confirmation)
        except ValueError:
            print("Invalid input.")
            continue
        except EOFError:
            return "\nDiscarded."


def create(task, deadline, priority, confirmation):

    if confirmation == "yes":
        id = 1
        if tasks:
            id = tasks[-1]._id + 1
        task = Task(id, task, priority, deadline)
        tasks.append(task)
        return "Successfully created 1 task ->" + str(task)
    return "Discarded."


"""help function is used to list available commands"""


def help():
    return "\nList of available commands\n---------------------------\n>> list: list the created tasks\n>> new: create a new task\n>> delete: delete a task\n>> quit: quit the system\n>> help: show available commands\n>> tick: tick a task\n>> untick: untick a task\n>> print: save your tasks as a csv file\n>> open: open a csv file of specified name\n---------------------------"


"""show function is used to list all the tasks in the system"""


def show():
    print("List of tasks")
    print("-------------")
    if not tasks:
        return "You haven't created any tasks"
    task_details = [str(task) for task in tasks]
    return "\n".join(task_details)


"""delete function is used to delete a task with the provided ID"""


def delete():
    try:
        id = int(input("Enter id of task you want to delete.\nID: "))
        for task in tasks:
            if task.id == id:
                if (
                    input(
                        f"Are you sure you want to delete task with ID {task.id} [yes/no] "
                    )
                    == "yes"
                ):
                    tasks.remove(task)
                    return f"Task with ID {id} has been deleted."

        return f"No task found with ID {id}."
    except EOFError:
        return "\nDiscarded."

"""print_csv function is used to print the tasks in a csv file of specified name"""


def print_csv():
    pattern = r"^[a-zA-Z0-9_]+$"
    try:

        file_name = input("Name for your csv file (without extensions): ")
        match = re.search(pattern, file_name)
        if not match:
            raise ValueError
        file_name = file_name + ".csv"
        if (
            input(
                f"Are you sure you want to print tasks in CSV file with name '{file_name}'? [yes/no] "
            )
            == "yes"
        ):
            file_exists = os.path.exists(file_name)
            with open(file_name, "a", newline="") as file:
                fieldnames = [
                    "task",
                    "priority",
                    "deadline",
                    "status",
                    "created",
                    "completed",
                ]

                writer = csv.DictWriter(file, fieldnames=fieldnames)

                if not file_exists:
                    writer.writeheader()
                    # id = 1

                for task in tasks:
                    writer.writerow(
                        {
                            # "id": task.id,
                            "task": task.task,
                            "priority": task.priority,
                            "deadline": task.deadline,
                            "status": task.status,
                            "created": task.created,
                            "completed": task.completed,
                        }
                    )
            tasks.clear()
            return f"Tasks successfully written to {file_name}"

    # except Exception as e:
    #     error = f"An error occurred: {e}. Deleting the file {file_name}."
    #     if os.path.exists(file_name):
    #         os.remove(file_name)
    #     else:
    #         error = "File does not exist to delete."
    #     return error
    except ValueError:
        return "Invalid format."
    except EOFError:
        return "\nDiscarded."


"""tick function is used to tick a task"""


def tick():
    try:
        id = int(input("Enter id of your completed task.\nID: "))
        for task in tasks:
            if task.id == id:
                if (
                    input(f"Are you sure you want to tick task with ID {task.id} [yes/no] ")
                    == "yes"
                ):
                    task.status = True
                    task.completed = date.today()
                    return f"Task with ID {id} has been ticked as completed."

        return f"No task found with ID {id}."
    except EOFError:
        return "\nDiscarded."
    except:
        return "Something went wrong."

"""untick function is used to untick a task"""


def untick():
    try:
        id = int(input("Enter id of the task you want to untick.\nID: "))
        for task in tasks:
            if task.id == id:
                if (
                    input(
                        f"Are you sure you want to untick task with ID {task.id} [yes/no] "
                    )
                    == "yes"
                ):
                    task.status = False
                    task.completed = None
                    return f"Task with ID {id} has been unticked as completed."

        return f"No task found with ID {id}."
    except EOFError:
        return "\nDiscarded."
    except:
        return "Something went wrong."

def tabulate_csv():
    try:
        extracted_tasks = open_csv()
        if extracted_tasks:
            table_data = [
                [
                    task["task"],
                    task["priority"],
                    task["deadline"],
                    task["status"],
                    task["created"],
                    task["completed"],
                ]
                for task in extracted_tasks
            ]
            headers = ["Task", "Priority", "Deadline", "Status", "Created", "Completed"]
            return tabulate(table_data, headers, tablefmt="grid")
        else:
            return ""
    except EOFError:
        return "\nDiscarded."

def open_csv():

    file_name = input("Name for your csv file (with extensions): ").strip()
    extracted_tasks = []
    try:
        with open(file_name, mode="r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                extracted_tasks.append(
                    {
                        "task": row["task"],
                        "priority": row["priority"],
                        "deadline": row["deadline"],
                        "status": row["status"],
                        "created": row["created"],
                        "completed": row["completed"],
                    }
                )
    except FileNotFoundError:
        print(f"The file {file_name} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return extracted_tasks if extracted_tasks else ""


def quit():
    if input("Are you sure you want to exit? [yes/no] ") == "yes":
        print(
            "============================================================================="
        )
        print("exited from task master pro. Thank you Cs50.")
        print(
                "============================================================================="
        )
        return True
    else:
        return False


def main():

    print(
        "============================================================================="
    )
    print(pyfiglet.figlet_format("Task Master Pro", font="slant"))
    print(
        "============================================================================="
    )
    while True:
        try:
            user_input = input("Task Master Pro >> ").strip().lower()
            if user_input == "quit":
                if quit():
                    break
            elif user_input == "new":
                print(validate_create())
            elif user_input == "help":
                print(help())
            elif user_input == "list":
                print(show())
            elif user_input == "delete":
                print(delete())
            elif user_input == "print":
                print(print_csv())
            elif user_input == "tick":
                print(tick())
            elif user_input == "untick":
                print(untick())
            elif user_input == "open":
                print(tabulate_csv())
            else:
                print("Unknown command. Type help for available commands.")
        except EOFError:
            if quit():
                break

if __name__ == "__main__":
    main()
