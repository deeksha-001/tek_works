x = input()
vc = cc = 0
n = len(x)

for i in range(0,len(x),1):
    if(i == 'a' or i == 'e' or i == 'i' or i =='o' or i == 'u'):
        vc = vc + 1
    
    else:
        cc = cc + 1

print("Vowel count: ",vc)
print("Character count: ",cc)