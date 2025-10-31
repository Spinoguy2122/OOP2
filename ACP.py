class ExpressionSolver:


    def __init__(self, expression_string):
       
        self.expression = expression_string
        self.result = None 

    def evaluate_expression(self):
       
        
            self.result = eval(self.expression)
            print(f"Expression '{self.expression}' evaluated successfully.")
       
        

    def get_result(self):
        
        return self.result

    def print_result(self):
       
        if self.result is not None:
            print(f"The result of the expression '{self.expression}' is: {self.result}")
        


if __name__ == "__main__":
    print("--- Expression Solver using OOP ---")

    
    expression1 = "10 + 5"
    solver1 = ExpressionSolver(expression1) 
    solver1.evaluate_expression()           
    solver1.print_result()                  
    print("-" * 30)

    
    expression2 = "(7 + 3) * 2 - 4 / 2"
    solver2 = ExpressionSolver(expression2) 
    solver2.evaluate_expression()
    solver2.print_result()
    print("-" * 30)

    
   
   
    

   
    
