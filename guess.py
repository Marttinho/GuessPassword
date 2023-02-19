# read the file and store the login attempts in a list
with open('keylog.txt', 'r') as f:
    login_attempts = f.read().splitlines()

# initialize a dictionary to count the frequency of each three-character string
freq = {}

def is_order_preserved(list1, list2):
    # initialize two pointers to keep track of the current index of both lists
    for i in list1:
        if i not in list2:
            return False
    i = 0
    j = 0
    
    # loop until the end of either list is reached
    while i < len(list1) and j < len(list2):
        # if the elements at the current indices are equal, move both pointers
        if list1[i] == list2[j]:
            i += 1
            j += 1
        # if the elements are not equal, only move the pointer for the second list
        else:
            j += 1
    
    # if the entire first list has been traversed, the order is preserved
    return i == len(list1)


# iterate over all login attempts and update the frequency dictionary
# for attempt in login_attempts:
#     for i in range(len(attempt)-2):
#         string = attempt[i:i+3]
#         if string in freq:
#             freq[string] += 1
#         else:
#             freq[string] = 1


# map = {}
# for attempt in login_attempts:
#     # print(attempt)
#     for i,v in enumerate(attempt):
#         if (v,i) not in map:
#             map[(v,i)] = 1
#         else:
#             map[(v,i)] += 1

# sor = sorted(map.items(), key=lambda x:x[1], reverse=True)

from itertools import permutations 

# spiltterd = login_attempts.split()
# print(login_attempts)
spiltterd = [list(i) for i in login_attempts]
# print(spiltterd)
  
# Get all permutations of [1, 2, 3] 
# perm5 = permutations(['1', '2', '3','6','7','8','9','0'], 5) 
# perm6 = permutations(['1', '2', '3','6','7','8','9','0'], 6) 
# perm7 = permutations(['1', '2', '3','6','7','8','9','0'], 7)
perm8 = permutations(['1', '2', '3','6','7','8','9','0'], 8)
check = 0  
for i in perm8:
    check = 0
    for j in spiltterd:
        if is_order_preserved(j,i) is False:
            check = 0
            break
        else:
            check = 1
    if check == 1:
        print("The shortest password is:")
        print(i)
# for i in perm6:
#     check = 0
#     for j in spiltterd:
#         if is_order_preserved(j,i) is False:
#             check = 0
#             break
#         else:
#             check = 1
#     if check == 1:
#         print(i)
#         print("True")
# for i in perm7:
#     check = 0
#     for j in spiltterd:
#         if is_order_preserved(j,i) is False:
#             check = 0
#             break
#         else:
#             check = 1
#     if check == 1:
#         print(i)
#         print("True")
    

# print("not good 5 perm")
# for i in perm6:
#     if i[0] == '7':
#         for j in spiltterd:
#             if is_order_preserved(j,i) is True:
#                 print(i)
# print("not good 6 perm")
# for i in perm7:
#     if i[0] == '7':
#         for j in spiltterd:
#             if is_order_preserved(j,i):
#                 print(i)
# print("not good 7 perm")
# for i in perm8:
#     if i[0] == '7':
#         for j in spiltterd:
#             if is_order_preserved(j,i):
#                 print(i)
# print("not good 8 perm")
                

