def schedule(n):
    if n==2:
        data[1][1] = 2
        data[2][1] = 1
        return
    if n > 2:
        if n %2 ==0:
            schedule(n//2)
            sysmes(n)
            fill(n)
            removelastday(n)
        else:
            schedule(n+1)
            removelastteam(n)

    else:
        schedule(n+1)


def sysmes(n):
    end = n//2
    for i in range(1,end+1):
        for j in range(1,end+1):
            if data[i][j] != 0:
                data[i+n//2][j] = data[i][j] + n/2

def fill(n):
    if n//2 % 2 == 0:
        start = n//2
        end = n-1
    else:
        start = n//2 + 1
        end = n

    last = n
    first = n//2 + 1
    k = last
    for i in range(1,n//2 + 1):
        for j in range(start,end + 1):
            data[i][j] = k
            data[k][j] = i
            if j != end:
                if k == first:
                    k = last
                else : 
                    k = k-1 

def print_teams(n):
    print("       ",end="")
    for i in range(1,n+1):
        print(f" day {i} ",end="")
    print("\n")
    for i in range(1,n+1):
        print(f"team {i} : ",end="")
        for j in range(1,n+1):
            if data[i][j] == 0:

                print(f"  _     ",end="")
            elif data[i][j] % 10 == data[i][j]:
                print(f"  {int(data[i][j])}    ",end="")
            else:
                print(f"  {int(data[i][j])}   ",end="")
        print("\n")


def removelastday(n):
    for i in range(1,n+1):
        temp = data[i][n]
        data[i][n] = 0
        j = 1
        while data[i][j] != 0:
            j = j+1
        data[i][j] = temp
        data[temp][j] = i

def removelastteam(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if data[i][j] == n +1 :
                data[i][j] = 0



if __name__ == "__main__":
    n = int(input("enter:"))
    data= [[0 for i in range(n+2)] for j in range(n+2)]
    schedule(n)
    print_teams(n)
