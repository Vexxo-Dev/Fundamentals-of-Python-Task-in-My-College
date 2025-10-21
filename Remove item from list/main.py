def remove_from_list(item, lst):
    """
    Removes the first occurrence of item from the list lst.
    
    Parameters:
    item: The item to be removed from the list.
    lst (list): The list from which the item will be removed.
    
    Returns:
    list: The list after removing the item.
    """
    
    lst.remove(item)
    return lst

##########################################

my_list = [1, 2, 3, 4, 2]

item_to_remove = int(input("Enter the item to remove: "))

if item_to_remove in my_list:
    updated_list = remove_from_list(item_to_remove, my_list)

    print("Updated list:", updated_list)

else:
    print("Item not found in the list.")