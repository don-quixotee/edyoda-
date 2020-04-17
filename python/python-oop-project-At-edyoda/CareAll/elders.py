from CareallUser import Alluser
class Elder(Alluser):

    listElders = []

    def __init__(self, name, age, gender):
        Alluser.__init__(self, name, age, gender)
        Elder.listElders.append(self)
        
    
    def setFund(self):
        self.fund = 300000      
    def getFund(self):
        return  self.fund
        
    def aprove_Adoption (self,youth):
        self.youth = youth
        
    def get_Adoption(self):
        return self.youth
    
    def approveAdoption(self, youth):
        if self.status == True:
            print("--------------------","Care taker detain","------------------------------")
            print()

            print("Name = {}, Age = {}, Gender = {}".format(youth.name, youth.age, youth.gender))
            print("\n")
            print("--------------------------------------------------------------------------")
            print()
            print("{} would you like to be taken care by {}. 1. say or 2. No".format(self.name, youth.name))

            print()
            print("____________")
            print()
            choice = input()
            print("____________")
            print()

            if choice =="Yes" or choice == "yes":
                self.setStatus(False)
                return True
            elif choice == "No" or choice =="no":
                return False
            else:
                print("type yes or No")
                return self.approveAdoption(youth)
                
            