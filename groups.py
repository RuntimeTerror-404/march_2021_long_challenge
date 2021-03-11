T = int(input())
for i in range(T):
    row = input().split('0')
    newRow = [x for x in row if x != '']
    print(len(newRow))

