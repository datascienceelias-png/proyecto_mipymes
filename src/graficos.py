import matplotlib.pyplot as plt
from funciones import *

def proporcion_macronutrientes(
    proporcion=[75, 15, 10],
    macronutrientes=['Carbohidratos', 'Grasas', 'Proteínas']
   
):
    colores = ["#1F74B1", "#F38D30", "#CC243C"]
    explode = [0, 0, 0.1 ]

    plt.pie(proporcion, labels=macronutrientes, autopct='%1.1f%%', startangle = 60, explode=explode, colors=colores)
    plt.title('Proporción de Macronutrientes', fontsize=16, fontweight='bold')
    plt.legend()
    plt.show()

def barra_costo_promedio_nutr(products,precios_carb, precios_gras, precios_prot):

    cantidad_barras = len(products)
    grosor_barras = 0.30

    espacio_barra = list(range(cantidad_barras)) 


    x_carbohidrato = [x-grosor_barras for x in espacio_barra]
    x_grasa = [x for x in espacio_barra]
    x_proteina = [x+grosor_barras for x in espacio_barra]

    
    plt.figure(figsize=(30, 6))

    carb_valores = list(carbohidrato.values())  
    gras_valores = list(grasa.values())
    prot_valores = list(proteina.values())

    #Se crean 3 barras unidas para cada grupo de alimentos
    plt.bar(x_proteina, prot_valores, width=grosor_barras, color = "#CC243C", label = "Proteina" )
    plt.bar(x_carbohidrato, carb_valores, width=grosor_barras, color='#1F74B1', label='Carbohidratos')
    plt.bar(x_grasa, gras_valores, width=grosor_barras, color = "#F38D30", label = "Grasa")

    #Etiquetas:
    plt.ylabel("Precio promedio(g/$)", fontweight='bold', fontsize=16)
    plt.xlabel("Productos", fontweight='bold', fontsize=16)
    plt.xticks(espacio_barra, productos, rotation=25, ha='right') #Posición de las etiquetas en el eje x
    plt.title("Costo promedio de macronutrientes por producto", fontweight='bold', fontsize=16)
    #plt.yscale('log') #Escala logarítmica para mejor visualización porque hay mucha diferencia entre los costos de las grasas y los de los carbohidratos/proteínas

    plt.legend()

    plt.show()

products = list(proteina.keys())

#barra_costo_promedio_nutr(productos, precios_carb, precios_gras, precios_prot)

# def grafico_stacked_bar(productos, precios_carb, precios_gras, precios_prot):
# # Data
#     grupos = productos
#     values1 = list(precios_prot.values())
#     values2 = list(precios_gras.values())
#     values3 = list(precios_carb.values())

#     fig, ax = plt.subplots()

#     # Stacked bar chart
#     ax.bar(grupos, values1)
#     ax.bar(grupos, values2, bottom = values1 )
#     ax.bar(grupos, values3, bottom = values2 and bottom values3)

#     plt.show() 
# grafico_stacked_bar(listado_de_productos, proteina, grasa, carbohidrato)
import matplotlib.pyplot as plt

def sumar_listas(lista1, lista2):
    # Suma elemento a elemento: [a1+b1, a2+b2, ...]
    return [lista1[i] + lista2[i] for i in range(len(lista1))]

def grafico_stacked_bar(productos, precios_carb, precios_gras, precios_prot):
    grupos = productos
    values1 = list(precios_prot.values())   # proteína
    values2 = list(precios_gras.values())   # grasa
    values3 = list(precios_carb.values())   # carbohidrato

    # asegurar mismas longitudes
    assert len(grupos) == len(values1) == len(values2) == len(values3)

    fig, ax = plt.subplots()

    ax.bar(grupos, values1, label="Proteínas")
    ax.bar(grupos, values2, bottom=values1, label="Grasas")
    ax.bar(grupos, values3, bottom=sumar_listas(values1, values2), label="Carbohidratos")

    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# AQUÍ debes llamar a la función, no imprimirla
grafico_stacked_bar(listado_de_productos, carbohidrato, grasa, proteina)



    


   




 
