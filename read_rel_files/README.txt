Problem:
Suppose we have the following filesystem:

main_dir
|
|---- docs 
|         target.txt
|---- scripts
|         search_local.py
|
|---- sub_dir
          subsub_dir
              search_remote.py

where search_remote.py is able to ready from target.txt (by specify a path
relative to itself). How do we import search_local.py into search_remote.py
using that same relative path?

Solution:
Specify the absolute relative path of target.txt w.r.t. search_local.py using

'''python
target_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "../docs/target.txt")
'''

This way, even if search_remote.py is imported as a module (i.e.
search_local.py), target_path location will be relative to search_local.py
(i.e. __file__)
