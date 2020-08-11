#entering different elements in a list
list1=[]
i=int(input("Enter number: "))
j=0
for j in range (0,i+1):
    inp=input("Enter element to be appended: ")
    list1.append(inp)
    j+=1
print (list1)

#accessing elements from a tuple
tup1=(1,2,3)
for i in tup1:
    print (i)

#deleting elements from a dictionary
food={1:"Pizza",2:"dry fruits",3:"Chaat"}
del food[2]
print (food)

    
