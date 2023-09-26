n1 =int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))

class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        
    def add(self):
       return self.num1 + self.num2
        
    def sub(self):
        return self.num1 - self.num2

    def multiply(self):
         return self.num1 * self.num2 
        
    def div(self):
        return self.num1/self.num2
        
obj = Calculator(n1,n2)
x = ('1.Add \n 2.Sub \n 3.Multiply \n 4.Divide ')
print(x)
while True:
   
   
    choice = int(input('Please select one of the following:'))
    if choice == 1:
        print("Result: ",obj.add()) 
        break 
    elif choice ==2:
            print("Result: ",obj.sub()) 
            break 
    elif choice == 3:
        print("Result: ",obj.multiply())   
        break 
    elif choice == 4:
        print("Result: ",obj.div())
        break
    elif choice == 0:
        print('Again try one of the following')
        break
    else:
        print('Invalid option') 
        break 
          

        


 

                

            
    
        