
##[type]              [container/flat seq]  [changable/unchangable seq]
##list                container             change 
##tuple               container             unchange
##str                 flat                  unchange
##dict                container             change
##collections.deque   container             change
#
import collections

def is_editable(obj):
    try:
        obj.__getattribute__("__setitem__")
        print(f'{obj.__class__.__name__} is mutable')
        
    except AttributeError:
        print(f"{obj.__class__.__name__} is immutable")

if __name__ == '__main__':  
    example_list = [1, 2, 3, 4, 5]      
    is_editable(example_list)