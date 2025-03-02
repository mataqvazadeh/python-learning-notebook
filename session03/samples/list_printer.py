"""
This module has all functions for printing lists
"""

def print_pretty(lst: list, message: str, sep:str=', ', end:str='\n') -> None:
    """ 
        This function print lists pretty.
        I love this function

        Parameters:
            - lst : is a list that we want to print
            - message : is a message to print before list
            - sep : is elements separator
            - end : is list ending character
    """
    print(f'{message} = {{', end='')
    for index, element in enumerate(lst):
        if index == (len(lst) - 1):
            print(element,end=f'}}{end}')
        else:
            print(element, end=sep)


def print_stupid(lst: list) -> None:
    print(lst)