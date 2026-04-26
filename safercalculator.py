while True:
    Command=input("Enter the anyt operation on any two numbers:")
    length=len(Command)
    operator=None
    if Command.lower()=="quit":
        break
    for op in "+-*/":
        if op in Command:
            operator = op
            Command = Command.replace(op, " ")
            break
    Command=Command.split()
  

    if operator=='+':
        try:
            result=int(Command[0])+int(Command[1])
            print(result)
        except:
            print("Please enter numbers")
    elif operator=='-':
        try:
            result=int(Command[0])-int(Command[1])
            print(result)
        except:
            print("Please enter numbers")        
    elif operator=='*':
        try:
            result=int(Command[0])*int(Command[1])
            print(result)
        except:
            print("Please enter numbers")
    elif operator=="/":
        try:
            result=int(Command[0])/int(Command[1])
            print(result)
        except:
            print("Please enter numbers and denominator should be not equal to zero")
    elif operator==None:
        print("Enter proper Command")        
    