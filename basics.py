# Find Maximum number without using in build function
l1=[2,3,4,7,5]
for i in l1:
    for j in l1:
        if j>i:
            i=j
print(i)

# Count vowels in python
word = "python"
counter =0
vowels = ['a','e','i','o','u']
for i in word:
    if i in vowels:
        counter+=1
    print(i)
    print(f"counter {i} - {counter}")

# Sum of Digits
sum =0
for i in range(5):
    sum+=i
print(sum)

# Remove Duplicates from List
# 1. using in build function
l1 = [1,2,2,3,3,4,4,5]
print(list(set(l1)))

# 2. without inbuilt function
l1 = [1,2,2,3,3,4,4,5]
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)

# Find Second Largest: [10, 20, 4, 45, 99]

l1=[10,20,4,45,99]
sorted_list=sort.l1()
print(sorted_list[-2]) # ask

# Fibonacci Series (n terms)
n=5
a=0
b=1
for i in range(n+1):
    print(a)
    a,b=b,a+b

# Count Frequency of Characters
word = "aabbc"
freq ={}
for ch in word:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print(freq)

# Merge Two Sorted List 
# using inbuilt
list1 = [1,3,5]
list2= [2,4,6]
merge_list=list1+list2
merge_list.sort()
print(merge_list)

# Find Missing Number
l1 = [1,2,3,5]
for i in range(1,6):
    if i not in l1:
        print(i)

# Anagram Check (length and charcter are same in 2 string, no matter what is order)
word1="silent"
word2="listen"
freq={}
if len(word1)!=len(word2):
    print("no anagram")
else:
    sort_w1 = sorted(word1)
    sort_w2 = sorted(word2)
    if sort_w1 ==sort_w2:
        print("agaram")
    else:
        print("not")

# First Non-Repeating Character
word1="aabbcde"
freq ={}
for ch in word1:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1

for j in freq:
    if freq[j]==1:
        print(j)

# Longest Substring Without Repeating Characters




# Two Sum Problem
l1 = [2,7,11,15]
target = 9
num_map={}
for i ,num in enumerate(l1):
    required = target - num
    if required in num_map:
        print([num_map[required],i])
    num_map[num] =i
        