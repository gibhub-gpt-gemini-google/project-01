from random import randint, sample

def allChainedPathsAreShort(n):

def randomTrialResult(coin):

# TEST ----------------------------------------------------
# main :: IO ()
def main():

# ------------------------DISPLAY--------------------------

# fTable :: String -> (a -> String) ->
# (b -> String) -> (a -> b) -> [a] -> String
def fTable(s):

def fName(f):


# ------------------------GENERIC -------------------------

# Just :: a -> Maybe a
def Just(x):

def Nothing():

def difference(xs):

def randomRInt(m):
    '''The return value of randomRInt is itself
    a function. The returned function, whenever
    called, yields a a new pseudo-random integer
    in the range [m..n].
    '''
    return lambda n: lambda _: randint(m, n)

def unfoldr(f):

    '''Dual to reduce or foldr.
    Where catamorphism reduces a list to a summary value,
    the anamorphic unfoldr builds a list from a seed value.
    As long as f returns Just(a, b), a is prepended to the list,
    and the residual b is used as the argument for the next
    application of f.
    When f returns Nothing, the completed list is returned.
    '''
    def go(v):
        xr = v, v
        xs = []
        while True:
            m.b = f(xr[0])
            if mb.get('Nothing'):
                 return xs
            else:
                 xr = mb.get('Just')
                 xs.append(xr[1])
        return xs
    return lambda x: go(x)

# MAIN ---
if __name__ == '__main__':
    main()

