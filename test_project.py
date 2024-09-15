import pytest
from project import help, create, validate_create, show, delete, tick, untick, tabulate_csv, open_csv, print_csv, quit
from tasks import Task
from datetime import date
from tabulate import tabulate

"""Testing instance creation and initilization"""


def test_Task():

    task = Task(1, "valid task", "high", "2024-09-15")
    assert task.task == "valid task"
    assert task.deadline == "2024-09-15"
    assert task.created == date.today()
    assert task.priority == "high"
    assert task.status == "unfinished"
    assert task.completed == None
    actual = print(task)
    result = print(
        f"ID: 1|Task: valid task|priority: high|deadline: 2024-09-15|status:  unfinished|created at: {date.today()}|completed at: None"
    )
    assert result == actual


"""Testing create function for both successful and unsuccessful cases: testing confirmation"""


def test_help():
    assert help() == "\nList of available commands\n---------------------------\n>> list: list the created tasks\n>> new: create a new task\n>> delete: delete a task\n>> quit: quit the system\n>> help: show available commands\n>> tick: tick a task\n>> untick: untick a task\n>> print: save your tasks as a csv file\n>> open: open a csv file of specified name\n---------------------------"

def test_create():
    assert (
        create("true case", "2020-12-1", "high", "yes")
        == f"Successfully created 1 task ->ID: 1|Task: true case|priority: high|deadline: 2020-12-1|status:  unfinished|created at: {date.today()}|completed at: None"
    )
    assert create("false case", "2020-12-1", "high", "no") == "Discarded."


"""Testing tick function for both successful and unsuccessful cases"""


def test_tick(monkeypatch):

    inputs_tick_1 = iter([1, "yes"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs_tick_1))
    assert tick() == "Task with ID 1 has been ticked as completed."

    inputs_tick_2 = iter([2, "yes"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs_tick_2))
    assert tick() == "No task found with ID 2."


"""Testing untick function for both successful and unsuccessful cases"""


def test_untick(monkeypatch):

    inputs_untick = iter([1, "yes"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs_untick))
    assert untick() == "Task with ID 1 has been unticked as completed."

    inputs_untick_2 = iter([2, "yes"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs_untick_2))
    assert tick() == "No task found with ID 2."


"""Testing validate create function and while loop"""


def test_validate_create(monkeypatch):
    inputs = iter(
        [
            "while loop test",
            "invalid-date",
            "while loop test",
            "2023-12-31",
            "high",
            "yes",
        ]
    )
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    expected = f"Successfully created 1 task ->ID: 2|Task: while loop test|priority: high|deadline: 2023-12-31|status:  unfinished|created at: {date.today()}|completed at: None"
    actual = validate_create()
    assert expected == actual


"""Testing show function"""


def test_list(monkeypatch):

    inputs_1 = iter(["list test 1", "2023-12-31", "high", "yes"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs_1))
    task_1 = validate_create()

    inputs_2 = iter(["list test 2", "2024-10-10", "medium", "yes"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs_2))
    task_2 = validate_create()

    assert show() == (
        f"ID: 1|Task: true case|priority: high|deadline: 2020-12-1|status:  unfinished|created at: {date.today()}|completed at: None"
        f"\nID: 2|Task: while loop test|priority: high|deadline: 2023-12-31|status:  unfinished|created at: {date.today()}|completed at: None"
        f"\nID: 3|Task: list test 1|priority: high|deadline: 2023-12-31|status:  unfinished|created at: {date.today()}|completed at: None"
        f"\nID: 4|Task: list test 2|priority: medium|deadline: 2024-10-10|status:  unfinished|created at: {date.today()}|completed at: None"
    )


"""Testing delete function for both successful and unsuccessful cases"""


def test_delete(monkeypatch):

    inputs = iter(["list test 1", "2023-12-31", "high", "yes"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    validate_create()

    inputs_delete_1 = iter([6, "yes"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs_delete_1))
    assert delete() == "No task found with ID 6."

    inputs_delete_2 = iter([5, "yes"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs_delete_2))
    assert delete() == "Task with ID 5 has been deleted."


def test_tabulate_csv(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "test.csv")

    assert tabulate_csv() == tabulate(
        [
            ["task 1", "high", "2024-12-3", "completed", "2024-09-13", "2024-09-13"],
            ["task 2", "low", "2024-1-1", "completed", "2024-09-13", "2024-09-13"],
        ],
        headers=["Task", "Priority", "Deadline", "Status", "Created", "Completed"],
        tablefmt="grid"
    )


    monkeypatch.setattr("builtins.input", lambda _: "unkown.csv")

    assert tabulate_csv() == ""

def test_print_csv(monkeypatch):

    monkeypatch.setattr("builtins.input", lambda _: "incorrect_format.csv")
    assert print_csv() == "Invalid format."

    inputs_correct_format = iter(["correct_format", "yes"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs_correct_format))
    assert print_csv() == "Tasks successfully written to correct_format.csv"

def test_quit(monkeypatch):

    monkeypatch.setattr("builtins.input", lambda _: "yes")
    assert quit() == 1
