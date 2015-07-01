import sys
sentence = []
quote = 0

def display():
	global sentence
	print(" ".join(w for w in sentence))
	sentence = []

def add(word):
	global sentence
	global quote
	
	q_pos = word.find("\"")
	if q_pos != -1:
		if quote == 0:
			quote = 1
		elif quote == 1:
			quote = 0

	sentence.append(word)
	if word[-1:] in (".","?","!") and quote == 0:
		display()

if __name__ == '__main__':

	ip = ["In the third category he included those Brothers (the majority) who saw nothing in Freemasonry but the external forms and ceremonies, and prized the strict performance of these forms without troubling about their purport or significance. Such were Willarski and even the Grand Master of the principal lodge. Finally, to the fourth category also a great many Brothers belonged, particularly those who had lately joined. These according to Pierre's observations were men who had no belief in anything, nor desire for anything, but joined the Freemasons merely to associate with the wealthy young Brothers who were influential through their connections or rank, and of whom there were very many in the lodge.Pierre began to feel dissatisfied with what he was doing. Freemasonry, at any rate as he saw it here, sometimes seemed to him based merely on externals. He did not think of doubting Freemasonry itself, but suspected that Russian Masonry had taken a wrong path and deviated from its original principles. And so toward the end of the year he went abroad to be initiated into the higher secrets of the order.What is to be done in these circumstances? To favor revolutions, overthrow everything, repel force by force?No! We are very far from that. Every violent reform deserves censure, for it quite fails to remedy evil while men remain what they are, and also because wisdom needs no violence. \"But what is there in running across it like that?\" said Ilagin's groom. \"Once she had missed it and turned it away, any mongrel could take it,\" Ilagin was saying at the same time, breathless from his gallop and his excitement."]
	# ip = sys.stdin.readlines()
	text = ip[0].split()
	
	for word in text:
		pos1 = word.find('.')
		pos2 = word.find('?')
		pos3 = word.find('!')
		
		if quote == 0:
			if (pos1 != -1):
				two_words = word.split('.')
				add(two_words[0] + ".")

				if (two_words[1] != ""):
					add(two_words[1])

			elif (pos2 != -1):
				two_words = word.split('?')
				add(two_words[0] + "?")

				if (two_words[1] != ""):
					add(two_words[1])

			elif (pos3 != -1):
				two_words = word.split('!')
				add(two_words[0] + "!")

				if (two_words[1] != ""):
					add(two_words[1])

			else:
				add(word)

		else:
			add(word)