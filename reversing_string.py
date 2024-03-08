def reverse_while(s: str) -> str:
    reversed_string = ""
    index = len(s) - 1
    while index >= 0:
        reversed_string += s[index]
        index -= 1
    return reversed_string

def reverse_for(s: str) -> str:
    reversed_string = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_string += s[i]
    return reversed_string

def reverse_foreach(s: str) -> str:
    reversed_string = ""
    for char in s[::-1]:
        reversed_string += char
    return reversed_string

s = "hello"
r_while = reverse_while(s)
print(r_while)

r_for = reverse_for(s)
print(r_for)

r_foreach = reverse_foreach(s)
print(r_foreach)
