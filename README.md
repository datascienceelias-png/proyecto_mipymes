# EL desafio del cubano: "Mantener una alimentacion saludable":
Se analizaron 17 productos en 30 Mypimes en 3 municipios de La Habana

En la base de datos del valor nutricioal, se tomaron los datos a partir de las etiquetas de los productos y tambien por la aplicacion [Fitia](https://fitia.app/es/). Estos valores presentan los macronutrientes de 100 gramos de cada producto en crudo excepto el huevo que se obtuvo de una unidad y la leche se covirtio de [litro a gramos](https://share.google/oaWMIUlMNlFlo1M0C): Ademas de que la leche em todas las mipymes se encuentran en un envase de caja de 1 litro
En el caso del atún, el producto es en lata y solo se considero el peso escurrido. 

Los datos de la evoluvión del precio del huvos desde enero del  2024 fueron obteneidos de la (ONEI)[https://www.onei.gob.cu/publicaciones-economico?field_categoria_de_temas_target_id=495&field_year_value=2025&title=], pero en el mes de diciembre obtuve el dato a partir de los precios de las mipymes y el promedio de la  función "precio_promedio_lb"

### Requisitos para una dieta saludable

En la sección adapté las proporciones de la OMS/FAO para el contexto cubano distrubuyendo dentro del rango más cantidad de carbohidratos que de grasas y proteina porque son los carbohidratos más baratos.

### Funciones
La función "precio_promedio_lb" tiene como objetivo calcular el precio promedio que una persona debe gastar en comprar 1 libra de cada producto. Pero el peso escurrido de las diferentes latas de atún de todas las mipymes nunca llega a 1 libra, por eso el análisis se basa en el precio promedio para comprar 1 lata. En el caso de la leche, todos los envases son en una caja que contiene 1 litro de leche aproximadamente de 1030g que son aproximadamente 2,27 libras (1034/453.592). Por tanto el resultado de la funcion de la leche es el promedio de costo de un envace de 1 litro de leche. El resultado del de huevo es el promedio del valor de una unidad.

