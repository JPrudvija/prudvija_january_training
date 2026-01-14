#Question 1
def count_message(msg, count=0):
    """
    msg   : message passed to the function
    count : default parameter (immutable integer)
    As we know integers are immutable,the value of count does not change.Increment happens only inside that call.
    When we call count_message function, again count start from zero.
    """
    count += 1
    print(f"Message: {msg}, Count: {count}")
    return count
count_message("heya")
count_message("heya")
count_message("Prudvi")