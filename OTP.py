from random import randint
encrypt = open("encryption", "w")
number_list = open("otp", "w")
def length():
	length = input("How many characters you like to be encrypted? ")
	return length
def message():
	message = input("What message would you like to be encrypted? ")
	return message
def num_generator():
	number = length()
	global number_list
	for x in range(number):
		random = randint(0,24)
		rand_num.write(random"\n"())
		rand_num.close()
def saving_message():
	global encrypt
	encrypt.write(message())
	encrypt.close()
def reading_message():
	global encrypt
	encrypt.read()
	person = input("Close file? Type Yes / No: ")
		if person = "Yes":
			encrypt.close()
		elif person = "No":
			break
		else:
			print("Invalid Response")
def encrypting(start = 0):
	global encrypt
	global number_list
	n = start
	for a, number in enumerate(encrypt): 
		number_list[n]
		encrypt[n]
		n + 1

