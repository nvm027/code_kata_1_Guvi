alpha = input("Type an alphabet: ")

if alpha in ('a', 'e', 'i', 'o', 'u'):
	print("%s is a vowel." % alpha)
elif alpha == 'y':
	print("May be a Vowel based on Usage")
else:
	print("%s is a consonant." % alpha) 
