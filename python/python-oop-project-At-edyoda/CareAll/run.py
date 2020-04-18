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
youth2 = Youth("sanjay", 25, "male")
youth3 = Youth("swati", 30, "female")

youthList = [youth1]

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



