# Aim: To manage tasks using stack and queue operations.


# ---------- Stack Operations ----------
# Stack follows LIFO (Last In, First Out)

stack = []

def add_task_stack(task):
    stack.append(task)

def complete_task_stack():
    if len(stack) == 0:
        print("No tasks in stack.")
    else:
        task = stack.pop()
        print("Completed task:", task)

def display_stack():
    print("Stack tasks:", stack)


# ---------- Queue Operations ----------
# Queue follows FIFO (First In, First Out)

queue = []

def add_task_queue(task):
    queue.append(task)

def complete_task_queue():
    if len(queue) == 0:
        print("No tasks in queue.")
    else:
        task = queue.pop(0)
        print("Completed task:", task)

def display_queue():
    print("Queue tasks:", queue)


# ---------- Main Program ----------

print("STACK - TASK MANAGEMENT")

add_task_stack("Study Python")
add_task_stack("Complete Assignment")
add_task_stack("Practice DSA")

display_stack()

complete_task_stack()
display_stack()


print("\nQUEUE - TASK MANAGEMENT")

add_task_queue("Attend Lecture")
add_task_queue("Submit Assignment")
add_task_queue("Prepare for Exam")

display_queue()

complete_task_queue()
display_queue()
