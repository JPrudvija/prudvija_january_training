#Question 3
def save_error(error, errors=None):
    # If errors is None, create a new empty list
    #Because we used errors is equal to None here which means when we call the function a nwe list is created, does not have stroed data
    # This avoids using a mutable object as a default parameter
    if errors is None:
        errors = []
    # Add the error to the list
    errors.append(error)
    # Return the current error list
    return errors
print(save_error("E1"))
print(save_error("E2"))
print(save_error("E3"))
