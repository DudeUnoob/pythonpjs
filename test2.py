import random

print("this shows the rational function evaluated close to 1")
print("My guess is 1.2")

def math_gen(x):
    expression1 = x**2-1
    expression2 = x-1

    final_expression = (expression1)/(expression2)
    #print(final_expression)
    random_num(final_expression)



def random_num (x):

   i=0
   for i in range(8):
    x = x/10
 
    print(x)
    #print(x)
    #print (i)
    #math_gen(x)
    
        

   



#random_num(4)

math_gen(1.1)

print("My guess was a little off")
