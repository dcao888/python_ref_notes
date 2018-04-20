import pickle

to_be_pickled = list("Hello World!")

filename = "testfile"

open_file = open(filename, 'wb') # open file
pickle.dump(to_be_pickled, open_file) # dump pickle
open_file.close() # close file


