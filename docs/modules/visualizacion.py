import sympy as sp
import numpy as np
from IPython.display import display, Math, Latex


def mostrar_matriz(array):
    """
    Muestra una matriz en formato LaTeX.
    """
    # Configuramos Sympy para usar parentesis en vez de corchetes
    sp.init_printing(use_latex='mathjax',
                     latex_mode='equation',
                     print_builtin=False,
                     forecolor='black',
                     backcolor='White',
                     fontsize='10pt',
                     use_unicode=True,
                     mat_str='matrix',
                     mat_delim='(',)
    # Mostramos la matriz
    display(array)