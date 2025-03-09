import sys
import json
import os

# Nombre del archivo donde se guardarán los clientes
CLIENTES_FILE = "clientes.json"

def cargar_clientes():
    """Carga la lista de clientes desde un archivo JSON."""
    if os.path.exists(CLIENTES_FILE):
        with open(CLIENTES_FILE, "r") as file:
            return json.load(file)
    return {}

def guardar_clientes(clientes):
    """Guarda la lista de clientes en un archivo JSON."""
    with open(CLIENTES_FILE, "w") as file:
        json.dump(clientes, file, indent=4)

def listar_clientes():
    """Lista todos los clientes registrados."""
    clientes = cargar_clientes()
    if not clientes:
        print("No hay clientes registrados.")
    else:
        for nombre, datos in clientes.items():
            print(f"Nombre: {nombre}, Dirección: {datos['direccion']}, Teléfono: {datos['telefono']}, Servicio: {datos['servicio']}")

def crear_cliente(nombre, direccion, telefono, servicio):
    """Crea un nuevo cliente con los datos proporcionados."""
    clientes = cargar_clientes()
    if nombre in clientes:
        print("El cliente ya existe.")
        return
    clientes[nombre] = {"direccion": direccion, "telefono": telefono, "servicio": servicio}
    guardar_clientes(clientes)
    print(f"Cliente {nombre} creado con éxito.")

def ver_cliente(nombre):
    """Muestra la información de un cliente específico."""
    clientes = cargar_clientes()
    if nombre in clientes:
        datos = clientes[nombre]
        print(f"Nombre: {nombre}, Dirección: {datos['direccion']}, Teléfono: {datos['telefono']}, Servicio: {datos['servicio']}")
    else:
        print("El cliente no existe.")

def actualizar_cliente(nombre, nuevo_servicio):
    """Actualiza el servicio de un cliente existente."""
    clientes = cargar_clientes()
    if nombre in clientes:
        clientes[nombre]["servicio"] = nuevo_servicio
        guardar_clientes(clientes)
        print(f"Cliente {nombre} actualizado con nuevo servicio: {nuevo_servicio}.")
    else:
        print("El cliente no existe.")

def main():
    if len(sys.argv) < 2:
        print("Uso: python gestor_clientes.py [listar|crear|ver|actualizar] [args...]")
        return
    
    comando = sys.argv[1]
    
    if comando == "listar":
        listar_clientes()
    elif comando == "crear" and len(sys.argv) == 6:
        _, _, nombre, direccion, telefono, servicio = sys.argv
        crear_cliente(nombre, direccion, telefono, servicio)
    elif comando == "ver" and len(sys.argv) == 3:
        _, _, nombre = sys.argv
        ver_cliente(nombre)
    elif comando == "actualizar" and len(sys.argv) == 4:
        _, _, nombre, nuevo_servicio = sys.argv
        actualizar_cliente(nombre, nuevo_servicio)
    else:
        print("Comando no válido o argumentos insuficientes.")

if __name__ == "__main__":
    main()