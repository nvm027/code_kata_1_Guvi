while True:
	print("Enter '?' for exit.")
	ch = input("Enter any single input: ")
	if ch == '?':
		break
	else:
		if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
			print(ch, "is an alphabet.\n")
		else:
			print(ch, "is not an alphabet.\n")
