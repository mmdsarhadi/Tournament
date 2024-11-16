from LinkedList import LinkedList


def ls(plan, low1, high1, low2, high2, flag=False):
    number = LinkedList()
    for i in range(high2 + 1, low2, -1):
        number.add(i)


    for i in range(low1, high1 + 1):
        helper = LinkedList()
        helper.add(number.tail.data)
        for j in range(low2, high2 + 1):
            temp = number.delete()
            plan[i][j] = temp
            if j == high2:
                continue
            helper.add(temp)
        number = helper
        helper = LinkedList()

    for i in range(low1, high1 + 1):
        for j in range(low2, high2 + 1):
            plan[plan[i][j] - 1][j] = i + 1

    k = 0
    for i in range(low2, high2 + 1):
        for j in range(low1, high1 + 1):
            if plan[k][j] == '-':
                continue
            plan[i][j] = plan[k][j] + high1 + 1
        k += 1
    for i in range(low1, high2 + 1):
        for j in range(low1, high2 + 1):
            if plan[i][j] == '-':
                plan[i][j] = plan[i][high2]


def schedule(plan, rows, cols, low, high, flag=False):
    if high <= low:
        return
    if high - 3 == low:
        if flag:
            plan[0][:3] = [2, 3, 4]
            plan[1][:3] = [1, 4, 3]
            plan[2][:3] = [4, 1, 2]
            plan[3][:3] = [3, 2, 1]
            return
        plan[0][:3] = [2, 3, '-']
        plan[1][:3] = [1, '-', 3]
        plan[2][:3] = ['-', 1, 2]
        return

    if high - 1 == low:
        plan[low][0] = high + 1
        plan[high][0] = low + 1
        return
    mid = (high + low) // 2
    if (high + 1) % 2 == 1:
        schedule(plan, rows, cols, low, high + 1)
        if high -2 == low:
            return
        for i in range(high + 1):
            for j in range(high + 1):
                if (plan[i][j] != '-' and plan[i][j] > high+1):
                    plan[i][j] = '-'
                    continue
        return
    else:
        schedule(plan, rows, cols, low, mid, True)
        ls(plan, low, mid, mid + 1, high, True)


n = int(input())
plan = []
rows = [set() for _ in range(n + 1)]
cols = [set() for _ in range(n + 1)]
for i in range(n + 1):
    plan.append(['-'] * (n + 1))
if n % 2 == 0:
    schedule(plan, rows, cols, 0, n - 1, True)
    for i in range(n):
        print("Team" + str(i+1) + " : " , end='')
        for j in range(n - 1):
            en = (4 - len(str(plan[i][j]))) * " "
            print(plan[i][j], end=en)
        print()

else:
    schedule(plan, rows, cols, 0, n)

    for i in range(n):
        print("Team" + str(i+1) + " : " , end='')

        for j in range(n):
            if plan[i][j] > n:
                print("-", end='   ')
                continue
            en = (4-len(str(plan[i][j])) )*" "
            print(plan[i][j], end=en)
        print()
