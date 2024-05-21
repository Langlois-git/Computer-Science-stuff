# Order of recursive calls
# When you make a function call you have to wait for it to return before you can do anything else.
# The Cascade Function

def cascade_complex(n):
    if n < 10:
        print(n, "1st print")
    else:
        print(n, "2nd print")
        cascade(n//10)
        print(n, "3rd print")

def cascade(n):
    print(n)
    if n > 10:
        cascade(n//10)
        print(n)

# The two definitions of cascade
# - Both are equally clear, so its better to use the shorter one
# When learning to write recursive functions put base cases first

