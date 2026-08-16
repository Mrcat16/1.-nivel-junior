lambis = [33,55,12,76]
for i in range(len(lambis)):
    for j in range(len(lambis)-1-i):
        if lambis[j] > lambis[j+1]:
            lambis[j], lambis[j+1] = lambis[j+1], lambis[j]
print(f"Lista ordenada {lambis}")

# i = 0 [33,12,55,76]

# i = 1 [12,33,55,76]

# i = 2 [12,33,55,76]

# i = 3 [12,33,55,76]