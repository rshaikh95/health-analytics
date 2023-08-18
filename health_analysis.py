import pandas as pd
import numpy as np

num = 1
num2 = 5
str = 'Rahil'

my_list = [num, str, 2, "shaikh"]

dict = {
    "str2": "Rahil2",
    "my_list2": [num, str, num2, "List"],
    "NestD": {
        'detail2':'something',
        'detail3':'something2',
        'detail4':'something3'
    }
}

def Cholesterol(LDL, HDL):
    # LDL
    if LDL <= 100:
        LDL_output = 'Heart-Healthy'
    else:
        LDL_output = 'Not Heart-Healthy'
    # HDL 
    if HDL >= 60:
        HDL_output = 'Heart-Healthy'
    else:
        HDL_output = 'Not Heart-Healthy'
    output = [LDL_output, HDL_output]
    return output 
chl_result = Cholesterol(120, 70)



print(num2)
print(str)
print(my_list)
print(dict)
print("Cholesterol Analysis:", chl_result)

