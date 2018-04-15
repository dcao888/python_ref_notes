import os

# specfiy location (rel to __file__) of target.txt
target_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "../docs/target.txt")
try:
    # read file and print contents 
    with open(target_path) as f:
        print(f.read())
except:
    print("ERROR: unable to read target.txt")

