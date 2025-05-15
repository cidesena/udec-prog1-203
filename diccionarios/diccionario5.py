#version GPT
vendedores = [
    {
        'nombre': 'Maria Lopez',
        'area': 'cosmeticos',
        'líder': 'Jose Perez',
        'productos': ['shampoo', 'jabón', 'bloqueador', 'crema dental', 'gel'],
        'precio': [20000, 10000, 25000, 12000, 30000]
    },
    {
        'nombre': 'Laura Castiblanco',
        'area': 'cosmeticos',
        'lider': 'Alejandra',
        'productos': ['Labial', 'rubor', 'polvos', 'base', 'iluminador'],
        'precio': [10000, 15000, 20000, 25000, 30000]
    },
    {
        'nombre': 'Laura Castiblanco',
        'area': 'Perecederos',
        'lider': 'Alejandra',
        'productos': ['uvas', 'manzanas', 'bananos', 'carne', 'pollo'],
        'precio': [8000, 1500, 2000, 25000, 11000]
    },
    {
        'nombre': 'Laura Castiblanco',
        'area': 'cosmeticos',
        'lider': 'Alejandra',
        'productos': ['pestañina', 'corrector', 'delineador', 'lapiz de labios', 'brochas'],
        'precio': [17000, 15000, 10000, 2500, 32000]
    },
    {
        'nombre': 'Laura Castiblanco',
        'area': 'no perecederos',
        'lider': 'Alejandra',
        'productos': ['miel', 'atun', 'sopas', 'maiz enlatado', 'cafe'],
        'precio': [5000, 9000, 6000, 2500, 10000]
    },
    {
        'nombre': 'Laura Castiblanco',
        'area': 'congelados',
        'lider': 'Alejandra',
        'productos': ['huevos', 'queso', 'hierbas', 'hongos', 'pescado'],
        'precio': [12000, 12000, 2000, 2500, 30000]
    },
    {
        'nombre': 'Jhonatan',
        'area': 'cosmeticos',
        'lider': 'Ducuara',
        'productos': ['sombras', 'esmalte', 'crema facial', 'serum', 'toallitas desmaquillantes'],
        'precio': [18000, 7000, 25000, 30000, 12000]
    },
    {
        'nombre': 'Jhonatan',
        'area': 'Perecederos',
        'lider': 'Ducuara',
        'productos': ['lechuga', 'tomate', 'pera', 'res', 'cerdo'],
        'precio': [3000, 3500, 2500, 27000, 21000]
    },
    {
        'nombre': 'Jhonatan',
        'area': 'cosmeticos',
        'lider': 'Ducuara',
        'productos': ['brillo labial', 'mascarilla facial', 'tinte de cejas', 'crema antiarrugas', 'kit de maquillaje'],
        'precio': [8500, 22000, 15000, 27000, 45000]
    },
    {
        'nombre': 'Jhonatan',
        'area': 'no perecederos',
        'lider': 'Ducuara',
        'productos': ['arroz', 'lentejas', 'harina', 'aceite', 'azúcar'],
        'precio': [5000, 4000, 3500, 12000, 4500]
    },
    {
        'nombre': 'Jhonatan',
        'area': 'congelados',
        'lider': 'Ducuara',
        'productos': ['nuggets', 'vegetales mixtos', 'helado', 'empanadas', 'filete de merluza'],
        'precio': [11000, 8000, 9500, 6000, 28000]
    }
]

# 1. Promedio de precios por vendedor
print("1. Promedio de precios por vendedor:")
promedios = {}
suma_precios = {}
conteo = {}

for vendedor in vendedores:
    nombre = vendedor["nombre"]
    if nombre not in suma_precios:
        suma_precios[nombre] = 0
        conteo[nombre] = 0
    for precio in vendedor["precio"]:
        suma_precios[nombre] += precio
        conteo[nombre] += 1

for nombre in suma_precios:
    promedio = suma_precios[nombre] / conteo[nombre]
    print(f"{nombre} → Promedio de precios: {promedio:.2f}")



# 1. Promedio de precios por vendedor
promedios = {}
suma_precios = {}
conteo = {}

for vendedor in vendedores:
    nombre = vendedor["nombre"]
    if nombre not in suma_precios:
        suma_precios[nombre] = 0
        conteo[nombre] = 0
    for precio in vendedor["precio"]:
        suma_precios[nombre] += precio
        conteo[nombre] += 1

for nombre in suma_precios:
    promedio = suma_precios[nombre] / conteo[nombre]
    print(f"{nombre} Promedio de precios: {promedio:.2f}")

#producto mas costoso
mayor_precio = 0
producto_mayor = ""
vendedor_mayor = ""

for vendedor in vendedores:
    for i in range(len(vendedor["productos"])):
        if vendedor["precio"][i] > mayor_precio:
            mayor_precio = vendedor["precio"][i]
            producto_mayor = vendedor["productos"][i]
            vendedor_mayor = vendedor["nombre"]

print(f"Producto más caro: '{producto_mayor}' vendido por {vendedor_mayor} a ${mayor_precio}")