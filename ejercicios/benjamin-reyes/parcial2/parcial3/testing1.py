def calcular_media(*args):
    """"Devuelve el valor de la media o promedio de un conjunto de datos numericos.

    Args:
    *args (int): Un número variable de argumentos que representan los datos numericos 
    Returns:
    (float): El valor de la medida  o promedio de los datos numericos 
    """

    return (sum(*args)/len(*args))
assert(calcular_media([]))