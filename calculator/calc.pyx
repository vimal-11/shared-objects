from utility.utils import db

def add(a,b):
    c = db(a,b)
    print(c)
    return a+b

def sub(a,b):
    return a-b