def add(num1,num2):
    return num1 +num2
def subtract(num1,num2):
    return num1-num2
def multiplication(num1,num2):
    return num1*num2
def division(num1,num2):
    num1/num2

# Creating dictionary to save the key and values
symbols={
    "+":add,
    "-":subtract,
    "*":multiplication,
    "/":division
}
def calculator():
    num1=float(input("Enter first number: "))
    for symbol in symbols:
        print(symbol)
    should_continue=True
    while should_continue:
        operation_symbol=input("Chose an operation: ")
        num2 = float(input("Enter next number: "))
        calculation_function=symbols[operation_symbol]
        answer=calculation_function(num1,num2)
        print(f"{num1}{operation_symbol}{num2}={answer}")

        if input("type y to continue with the {answer} or type 'n' to start new: ")=="y":
            num1=answer
        else:
            should_continue=False
            calculator()
calculator()