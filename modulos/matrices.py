# Casting de matrices
def convertir_a_sympy(objeto):
    """
    Convierte un objeto a una matriz de SymPy.
    ----------
    @objeto : array de NumPy, matriz de SymPy o lista
    @return : matriz de SymPy
    """
    import sympy as sp
    import numpy as np

    # Comprobar si el objeto es una instancia de un array de NumPy
    if isinstance(objeto, np.ndarray):
        # Convertir el array de NumPy a una matriz de SymPy
        return sp.Matrix(objeto)
    elif isinstance(objeto, list):
        # Convertir la lista a una matriz de SymPy
        return sp.Matrix(objeto)
    # Comprobar si el objeto es una instancia de una matriz de SymPy
    elif isinstance(objeto, sp.Matrix):
        # No es necesario convertir, ya es una matriz de SymPy
        return objeto
    # Comprobar si el objeto es una lista
    else:
        raise TypeError(
            "El objeto proporcionado no es ni un array de NumPy, ni una matriz de SymPy, ni una lista.")


# Resoluciones sistemas de ecuaciones
def resolucion_sistema_inv(m_c,v_i):
    """
    Función que resuelve un sistema de ecuaciones lineales
    mediante la multiplicación de la inversa de la matriz
    de coeficientes por el vector de términos independientes.
    """
    # Se importa la función de inversión de matrices
    from numpy.linalg import inv
    # Se importa la función de multiplicación de matrices
    from numpy import dot

    ### Comprueba que se puede invertir la matriz
    # Se comprueba que la matriz de coeficientes sea cuadrada
    if m_c.shape[0] != m_c.shape[1]:
        return "La matriz de coeficientes no es cuadrada"
    
    # Se calcula la inversa de la matriz de coeficientes
    m_i = inv(m_c)

    # Se multiplica la inversa por el vector de términos independientes
    v_s = dot(m_i,v_i)
    # Se devuelve el vector solución

    return v_s

def resolución_sistema_diag(m_c,v_i):
    """
    Función que resuelve un sistema de ecuaciones lineales
    mediante la división de los elementos de la diagonal de la matriz
    de coeficientes por el vector de términos independientes.
    """
    # Se importa la función de división de matrices
    from numpy import divide

    # Se comprueba que la matriz de coeficientes sea cuadrada
    if m_c.shape[0] != m_c.shape[1]:
        return "La matriz de coeficientes no es cuadrada"

    # Se divide el vector de términos independientes por los elementos de la diagonal
    v_s = divide(v_i, m_c.diagonal())
    # Se devuelve el vector solución
    return v_s