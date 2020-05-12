# 6kyu - Silent Import

""" As part of your spy training, You were taught to be as stealthy as possible while carrying out missions. 
This time, you have to silently import modules from a without getting caught. Most of your peers are skeptical 
if you will be able to do this. But, you are the G.O.A.T and you always have a plan.

Write a function silent_thief that will import any module passed in to it and return it.

Your code must NOT:

    Contain the word import
    Contain any double underscores: __
    Use either eval or exec. """


# def silent_thief(module_name):
#     return globals()['_''_builtins_''_']['_''_imp''ort_''_'](module_name)

silent_thief = globals()['_'+'_builtins_'+'_']['_'+'_im'+'port_'+'_']    

math = silent_thief("math")
import math as also_math
q = math, also_math
q
