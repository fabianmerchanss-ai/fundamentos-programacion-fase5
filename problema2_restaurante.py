# Evaluación Final POA - Fase 5
# Estudiante: Fabián Leonardo Merchán Mesa
# Grupo: 213022_517
# Problema 2: Cálculo de promociones en el menú de un restaurante

def calcular_precio_final(categoria_producto, precio_base, categoria_objetivo, precio_umbral):
    # Evalúa si el producto pertenece a la categoría objetivo y supera el precio umbral
    if categoria_producto == categoria_objetivo and precio_base > precio_umbral:
        descuento = precio_base * 0.15
        precio_final = precio_base - descuento
    else:
        precio_final = precio_base
        
    return precio_final

def main():
    # Matriz del menú: [Nombre del producto, Categoría, Precio base]
    menu_restaurante = [
        ["Bandeja Paisa", "Platos Fuertes", 32000],
        ["Ajiaco Santafereño", "Platos Fuertes", 24000],
        ["Churrasco a la Parrilla", "Platos Fuertes", 38000],
        ["Limonada de Coco", "Bebidas", 11000],
        ["Jugo Natural en Agua", "Bebidas", 6500],
        ["Patacones con Hogao", "Entradas", 14000],
        ["Trucha al Ajillo", "Platos Fuertes", 35000]
    ]

    # Criterios establecidos para aplicar la promoción
    categoria_promo = "Platos Fuertes"
    umbral_precio = 30000

    print("=================================================================")
    print("       REPORTE DE PROMOCIONES DEL MENÚ - RESTAURANTE")
    print(f"Promoción activa: 15% de descuento en '{categoria_promo}' mayores a ${umbral_precio:,}")
    print("=================================================================\n")
    print(f"{'PRODUCTO':<28} | {'PRECIO BASE':<14} | {'PRECIO FINAL':<14}")
    print("-" * 65)

    # Ciclo repetitivo para recorrer cada fila de la matriz
    for producto in menu_restaurante:
        nombre = producto[0]
        categoria = producto[1]
        precio_base = producto[2]

        precio_con_descuento = calcular_precio_final(categoria, precio_base, categoria_promo, umbral_precio)

        print(f"{nombre:<28} | ${precio_base:<13,.0f} | ${precio_con_descuento:<13,.0f}")

    print("-" * 65)

if __name__ == "__main__":
    main()