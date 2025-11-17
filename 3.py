n = 5
for i in range(1, n+1):            # Loop for rows
    for j in range(n-i):           # Loop for '#'
        print("#", end="")
    for k in range(2*i-1):         # Loop for '*'
        print("*", end="")
    print()

print("another pattern")
n = 5
for i in range(1, n+1):            # Loop for rows
    # Print '#' before stars
    for j in range(n-i):
        print("#", end="")
    # Print stars
    for k in range(2*i-1):
        print("*", end="")
    # Print '#' after stars
    for j in range(n-i):
        print("#", end="")
    print()
