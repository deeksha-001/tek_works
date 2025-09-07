#reverse of string without slicing

a = input("enter name: ")
n = len(a)
start = 0
end = n - 1

rev =" "

while(start <= end):
    rev = rev + a[end]
    end = end - 1
    
print(rev)