import sys

def main():
    ans = 0
    i = 0
    temp = []
    for line in sys.stdin:
        temp.append(int(line))
    while True:
        ans += 1
        j = i
        i = j + temp[j]
        if temp[j] > 2:
            temp[j] -= 1
        else:
            temp[j] += 1
        if (i < 0 or i >= len(temp)):
            break
    print(ans)

main()
