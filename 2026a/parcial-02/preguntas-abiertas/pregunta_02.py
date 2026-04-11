def fibbo(n):
    if n == 0:
        return 1
    if n == 1: 
        return 1
    return fibbo(n - 1) + fibbo(n - 2)

print(fibbo(3))
print(fibbo(4))
print(fibbo(5))
print(fibbo(6))
