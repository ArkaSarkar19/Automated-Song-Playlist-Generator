import os
import pickle

f1 = open("Msd_id_to_spotify_id_0-80000.pkl", "rb")
f2 = open("Msd_id_to_spotify_id_80000_to_160000.pkl", "rb")
f3 = open("Msd_id_to_spotify_id_160k_end.pkl", "rb")

dict_1 = pickle.load(f1)
dict_2 = pickle.load(f2)
dict_3 = pickle.load(f3)

# print(len(dict_1))
# print(len(dict_2))
# print(len(dict_3))

dict_1.update(dict_2)
dict_1.update(dict_3)

f1.close()
f2.close()
f3.close()
# print(len(dict_1))

save_file = open("Msd_id_to_spotify_id.pkl", "wb")

pickle.dump(dict_1, save_file)
save_file.close()

print("Successfully combined MSD_ID to SPOTIFY_ID")