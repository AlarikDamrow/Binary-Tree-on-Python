#Alarik Damrow CECS 328 9 Feb 2024
class TreeNode: #TreeNode creator function
    def __init__(self, val=0, left=None, right=None): #What the node would look like
        self.val = val # Has a set value but defaults to zero
        self.left = left # Whatever is declared to be left will be for this node unless default
        self.right = right # Whatever is declared to be right will be for this node unless default

#Updates the tree with a value of all 1. 
def traverse(x): # Only way to go down the tree 
    if x is not None: # If there is not a node then do not act
        x.val = 1 # Change value to one
        traverse(x.left) #Go to the left node
        traverse(x.right) #Go to the right node

#Prints the tree as a string.
def print_tree(x): #Function needed to print the whole tree
    if x is None: # If there is none in the current node
        return # Go back to the original statement the was went through prior
    print("TreeNode(", x.val, sep="", end=",") # Print out the current node
    if x.left is None: #If left node is none
        print(None, end=",") #Print none and then a comma
    else: #If left node is anything else other than none
        print_tree(x.left) # Rucursive call this function to act on this node
        print(",",end="") # Print comma after recursive call
    if x.right is None: #If right node is none
        print(None, end="") #Print none
    else: #If right node is anything else other than none
        print_tree(x.right) # Rucursive call this function to act on this node
    print(")", end="")# Print end parathesis and comma after recursive call
    
def my_function(x): # Main function
    ind = 0
    traverse(x)
    print_tree(x)
    print("") # this creates a new line after the printed result


