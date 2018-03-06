arr = []
ipt=int(input("Enter No. of Elements:"))
for i in range(1,ipt+1):
    arr.append(int(input("Enter the %s number: ")))
arr_size = len(arr)
def printRepeating(arr,size) :
	count = [0] * size
	print(" Repeating elements are ",end = "")
	for i in range(0, size) :
		if(count[arr[i]] == 1) :
			print(arr[i], end = " ")
		else :
			count[arr[i]] = count[arr[i]] + 1
			print("Unique")
printRepeating(arr, arr_size)
