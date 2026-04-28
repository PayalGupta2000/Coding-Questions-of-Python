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

# Input: [10, 20, 4, 45, 99]

