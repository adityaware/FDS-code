# Write a Python program to store first year percentage of students in array. Write function for sorting array of floating point numbers in ascending order using
# a) Selection Sort
# b) Bubble sort and display top five scores.
marks=[]
def get_stu():
    n=int(input("enter the no. student"))
    for i in range(n):
        m=float(input("Enter the marks "))
        marks.append(m)
        print(marks)
def bubble ():
    for i in range(len(marks)-1,0,-1):
        for j in range(i):
            if marks[j]>marks[j+1]:
                #swap
                temp=marks[j]
                marks[j]=marks[j+1]
                marks[j+1]=temp
                print(marks)

def sel():
    for i in range(len(marks)):
        min=i
        for j in range(i+1,len(marks)):
            if marks[min]>marks[j]:
                min=j
                #swap
                temp =marks[min]
                marks[min]=marks[i]
                marks[i]=temp
                print(marks)
get_stu()
while True:
    print(" 1 for bubble sort")
    print(" 2 for selaction sort")
    print(" 3 exit")
    ch=int(input("enter the choice"))
    if ch==1:
        bubble()
    if ch==2:
        sel()
    if ch==3:
        exit()




