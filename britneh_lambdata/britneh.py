from pandas import DataFrame
df = DataFrame({'state':['CT','CO','CA','TX']})


def enlarge(n):
    """
    Param n is a number
    Function will enlarge the number
    """
    return n*5

#this code breaks our ability to import enlarge from other files if left

y = int(input("Please choose a number"))
print(y, enlarge(y))
