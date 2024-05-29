while True:
    user_input1 = input("Enter a decimal or an integer: ")
    user_input2 = input("Enter a decimal or an integer: ")
    try:
        user_input1 = float(user_input1)  
        user_input2 = float(user_input2)

        if user_input1.is_integer():  
            print("Valid input!")
            break  
    except ValueError:
        pass  
        if user_input2.is_integer():  
            print("Valid input!")
            break  
    except ValueError:
        pass 

while True:
    oper = input(" (1 For Add) (2 for Sub) (3 for Div) (4 for Mul): ")
    try:
        oper = int(oper)  
        if 1 <= oper <= 4:  
            print("Valid input!")
            break  
    except ValueError:
        pass  
    
    print("Invalid input! Please enter a number between 1 and 4.")

def add (user_input1, user_input2):
    if oper == 1:
        print (user_input1 + user_input2)
add (user_input1, user_input2)

def sub (user_input1, user_input2):
    if oper == 2:
        print (user_input1 - user_input2)
sub (user_input1, user_input2)

def div (user_input1, user_input2):
    if oper == 3:
        print (user_input1 / user_input2)
div (user_input1, user_input2)

def mult (user_input1, user_input2):
    if oper == 1:
        print (user_input1 * user_input2)
mult (user_input1, user_input2)