def num_grid(lst):
    for i in range(5):
        for j in range(5):
            lst[i][j]=-1 if lst[i][j]=='#' else 0
    for i in range(5):
        for j in range(5):
            if lst[i][j]==-1:
                if i==0:
                    if j==0:
                        lst[i+1][j] = lst[i+1][j]+1 if lst[i+1][j]!=-1 else -1
                        lst[i][j+1] = lst[i][j+1]+1 if lst[i][j+1]!=-1 else -1
                        lst[i+1][j+1] = lst[i+1][j+1]+1 if lst[i+1][j+1]!=-1 else -1
                    elif j==4:
                        lst[i+1][j] = lst[i+1][j]+1 if lst[i+1][j]!=-1 else -1
                        lst[i][j-1] = lst[i][j-1]+1 if lst[i][j-1]!=-1 else -1
                        lst[i+1][j-1] = lst[i+1][j-1]+1 if lst[i+1][j-1]!=-1 else -1
                    else:
                        lst[i+1][j] = lst[i+1][j]+1 if lst[i+1][j]!=-1 else -1
                        lst[i][j+1] = lst[i][j+1]+1 if lst[i][j+1]!=-1 else -1
                        lst[i+1][j+1] = lst[i+1][j+1]+1 if lst[i+1][j+1]!=-1 else -1
                        lst[i][j-1] = lst[i][j-1]+1 if lst[i][j-1]!=-1 else -1
                        lst[i+1][j-1] = lst[i+1][j-1]+1 if lst[i+1][j-1]!=-1 else -1
                elif i==4:
                    if j==0:
                        lst[i-1][j] = lst[i-1][j]+1 if lst[i-1][j]!=-1 else -1
                        lst[i][j+1] = lst[i][j+1]+1 if lst[i][j+1]!=-1 else -1
                        lst[i-1][j+1] = lst[i-1][j+1]+1 if lst[i-1][j+1]!=-1 else -1
                    elif j==4:
                        lst[i-1][j] = lst[i-1][j]+1 if lst[i-1][j]!=-1 else -1
                        lst[i][j-1] = lst[i][j-1]+1 if lst[i][j-1]!=-1 else -1
                        lst[i-1][j-1] = lst[i-1][j-1]+1 if lst[i-1][j-1]!=-1 else -1
                    else:
                        lst[i-1][j] = lst[i-1][j]+1 if lst[i-1][j]!=-1 else -1
                        lst[i][j+1] = lst[i][j+1]+1 if lst[i][j+1]!=-1 else -1
                        lst[i-1][j+1] = lst[i-1][j+1]+1 if lst[i-1][j+1]!=-1 else -1
                        lst[i][j-1] = lst[i][j-1]+1 if lst[i][j-1]!=-1 else -1
                        lst[i-1][j-1] = lst[i-1][j-1]+1 if lst[i-1][j-1]!=-1 else -1
                else:
                    if j==0:
                        lst[i-1][j] = lst[i-1][j]+1 if lst[i-1][j]!=-1 else -1
                        lst[i][j+1] = lst[i][j+1]+1 if lst[i][j+1]!=-1 else -1
                        lst[i-1][j+1] = lst[i-1][j+1]+1 if lst[i-1][j+1]!=-1 else -1
                        lst[i+1][j] = lst[i+1][j]+1 if lst[i+1][j]!=-1 else -1
                        lst[i+1][j+1] = lst[i+1][j+1]+1 if lst[i+1][j+1]!=-1 else -1
                    elif j==4:
                        lst[i+1][j] = lst[i+1][j]+1 if lst[i+1][j]!=-1 else -1
                        lst[i][j-1] = lst[i][j-1]+1 if lst[i][j-1]!=-1 else -1
                        lst[i+1][j-1] = lst[i+1][j-1]+1 if lst[i+1][j-1]!=-1 else -1
                        lst[i-1][j] = lst[i-1][j]+1 if lst[i-1][j]!=-1 else -1
                        lst[i-1][j-1] = lst[i-1][j-1]+1 if lst[i-1][j-1]!=-1 else -1
                    else:
                        lst[i-1][j-1] = lst[i-1][j-1]+1 if lst[i-1][j-1]!=-1 else -1
                        lst[i-1][j] = lst[i-1][j]+1 if lst[i-1][j]!=-1 else -1
                        lst[i-1][j+1] = lst[i-1][j+1]+1 if lst[i-1][j+1]!=-1 else -1
                        lst[i+1][j] = lst[i+1][j]+1 if lst[i+1][j]!=-1 else -1
                        lst[i][j+1] = lst[i][j+1]+1 if lst[i][j+1]!=-1 else -1
                        lst[i+1][j+1] = lst[i+1][j+1]+1 if lst[i+1][j+1]!=-1 else -1
                        lst[i][j-1] = lst[i][j-1]+1 if lst[i][j-1]!=-1 else -1
                        lst[i+1][j-1] = lst[i+1][j-1]+1 if lst[i+1][j-1]!=-1 else -1
    for i in range(5):
        for j in range(5):
            lst[i][j] = str(lst[i][j]) if lst[i][j]!=-1 else '#'
    return lst

print("*** Minesweeper ***")
input_list = [i.split()for i in input("Enter input(5x5) : ").split(",")]
print("\n")
for i in input_list:
    print(i)
print("\n")
for i in num_grid(input_list):
    print(i)
