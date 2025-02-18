names_tuple = ('Rod', 'Jane', 'Freddy')
# the variable is a tuple (commas) - immutable

try:
    print("####### TRY #######")
    print("The TRY block attempts to run")
    print(f"Original Tuple: {names_tuple}")
    # try block contains code to be tested - if any code raises exception - it can be trapped and handled by except block
    # does not interrupt program running
    # f string contains variable

    names_sorted_as_list = sorted(names_tuple)
    print(names_sorted_as_list)
    # sorted function returns tuple as list in ascending order
    # new variable for the list

    names_sorted_as_list.append("Bungle")
    print("Added Bungle:", names_sorted_as_list)
    # method (.append) adds string to the end of the list (mutable)
    # .append can only add one argument, list can be manipulated
    print("Attempt to manipulate the tuple...")

    names_tuple[0] = 'Zippy'  # This will raise a TypeError
    # attempting to change first item in tuple to 'Zippy'
    # cannot add data to a tuple like you can in a list - Type Error - tuples are immutable

    print("Is this code reached?")
    # print statement is not executed because of the above error - goes straight to 'except' block

except FileNotFoundError as error:
    # exception is an error (in this case - TypeError)
    print("####### EXCEPT: FileNotFoundError #######")
    # this print statement runs as part of the except block
    # this exception is raised when a file/directory is requested but does not exist
    print("The EXCEPT / CATCH block only runs if this error happens")
    print(f"The following file can not be found: {error.filename}. Please try another file")
    # code is not handling files, print statement is ignored.

except TypeError as error:
    print("####### EXCEPT: TypeError #######")
    # this exception is raised when an operation is applied to an object of inappropriate type
    print("Oh dear, that is not allowed on that type")
    # associated value is a string explaining the mismatch
    # print statement works
    print(error)
    # error is a variable name that produces the error message

except Exception as error:
    print("####### EXCEPT: Exception #######")
    print("Generic catch-all except / catch block")
    print(error)
    # handles all errors that weren't caught by previous blocks

finally:
    # always executes even if there wasn't an error
    # Always close file handle after use
    print("The FINALLY block ALWAYS runs")
    print("The finally block is used to tidy up")

    if names_tuple:
        names_tuple = None
    # variable is immutable

print("After exception handling is finished...the program can continue")
# confirms program is not prevented from running because of the error