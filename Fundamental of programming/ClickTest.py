
def integer_sum(n):
  if n < 1:
    return 0
  else:
    return n + integer_sum(n-2)


n = int(input("Give a non-negative integer n:\n"))
print("n + (n-2) + (n-4) + ... =", integer_sum(n))

input("Press Enter to exit...")
 
