a,n=map(int,input().split())
def power(a, n):
    if n == 0: return 1
    return power(a, n - 1) * a

print(power(a,n))