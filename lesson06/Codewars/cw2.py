'''
Create a function called _if which takes 3 arguments:
a value bool and 2 functions (which do not take any parameters):
func1 and func2
'''
def _if(bool, func1, func2):
    if bool: return func1()
    return func2()

'''
alternative

def _if(bool, func1, func2):
    return func1() if bool else func2()
    
_if = lambda b, f, g: f() if b else g()

def _if(bool, func1, func2):
    return {True: func1, False: func2}[bool]()
    
def _if(bool, func1, func2):
  return [func2, func1][bool]()


'''