#white williamson algorithm Implementation for symmetric chain decomposition (SCD)
#source: Ian Anderson, combinatorics of finite sets, p.36
#author: K. Chatzikokolakis, University of Piraeus
data=input("Give the initial set of the chain. Separate each term with commas.\n")
data=data.split(",")#split the input to a list
data=list(map(int, data)) #convert string list to int list
data.append(0)#insert into the list the value 0
data.sort() #sort the array
chain=[] #list with the sets of the chain
chain.append(data[1:])
#print(data)
while(True):
    l=len(data)#get the length of the array
    #print(l)
    result=[]
    for i in range(l):
        result.append(data[i]-2*i)
    #print(result)
    argmin=result.index(min(result)) #position of the min element of result list
    data.append(1+data[argmin]) #this is the next element of the chain
    data.sort()
    print("New set of the chain:\n", data[1:])
    chain.append(data[1:])
    answer=input("Do you want to perform the operation again? y/n\n")
    if answer=="n":
        break
print("The constructed chain is:\n", chain)
