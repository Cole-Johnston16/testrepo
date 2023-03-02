def f(x):
    return x**3*(x-141)
x=67.5
for n in range(-2,-15,-1):
    delta=10**n
    df_dx=(f(x+delta)-f(x))/delta
    print("the derivative with delta=",delta,"is",df_dx)
#the delta that is most accurate is 10^-6