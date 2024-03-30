def checkPalindrome(s):
    # Write your code here
	# Return a boolean
	k=['a','b','c','d','e','f','g','i','j','k','l','m',
	'n','o','p','q','r','s','t','u','v','w','x','y','z','h']
	l=[]
	st=s.lower()
	for i in range(len(st)):
		if st[i] in k:
			l.append(st[i])
	lt=str(l)
	sti=str(st)
	if lt==st:
		return "Yes"
	return "No"
print(checkPalindrome("mam"))
    