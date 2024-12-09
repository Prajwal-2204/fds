def add(m1, m2):
    result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            result[i][j] = m1[i][j] + m2[i][j]
    for r in result:
        print(r)

def mult(m1, m2):
    result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                result[i][j] += m1[i][k] * m2[k][j]
    for r in result:
        print(r)

def sub(m1, m2):
    result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            result[i][j] = m1[i][j] - m2[i][j]
    for r in result:
        print(r)

def trans(m1):
    result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            result[j][i] = m1[i][j]
    for r in result:
        print(r)

# Input matrices
m1 = []
print("Enter 1st matrix m1: ")
r1 = int(input("Enter the number of rows: "))
c1 = int(input("Enter the number of columns: "))

print("Enter the entries row-wise:")
for i in range(r1):
    a1 = []
    for j in range(c1):
        a1.append(int(input()))
    m1.append(a1)

print("Matrix m1:")
for i in range(r1):
    for j in range(c1):
        print(m1[i][j], end=" ")
    print()

m2 = []
print("Enter 2nd matrix m2: ")  # corrected prompt for matrix m2
r2 = int(input("Enter the number of rows: "))
c2 = int(input("Enter the number of columns: "))

print("Enter the entries row-wise:")
for i in range(r2):
    a2 = []
    for j in range(c2):
        a2.append(int(input()))
    m2.append(a2)

print("Matrix m2:")
for i in range(r2):
    for j in range(c2):
        print(m2[i][j], end=" ")
    print()

print("The 1st matrix m1 is:", m1)
print("The 2nd matrix m2 is:", m2)

flag = True
while flag:
    print("\n\n--------------------MENU--------------------\n")
    print("1. Addition of two matrices")
    print("2. Subtraction of two matrices")
    print("3. Multiplication of two matrices")
    print("4. Transpose of matrix")
    print("5. Exit\n")
    ch = int(input("Enter your Choice (1 to 5): "))
    
    if ch == 1:
        print("Addition of Two matrices is: ")
        add(m1, m2)
    elif ch == 2:
        print("Subtraction of Two matrices is: ")
        sub(m1, m2)
    elif ch == 3:
        print("Multiplication of Two matrices is: ")
        mult(m1, m2)
    elif ch == 4:
        print("Transpose of First matrix is: ")
        trans(m1)
    elif ch == 5:
        flag = False
        print("Thanks for using this program!")
    else:
        print("!!Wrong choice!!")

    a = input("Do you want to continue (y/n) : ")
    if a.lower() != "y":
        flag = False

print("Thanks for using this program!")
