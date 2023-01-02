#Write a python program to store marks stored in subject "Fundamentals of Data Structure" by N students in the class. Write functions to compute following:
    #                     1. The average score of the class.
    #                     2. Highest score and lowest score of the class.
    #                     3. Count of students who were absent for the test.
    #                     4. Display mark with highest frequency.



marks=[]
def stud_get():
    print("enter the number of student")
    n=int(input())
    global marks
    for i in range(n):
        print("Enter the marks (write -1 for absent student)")
        m=int(input())
        marks.append(m)
    print(marks)

def avg_marks():
    sum=0
    cont=0
    for i in range(len(marks)):
        sum=sum+marks[i]
        cont+=1
    print("Total marks =", sum)
    print("cont = ",cont)
    print("Avg = ",sum/cont)
def low_high():
    temp=marks
    for i in range(len(marks)):
        if temp<marks[i]:
            temp=marks[i]
        print("the highest marks = ",temp)

    for i in range(len(marks)):
        if temp>marks[i]:
            temp=marks[i]
        print("the lowest marks is = " ,temp)
def abs_conut():
    cont=0
    for i in range(len(marks)):
        if marks== -1:
            cont +=1
        print("the absent no. ",cont)
def high_freq():
    freq=[]
    for i in range(len(marks)):
        if marks!=-1:
            freq.append(marks.count(marks[i]))
    print(freq)
    k=max(freq)
    print("highest frequency",k)
    print("highest marks",marks[k])
if __name__=='__main__':
    print("Take the input")
    stud_get()
    while(True):
        print("Enter 1 to calculate Avarege of class")
        print("enter 2 to Highest Score and Lowest Score of Class:")
        print("enter 3 to calculate absent student of Class:")
        print("enter 4 to Highest Score and Lowest Score of Class:")
        print("4. Display Marks with Highest frequency: ")
        print("5. exit ")
        print("enter the choise")
        choise=int(input())
        if (choise==1):
            avg_marks()
        if (choise==2):
            low_high()
        if (choise==3):
            abs_conut()
        if (choise==4):
            high_freq()
        if (choise==5):
            exit()




                