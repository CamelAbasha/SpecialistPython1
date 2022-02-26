a = int(input("1 сторона:"))
b = int(input("2 сторона:"))
c = int(input("3 сторона:"))

answer="NO"
if a==b or a==c or b==c:
	answer="YES"
print(answer)
