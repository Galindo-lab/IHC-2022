nums = [8,1,2,2,3]

def numeros_menores(v: int, l: "list") -> "list":
    return [x for x in l if x < v]

print( [len(numeros_menores(x, nums)) for x in nums ] )
