
class completepython:
    def __init__(self):
            print("__init__ methods")

    def get(self):
           print("get methods")

    def logicmethods(self):
        print("logic methods")
        
    @staticmethod
    def methods():
         print("static  methods")
      
class inherit(completepython): # reuse all methods of completepython
     pass

venkatesh=inherit()
venkatesh.logicmethods()

class reuse(completepython):
    def __init__(self):
            #completepython.__init__(self)
            super().__init__()
            print("reuse __init__ methods")

    def get(self):
           print("get methods")

    def logicmethods(self):
        super().logicmethods()
        print("reuse logic methods")
        
    @staticmethod
    def methods():
         print("static  methods")

breakup = reuse( )
breakup.logicmethods()
         
import Day_10
from jolly import  Rahuldonofpython


try :
    hotchips
except NameError:
    print("rahul is mad boy")


try :
    a=2/0
except Exception:
    print("divison erorr")
    
    
    
