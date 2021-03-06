# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python3
import math

def is_prime(n):
    if n <= 1:
        return "Not prime"
 
    max_div = math.floor(math.sqrt(n))
    for i in range(2, 1 + max_div):
        if n % i == 0:
            return "Not prime"
    return "Prime"

if __name__ == '__main__':

    T=int(input())
    container_nbr = []
    for i in range(T):
        n = float(input())
        container_nbr.append(n)

    for i in container_nbr:
        print(is_prime(i))