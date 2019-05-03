#Leeb/Greene&Kleitman algorithm for symmetric chain decomposition
#source: Ian Anderson, combinatorics of finite sets, p.33
#author: K. Chatzikokolakis, University of Piraeus
initial_set=input("Give the initial set. Ex: 1,2,3.\n")
set=input("Give the initial set. Ex: 2, 3, 4, 7, 8.\n")
initial_set=initial_set.split(",")#split the input to a list
initial_set=list(map(int, initial_set)) #convert string list to int list
set=set.split(",")#split the input to a list
set=list(map(int, set)) #convert string list to int list
parentheses, unpaired, complements_unpaired, basic, scd=[], [], [], [], []
#print(initial_set, set)
left, right=0, 0
for i in range(len(initial_set)):
    if initial_set[i] in set:
        parentheses.append(")")
    else:
        parentheses.append("(")
#print(parentheses)
for i in range(len(parentheses)):
    if parentheses[i]=="(":
        #print(parentheses[i], "left")
        left=left+1
        print(left, right)
    if parentheses[i]==")":
        if i==0:
            continue
        #print(parentheses[i], "right")
        right=right+1
        print(left, right)
    if right>left:
        unpaired.append(initial_set[i])
        left, right=0, 0
    if (left==right):
        if (left!=0):
            for j in range(left):
                basic.append(initial_set[i-j])
            left, right=0, 0
    if i==len(initial_set)-1:
        if left!=0:
            for j in range(left):
                complements_unpaired.append(initial_set[i-j])
basic.sort()
print("The basic elements of the set are: ", basic)
print("The unpaired elements of the set are: ", unpaired)
print("The unpaired elements of the complement are: ", complements_unpaired)
for i in range(len(basic)):
    scd.append(basic[i])
print("current term of the scd: ", scd)
for i in range(len(unpaired)):
    scd.append(unpaired[i])
    scd.sort()
    print("current term of the scd: ", scd)
for i in range(len(complements_unpaired)):
    scd.append(complements_unpaired[i])
    scd.sort()
    print("current term of the scd: ", scd)
