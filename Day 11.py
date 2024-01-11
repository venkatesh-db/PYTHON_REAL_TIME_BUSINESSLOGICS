
# kirana store 
# customer1 : { "headshoulder" :2 , "paid":4 }
# customer2 : { "snacks" : [ "lays","hot chips" ,"5 star" ,"munch"] ,  "rice" : [ "idly rice","eating rice"]   ,  "paid":4000}
# customer2 : { "haridie" ,"garnier","paid":15}
# endless customers 
# Shop owner :=>  Total items are most buyed , most profited  , less purchsed items which are not prchased more than onice , total purcahse in day

# Concept of program

# class variables    --> what each customer purchases
# object variables  --> what all customers are buying
# customer           -->  changeitem , return item , 
# Shopowner         -> every customer request of items is stored

# step1: class & method design
# step2: class variables
# step3:  object variables
# step4:  implment methods with statment of operations that is requirmenets
# step5 : requirmements  Total items are most buyed , most profited  , less purchsed items which are not prchased more than onice , total purcahse in day
# step6 : object creation and method calls
# step7 : Logics copy data from one memory instance memory to class memory  or dict to list 

class  Generalstore:
    allitems=[]
    def __init__(self,ask):
         self.asks = ask
         Generalstore.allitems.append(ask)    #logic 1
        
    def changeitem(self, i ):
          self.asks.update(i)

    def returnitem(self,i):
         self.asks.pop(i)

    def  mosytbuyed(self):              # logics performed on class variables       #logic 2
       most = []
       for j in   Generalstore.allitems:   # 3 times executes below code in the block repeadtely
            x=(list)( j.keys())
            most.append(x)
       print(most)
       count =0
       for i in most:                           # 3 times executes code in the block repeadtely if condition is true 
              if "headshoulder" in i: 
                count =count+1
                print("found headshoulder")
                print(count)

    def mostprofited(self):              # logics performed on class variables
        actualprice   = [  { "headshoulder" : 1.50     } ]
        seelingprice  =   {  "headshoulder" : 2   } 
        profit =0
        for i in  actualprice  :  # 3 times executes code in the block repeadtely
              profit =  seelingprice[ "headshoulder"] -  i["headshoulder" ]
        print(profit)
            
    def totalpurchased(self):            # logics performed on class variables        #logic 3
         count =0
         for i in   Generalstore.allitems :  # 3 times executes code in the block repeadtely
             count = count + i["paid"]
         print( " totalpurchased " ,count )
         
    def instnacedisplay(self):
         print(self.asks)  
    
    @staticmethod 
    def display():
        print(Generalstore.allitems)   # works with class variable


venkateh=Generalstore( { "headshoulder" :2 , "paid":4 })
venkateh1=Generalstore({ "snacks" : [ "lays","hot chips" ,"5 star" ,"munch"] ,  "rice" : [ "idly rice","eating rice"]   ,  "paid":4000} )
venkateh2=Generalstore( { "haridie":"garnier", "headshoulder" :2 ,"paid":17})
Generalstore.display()
venkateh.instnacedisplay()
venkateh.changeitem({ "headshoulder" :3 ,  "paid":6  })
venkateh.instnacedisplay()
#venkateh.returnitem("headshoulder" )
venkateh.instnacedisplay()
venkateh.totalpurchased()
venkateh.mosytbuyed()
venkateh.mostprofited()
