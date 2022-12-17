for i in range(0, 5):  # outer loop -> i: 0, 1, 2, 3, 4
    for j in range(0, 10):  # inner loop -> j: 0, 1, 2, ,3, 4, 5, 6, 7, 8, 9
        if 5 - i <= j <= 5 + i: # 5 <= j <= 5
            print("*", end="")
        else:
            print(" ", end="")
    print()
# 0123456789
# bbbbb*bbbb i=0
# bbbb***bbb i=1
# bbb*****bb i=2
# bb*******b i=3
# b********* i=4