import os, sys, argparse

def __get_root_project(number_of_descent): 
    # For .py files
    __file = __file__ 
    print("__file__", __file__)
    # For .ipynb files
    #__file = os.getcwd()
    for _ in range(number_of_descent):
        __file = os.path.dirname(__file)
    sys.path.append(__file)
    sys.path = list(set(sys.path))

# Step 1: set root folder '5 up'
__get_root_project(number_of_descent=5)

# Step 2: import
from week5.day1.theory.python.my_module import suma

if __name__ == "__main__":
    
    # Step 3: argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--a", type=int, help="num x")
    parser.add_argument("-b", "--b", type=int, help="the exponent")
    args = vars(parser.parse_args())
    num_a = args["a"]
    num_b = args["b"]
    
    # Step 4: use imported function with argparse vars
    result = suma(num_a, num_b)
    print("Final result:\n", result)
    
    
    
    
    