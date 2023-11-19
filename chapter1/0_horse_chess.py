# Pablo Nicolas Ramos
# linkedin: https://ar.linkedin.com/in/pablonicolasr

import os


class ClearScreen:
    
    def __init__(self):
    
        pass
    
    def clear(self):
        
        # clear the screen
    
        return os.system("cls" if os.name=="nt" else "clear")


class HorseMobile:

    def __init__(self, num):
        
        # Create the numbers in mobile phone
        self.board = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [None, 0, None]
        ]
        
        # shape of board, row x column
        self.dimension = (len(self.board), len(self.board[0]))        
        
        # number of movements
        self.num = num                      
         
                
    def PossibleMovement(self, i, j):
    
        # Third step function
        
        count = 0
        
        num_list = []
        
        post_list = []
        
        combinations = [(2, 1), (2, -1), (-2, -1), (-2, 1), (1, 2), (1, -2), (-1, -2), (-1, 2)]
        
        for c in combinations:
            
            if c[0] > 0 and c[1] > 0:                
                
                if i + c[0] < self.dimension[0] and j + c[1] < self.dimension[1]:
                    
                    if self.board[i + c[0]][j + c[1]] is not None and self.board[i + c[0]][j + c[1]] not in num_list:
                        
                        count += 1
                
                        num_list.append(self.board[i + c[0]][j + c[1]])
                        
                        post_list.append([i + c[0], j + c[1]])            
                        
            
            elif c[0] > 0 and c[1] < 0:
                
                if i + c[0] < self.dimension[0] and j + c[1] >= 0:
                    
                    if self.board[i + c[0]][j + c[1]] is not None and self.board[i + c[0]][j + c[1]] not in num_list:
                        
                        count += 1
                
                        num_list.append(self.board[i + c[0]][j + c[1]])
                        
                        post_list.append([i + c[0], j + c[1]]) 
            
            elif c[0] < 0 and c[1] < 0:
                
                if i + c[0] >= 0 and j + c[1] >= 0:
                    
                    if self.board[i + c[0]][j + c[1]] is not None and self.board[i + c[0]][j + c[1]] not in num_list:
                        
                        count += 1
                
                        num_list.append(self.board[i + c[0]][j + c[1]])
                        
                        post_list.append([i + c[0], j + c[1]])
            
            elif c[0] < 0 and c[1] > 0:
                
                if i + c[0] >= 0 and j + c[1] < self.dimension[1]:
                    
                    if self.board[i + c[0]][j + c[1]] is not None and self.board[i + c[0]][j + c[1]] not in num_list:
                        
                        count += 1
                
                        num_list.append(self.board[i + c[0]][j + c[1]])
                        
                        post_list.append([i + c[0], j + c[1]])
            
        return count, post_list, num_list
        
    
    def CountMovements(self):
    
        '''This function consist in iterate for every number of mobile phone, and call PossibleMovement function'''
    
        # Second step function
    
        lista = [] # Create an empty list
        
        for i, value in enumerate(self.board): # 0 to 3
        
            lista_row = [] # Create an empty list (row)
            
            for j, val in enumerate(value): # Iterate column in row i
                
                if self.board[i][j] is not None: # If the value != None, evaluate  
                    
                    lista_row.append(self.PossibleMovement(i, j)[1]) # Add the second element of a tuple in self.PossibleMovement function
                    
                else:
                
                    lista_row.append([])
                    
            
            lista.append(lista_row)        
        
        return lista 
    
       
        
    def TreeOrig(self):
        
        # First step function
        
        lista = self.CountMovements() # 
        
        cantidad = 0
        
        a = 1
        
        while a < self.num:        
        
            for i, value in enumerate(lista):
                
                for j, val in enumerate(value):    
                    
                    if len(lista[i][j]) > 0:

                        aux_list = []
                            
                        for x, valor in enumerate(lista[i][j]):           
                                
                            aux_list += self.PossibleMovement(valor[0], valor[1])[1]                            
                        
                        lista[i][j] = aux_list
                                            
            a += 1                                
                           
        
        suma = 0
        
        print(f"lista {lista}")
        
        for u, value in enumerate(lista):
            
            for v, val in enumerate(value):
               
                suma += len(val)
            
                                
        return suma 
            
                    
if __name__ == "__main__":
    
    band = False
    while not band:
        # Define the number of movements    
        try:
            number = int(input("Enter the number of movements: "))
            if number in range(1, 33):
                band = True
            else:
                print("You must enter a number in range [1, 33)\n")
                input("Press any key to continue...")
                ClearScreen().clear
        except Exception as e:
            print(str(e)+"\n")
            print("You must enter an integer\n")
            input("Press any key to continue...")
            ClearScreen().clear
    
    
    cantidad_movimientos = HorseMobile(number).TreeOrig()
    print(cantidad_movimientos)     
        