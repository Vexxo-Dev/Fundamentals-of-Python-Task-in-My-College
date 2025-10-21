def affordable(product,yourmoney):
    """
    This function checks if the product price exceeds your budget.

    Parameters:
    product (int): The price of the product.
    yourmoney (int): Your budget amount.

    Returns:
    int: Returns 1 if product price exceeds budget, otherwise returns 0.
    """
    if product > yourmoney:
        return 1
    else:
        return 0
    
##########################################

product = int(input("Enter Product Price: "))

yourmoney = int(input("\nEnter Your Budget: "))

res1 = product - yourmoney

res2 = yourmoney - product

if affordable(product,yourmoney) == 1:
   
   print(f"\nYour Need {res1}") 
else:
    print(f"\nYou can buy product and your money after buy = {res2}\n")