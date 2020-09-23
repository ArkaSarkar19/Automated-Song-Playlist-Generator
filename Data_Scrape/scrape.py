import os
import pickle

maxm_779k_dataset = open("mxm_779k_matches.txt", "r")
mxm_train_dataset = open("mxm_dataset_train.txt", "r")
mxm_test_dataset = open("mxm_dataset_test.txt", "r")
bow = open("BOW.txt", "r")

# print(maxm_779k_dataset.read())

"""
779k_matches Format : 
    -> comment, ignore
#     tid|artist name|title|mxm tid|artist_name|title
#        tid          -> Million Song Dataset track ID
#        artist name  -> artist name in the MSD
#        title        -> title in the MSD
#        mxm tid      -> musiXmatch track ID
#        artist name  -> artist name for mXm
#        title        -> title for mXm
#        |            -> actual separator: <SEP>

"""
bow = list(bow.read().split(","))
# print(bow)
dict_ = {}

for line in maxm_779k_dataset:
	content = line.split("<SEP>")
	content[-1] = content[-1][:-1]
	dict_[content[0]] = (content[1:])
	# print(contents)

lyrics = {}
for line in mxm_train_dataset:
	content = line.split(",")
	content[-1] = content[-1][:-1]
	if(content[0] in dict_):
		lyrics[content[0]] = (dict_[content[0]], list(content[2:]))
	# print(content)


for line in mxm_test_dataset:
	content = line.split(",")
	content[-1] = content[-1][:-1]
	if(content[0] in dict_):
		lyrics[content[0]] = (dict_[content[0]], list(content[2:]))


# print(len(lyrics))


# for i in lyrics:
# 	print(" song = ", lyrics[i][0][4], " artist  = ", lyrics[i][0][3] )

f = open("dataset.pkl" , "wb")

pickle.dump(lyrics,f)
f.close()

print("Dataset Saved to dataset.pkl")

import pickle

f = open("dataset.pkl" , "rb")
dict1 = pickle.load(f)
f.close()
for key in dict1:
	print(dict1[key][0][3], dict1[key][0][4])

print(len(dict1))