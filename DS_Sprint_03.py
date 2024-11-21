#!/usr/bin/env python
# coding: utf-8

# # ¡Llena ese carrito!

# # Introducción
# 
# Instacart es una plataforma de entregas de comestibles donde la clientela puede registrar un pedido y hacer que se lo entreguen, similar a Uber Eats y Door Dash.
# El conjunto de datos que te hemos proporcionado tiene modificaciones del original. Redujimos el tamaño del conjunto para que tus cálculos se hicieran más rápido e introdujimos valores ausentes y duplicados. Tuvimos cuidado de conservar las distribuciones de los datos originales cuando hicimos los cambios.
# 
# Debes completar tres pasos. Para cada uno de ellos, escribe una breve introducción que refleje con claridad cómo pretendes resolver cada paso, y escribe párrafos explicatorios que justifiquen tus decisiones al tiempo que avanzas en tu solución.  También escribe una conclusión que resuma tus hallazgos y elecciones.
# 

# ## Diccionario de datos
# 
# Hay cinco tablas en el conjunto de datos, y tendrás que usarlas todas para hacer el preprocesamiento de datos y el análisis exploratorio de datos. A continuación se muestra un diccionario de datos que enumera las columnas de cada tabla y describe los datos que contienen.
# 
# - `instacart_orders.csv`: cada fila corresponde a un pedido en la aplicación Instacart.
#     - `'order_id'`: número de ID que identifica de manera única cada pedido.
#     - `'user_id'`: número de ID que identifica de manera única la cuenta de cada cliente.
#     - `'order_number'`: el número de veces que este cliente ha hecho un pedido.
#     - `'order_dow'`: día de la semana en que se hizo el pedido (0 si es domingo).
#     - `'order_hour_of_day'`: hora del día en que se hizo el pedido.
#     - `'days_since_prior_order'`: número de días transcurridos desde que este cliente hizo su pedido anterior.
# - `products.csv`: cada fila corresponde a un producto único que pueden comprar los clientes.
#     - `'product_id'`: número ID que identifica de manera única cada producto.
#     - `'product_name'`: nombre del producto.
#     - `'aisle_id'`: número ID que identifica de manera única cada categoría de pasillo de víveres.
#     - `'department_id'`: número ID que identifica de manera única cada departamento de víveres.
# - `order_products.csv`: cada fila corresponde a un artículo pedido en un pedido.
#     - `'order_id'`: número de ID que identifica de manera única cada pedido.
#     - `'product_id'`: número ID que identifica de manera única cada producto.
#     - `'add_to_cart_order'`: el orden secuencial en el que se añadió cada artículo en el carrito.
#     - `'reordered'`: 0 si el cliente nunca ha pedido este producto antes, 1 si lo ha pedido.
# - `aisles.csv`
#     - `'aisle_id'`: número ID que identifica de manera única cada categoría de pasillo de víveres.
#     - `'aisle'`: nombre del pasillo.
# - `departments.csv`
#     - `'department_id'`: número ID que identifica de manera única cada departamento de víveres.
#     - `'department'`: nombre del departamento.

# # Paso 1. Descripción de los datos
# 
# Lee los archivos de datos (`/datasets/instacart_orders.csv`, `/datasets/products.csv`, `/datasets/aisles.csv`, `/datasets/departments.csv` y `/datasets/order_products.csv`) con `pd.read_csv()` usando los parámetros adecuados para leer los datos correctamente. Verifica la información para cada DataFrame creado.
# 

# ## Plan de solución
# 
# Escribe aquí tu plan de solución para el Paso 1. Descripción de los datos.

# In[ ]:


# importar librerías


# In[ ]:


# leer conjuntos de datos en los DataFrames


# In[ ]:


# mostrar información del DataFrame


# In[ ]:


# mostrar información del DataFrame


# In[ ]:


# mostrar información del DataFrame


# In[ ]:


# mostrar información del DataFrame


# In[ ]:


# mostrar información del DataFrame


# ## Conclusiones
# 
# Escribe aquí tus conclusiones intermedias sobre el Paso 1. Descripción de los datos.
# 

# # Paso 2. Preprocesamiento de los datos
# 
# Preprocesa los datos de la siguiente manera:
# 
# - Verifica y corrige los tipos de datos (por ejemplo, asegúrate de que las columnas de ID sean números enteros).
# - Identifica y completa los valores ausentes.
# - Identifica y elimina los valores duplicados.
# 
# Asegúrate de explicar qué tipos de valores ausentes y duplicados encontraste, cómo los completaste o eliminaste y por qué usaste esos métodos. ¿Por qué crees que estos valores ausentes y duplicados pueden haber estado presentes en el conjunto de datos?

# ## Plan de solución
# 
# Escribe aquí tu plan para el Paso 2. Preprocesamiento de los datos.

# ## Encuentra y elimina los valores duplicados (y describe cómo tomaste tus decisiones).

# ### `instacart_orders` data frame

# In[ ]:


# Revisa si hay pedidos duplicados


# ¿Tienes líneas duplicadas? Si sí, ¿qué tienen en común?

# In[ ]:


# Basándote en tus hallazgos,
# Verifica todos los pedidos que se hicieron el miércoles a las 2:00 a.m.


# ¿Qué sugiere este resultado?

# In[ ]:


# Elimina los pedidos duplicados


# In[ ]:


# Vuelve a verificar si hay filas duplicadas


# In[ ]:


# Vuelve a verificar si hay IDs duplicados de pedidos


# Describe brevemente tus hallazgos y lo que hiciste con ellos

# ### `products` data frame

# In[ ]:


# Verifica si hay filas totalmente duplicadas


# In[ ]:


# Verifica si hay IDs duplicadas de productos


# In[ ]:


# Revisa si hay nombres duplicados de productos (convierte los nombres a letras mayúsculas para compararlos mejor)


# In[ ]:


# Revisa si hay nombres duplicados de productos no faltantes


# Describe brevemente tus hallazgos y lo que hiciste con ellos.

# ### `departments` data frame

# In[ ]:


# Revisa si hay filas totalmente duplicadas


# In[ ]:


# Revisa si hay IDs duplicadas de productos


# Describe brevemente tus hallazgos y lo que hiciste con ellos.

# ### `aisles` data frame

# In[ ]:


# Revisa si hay filas totalmente duplicadas


# In[ ]:


# Revisa si hay IDs duplicadas de productos


# Describe brevemente tus hallazgos y lo que hiciste con ellos.

# ### `order_products` data frame

# In[ ]:


# Revisa si hay filas totalmente duplicadas


# In[ ]:


# Vuelve a verificar si hay cualquier otro duplicado engañoso


# Describe brevemente tus hallazgos y lo que hiciste con ellos.

# ## Encuentra y elimina los valores ausentes
# 
# Al trabajar con valores duplicados, pudimos observar que también nos falta investigar valores ausentes:
# 
# * La columna `'product_name'` de la tabla products.
# * La columna `'days_since_prior_order'` de la tabla orders.
# * La columna `'add_to_cart_order'` de la tabla order_productos.

# ### `products` data frame

# In[ ]:


# Encuentra los valores ausentes en la columna 'product_name'


# Describe brevemente cuáles son tus hallazgos.

# In[ ]:


#  ¿Todos los nombres de productos ausentes están relacionados con el pasillo con ID 100?


# Describe brevemente cuáles son tus hallazgos.

# In[ ]:


# ¿Todos los nombres de productos ausentes están relacionados con el departamento con ID 21?


# Describe brevemente cuáles son tus hallazgos.

# In[ ]:


# Usa las tablas department y aisle para revisar los datos del pasillo con ID 100 y el departamento con ID 21.


# Describe brevemente cuáles son tus hallazgos.

# In[ ]:


# Completa los nombres de productos ausentes con 'Unknown'


# Describe brevemente tus hallazgos y lo que hiciste con ellos.

# ### `orders` data frame

# In[ ]:


# Encuentra los valores ausentes


# In[ ]:


# ¿Hay algún valor ausente que no sea el primer pedido del cliente?


# Describe brevemente tus hallazgos y lo que hiciste con ellos.

# ### `order_products` data frame

# In[ ]:


# Encuentra los valores ausentes


# In[ ]:


# ¿Cuáles son los valores mínimos y máximos en esta columna?


# Describe brevemente cuáles son tus hallazgos.

# In[ ]:


# Guarda todas las IDs de pedidos que tengan un valor ausente en 'add_to_cart_order'


# In[ ]:


# ¿Todos los pedidos con valores ausentes tienen más de 64 productos?
# Agrupa todos los pedidos con datos ausentes por su ID de pedido.
# Cuenta el número de 'product_id' en cada pedido y revisa el valor mínimo del conteo.


# Describe brevemente cuáles son tus hallazgos.

# In[ ]:


# Remplaza los valores ausentes en la columna 'add_to_cart? con 999 y convierte la columna al tipo entero.


# Describe brevemente tus hallazgos y lo que hiciste con ellos.

# ## Conclusiones
# 
# Escribe aquí tus conclusiones intermedias sobre el Paso 2. Preprocesamiento de los datos
# 

# # Paso 3. Análisis de los datos
# 
# Una vez los datos estén procesados y listos, haz el siguiente análisis:

# # [A] Fácil (deben completarse todos para aprobar)
# 
# 1. Verifica que los valores en las columnas `'order_hour_of_day'` y `'order_dow'` en la tabla orders sean razonables (es decir, `'order_hour_of_day'` oscile entre 0 y 23 y `'order_dow'` oscile entre 0 y 6).
# 2. Crea un gráfico que muestre el número de personas que hacen pedidos dependiendo de la hora del día.
# 3. Crea un gráfico que muestre qué día de la semana la gente hace sus compras.
# 4. Crea un gráfico que muestre el tiempo que la gente espera hasta hacer su siguiente pedido, y comenta sobre los valores mínimos y máximos.

# ### [A1] Verifica que los valores sean sensibles

# In[ ]:





# In[ ]:





# Escribe aquí tus conclusiones

# ### [A2] Para cada hora del día, ¿cuántas personas hacen órdenes?

# In[ ]:





# Escribe aquí tus conclusiones

# ### [A3] ¿Qué día de la semana compran víveres las personas?

# In[ ]:





# Escribe aquí tus conclusiones

# ### [A4] ¿Cuánto tiempo esperan las personas hasta hacer otro pedido? Comenta sobre los valores mínimos y máximos.

# In[ ]:





# Escribe aquí tus conclusiones

# # [B] Intermedio (deben completarse todos para aprobar)
# 
# 1. ¿Existe alguna diferencia entre las distribuciones `'order_hour_of_day'` de los miércoles y los sábados? Traza gráficos de barra de `'order_hour_of_day'` para ambos días en la misma figura y describe las diferencias que observes.
# 2. Grafica la distribución para el número de órdenes que hacen los clientes (es decir, cuántos clientes hicieron solo 1 pedido, cuántos hicieron 2, cuántos 3, y así sucesivamente...).
# 3. ¿Cuáles son los 20 principales productos que se piden con más frecuencia (muestra su identificación y nombre)?

# ### [B1] Diferencia entre miércoles y sábados para  `'order_hour_of_day'`. Traza gráficos de barra para los dos días y describe las diferencias que veas.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# Escribe aquí tus conclusiones

# ### [B2] ¿Cuál es la distribución para el número de pedidos por cliente?

# In[ ]:





# In[ ]:





# Escribe aquí tus conclusiones

# ### [B3] ¿Cuáles son los 20 productos más populares (muestra su ID y nombre)?

# In[ ]:





# In[ ]:





# In[ ]:





# Escribe aquí tus conclusiones

# # [C] Difícil (deben completarse todos para aprobar)
# 
# 1. ¿Cuántos artículos suelen comprar las personas en un pedido? ¿Cómo es la distribución?
# 2. ¿Cuáles son los 20 principales artículos que vuelven a pedirse con mayor frecuencia (muestra sus nombres e IDs de los productos)?
# 3. Para cada producto, ¿cuál es la tasa de repetición del pedido (número de repeticiones de pedido/total de pedidos?
# 4. Para cada cliente, ¿qué proporción de los productos que pidió ya los había pedido? Calcula la tasa de repetición de pedido para cada usuario en lugar de para cada producto.
# 5. ¿Cuáles son los 20 principales artículos que la gente pone primero en sus carritos (muestra las IDs de los productos, sus nombres, y el número de veces en que fueron el primer artículo en añadirse al carrito)?

# ### [C1] ¿Cuántos artículos compran normalmente las personas en un pedido? ¿Cómo es la distribución?

# In[ ]:





# In[ ]:





# In[ ]:





# Escribe aquí tus conclusiones

# ### [C2] ¿Cuáles son los 20 principales artículos que vuelven a pedirse con mayor frecuencia (muestra sus nombres e IDs de los productos)?

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# Escribe aquí tus conclusiones

# ### [C3] Para cada producto, ¿cuál es la proporción de las veces que se pide y que se vuelve a pedir?

# In[ ]:





# In[ ]:





# In[ ]:





# Escribe aquí tus conclusiones

# ### [C4] Para cada cliente, ¿qué proporción de sus productos ya los había pedido?

# In[ ]:





# In[ ]:





# Escribe aquí tus conclusiones

# ### [C5] ¿Cuáles son los 20 principales artículos que las personas ponen primero en sus carritos?

# In[ ]:





# In[ ]:





# In[ ]:





# Escribe aquí tus conclusiones

# ### Conclusion general del proyecto:

# In[ ]:




