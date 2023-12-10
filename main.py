print("hello world")
# write some code with 5 functions all need to do something also class

def func1():
    print("func10")
    
def func2():
    print("func2")
    
def func3():
    print("func3")

def func4():
    print("func4")
    
def func5():
    print("func5")
    
class MyClass:
    
    def __init__(self):
        print("MyClass")
    
    def func1(self):
        print("func1")
        
        
        
if __name__ == "__main__":
    func1()
    func2()
    func3()
    func4()
    func5()
    myclass = MyClass()
    myclass.func1()