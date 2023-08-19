# write a code to print the fibonacci series till nth term

n = int(input("Enter the nth term: "))

a = 0

b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c
    