# Aim: To implement stack operations and
# convert infix expression to postfix.


# Stack implementation
stack = []


# Push operation
def push(item):
    stack.append(item)


# Pop operation
def pop():
    if len(stack) == 0:
        return None
    return stack.pop()


# Display stack
def display():
    print("Stack:", stack)


# Operator precedence
def precedence(operator):
    if operator == '^':
        return 3
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '+' or operator == '-':
        return 1
    else:
        return 0


# Infix to Postfix conversion
def infix_to_postfix(expression):
    operators = []
    postfix = ""

    for char in expression:

        # If character is an operand
        if char.isalnum():
            postfix += char

        # If opening bracket
        elif char == '(':
            operators.append(char)

        # If closing bracket
        elif char == ')':
            while operators and operators[-1] != '(':
                postfix += operators.pop()

            if operators:
                operators.pop()

        # If operator
        else:
            while (operators and operators[-1] != '(' and
                   precedence(operators[-1]) >= precedence(char)):
                postfix += operators.pop()

            operators.append(char)

    # Pop remaining operators
    while operators:
        postfix += operators.pop()

    return postfix


# ---------- Main Program ----------

print("STACK OPERATIONS")

push(10)
push(20)
push(30)

display()

print("Popped element:", pop())

display()


print("\nINFIX TO POSTFIX")

infix = input("Enter an infix expression: ")

postfix = infix_to_postfix(infix)

print("Postfix expression:", postfix)
