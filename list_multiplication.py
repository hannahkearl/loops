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
        c.append(a * b)
        i += 1
    return c
