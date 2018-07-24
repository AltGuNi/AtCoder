S = input()
T = input()
if( len(S) != len(T) ):
	print("No")
	exit()
for i in range(len(S)):
	if(S == T):
		print("Yes")
		exit()
	S = S[1:]+S[0]
print("No")
