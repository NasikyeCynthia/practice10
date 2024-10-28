#Find sum of items in a list
#using functions
def sum_items(items):
    total = 0
    for i in items:
        total += i
    return total
print(sum_items([1, 2, 3]))

# using sum function
items = [1, 2, 3]
print(sum(items))

#Multiply all items in a list
def mult_items(list):
    t = 1
    for x in list:
        t *= x
    return t
print(mult_items([2,3,4]))

#Get largest number from a list
list1 = [9, 1, 2, 3, 5, 10]
max_no = max(list1)
print("Largest number in the list is:", max_no)

#Get smallest number in a list
list2 = [9, 1, 2, 3, 5, 10]
min_no = min(list2)
print("Smallest number in the list is:", min_no)

#Count number of strings in a string with length 2 or more and whose first and last characters are the same
def string1(words):
    ctr = 0
    for i in words:
        if len(i) > 1 and i[0] == i[-1]:
            ctr += 1 
    return ctr
print(string1(['aba', 'xyz', 'abc' ,'1221']))

#sorted list by last element in increasing order from a given tuples[(2,5), (1,2), (4,4), (2,3), (2,1)]
def last(n):
    return n[-1]
def custom_sorted(tuples):
    return sorted(tuples, key = last)
print(custom_sorted([(2,5), (1,2), (4,4), (2,3), (2,1)]))

#Remove duplicates from a list
list3 = ['a', 'e', 'a', 'e', 'i', 'o', 'u', '0']
unique_list = list(dict.fromkeys(list3))
print(unique_list) 

# Check if a list is empty or not
lst = [1, 2, 3]
if lst != []:
    print("List is not empty")
else:
    print("List is empty")

l = []
if not l:
    print("List is empty")

# clone or copy a list
lst1 = [1, 2, 3, 4]
clone_lst = list(lst1)
print(lst1)
print(clone_lst)

# find a list of words longer than n from  given list 
x = ['Nible', 'Cynthia', 'Minnie', 'oh', 'anc', 'kjl']
for i in x:
    if len(i) > 3:
        print(i)

#find a list of words longer than n from  given string
def stringq(n, str):
    word = []
    x = str.split(" ")
    for i in x:
        if len(i) > n:
            word.append(i)
    return word
print(stringq(3, "For the love of God Be yourself now and them"))        

#takes two lists and returns true if they have atleast one common member
def common(listl, listm):
    result = False
    for x in listl:
        for y in listm:
            if x == y:
                result = True
    return result
print(common([1,2,3], [1,4,5]))
print(common([2,4,6], [1,3,5]))

# print specified list after removing the oth, 4th and 5th elements 
colour = ["Red", "Green", "White", "Black", "Pink", "Yellow"]
colour1 = [x for (i, x) in enumerate(colour) if i not in (0, 4, 5)]
print(colour1)

# generate 3*4*6 3D array whose element is * 
array = [[['*' for col in range(6)] for col in range(4)] for row in range(3)]
print(array)

# print the numbers of a specified list after removing even numbers from it 
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num = [x for x in num if x%2 != 0]
print(num)

# shuffle and print a specified list 
from random import shuffle
colour = ["Red", "Green", "White", "Black", "Pink", "Yellow"]
shuffle(colour)
print(colour)

# list of first and last 5 elements where values are square numbers between 1 and 30 
def squareno():
    l = list()
    for i in range(1, 31):
        l.append(i**2)
    print(l[:5])
    print(l[-5:])
squareno()











































