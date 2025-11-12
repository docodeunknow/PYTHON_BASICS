# EXCEPTION HANDING


# this code for print only message which error we have
# except Exception as e:
#     print(e)

class NegetiveNumberError(Exception):
    """custem exception for negetive number user define exception"""
    pass

def add_positive_number(a,b):
    try:
        print("trying to adding number !!!! ")

        if a < 0 or b < 0:
            error = NegetiveNumberError("number must be positive")

            print(f"cutem error : {error}")
        else:
            result  = a + b
    
    except NegetiveNumberError as e:
        print(f"handerl in except block  : {e}")

    except Exception as e:
        print(e)

    else:
        print(f"addition is : {result}")

    finally:
        print("oretion is done")

    return

n1 = int(input("enter the number A :"))
n2 = int(input("enter the numebr B :"))

add_positive_number(n1, n2)

# USE RAISE 

class NegativeNumberError(Exception):
    """Raised when one of the numbers is negative."""
    pass


def add_positive_numbers(a, b):
    try:
        print("Trying to add numbers...")

        # manually raise a custom exception
        if a < 0 or b < 0:
            raise NegativeNumberError("Numbers must be positive!")

        result = a + b

    except NegativeNumberError as e:
        print(f"Custom Error: {e}")
    else:
        print(f"Addition successful! Result = {result}")
    finally:
        print("Operation finished.\n")

n1 = int(input("enter the number A :"))
n2 = int(input("enter the numebr B :"))

add_positive_number(n1, n2)
