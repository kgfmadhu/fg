k=['a','b','c','d','e','f','g','i','j','k','l','m',
	'n','o','p','q','r','s','t','u','v','w','x','y','z','h']
s="5?36@6?35"
s=s.lower()
l=""
print(s)
for i in s:
    if i in k:
        l+=i
print(l)
result=l[::-1]
print(result)
if result==l:
    print("Yes")
else:
    print("No")