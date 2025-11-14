from random import randint, sample

def allChainedPathsAreShort(n):
    '''1 if none of the index-chasing cycles in a shuffled
       sample of [1..n] cards are longer than half the
       sample size. Otherwise, 0.
    '''
    limit = n // 2
    xs = range(1, 1 + n)
    shuffled = sample(xs, k=n)

    # A cycle of boxes, drawn from a shuffled
    # sample, which includes the given target.
    def cycleIncluding(target):
        boxChain = [target]
        v = shuffled[target - 1]
        while v != target:
            boxChain.append(v)
            v = shuffled[v - 1]
        return boxChain
    # Nothing if the target list is empty, or if the cycle which contains the
    # first target is larger than half the sample size.
    # Otherwise, just a cycle of enchained boxes containing the first target
    # in the list, tupled with the residue of any remaining targets which
    # fall outside that cycle.
    def boxCycle(targets):
        if targets:
            boxChain = cycleIncluding(targets[0])
            return Just((
                difference(targets[1:])(boxChain),
                boxChain
            )) if limit >= len(boxChain) else Nothing()
        else:
            return Nothing()

    # No cycles longer than half of total box count ?
    return int(n == sum(map(len, unfoldr(boxCycle)(xs))))

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
    '''Constructor for an inhabited Maybe (option type) value.
       Wrapper containing the result of a computation.
    '''
    return {'type': 'Maybe', 'Nothing': False, 'Just': x}
    
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

