def parse_expression(expression):
    num = 0
    stack = []
    sign = 1
    result = 0
    i = 0

    while i < len(expression):
        char = expression[i]

        if char.isdigit():
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            result += sign * num
            continue

        if char == '+':
            sign = 1
        elif char == '-':
            sign = -1
        elif char == '*':
            i += 1
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            result *= num
            continue
        elif char == '/':
            i += 1
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            if num != 0:
                result //= num 
            else:
                return "Error: Division by zero."
            continue

        i += 1

    return result

print("Simple Calculator")
print("Enter a mathematical expression using integers and operators (+, -, *, /).")

expression = input("Enter expression: ")
expression = expression.replace(" ", "")
print(f"Expression: {expression}")

result = parse_expression(expression)
print(f"Result: {result}")