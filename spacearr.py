T = int(input())
for i in range(T):
    N = int(input())
    temp = (N * (N+1))/2
    a = list(map(int,input().split()))
    a.sort()
    s = sum(a)
    s = temp-s
    j = 1
    for item in a:
        if item > j:
            print("Second")
            break
        j += 1
    else:
        if(s <= 0 or s%2 == 0):
            print("Second")
        else:
            print("First")
        
    