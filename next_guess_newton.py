x=int(input("What x to find the square root of? "))
g=int(input("What guess to start with? "))
print(g**2)
guess=g**2-x
next_guess=g-(guess/(2*g))
print(next_guess)