from random import randint
encrypt = open("encryption", "w")
def length():
	length = input("How many characters you like to be encrypted? ")
	return length
def message():
	message = input("What message would you like to be encrypted? ")
	return message
def num_generator():
	number = length()
	rand_num = open("otp", "w")
	for x in range(number):
		random = randint(0,24)
		rand_num.write(random"\n"())
		rand_num.close()
def encrypting(count):
	global encrypt
	for count, number in enumerate(encrypt):
		print(count, number)

# def enter_message(): 
#	global encrypt
#	encrypt.write(message())
#	encrypt.close()
	
