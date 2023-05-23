
x=int(input('dose akeraio arithmo x='))
y=int(input('dose akeraio arithmo y='))

mylist=[x*i for i in range(1,y+1)]
print(mylist)

mylist01=[i%2 for i in mylist]
print(mylist01)

mylist_p=[mylist[k] for k in range(len(mylist)) if k%2]
print(mylist_p)

mylist_a=[mylist[k] for k in range(len(mylist)) if k%2==0]
print(mylist_a)
