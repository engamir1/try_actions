

 

# we want to compare between l1 and l2 
# first try to make checker var 

def equal_stacks(s1, s2):
    # Create a checker variable
    # And initialize it with True
    val = True
 
    # Check the size of both stacks
    # Passed as arguments
    if len(s1) != len(s2):
        val = False
        return val
 
    # Compare the top of each stack
    while(len(s1)):
        if s1[0] == s2[0]:
            s1.pop()
            s2.pop()
        else:
            val = False
            break
    # Return the final value
    # Of checker variable val
    return val
 
 
 
 
# Driver Code
# Define two stacks
stack1 = [8, 15, 9, 11]
stack2 = [8, 15, 9, 11]
 
# Pass the above two Stacks to equal_stacks() function
# And check their equality
if equal_stacks(stack1, stack2):
    print("Two stacks are equal!")
else:
    print("Two stacks are not equal!!")
 
# Print the contents of both the stacks
# After their comparison
print(f'\nStack-1 after comparison: {stack1}')
print(f'\nStack-2 after comparison: {stack2}')


