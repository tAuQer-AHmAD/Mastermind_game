import random as rand

x=0
codeBreak={}
colors = ["RED", "GREEN", "YELLOW", "BLUE", "BLACK", "ORANGE"]
pins={1:"Red",2:"white",3:"No pin"}
colors_map = {1:"RED", 2:"GREEN", 3:"YELLOW", 4:"BLUE", 5:"BLACK", 6:"ORANGE"}
num=[1,2,3,4,5,6]
not_include=set()
temp=[]
comp=[]
no=[]

score=1

while x!=1:

    print(colors_map)

    code=list(map(int,input("\nEnter the choice : ")))
    if len(code)!=4:
        print("\nYou entered Wrong choice ")
        flag = 0
        for x in code:
            if x > 6 or x < 1:
                flag = 1
 
        if flag == 1:           
        
            print("\tWrong choice!! Try again!!")
            continue
    else:
        x=1
   


for i in range(4):
        rand.shuffle(num)
        comp.append(num[0])

print(colors_map)
print("The computer has chosen : ")
print(comp)
x=0

while x!=1:

    print(pins)

    feed=list(map(int,input("\nEnter the FeedBack : ")))
    if len(feed)!=4:
        print("\nYou entered Wrong choice ")
        flag = 0
        for x in feed:
            if x > 3 or x < 1:
                flag = 1
 
        if flag == 1:           
        
            print("\tWrong choice!! Try again!!")
            continue
    else:
        x=1

for i in range(len(feed)):
    if feed[i]==1:
        codeBreak.update({i:comp[i]})
    if feed[i]==2:
        temp.append(comp[i])

    elif feed[i]==3:
        if comp[i]  in no:
            break
        else:

            no.append(comp[i])
            num.remove(comp[i])


# print(num)

while score<=10:
    print("compute is on "+str(score)+" turn")

    # print(num)

    num=num+temp
    temp.clear()
    comp.clear()
    for i in range(4):
        rand.shuffle(num)
        comp.append(num[0])
    print("\n\n")
    print(colors_map)
    print("The computer has chosen : ")
    print(comp)
    x=0

    while x!=1:

        print(pins)

        feed=list(map(int,input("\nEnter the FeedBack : ")))
        if len(feed)!=4:
            print("\nYou entered Wrong choice ")
            flag = 0
            for x in feed:
                if x > 3 or x < 1:
                    flag = 1
    
            if flag == 1:           
            
                print("\tWrong choice!! Try again!!")
                continue
        else:
            x=1
    

    for i in range(len(feed)):
        if feed[i]==1:
            

                codeBreak.update({i:comp[i]})
        if feed[i]==2:
            temp.append(comp[i])
        elif feed[i]==3:
            if comp[i]  in no:
                break
            else:
                no.append(comp[i])
                num.remove(comp[i])
    print(codeBreak)
    if len(codeBreak.keys())==4:
        print("Computer Won")
        print("\n\n")
        # seq=codeBreak.values()
        print("The correct sequence is :")
        print("\n")
        for i in sorted (codeBreak.keys()) :
            print(codeBreak[i], end = " ")
 
        # print(seq)
        break
    else:
        score=score+1



