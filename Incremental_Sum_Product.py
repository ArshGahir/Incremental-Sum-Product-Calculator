#Author: Arshveer Gahir

def incremental_sum(start, end, inc):
    #Sum of each number added to the next
    sum = 0   
    for i in range(start,end, inc):
        sum += i
        print(f'{sum-i} + {i} = {sum}')                             # prints sum after every iteration
        
        
    print(f'Sum Total from {start} to {end-1} is {sum}')              # prints the sum result only

def incremental_multiplier(start, end, inc):    
    #Product of each number multiplied to the next, also called a Factorial                           
    product = 1   
    for i in range(start,end, inc):
        product *= i
        print(f'{product/i} x {i} = {product}')                             # prints product after every iteration

        
    print(f'Product Total from {start} to {end-1} is {product}')              # prints the end product only



def main():

    start       =       int(input("Enter the Starting Number: "))               # ask for range start
    end         =       int(input("Enter the Ending Number: "))                 # ask for range end
    increment   =       int(input("Enter the Increment By Amount: "))           # ask for increment amt

    if increment <= 0:
        increment = 1
        print('Increment cannot be Negative or Zero. Increment reset to One')
   
    incremental_sum(start, end, increment)
    incremental_multiplier(start, end, increment)
                                                     

if __name__ == "__main__":
    main()