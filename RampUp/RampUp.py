import pyfiglet
import random
import time
from PIL import Image


def encrypt(word):
	word = word.lower()
	# layer 1: randomized encryption
	numLet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
	'p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6',
	'7','8','9']

	reset()
	random.shuffle(numLet)
	shuffled = numLet
	numLet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
	'p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6',
	'7','8','9']

	newWord = ""
	for i in range(len(word)):
		for j in range(len(numLet)):
			# find the char in word and match it to the shuffled value
			if word[i] == numLet[j]:
				adder = shuffled[j]
				break
			else:
				adder = ' '

		newWord = newWord + adder


	# layer 2: hard-coded encryption
	# converts to Chinese/Wa(Myanmar)??
	encrypted = ''
	for i in newWord:
		# takes the ascii value and multiplies by 200
		asc = ord(i)
		asc *= 200
		encrypted = encrypted + chr(asc)

	return encrypted


def decrypt(word):
	# layer 1: hard-coded decryption
	decrypted = ''
	for i in word:
		# takes the ascii value and divides by 200
		asc = ord(i)
		asc /= 200
		decrypted = decrypted + chr(int(asc))

	# layer 2: randomized decryption
	numLet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
	'p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6',
	'7','8','9']

	random.shuffle(numLet)
	shuffled = numLet
	numLet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
	'p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6',
	'7','8','9']

	newWord = ""
	for i in range(len(decrypted)):
		for j in range(len(shuffled)):
			# find the character in the word and match it to the correct value
			if decrypted[i] == shuffled[j]:
				adder = numLet[j]
				break
			else:
				adder = ' '

		newWord = newWord + adder

	return newWord


def reset():
	random.seed(10)


def main():
	# Project title
	example = pyfiglet.figlet_format("Ramp Up Project!")
	print(example)

	while True:
		command = input("Input command: ")

		if command.lower()[0] == 'r':
			reset()

		elif command.lower()[0] == 'e':
			encWord = input("Enter the message to be encrypted: ")
			print("Encrypting...")
			time.sleep(1)

			print("Encrypted Message:")
			print(encrypt(encWord), '\n')

		elif command.lower()[0] == 'd':
			decWord = input("Enter the message to be decrypted: ")
			print("Decrypting...")
			time.sleep(1)

			print("Decrypted Message:")
			print(decrypt(decWord), '\n')
		else:
			print("Invalid selection!")

		cont = input("Continue with another operation?[y/n]: ")
		print()
		if cont.lower()[0] == 'n':
			print("Thak you for using the Ramp Up Project!")
			print("Here's a picture of my cat :)")
			im = Image.open(r"cat.jpg")
			im.show()
			break
	
main()
