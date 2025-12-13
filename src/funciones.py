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
                    gramos = float(producto["quantity"])
                    price = float(producto["price"])

                    proteina_total = (proteina_por_100g[i] / 100.0) * gramos
                    if proteina_total > 0: # Evitar división por cero cuando no hay carbhidratos en algunos alimentos
                        costo_por_gramo = price / proteina_total
                        lista_costos.append(costo_por_gramo)

        
            output[nombre_nutri] = round(promedio(lista_costos), 4)

    return output
