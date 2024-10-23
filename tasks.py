import pandas as pd

def prompt_action():

    task_table = pd.DataFrame(columns=["TaskID", "Task", "CompletionStatus"])

    while True: 
        action = input("Your move (Enter number as stated below): \n"
                    "1: Create a task \n"
                    "2: View a list of incomplete tasks \n"
                    "3: Mark a task as completed \n"
                    "4: EXIT \n")

        if action ==  "1":
            taskname = input("Enter name of task: \n")
            taskid = len(task_table)+1
            new_row = {'TaskID': taskid, 'Task': taskname, 'CompletionStatus': "Incomplete"}
            task_table = pd.concat([task_table, pd.DataFrame([new_row])], ignore_index=True)

        elif action == "2": 
            incomplete_tasks_table = task_table[(task_table.CompletionStatus == "Incomplete")]
            print(incomplete_tasks_table)
            print("\n\n")

        elif action == "3":
            taskid = input("Enter the TaskID of the task you have completed: \n")
            try:
                taskid = int(taskid)
                task_table.loc[task_table['TaskID'] == taskid, 'CompletionStatus'] = 'Completed'
                print(f"Task ID {taskid} marked as completed.")
            except ValueError:
                print("Invalid TaskID. Please enter a valid number.")

        elif action == "4":
            return

prompt_action()
