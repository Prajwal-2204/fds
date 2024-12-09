def avarage(listofmarks):
    sum=0
    count=0
    for i in range(len(listofmarks)):
        if listofmarks[i]!=-999:
           sum+=listofmarks[i]
           count+=1
    avg=sum/count
    print("Total marks:",sum)
    print("Avarage marks:{:.2f}".format(avg))
    
def Maximum(listofmarks):
    for i in range(len(listofmarks)):
        if listofmarks[i]!=-999:
            Max=listofmarks[0]
            break
    for i in range(1,len(listofmarks)):
        if listofmarks[i]>Max:
            Max=listofmarks[i]
    return(Max)

def Minimum(listofmarks):
    for i in range(len(listofmarks)):
        if listofmarks[i]!=-999:
            Min=listofmarks[0]
            break
    for i in range(1,len(listofmarks)):
        if listofmarks[i]<Min:
            Min=listofmarks[i]
    return(Min)

def absentcount(listofmarks):
    count=0
    for i in range(len(listofmarks)):
        if listofmarks[i]==-999:
         count+=1
    return(count)

def maxfrequency(listofmarks):
    i=0
    Max=0
    print("Marks | Frequency")
    for j in listofmarks:
        if(listofmarks.index(j)==i):
            print(j,"  | ",listofmarks.count(j))
            if listofmarks.count(j)> Max:
             Max=listofmarks.count(j)
             mark=j
        i=i+1
    return(mark,Max)


marksinFDS=[]
numberofstudent=int(input("Enter the total no of student:"))
for i in range(numberofstudent):
    marks=int(input("Enter marks of student"+str(i+1)+":"))
    marksinFDS.append(marks)
flag=1
while flag==1:
    print("\n\n..........MENU..........\n")
    print("1.Total and avarage marks of the class")
    print("2.Higest andLowest marks in the class")
    print("3.Number of student absent for the test")
    print("4.Marks with higest frequency")
    print("5.exit\n")
    ch=int(input("Enter your choice(from 1 to 5):"))
    
    if ch==1:
        avarage(marksinFDS)
        a=input("Do you want continue?(yes/no):")
        if a=="yes":
            flag=1
        else:
            flag=0
            print("Thanks for using the programe!")
    elif ch==2:
        print("Higest score in the class:",Maximum(marksinFDS))
        print("Lowest score in the class:",Minimum(marksinFDS))
        a=input("Do you want continue?(yes/no):")
        if a=="yes":
            flag=1
        else:
            flag=0
            print("Thanks for using the programe!")
            
    elif ch==3:
        print("Absent student in the test",absentcount(marksinFDS))
        a=input("Do you want continue?(yes/no):")
        if a=="yes":
            flag=1
        else:
            flag=0
            print("Thanks for using the programe!")
            
    elif ch==4:
        mark,fr=maxfrequency(marksinFDS)
        print("Higest frequency is of marks{0} that is{1}".format(mark,fr))
        a=input("Do you want continue?(yes/no):")
        if a=="yes":
            flag=1
        else:
            flag=0
            print("Thanks for using the programe!")
    elif ch==5:
        flag=0
        print("Thanks for using the programe!")
    else:
        print("wrong choice!")
        a=input("Do you want continue?(yes/no):")
        if a=="yes":
            flag=1
        else:
            flag=0
            print("Thanks for using the programe!")
