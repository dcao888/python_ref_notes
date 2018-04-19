Problem:
which direction does an import go? i.e. if module A imports module B, is env A
passed to B or vice versa, or both?

Solution: 
running primary.py (A) imports from both secondary (B) and tertiary (C). Env C
is passed to A but env A is not passed to B. Thus, when only the called
module's env is passed to the caller module, but not vice versa.
