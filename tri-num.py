limit = int(input("Limit: "))
n = 0
m = 1
while n <= limit:
  n = n + m
  if n <= limit:
    print(n)
  m = m + 1
