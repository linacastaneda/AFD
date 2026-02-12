import sys # Importa el módulo sys para poder leer argumentos de la consola (sys.argv)

# Estados finales, de aceptacion, si al final queda en "q2" ACEPTA
ESTADOS_FINALES = {"q2"}

# Función de transición
def transicion(estado, simbolo):
    #Estado = estado actual"
    #simbolo = simbolo leido de la cadena "
    if estado == "q1":  # inicial
        if simbolo == "0":
            return "q2"
        elif simbolo == "1":
            return "q3"
    elif estado == "q2": # aceptacion
        if simbolo in {"0", "1"}:
            return "q2"
    elif estado == "q3": # rechazo
        if simbolo in {"0", "1"}:
            return "q3"
    return None # si no existe transicion valida

def procesar_cadena(cadena): # cadena entrada binaria retorna bool
    estado_actual = "q1"
    for simbolo in cadena.strip(): #recorre cada simbolo de cadena .strip() es .strip() elimina espacios en blanco al inicio y al final de un texto.
        if simbolo not in {"0", "1"}:#verifica que el simbolo este en el alfabeto 0,1
            return False
        estado_siguiente = transicion(estado_actual, simbolo) #aplica la funcion de transicion
        if estado_siguiente is None: #si no existe transicion la rechaza
            return False
        estado_actual = estado_siguiente #actualiza el estado actual
    return estado_actual in ESTADOS_FINALES

def main():
    #lee el archivo, procesa la linea como cadena,imprime ACEPTA O NO ACEPTA
    if len(sys.argv) != 2: # # Verificar que se haya pasado un archivo como argumento
        print("Uso: python AFD.py entrada.txt")
        sys.exit(1)
    
    archivo = sys.argv[1]  # Nombre del archivo recibido como parámetro
    
    try:
        with open(archivo, "r") as f:
            lineas = f.readlines()
        
        for linea in lineas:
            cadena = linea.strip()
            if cadena:  # Evitar líneas vacías
                if procesar_cadena(cadena):
                    print("ACEPTA")
                else:
                    print("NO ACEPTA")
    
    except FileNotFoundError:
        print(f"Error: Archivo '{archivo}' no encontrado.")
        sys.exit(1)
    except Exception as e:
        print(f"Error inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()