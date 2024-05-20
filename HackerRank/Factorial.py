def fac(n):
    if n == 1:
        return 1
    else:
        return (n * fac(n-1))


############ don't touch code after this line ############

print(fac(int(input())))