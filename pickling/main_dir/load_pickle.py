import pickle

filename = "testfile"

open_file = open(filename, 'rb') # open file
loaded_pickle = pickle.load(open_file) # load pickle
open_file.close() # close file

print(loaded_pickle)
