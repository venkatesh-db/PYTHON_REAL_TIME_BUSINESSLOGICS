
# step1: class & method design
# step2: class variables
# step3:  object variables
# methods & business logics
# step4:  implment methods with statment of operations that is requirmenets
# step5 : requirmements  priveleges for the customer based on amount of donations
# step6 : object creation and method calls
# step7 : Logics copy data from one memory instance memory to class memory  or dict to list 


class  Donations:
    Totaldonars = []
    donor =True
    def __init__(self, amount):                        # method called once when we create object
        if amount >=1 and  amount <= 9999 :
             self.noofpeople =0
             self.donatedamount =amount
             self.date ="18-12-2023"
             self.trustname="Srivani trust"
             Donations.Totaldonars.append(amount )
        elif amount >= 10000 and  amount <= 19999:
             self.noofpeople =1
             self.donatedamount =amount
             self.breakdarshan =1
             self.date ="18-12-2023"
             self.trustname="Srivani trust"
             Donations.Totaldonars.append(amount )
        elif amount >= 20000 and  amount <= 29999 :
             self.noofpeople =2
             self.donatedamount =amount
             self.breakdarshan =2
             self.date ="18-12-2023"
             self.trustname="Srivani trust"
             self.donor =False
             self.privelegies = {}
             Donations.Totaldonars.append(amount )
        elif amount >= 100000 and  amount <= 500000 :
             self.donatedamount =amount
             self.privelegies = { "seva" : "", "darshan":"1day darshan supabhtham", "accomodation": "1 day100","prasadam":"6 laddus","bhaumanam":"blouse piece"}
             self.donor =True
             Donations.Totaldonars.append(amount )
        elif amount >= 10000000 :
            self.donatedamount =amount
            self.privelegies = {"seva":  " 3 suprabhtham", "darshan": [ "3day darshan supabhtham" , " 3 breaks  " ] , "accomodation": "3 day2500","prasadam": [  "10 big laddu","6 laddus"],"bhaumanam":"blouse piece" , "ornaments":"1  god dollars"}
            self.donor =True
            Donations.Totaldonars.append(amount )
            
    def display(self):                      # method can be invoked as many times 
             if self.donor  != Donations.donor :
               print( self.breakdarshan,self.date,  self.trustname)
             elif self.donor  == Donations.donor:
                 print( self.privelegies)

    def features(self):                     # method when to add a features
         if self.donatedamount >= 100000 :
             self.privelegies["homam"]= "sit one family god homam1 day"  # add one more key in dict
         else:
             self.homam="See live homam"

    def Totaldonations(self):
          count =0
          for i  in Donations.Totaldonars :   # value of list is added to another value
               count =count + i
          print("Totaldonations",count)

    def highestamountdonation(self):
         max = Donations.Totaldonars[0]   # [  0 :=> 20000 , 1 :=> 10000006 ]

         for i in range(1,2):
             if  Donations.Totaldonars[i]>max :
                    max = Donations.Totaldonars[i]
         print(max)

    def totoalnofdonars(self):
          count =0
          for i  in Donations.Totaldonars :    #  if the list has value then another count is incremented
               count =count + 1                     
          print("totoalnofdonars",count)

             
Rahul = Donations( 20000 )
venkatesh =Donations(10000006)
Rahul.display()
venkatesh.display()
venkatesh.features()
venkatesh.Totaldonations()
venkatesh.highestamountdonation()
venkatesh.totoalnofdonars()




            
             
             
             
      
        
             
             
