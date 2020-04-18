from CareallUser import Alluser
class Youth(Alluser):
    allyouth = []
    def __init__(self, name, age, gender):
        Alluser.__init__(self, name, age, gender)
        self.elderCount = 0
        self.elderlist = []
        self.selected = []
        self.status = True
        Youth.allyouth.append(self)
        
    def addElder(self, name):
        if len(self.elderlist)<4:
            self.elderlist.append(name)
            return True
        else:
            self.status = False
            return False
    def setsalary(self,fund):
        self.fund = fund
    def getsalary(self):
        return self.fund
    
    def displayElder(self):
        for name in self.elderlist:
            print(name)

    def adoptElder(self, allelders):
        

        for elder in allelders:
            if elder.getStatus:
                print("________________________________________________________________________________")
                print()

                
                print("""elders detail:-
                        ----------------------------------------------------------
                         name: {}, 
                         age: {},
                         gender: {}
                         ---------------------------------------------------------
                         """.format(elder.name, elder.age, elder.gender))
                print("")
                print("_________________________________________________________________________________")
                print()

                print("{} would you like to take care of {}".format(self.name, elder.name))

                print("__________________________________________________________________________________")
                choice = self.action(elder)
    def action(self, elders):
        
        print()

        print("Type Yes or No")
        print("______________")
        print()
        choice = input()
        print("______________")
        print()
        if choice == 'Yes' or choice =="yes":
            self.selected.append(elders)
        elif choice =='No' or choice =='no':
            pass
        else:
            return self.action(elders)
        
        
            