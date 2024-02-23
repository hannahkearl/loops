# list_multiply_while(a: list[int], b: list[int]) -> c: list[int]

# list_multiply_for(a:list[int], b: list[int]) -> c:  list[int]

# list_multiply_foreach(a: list[int] b: list[int]) -> c:  list[int]

# a = [1,2,3]
# b = [4,5,6]
# c= list_multiply_while(a,b)
# print(c)

def list_multiply_while(a: list[int], b: list[int]) -> list[int]:
    c = []
    i = 0
    while i < len(a) and i < len(b):
        c.append(a[i] * b[i])
        i += 1
    return c

def list_multiply_for(a: list [int], b: list [int]) -> list[int]:
    c = []
    for i in range(len(a)):
        c.append(a[i] * b[i])
        i += 1
    return c

def list_multiply_foreach(a: list[int], b:list [int]) -> list[int]:
    


a = [1, 2, 3]
b = [4, 5, 6]


c_while = list_multiply_while(a, b)
print(c_while)

c_for = list_multiply_for(a, b)
print(c_for)

c_foreach = list_multiply_foreach(a, b)
print(c_foreach)

