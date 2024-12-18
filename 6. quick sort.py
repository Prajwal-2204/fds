def input_percentage():
    perc=[]
    number_of_students=int(input("enter the number of students:"))
    for i in range(number_of_students):
        perc.append(float(input("enter the pecentage of students{0}:".format(i+1))))
    return perc

def print_percentage(perc):
    for i in range(len(perc)):
        print(perc[i],sep="\n")


def percentage_partition(perc,start,end):
    pivot=perc[start]
    lower_bound=start+1
    upper_bound=end
    while True:
        while lower_bound<=upper_bound and perc[lower_bound]<=pivot:lower_bound+=1
        while lower_bound<=upper_bound and perc[upper_bound]>=pivot:upper_bound-=1
        if lower_bound<=upper_bound:
            perc[lower_bound],perc[upper_bound]=perc[upper_bound],perc[lower_bound]
        else:
            break
    perc[start],perc[upper_bound]=perc[upper_bound],perc[start]
    return upper_bound
        
def Quick_sort(perc,start,end):
    while start<end:
        partition =percentage_partition(perc,start,end)
        Quick_sort(perc,start,partition-1)
        Quick_sort(perc,partition+1,end)
        return perc

def display_top_five(perc):
    print("top five percentage are:")
    if len(perc)<5:
        start,stop=len(perc)-1,-1
    else:
        start,stop=len(perc)-1,len(perc)-6
    for i in range(start,stop,-1):
        print(perc[i],sep="\n")

#main
unsorted_percentage=[]
sorted_percentage=[]
flag=1
while flag==1:
    print("\n\n--------------MENU--------------------\n")
    print("1.Accept the percentage of students")
    print("2.display the percentage of students")
    print("3.Perform Quick sort on the data")
    print("4.Exit")
    ch=int(input("enter your choice(from 1 to 4):"))
    if ch==1:
        unsorted_percentage=input_percentage()
    elif ch==2:
        print_percentage(unsorted_percentage)
    elif ch==3:
        print("Percentage of students after performing Quick sort:")
        sorted_percentage=Quick_sort(unsorted_percentage,0,len(unsorted_percentage)-1)
        print_percentage(sorted_percentage)
        a=input("Do you want to display the top 5 percentage of students(yes/no):")
        if a=="yes":
            display_top_five(sorted_percentage)
    elif ch==4:
        print("thanks for using this program!!")
    else:
        print("invalid choice")
