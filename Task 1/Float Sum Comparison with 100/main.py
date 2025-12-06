def comparison(num1,num2):
    """
    This function compares the sum of two floating-point numbers to 100.

    Parameters:
    num1 (float): The first floating-point number.

    num2 (float): The second floating-point number.
    
    Returns:
    None
    """

    if num1+num2 >= 100:
        return "More than 100"
    else:

        return "Less than 100"

##########################################
    
num1= float(input("Enter Number 1: "))
num2= float(input("\nEnter Number 2: "))

result = comparison(num1,num2)

print("\nThe sum of the two numbers is:", result)