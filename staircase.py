def num_ways(n):
    for i in range(0, n):
        for j in range(0,n):
            if i + j >= n - 1:
                print("#", end="")
            else:
                print(" ", end="")
        print("\r",)
    return " "

print(num_ways(20))