#How to print a dictionary
d={'a':'apple','b':'banana','c':'carrot','d':['almond','cashew','pista']}
d['f']='fruits'
d['k']='junkfood'
del d['k']
d2={'b':'brinjal','p':'potato'}
d.update(d2)
print(d.items())

#list
##to find unique number
# list2=[]
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(list2)

#to reverse the string
# string="My name is shweta"
# list=string.split()
# output=""
# for i in range(len(list)-1,-1,-1):
#     output += list[i]
#     output += " "
# print(output)

#To count words in a file
with open('test.txt',mode='r') as myfile:
    count = 0
    for lines in myfile:
        for words in lines.split(" "):
            if words == 'NAME':
                count += 1
    print(count)

arr=[1,2,5,8,6,5,8,7,8,5,58,25,24,25,54,55,5,41,3,6]
n=len(arr)
max=arr[0]
min=arr[0]
for i in range(1,n):
    if arr[i]>max:
        max=arr[i]
print("the maximum element is {} ".format(max))

for i in range(1,n):
    if arr[i]<min:
        min=arr[i]
print("the maximum element is {} ".format(min))
l2=[]
for i in range(1,n):
    if arr[i] not in l2:
        l2.append(arr[i])
print(l2)