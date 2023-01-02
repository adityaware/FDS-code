 
#  In second year computer engineering class, group A student's play cricket, 
# group B students play badminton and group C students play football.
#  Write a Python program using functions to compute following  

# a)List of students who play both cricket and badminton
# b)List of students who play either cricket or badminton but not both
# c)Number of students who play neither cricket nor badminton
# d) Number of students who play cricket and football but not badminton

# Group A = group of students who play cricket
# Group B = group of students who play badminton
# Group C = group of students who play football
cricket=[]
badminton=[]

football=[]
uni=[]
def get():
    global cricket
    c=int(input(" No . of student who play cricket "))
    for i in range(c):
        cr=int(input("enter the roll no. play cricket "))
        cricket.append(cr)
        
    global badminton
    b=int(input(" No . of student who play Badminton "))
    for i in range(b):
        br=int(input("enter the roll no. play badminton "))
        badminton.append(br)
        
    global football
    f=int(input(" No . of student who play football "))
    for i in range(f):
        fr=int(input("enter the roll no. play football "))
        football.append(fr)
  
    
    global uni
    u=int(input(" No . of student in class "))
    for i in range(u):
        uni.append(u)
       

def cri_bad():
    cri_bad=[]
    for i in cricket:
        for j in badminton:
            if i==j:
                cri_bad.append(j)
            print(cri_bad)

#List of students who play either cricket or badminton but not both
def no_both_cri_bad():
    no_cri_bad=[]
    for i in cricket:
        if i not in badminton:
            no_cri_bad.append(i)
    for i in badminton:
        if i not in cricket:
            no_cri_bad.append(i)
        print(no_cri_bad)

# Number of students who play neither cricket nor badminton
def nor_cri_bad():
    uni_cri_bad=[]
    uni_cri_bad.extend(cricket)
    for i in badminton:
        if i not in cricket:
            uni_cri_bad.append(i)
    nor_cri_bad=[]
    for i in uni:
        if i not in uni_cri_bad:
            nor_cri_bad.append(i)

# d) Number of students who play cricket and football but not badminton
def cri_foot_not_bad():
    cri_foot=[]
    cri_foot.extend(cricket)
    for i in football:
        if i not in cricket:
            cri_foot.append(i)
    cri_foot_not_bad =[]   
    for i in cri_foot:
        if i not in badminton:
            cri_foot_not_bad.append(i)  
    print(cri_foot_not_bad)
if __name__ == '__main__':
    print("***** Take Input *****")
    get()
    while(True):
        print("1. List of Students who play both Cricket And Badminton: ")
        print("2. List of Students who play either Cricket Or Badminton but Not Both: ")
        print("3. List of Students who play neither Cricket nor Badminton but Not Both: ")
        print("4. List of students who play Cricket And football but not Badminton: ")
        print("5. Exit")
        print("Enter Choice ")
        choice=int(input())
        if(choice==1):
            cri_bad()
        if(choice==2):
            no_both_cri_bad()
        if(choice==3):
            cri_foot_not_bad()
        if(choice==4):
            cri_foot_not_bad()
        if(choice==5):
            exit()


    
    