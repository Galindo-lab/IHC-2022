# Dado un arreglo de números enteros nums y un entero target, implementar una
# función que regrese los indices de dos números que sumados den como resultado
# el target.

# Asumir que siempre habrá al menos una solución, y tampoco se puede repetir
# el mismo elemento más de una vez. La respuesta se puede regresar en cualquier
# orden.

nums = [2,7,11,15]
target = 10


def sumaDos(nums, target):
    for i, v in enumerate(nums):
        missing = target - v
        if missing < 0: pass
        for j, w in enumerate(nums):
            if w == missing: return (i,j)
        
    
print(sumaDos(nums, target))
