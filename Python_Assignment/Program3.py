class Calculator:
    def square(self, num):
    
        return num ** 2
    
    def cube(self, num):
        
        return num ** 3

calc = Calculator()
print("Square:", calc.square(5))  
print("Cube:", calc.cube(5))   