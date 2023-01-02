# Write a Python program to store second year percentage of students in array, Write function for sorting array of floating point numbers in ascending order using:

# a) Insertion sort

# b) Shell Sort and display top five scores
def get(a):
    n=int(input("Enter the no. of stud "))
    for i in range(n):
        m=float(input("Enter the marks"))
        a.append(m)
        print(a)
def insertions(a):
    n=len(a)
    for i in range(1,n):
        k=a[i]
        j=i-1
        while j>=0 and k<a[j]:
            a[j+1]=a[j]
            j-=1
        a[j+1]=k
        print(a)

def sell_sort(a):
    gap=len(a)//2
    while gap>0:
        for i in range(gap,len(a)):
            temp=a[i]
            j=i
            while j>=gap and a[j-gap]>temp:
                a[j]=a[j-gap]
                j-=gap
            a[j]=temp
        gap//=2
    print(a)

a = []
while True:
   
    print("1. sort by Insertion sort")
    print("2. sort by shell sort")
    
    print("3. Exit.")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        get(a)
        insertions(a)
    if ch == 2:
        get(a)
        sell_sort(a)
        
    elif ch == 3:
        exit()
    
