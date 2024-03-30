# Write a Python program to get the largest number from a list
list1=[73,1,5,14,2,40,7,10]
largest=list1[0]
for i in range(len(list1)):
    if list1[i]>largest:
        largest=list1[i]
print(f"The largest number is {largest}.")

# Write a Python program to clone or copy a list
original_list=[1,2,3,4,5,6]
clone=(original_list)
print(f"Original list is {original_list}")
print(f"copy of the list is {clone}")

# Write a Python program to find the repeated items of a tuple

tuple1=(4,2,7,8,4,3,7,5,9,2,6,4,3,7,8,0)
print(f"3 has repeated {tuple1.count(3)} times.")
print(f"4 has repeated {tuple1.count(4)} times.")
print(f"7 has repeated {tuple1.count(7)} times.")
print(f"9 has repeated {tuple1.count(9)} times.")