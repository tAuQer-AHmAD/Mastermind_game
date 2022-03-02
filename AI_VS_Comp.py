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
code=[]
score=1

feed=[]

print(colors_map)

print("Please Wait while Computer is picking the code .........\n\n")
for i in range(4):
    rand.shuffle(num)
    code.append(num[0])
print("\tComputer has made Its choice Now AI will Break the code\n")

print(code)  


for i in range(4):
        rand.shuffle(num)
        comp.append(num[0])
print("\tThese are the avalable color ")
print("\t",colors_map)
print("The computer has chosen : ")
print(comp)
x=0

while x!=1:

    print(pins)

    for i in range(4):
        if comp[i]==code[i]:
            feed.append(1)
        elif comp[i] in code:
            feed.append(2)
        elif comp[i] not in code:
            feed.append(3)

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
print(feed)
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
    print("\tThese are the avalable color : ")
    print("\t",colors_map)
    print("The computer has chosen : ")
    print(comp)
    x=0

    while x!=1:

        print(pins)
        feed.clear()

        for i in range(4):
            if comp[i]==code[i]:
                feed.append(1)
            elif comp[i] in code:
                feed.append(2)
            elif comp[i] not in code:
                feed.append(3)
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



