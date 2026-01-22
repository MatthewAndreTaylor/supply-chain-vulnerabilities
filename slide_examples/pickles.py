import pickle, builtins

class A:
    def __reduce__(self):
        return (builtins.print, ("hello world",))

class B:
    def __reduce__(self):
        return (pickle.loads, (pickle.dumps(A()),))

outer_pickle = pickle.dumps(B())
print(outer_pickle)

pickle.loads(outer_pickle)