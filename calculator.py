import re

def calculator(number1, number2, operator):
    number1=float(number1)
    number2=float(number2)
    if(operator=="+"):
        return(float(number1+number2))
    if(operator=="-"):
        return(float(number1-number2))
    if(operator=="*"):
        return(float(number1*number2))
    if(operator=="/"):
        return(float(number1/number2))
    if(operator--"//"):
        return(float(number1//number2))
    if(operator=="**"):
        return(float(number1**number2))
    else:
        return False

def parse_input():
    numbers1=""
    numbers2=""
    number1finished="False"
    MathProblem=input("Enter equation: ")
    # Assigning MathProblem as any equation you would put in a calculator
    answer=re.findall(r'[0-9\.]+',MathProblem)
    print(calculator(answer[0], answer[2], answer[1]))
    # Display the answer inputed in the calculator

               
    
