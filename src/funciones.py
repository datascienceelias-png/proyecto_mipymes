import json


def cargar_json(ruta_relativa):
    with open(ruta_relativa, "r" , encoding="utf-8") as archivo:
        dato = json.load(archivo)
    return dato
mipyme = cargar_json("Data/mypimes.json")
nutrientes = cargar_json("Data/valor_nutricional.json")


# Listado de productos 
lista = list(nutrientes.keys())
listado_de_productos = [producto.lower() for producto in lista]

# Listas con valores nutricionales por producto
proteinas_por_productos = []
grasas_por_productos = []
carbohidratos_por_productos = []

for producto in nutrientes:
    
    proteinas_por_productos.append(nutrientes[producto]["proteina"])
    grasas_por_productos.append(nutrientes[producto]["grasas"])       
    carbohidratos_por_productos.append(nutrientes[producto]["carbohidratos"]) 



def promedio(lista):
    """
    Calcula el promedio de una lista
    """
    suma = 0
    for i in lista:
        suma += i
    if len(lista) > 0:
        return suma / len(lista)
    return 0

def costo_promedio_nutr(data_mipyme, productos, proteina_por_100g):
    """
    Calcula el costo promedio de 1 g de proteína para cada producto,
    """
    output = {}

    for i, nombre_nutri in enumerate(productos):
        lista_costos = []

        for mipyme in data_mipyme["mypyme"]:
            for producto in mipyme["products"]:

                if producto["name"] == nombre_nutri:
                    gramos = float(producto["quantity"]) # Convertir en float, de lo contrario da error porque se lee como string
                    price = float(producto["price"])

                    proteina_total = (proteina_por_100g[i] / 100) * gramos
                    if proteina_total > 0: # Evitar división por cero cuando no hay carbohidratos en algunos alimentos
                        costo_por_gramo = price / proteina_total
                        lista_costos.append(costo_por_gramo)

        
            output[nombre_nutri] = round(promedio(lista_costos), 2)

    return output
proteina = costo_promedio_nutr(mipyme, listado_de_productos, proteinas_por_productos)
grasa = costo_promedio_nutr(mipyme, listado_de_productos, grasas_por_productos)
carbohidrato = costo_promedio_nutr(mipyme, listado_de_productos, carbohidratos_por_productos)

print(proteina)
print(grasa)
print(carbohidrato)

def ordenar_costos(dic_costos, descendente=False):
    """
    Ordena un diccionario {producto: costo} por el valor del costo.
    Devuelve una lista de tuplas (producto, costo) ordenada.
    """
    # Filtrar posibles valores None o 0 si no los quieres considerar
    items_validos = [(prod, costo) for prod, costo in dic_costos.items()
                     if costo is not None]

    return sorted(items_validos, key=lambda x: x[1], reverse=descendente)
#print(ordenar_costos(proteina))
# print(ordenar_costos(grasa))
# print(ordenar_costos(carbohidrato))


def calcular_macronutrientes(kcal):
    """
    Calcula la cantidad de macronutrientes en gramos según las calorías necesarias.
    """
    carbohidratos = (0.74 * kcal) / 4
    grasas = (0.15 * kcal) / 9
    proteinas = (0.10 * kcal) / 4

    return {
        "carbohidratos_g": round(carbohidratos, 2),
        "grasas_g": round(grasas, 2),
        "proteinas_g": round(proteinas, 2)
    }
 