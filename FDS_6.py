# Write a Python program to store first year percentage of students in array. 
# Write function for sorting array of floating point mumbers in ascending order 
# using quick sort and display top five scores.

def get_percentage(a):
    n=int(input("enter no . of stu"))
    for i in range (n):
        f=float(input("enter the peracentage"))
        a.append(f)
        print(a)

def quickSort(a):
    n=len(a)
    if len(a)<=1:   
        return (a)
    else:
        pivot=a.pop()
    greater=[]
    lower=[]
    for i in a:
        if i >pivot:
            greater.append(i)
        else:
            lower.append(i)
    o=quickSort(lower) +[pivot]+quickSort(greater)
    print(o[n-1:-6:-1])
    return o
a=[]
while True:
    print("1. sort by quicksort")
    print("2. Exit.")
    ch=int(input("enter the choice : "))
    if ch==1:
        get_percentage(a)
        print(quickSort(a))

