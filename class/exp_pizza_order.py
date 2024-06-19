"""
Your job is to build an automatic pizza order program.
Based on a user's order, work out their final bill.
Small pizza (S): $15
Medium pizza (M): $20
Large pizza (L): $25
Add pepperoni for small pizza (Y or N): +$2
Add pepperoni for medium or large pizza (Y or N): +$3
Add extra cheese for any size pizza (Y or N): +$1
"""


def calcular_factura(tamaño, pepperoni, extra_queso):
    precio_base = 0

    # Precio base según el tamaño de la pizza
    if tamaño == 'S':
        precio_base = 15
    elif tamaño == 'M':
        precio_base = 20
    elif tamaño == 'L':
        precio_base = 25
    else:
        print("Tamaño de pizza no válido. Por favor elige S, M, o L.")
        return None

    # Costo de pepperoni
    if pepperoni == 'Y' or pepperoni == 'SÍ':
        if tamaño == 'S':
            precio_base += 2
        elif tamaño == 'M' or tamaño == 'L':
            precio_base += 3

    # Costo de queso extra
    if extra_queso == 'Y' or extra_queso == 'SÍ':
        precio_base += 1
    return precio_base

def main():
    print("Bienvenido al programa automático de pedido de pizza!")
    tamaño = input("Ingresa el tamaño de la pizza que deseas ordenar (S, M, L): ").strip().upper()
    pepperoni = input("¿Quieres agregar pepperoni? (SÍ o NO): ").strip().upper()
    extra_queso = input("¿Quieres agregar queso extra? (SÍ o NO): ").strip().upper()

    if pepperoni == 'SÍ':
        pepperoni = 'Y'
    if extra_queso == 'SÍ':
        extra_queso = 'Y'

    factura_total = calcular_factura(tamaño, pepperoni, extra_queso)

    if factura_total is not None:
        print(f"Tu factura total es de ${factura_total}. ¡Disfruta tu pizza!")


if __name__ == "__main__":
    main()

