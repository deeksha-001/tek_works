a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if(a>b and a>c and a>d and a>e):
    print(a)
    if(b>c and b>d and b>e):
        print(b)
        if(c>d and c>e):
            print(c)
            if(d>e):
                print(d)

else:
    print(e)
