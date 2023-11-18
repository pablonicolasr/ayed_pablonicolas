# Pablo Nicolas Ramos
# linkedin: https://ar.linkedin.com/in/pablonicolasr

import os


class ClearScreen:
    
    def __init__(self):
    
        pass
    
    def clear(self):
        
        # clear the screen
    
        return os.system("cls" if os.name=="nt" else "clear")
        


def fibonacci(n):
    
    if n == 0 or n == 1:
        
        return n
        
    else:
        
        return fibonacci(n - 1) + fibonacci(n - 2)       


if __name__ == "__main__":
    
    '''Exercised:    
    Implement a function that allow to obtain the value of
    Fibonacci Sequence for a given number    
    '''
    
    band = False
    
    while not band:
        '''
        Ask if the user wants to introduce a new number
        '''
        flag = False
        while not flag:        
            try:
                number = int(input("Please, you must to introduce a natural number: \n"))
                if number < 0:
                    print("You are wrong. You must to introduce a natural number, please\n")
                    input("Press any key to continue...\n")
                    ClearScreen().clear
                else:
                    print(f"You introduce a valid number. This number is: {number}\n")
                    input("Press any key to continue...\n")
                    ClearScreen().clear
                    flag = True
            except Exception as e:
                print(str(e)+"\n")
                print("You must enter an integer\n")
                input("Press any key to continue...\n")
                ClearScreen().clear
        
        
        result = fibonacci(number)       
        
        print(f"The result of Fibonacci Sequence for the {number} term is: {result}\n")
        input("Press any key to continue...\n")
                
        correct = False       
        while not correct:
            answer = str(input("Do you want to introduce a new number?: (S/N)\n"))
            if answer.upper() != "S" and answer.upper() != "N":
                print("Please, introduce only S or N\n")
                input("Press any key to continue...\n")
                ClearScreen().clear
            elif answer.upper() == "N":
                print("You finish the algorithm\n")
                input("Press any key to continue...\n")
                correct = True
                band = True
            else:
                correct = True
            
            
    
    
        
    
    
    