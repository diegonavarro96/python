import random
#make a list of words
#	
words = [
		'apple',
		'bannana',
		'orange',
		'cococnut',
		'strawberry',
		'lime',
		'grapefruit',
		'lemon',
		'kumquat',
		'blueberry',
		'melon'
]
while True:
	start=input("press enter/ return to start over, or enter Q to quit")
	if start.lower() == 'q':
		break
	secret_word = random.choice(words)
	bad_guesses = []
	good_guesses = []
	while len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_word)):
		#draw spaces
		for letter in secret_word:
			if letter in good_guesses:
				print(letter,end='')
			else:
				print('_', end='')
		print('')
		print('strikes: {}/7'.format(len(bad_guesses)))
		print('')
		guess=input("Guess a letter:").lower()

		if len(guess)!= 1:
			print ("you can only guess a single letter!")
			continue
		elif guess in bad_guesses or guess in good_guesses:
			print ("you've alraedy guess that letter")
			continue
		elif not guess.isalpha():
			print ("you can only guess letters!")
			continue
		if guess in secret_word:
			good_guesses.append(guess)
			if len(good_guesses) == len(list(secret_word)):
				print ("you win! the word was {}".format(secret_word))
				print("")
				break
		else: 
			bad_guesses.append(guess)
	else:
		print("you didint guess the secret word, the secret wor was {}".format(secret_word))
