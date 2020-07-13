import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-x", "--x", type=int, help="the base")
parser.add_argument("-y", "--y", type=int, help="the exponent")
parser.add_argument("-v", "--v", default=0, type=int, help="the result will be multiplied by 'v'")
args = vars(parser.parse_args())

def exponent(x, y, v=None):
    result = x ** y
    return (result * v) if v else result
print("####################")
print(type(args))
print(args)
base = args["x"]
exp = args["y"]
v = args["v"]
result = exponent(x=base, y=exp, v=v)
print("\nThe operation was: (x^y)*v (if v exists)")
print("(" + str(base) + "^" + str(exp) + ")" + "*" + str(v) + "[if exists]" + " = " + str(result))
print("The final result is:", result)
print("####################")
# TO RUN: 
#"python z:/Data_Science/TheBridge/Content/Contenido_Curso/data_science_jun_2020/week5/day1/theory/python/arg_parse.py -x 2 -y 4 -v 2"

# 1
# python o python3 
# 2
# ruta al fichero 
# 3
# args

# 'python' 'ruta' 'args'
 