# creating a tuple of strings
names_tuple= 'Rod', 'Jane', 'Freddy'
# this is a try block, which will execute unless an exception occurs
try:
    # print statement
    print("####### TRY #######")
    # print statement
    print("The TRY block attempts to run")
    # printing the original tuple through an if statement
    print(f"Original Tuple: {names_tuple}")
    # sorting the tuple as list in ascending order, which ends up being in alphabetical order
    names_sorted_as_list = sorted(names_tuple)
    # appending Bungle to the list
    names_sorted_as_list.append("Bungle")
    # printing the list
    print("Added Bungle:", names_sorted_as_list)
    print("Attempt to manipulate the tuple...")
    # trying to change the first position in the tuple to Zippy, but tuples are immutable
    names_tuple[0] = 'Zippy'
    print("Is this code reached?")
# except blocks run depending on the type of error
# because it is a Type error, the second except block is executed
# prints some print statements followed by the error message
except FileNotFoundError as error:
    print("####### EXCEPT: FileNotFoundError #######")
    print("The EXCEPT / CATCH block only runs if this error happens")
    print(f"The following file can not be found: {error.filename}. Please try another file")
except TypeError as error:
    print("######## EXCEPT: Type Error #######")
    print("Oh dear, that is not allowed on that type")
    print(error)
except Exception as error:
    print("####### EXCEPT: Exception ########")
    print("Generic catch-all except/ catch block")
    print(error)
# the final block just runs
finally:
    # Always close file handle after use
    print("The FINALLY block ALWAYS runs")
    print("The finally block is used to tidy up")
    if names_tuple:
        names_tuple=None
# this reassigns the tumple to an empty value