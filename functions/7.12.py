def f(n):
    if n == 0:
        return ""
    return "*/" * (n - 1) + "*"
    
print(f(4))  # "*/*/*/*"
print(f(1))  # "*"