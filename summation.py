#Write two functions that take in a number n and sum up all the numbers between 1-n:
# summation_while: Implements the summation using a while loop
# summation_for: Implements the summation using a for loop

def summation_while(n: int) -> int:
    total = 0
    i = 1
    while i<= n:
        total += i
        i += 1
    return total

def summation_for(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total += i
    return total    

n = int(input("Enter a number: "))
print("Summation using while loop:", summation_while(n))
print("Summation using for loop:", summation_for(n))
