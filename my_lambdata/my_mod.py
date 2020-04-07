def enlarge(n):
    """
    Param is a number 
    Function will enlarge the number 

    """
    return n * 100

    # if in global scope this will mess up our ability to 
    # ..to import other functions 
    # so we need to nest if under the main conditional 

# x = int(input("please choose a number like 5 "))
# result = enlarge(x)
# print(result)

if __name__ == "__main__":
    # special conditional
    # only invoke the code below 
    # if running this file from command line 
    # not if importing from another file 
    # pass
    x = int(input("please choose a number like 5 "))
    result = enlarge(x)
    print(result)