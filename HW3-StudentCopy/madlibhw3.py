# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
print("START*******")

# code developed by Jackie Cohen; revised by Paul Resnick
# further revised by Colleen van Lent for Python3
import nltk 
from nltk.book import *
import random
from nltk import word_tokenize,sent_tokenize

print('\nKennedy Kaufman // 61371023\n\n\n')


nltk.download('punkt')    # import nltk



debug = False #True

text2 = (text2[:150])
para = ' '.join(text2)
print(para)                       # generate original text
tokens = nltk.word_tokenize(para)
tagged_tokens = nltk.pos_tag(tokens) # gives a tagged list of tuples
if debug:
	print ("First few tagged tokens are:")
	for tup in tagged_tokens[:5]:
		print (tup)

tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective"}        # what parts of speech to tag
substitution_probabilities = {"NN":.15,"NNS":.1,"VB":.1,"JJ":.1, "RB":.1}

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:         #look only for words and not extra characters
		return word
	else:
		return " " + word

final_words = []


for (word, tag) in tagged_tokens:                        # replacing tagged words
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))

print ("".join(final_words))

print("\n\nEND*******")
