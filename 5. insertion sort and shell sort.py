def insertion_sort(list1):
    for i in range(1, len(list1)):
        value = list1[i]
        j = i - 1
        while j >= 0 and value < list1[j]:
            list1[j + 1] = list1[j]
            j -= 1
        list1[j + 1] = value
    return list1

def shellsort(array, n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        interval //= 2

list1 = []
num_stu = int(input("How many numbers of students: "))
for i in range(num_stu):
    list1.append(float(input("Enter the marks: ")))

print("1. Insertion Sort \n2. Shell Sort")
ch = int(input("Enter your choice: "))
if ch == 1:
    print("The unsorted list is:", list1)
    print("The sorted marks list by insertion method is:", insertion_sort(list1))
elif ch == 2:
    print("The unsorted list is:", list1)
    size = len(list1)
    shellsort(list1, size)
    print("The sorted marks list by shell sort method is:", list1)
else:
    print("Invalid choice")
