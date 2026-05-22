main
# --- FUNCION 1: Pedir datos al usuario ---
def capturar_datos():
    """
    Solicita al usuario los datos del producto.

    Retorno:
        nombre (str): Nombre del producto.
        precio (float): Precio unitario del producto.
        cantidad (int): Cantidad de unidades.

# SISTEMA DE COBRO v1.0
nombre (str): Nombre del producto.
        precio (float): Precio unitario del producto.
        cantidad (int): Cantidad de unidades.
        
def capturar_datos():
    """
    Solicita al usuario los datos de un producto.

    Returns:
        tuple:
            nombre (str): Nombre del producto.
            precio (float): Precio unitario del producto.
            cantidad (int): Cantidad de productos.  
              main
    """
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio unitario: "))
    cantidad = int(input("Cantidad: "))
    return nombre, precio, cantidad

 main
# --- FUNCION 2: Calcular el subtotal ---
def calcular_subtotal(precio, cantidad):
    """
    Calcula el subtotal multiplicando el precio por la cantidad.

    Argumentos:
        precio (float): Precio unitario.
        cantidad (int): Número de unidades.

    Retorno:
        float: Resultado de la multiplicación.
    """
    return precio * cantidad

# --- FUNCION 3: Aplicar descuento ---
def aplicar_descuento(monto):
    """
    Aplica un descuento del 10% si el monto es mayor a $1000.

    Argumentos:
        monto (float): El subtotal de la compra.

    Retorno:
        float: Valor del descuento a restar.


def calcular_subtotal(precio, cantidad):
    """
    Calcula el subtotal de la compra.

    Args:
        precio (float): Precio unitario del producto.
        cantidad (int): Cantidad comprada.

    Returns:
        float: Resultado de multiplicar precio por cantidad.
    """
    return precio * cantidad


def aplicar_descuento(monto):
    """
    Aplica un descuento del 10% si el monto es mayor a 1000.

    Args:
        monto (float): Subtotal de la compra.

    Returns:
        float: Monto del descuento aplicado. Retorna 0 si no aplica.
 main
    """
    if monto > 1000:
        descuento = monto * 0.10
        print(f"Se aplicó un descuento del 10%: -${descuento:.2f}")
        return descuento
    return 0


main
# --- FUNCION 4: Calcular IVA ---
def calcular_iva(monto):
    """
    Calcula el impuesto IVA del 16%.

    Argumentos:
        monto (float): Monto sobre el cual calcular el impuesto.

    Retorno:
        float: Valor del IVA calculado.
    """
    return monto * 0.16

# --- FUNCION 5: Imprimir el ticket ---
def mostrar_ticket(producto, sub, desc, iva, total):
    """
    Muestra en pantalla el ticket de venta formateado.

    Argumentos:
        producto (str): Nombre del artículo.
        sub (float): Monto del subtotal.
        desc (float): Monto del descuento.
        iva (float): Monto del impuesto.
        total (float): Monto final a pagar.
        
def calcular_iva(monto):
    """
    Calcula el IVA del 16% sobre un monto.

    Args:
        monto (float): Monto al que se le aplicará el IVA.

    Returns:
        float: IVA calculado.
    """
    return monto * 0.16


def mostrar_ticket(producto, subtotal, descuento, iva, total):
    """
    Muestra el resumen de la compra en formato de ticket.

    Args:
        producto (str): Nombre del producto.
        subtotal (float): Subtotal de la compra.
        descuento (float): Descuento aplicado.
        iva (float): IVA calculado.
        total (float): Total final a pagar.
    main
    """
    print("\n--- TICKET DE VENTA ---")
    print(f"Producto: {producto}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Descuento: -${descuento:.2f}")
    print(f"IVA: ${iva:.2f}")
    print(f"TOTAL A PAGAR: ${total:.2f}")
    print("------------------------")


def main():
    """
    Función principal del programa.

    Flujo del sistema:
    1. Solicita los datos del producto al usuario.
    2. Calcula el subtotal.
    3. Aplica descuento si corresponde.
    4. Calcula el IVA sobre el subtotal con descuento.
    5. Calcula el total final.
    6. Muestra el ticket de compra.

    Returns:
        None
    """
    print("--- Sistema de Cobro v1.0 ---")

    # Captura de datos
    producto, precio, cantidad = capturar_datos()

    # Cálculos principales
    subtotal = calcular_subtotal(precio, cantidad)
    descuento = aplicar_descuento(subtotal)
    subtotal_con_desc = subtotal - descuento

    # Impuestos y total
    iva = calcular_iva(subtotal_con_desc)
    total_final = subtotal_con_desc + iva

    # Mostrar ticket
    mostrar_ticket(producto, subtotal, descuento, iva, total_final
# EJECUCIÓN DEL PROGRAMA

 main
mostrar_ticket(producto, subtotal, descuento, iva, total_final)

if __name__ == "__main__":
    main()
 main
