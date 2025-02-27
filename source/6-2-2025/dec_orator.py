# this code is for if i want decorator for few functions but not for few functions
# gift wrapping
# in few gifts i want gift wrapper but in few i dont want
# so this code is the example of the gift wrapping (if you want you can wrap or leave it)

# give_gift(): 
# This is the actual gift – the core functionality.  It represents the action of giving a gift.

# add_ribbon(gift): This is the decorator factory.
#   It's like the wrapping station where the ribbon is added.  It takes the gift as input.

# wrapper(): This is the actual decorator – the person who adds the ribbon
# .  It adds the extra behavior (printing "Adding a beautiful ribbon!") around the act of giving the gift.

# wrap_gift(gift, add_ribbon_flag): This function controls whether the gift should be wrapped or not.
#  It's like you deciding whether or not to add ribbon to the gift.

# wrapped_present1 = wrap_gift(give_gift, add_ribbon_flag=True): This is like taking the gift to the wrapping 
# station and asking for a ribbon to be added.  wrapped_present1 now represents the gift with the ribbon.

# wrapped_present2 = wrap_gift(give_gift, add_ribbon_flag=False):  
# This is like taking the gift but not asking for a ribbon.  wrapped_present2 is just the original gift.

# wrapped_present1() and wrapped_present2(): These are the actions of giving the gift 
# – either the wrapped version (with ribbon) or the unwrapped version (without ribbon).

def add_ribbon(gift):  # The decorator factory
    def wrapper():  # The actual decorator
        print("Adding a beautiful ribbon!")
        gift()  # The actual gift (function call)
        print("Ribbon added.")
    return wrapper

def give_gift():  # The gift itself (the function)
    print("Here's your gift!")

def wrap_gift(gift, add_ribbon_flag=True):
    if add_ribbon_flag:
        return add_ribbon(gift)  # Apply the decorator
    else:
        return gift  # Return the original function

# Scenario 1: Gift with a ribbon
wrapped_present1 = wrap_gift(give_gift, add_ribbon_flag=True)
wrapped_present1()
print("-" * 20)

# Scenario 2: Gift without a ribbon
wrapped_present2 = wrap_gift(give_gift, add_ribbon_flag=False)
wrapped_present2()
print("-" * 20)

# Scenario 3: Directly applying the decorator
wrapped_present3 = add_ribbon(give_gift)
wrapped_present3()