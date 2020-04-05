#TASK-1
#create empty list
list1=[]
print(list1)
print(list())
#concatenate it with [5,6,8,9]
#add 8,9,1,5,6,7,8
list1=[5,6,8,9]
list2=[8,9,1,5,6,7,8]
list3=list1+list2
print(list3)
#find no of occurence of 8
print(list3.count(8))
#find average of the list
avg=sum(list3)/len(list3)
print(int(avg))
#find sum of list
print(sum(list3))
#sort a list
list3.sort()
print(list3)
#min element
print(min(list3))
#max element
print(max(list3))
#find median of list
print(len(list3)//2)
#remove duplicates from concatenated list # give output in tuple format
list4=set(list3)
print(list4)
# output in tuple format
print(list(list4))
#TASK-2
#create two tuples (1,4,5,6,7) (5,6,7,8,9)
tuple1=(1,4,5,6,7)
tuple2=(5,6,7,8,9)
#concatenate two tuples after duplicate removal from both
tuple3=(list(tuple1)+list(tuple2))
tuple4=(tuple(tuple3))
#find the index value of 9
print(tuple4.index(9))
#find common elements between above elements with {0,4,5}
print(set(tuple4).intersection({0,4,5}))
#multiple above tuple 3 times
print(tuple4*3)
#TASK4
#create a dictionary {1:["english","maths","science",["bio-zoology","bio-botany","physics"]],2:(10,20,40,"python program")}
dict1={1:["english","maths","science",["bio-zoology","bio-botany","physics"]],2:(10,20,40,"python program")}
#extract botany
print(dict1[1][3][1][4:])
#extract "english","maths","science" from that dictionary and convert it into  tuple and print len
print(len(tuple(dict1[1][0:3])))
#print all keys in dictionary
print(dict1.keys())
#extract "python" from dictionary
print(dict1[2][3][0:6])
#add all numbers in values under key 2
print(dict1[2][0:3])

#task2
#create two empty sets
set1=set()
set2=set()

#update set1 with 7,8,9,1,2,3,4,5,0#update set2 with 4,5,6,0
a={7,8,9,1,2,3,4,5,0}
set3=set1.union(a)
print(set3)
b={4,5,6,0}
set4=set2.union(b)
print(set4)

#check whether set2 is subset of set 1 ?
print(set3.issubset(set4))
#check whether both are disjoint ?
print(set3.isdisjoint(set4))
#remove 8 from set1
rev=set3.remove(8)
print(rev)
#discard 0 from set2
dis=set4.discard(0)
print(dis)
#find sum(set1 union set2)
print(set3.union(set4))
