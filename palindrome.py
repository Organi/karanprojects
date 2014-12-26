word = raw_input()
length = len(word)

start = word[0:length/2]
if length % 2 == 0:
	end = word[length/2:length]
else:
	end = word[length/2+1:length]

isPalendrome = True
for i in range(0,len(start)):
	if start[i] != end[len(end)-(i+1)]:
		isPalendrome = False
		break

if isPalendrome:
	print word+" is a palendrome"
else:
	print word+" is not a palendrome"
