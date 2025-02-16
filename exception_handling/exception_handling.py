names_tuple = ('Rod', 'Jane', 'Freddy')

try:
    print("####### TRY #######")
    print("The TRY block attempts to run")
    print(f"Original Tuple: {names_tuple}")

    names_sorted_as_list = sorted(names_tuple)
    print(names_sorted_as_list)

    names_sorted_as_list.append("Bungle")
    print("Added Bungle:", names_sorted_as_list)

    print("Attempt to manipulate the tuple...")
    names_tuple[0] = 'Zippy'  # This will raise a TypeError

    print("Is this code reached?")
except FileNotFoundError as error:
    print("####### EXCEPT: FileNotFoundError #######")
    print("The EXCEPT / CATCH block only runs if this error happens")
    print(f"The following file can not be found: {error.filename}. Please try another file")
except TypeError as error:
    print("####### EXCEPT: TypeError #######")
    print("Oh dear, that is not allowed on that type")
    print(error)
except Exception as error:
    print("####### EXCEPT: Exception #######")
    print("Generic catch-all except / catch block")
    print(error)
finally:
    # Always close file handle after use
    print("The FINALLY block ALWAYS runs")
    print("The finally block is used to tidy up")

    if names_tuple:
        names_tuple = None

print("After exception handling is finished...the program can continue")
