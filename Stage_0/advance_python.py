
"""Advance Python"""


"""normal_function : -""" 

# def count_num(n):
#     numbers_lst = []
#     count = 1
#     while count <= n:
#         numbers_lst.append(count)
#         count += 1
#     return numbers_lst

# number = int(input("enter the number : "))

# for i in count_num(number):
#     print(i)
# ----------------------------------

"""generator : -""" 

# def count_num(n):
#     count  = 1
#     while count <= n:
#         yield count
#         count += 1

# number = int(input("enter the number : "))

# for i in count_num(number):
#     print(i)
# ---------------------------------------

# read line by line data from a file using generator : - 

# import time

# file_path = "/home/user/Data_Science/Stage_0/test.txt"

# def read_lines(file_path):
#     with open(file_path) as f:
#         for line in f:
#             time.sleep(1)
#             yield line.strip()

# for i in read_lines(file_path):
#     print(i)
# ----------------------------------------------




    

