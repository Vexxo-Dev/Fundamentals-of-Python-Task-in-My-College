def changetotitle(text):
    """
    This function changes the input text to title case.

    Parameters:
    text (str): The input string to be converted to title case.

    Returns:
    str: The title-cased version of the input string.
    """
    if str.istitle(text):
        print("\nyour sentence is already title")
    else:
        print('\n',str.title(text))

##########################################

text = input("Enter your sentence: ")

changetotitle(text)