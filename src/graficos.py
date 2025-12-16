import matplotlib.pyplot as plt


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

def barra_costo_promedio_macro(productos,precios_carb, precios_gras, precios_prot):

    cantidad_barras = len(productos)
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

def barra_costo_promedio(productos, precio):
    plt.barh(productos,precio, color="#1F74B1")
    plt.title("Precio promedio de cada producto",fontweight='bold', fontsize=16)
    plt.xlabel("Productos",fontweight='bold', fontsize=12)
    plt.ylabel("Precio",fontweight='bold',  fontsize=12)
    
    plt.show()






    


   




 
