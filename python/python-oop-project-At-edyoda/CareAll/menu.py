from youth import Youth
from elders import Elder

elder1 = Elder("Anand" , 55, "male")
elder2 = Elder("seema" , 65, "female")

elder3 = Elder("Anandi" , 75, "female")
elder4 = Elder("kalyan" , 80, "female")
elder5 = Elder("kamal" , 75, "male")
               
elder6 = Elder("nidhi" , 67, "female")
elder7 = Elder("nirmal" , 77, "male")

elderList = [elder1,elder2,elder3,elder4, elder5]

youth1 = Youth("amay", 30, "male")
# youth2 = Youth("sanjay", 25, "male")
# youth3 = Youth("swati", 30, "female")


youthList = [youth1]




print("""
__________________________________________________________________________

please enter :-
__________________________________________________________________________

------------------------
1. For adoption
------------------------
2. For Rating & Writing Reviews
------------------------
3. For User Details
------------------------
__________________________________________________________________________

""")
print()

choice = input("")

print()

if choice =="1":
    n = {}
    for youth in youthList:
        if (youth.status):
            youth.adoptElder(elderList)
            for elder in youth.selected:
                if elder.approveAdoption(youth):
                    el = youth.addElder(elder)
                    if(el):
                        
                        print("---------------------------------------------------------------------------")

                        print()
                        print("{} is taking care of {}".format(youth.name, elder.name))
                        print()
                        print("---------------------------------------------------------------------------")
                        elder.approveAdoption(youth)
                        n.__setitem__(elder.name, youth.name)
                    
                    else:

                        print("----------------------------------------------------------------------------")
                        print()
                        print("{} is  has reached the adoption limit, choose another".format(youth.name))
                        print()
                        print("----------------------------------------------------------------------------")

                        youth.setStatus(False)
                        elder.setStatus(True)
elif choice =="2":
    print("""" please entere
               1. to rate youths
               2. to rate elders
               
               """)
    n = input()

    print()
    print("please enter your rating out of 10")
    print()

    if n =="1":
        for youth in youthList:
            print("________________________________________________________________________")
            print()

            youth.setRating(input("enter your rating:  "))

            print("_________________________________________________________________________")
            print()
            youth.setReview(input("write your reviews:  "))
            print("_________________________________________________________________________")

    elif n=="2":
        for elder in elderList:
            print("__________________________________________________________________________")
            print()
            elder.setRating(input("please enter your rating:  "))
            print("__________________________________________________________________________")
            print()
            elder.setReview(input("write your review:  "))
            print("__________________________________________________________________________")
    else:
        print("Invalid choice")
            
          
    
elif choice == "3":
    print("---------------------------------------------------------------------------------")
    print("""
           please enter:
           1 for elders detail
           2 for youth details""")
    print("---------------------------------------------------------------------------------")
    print()

    x = input()

    print()

    print("___________________________________________________________________________________")
    print()

    if x =="1":
        for elder in elderList:
            elder.display()
    elif x == "2":
        for youth in youthList:
            youth.display()
    else:
        print("Invalid choice")

else:
    print("Invalid Choice")


    print("___________________________________________________________________________________")
    







