utils.py



def ler_float(num):    
   while True:
    try:
        return float(input(num))
    except ValueError:
        print("Entrada inválida, digite um número.")
    
def ler_str(nome):   

    return input(nome)
