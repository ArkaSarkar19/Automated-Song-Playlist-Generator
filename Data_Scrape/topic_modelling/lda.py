import pickle
import gensim

f = open("../Dataset/BOW.txt", "r")

for line in f:
	list_of_words = line.split(',')
f.close()

# print(list_of_words)

index_to_words = {}
for i in range(len(list_of_words)):
	index_to_words[i] = list_of_words[i]

f = open("../Dataset/dataset.pkl", "rb")
msdid_to_lyrics =  pickle.load(f)
f.close()

msd_ids = list(msdid_to_lyrics.keys())

# print(msd_ids)
# print(msdid_to_lyrics[list(msdid_to_lyrics.keys())[0]])
processed_docs = []

for msd_id in msd_ids:
	lyrics = msdid_to_lyrics[msd_id][-1]

	word_lyrics = []
	for c in lyrics:
		collon_index = c.find(':')
		ind = int(c[:collon_index])
		freq = int(c[collon_index+1:])
		for i in range(freq):
			word_lyrics.append(index_to_words[ind])
	processed_docs.append(word_lyrics)
		# print(ind, freq)


