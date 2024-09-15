# Task Master Pro

**Task Master Pro** is a command-line interface (CLI) application designed for managing tasks efficiently. As its name suggests, it helps you keep track of tasks, manage them, and interact with CSV files for saving and reading task data.


##Video Demo:  https://youtu.be/ez4Kezpx5lo
## Features

- **List Tasks**: View all created tasks.
- **Create New Task**: Add a new task with details including name, deadline, and priority.
- **Delete Task**: Remove a task by its ID.
- **Tick Task**: Mark a task as completed.
- **Untick Task**: Undo the completion status of a task.
- **Print Tasks**: Save all tasks to a CSV file.
- **Open CSV File**: Open and review a CSV file containing tasks.
- **Help**: Display available commands.
- **Quit**: Exit the system.

## Commands

### `list`
Lists all created tasks starting from ID 1.

### `new`
Creates a new task. You will be prompted to provide:
- Task Name
- Deadline (format: YYYY-MM-DD)
- Priority (high, medium, low)

If the deadline or priority format is incorrect, you will be prompted to re-enter the information. Press `Ctrl+D` to cancel task creation. Upon successful creation, task details will be displayed, including:
- ID
- Name
- Priority
- Deadline
- Status
- Created Date
- Completed Date (initially empty)

### `delete`
Deletes a task by specifying its ID. The task will only be deleted if the ID is known.

### `tick`
Marks a task as completed. The status will change to "completed," and the completion date will be recorded.

### `untick`
Reverts the status of a task from completed to unfinished.

### `print`
Saves tasks to a CSV file. You need to provide a filename without an extension. If the filename exists, new tasks will be appended below the existing ones. Invalid formats or filenames with extensions will be discarded.

### `open`
Opens a CSV file to review tasks. The file name must include the extension. Invalid formats or filenames without extensions will be discarded.

### `help`
Displays a list of available commands.

### `quit`
Exits the system. You can also use `Ctrl+D` to quit.

## Handling User Inputs

- If incorrect input is provided during task creation or file operations, the system will prompt the user to re-enter the correct information.
- You can cancel any ongoing operation by pressing `Ctrl+D`.
- The system confirms each action and allows you to discard changes in progress.

## Testing

The system has been tested using `test_project.py` to ensure all functionalities are working as expected.


