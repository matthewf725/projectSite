from binary_search_tree import *

def printValues(instanceOfObject):
    objects = vars(instanceOfObject)
    subObjectVals = list(objects.values())
    subObjectKeys = list(objects.keys())     
    for i in range(len(subObjectVals)):
        if(hasattr(subObjectVals[i], "__dict__")):
            print(objects[subObjectKeys[i]])
            printValues(subObjectVals[i])
        else:
            print("    " + subObjectKeys[i] + ": " + str(subObjectVals[i]))

# Create an instance of the class
instance = BinarySearchTree()  # Replace with your actual class instance
instance.insert(5, "stuff")
instance.insert(6, "stuff")
instance.insert(7, "stuff")
instance.insert(8, "stuff")
instance.insert(2, "stuff")
instance.insert(4, "stuff")
printValues(instance)
