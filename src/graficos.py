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

def barra_costo_promedio_nutr(productos,precios_carb, precios_gras, precios_prot):

    cantidad_barras = len(productos)
    grosor_barras = 0.30

    espacio_barra = list(range(cantidad_barras)) 


    x_carbohidrato = [x-grosor_barras for x in espacio_barra]
    x_grasa = [x for x in espacio_barra]
    x_proteina = [x+grosor_barras for x in espacio_barra]

    
    plt.figure(figsize=(30, 6))

    carb_valores = [precios_carb[p] for p in productos]
    gras_valores = [precios_gras[p] for p in productos]
    prot_valores = [precios_prot[p] for p in productos]

    #Se crean 3 barras unidas para cada grupo de alimentos
    plt.bar(x_proteina, prot_valores, width=grosor_barras, color = "#CC243C", label = "Proteina" )
    plt.bar(x_carbohidrato, carb_valores, width=grosor_barras, color='#1F74B1', label='Carbohidratos')
    plt.bar(x_grasa, gras_valores, width=grosor_barras, color = "#F38D30", label = "Grasa")

    #Etiquetas:
    plt.ylabel("Precio promedio(g/$)", fontweight='bold', fontsize=16)
    plt.xlabel("Productos", fontweight='bold', fontsize=16)
    plt.xticks(espacio_barra, productos, rotation=25, ha='right') #Posición de las etiquetas en el eje x
    plt.title("Costo promedio de macronutrientes por producto", fontweight='bold', fontsize=16)
    plt.yscale('log') #Escala logarítmica para mejor visualización porque hay mucha diferencia entre los costos de las grasas y los de los carbohidratos/proteínas

    plt.legend()

    plt.show()

precios_prot = {'muslo de pollo': 5.14, 'pechuga de pollo': 13.52, 'huevo': 5, 'molleja de pollo': 6.5, 'lomo de cerdo': 15.98, 'atún': 30.88, 'pierna de cerdo': 11.5, 'solmillo de cerdo': 14.17, 'garbanzos': 7.33, 'frijoles negros': 6.56, 'frijoles colorados': 7.48, 'leche de vaca': 40.13, 'arroz': 10.88, 'codito': 6.44}
precios_gras = {'muslo de pollo': 12.85, 'pechuga de pollo': 103.62, 'huevo': 5.0, 'molleja de pollo': 58.5, 'lomo de cerdo': 87.88, 'atún': 38.9, 'pierna de cerdo': 17.64, 'solmillo de cerdo': 148.81, 'garbanzos': 33.61, 'frijoles negros': 144.22, 'frijoles colorados': 168.33, 'leche de vaca': 30.1, 'arroz': 38.1, 'codito': 48.33}
precios_carb = {'muslo de pollo': 0, 'pechuga de pollo': 0, 'huevo': 0, 'molleja de pollo': 0, 'lomo de cerdo': 0, 'atún': 0, 'pierna de cerdo': 0, 'solmillo de cerdo': 0, 'garbanzos': 2.64, 'frijoles negros': 2.44, 'frijoles colorados': 2.76, 'leche de vaca': 24.08, 'arroz': 1.14, 'codito': 1.26}
productos = list(precios_prot.keys())

barra_costo_promedio_nutr(productos, precios_carb, precios_gras, precios_prot)

    


   




 
