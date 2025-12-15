import matplotlib.pyplot as plt

def proporcion_macronutrientes(
    proporcion=[75, 15, 10],
    macronutrientes=['Carbohidratos', 'Grasas', 'Proteínas']
   
):
    colores = ["#1F74B1", "#F38D30", "#CC243C"]
    explode = [0, 0, 0.1 ]

    plt.pie(proporcion, labels=macronutrientes, autopct='%1.1f%%', startangle = 360, explode=explode, colors=colores)
    plt.title('Proporción de Macronutrientes', fontsize=16, fontweight='bold')
    plt.legend()
    plt.show()