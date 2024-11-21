#!/usr/bin/env python
# coding: utf-8

# # ¿Qué vende un coche?
# 
# En Crankshaft List, cientos de anuncios gratuitos de vehículos se publican en tu sitio web cada día. Necesitas estudiar los datos recopilados durante los últimos años y determinar qué factores influyen en el precio de un vehículo.

# ## Inicialización

# In[77]:


"""
Carga de librerías. 
Pandas nos permite utilizar funciones importantes para el análisis y procesamiento de datos.
"""

import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np


# ### Cargar datos

# [Carga los datos del proyecto y mira la información general.]

# In[78]:


"""
Carga del archivo de datos en un DataFrame
df1 es el DataFrame original
"""
df1 = pd.read_csv("https://code.s3.yandex.net/datasets/vehicles_us.csv")


# ### Explorar datos iniciales

# El dataset contiene los siguientes campos:
# - `price`
# - `model_year`
# - `model`
# - `condition`
# - `cylinders`
# - `fuel` — gasolina, diesel, etc.
# - `odometer` — el millaje del vehículo cuando el anuncio fue publicado
# - `transmission`
# - `paint_color`
# - `is_4wd` — si el vehículo tiene tracción a las 4 ruedas (tipo Booleano)
# - `date_posted` — la fecha en la que el anuncio fue publicado
# - `days_listed` — desde la publicación hasta que se elimina
# 
# [Al comprender los campos, explóralos para familiarizarte con los datos.]

# In[79]:


"""
Información general sobre el DataFrame.
Contiene:
13 columnas de datos
51,525 entradas
"""

df1.info()


# In[80]:


"""
Primer observación de los datos, familiarizandonos con la información contenida en el archivo.
"""

df1.head(10)


# ***Comentarios iniciales***
# 
# A raíz de lo observado en la vista general y en la primera impresión de datos, podemos observar lo siguiente:
# 
# 1. Valores ausentes en las columnas [moder_year, cylinders, odometer, paint_color, is_4wd]
# 2. Posible tipo de variable incorrecta en [model_year, cylinders, is_4wd, date_posted]
# 
# Estos puntos requieren mayor estudio.

# In[81]:


#Obteniendo el porcentaje de valores ausentes en los datos#
df1.isna().sum().sort_values(ascending = False) / len(df1)


# Previamente se describieron las columnas con valores ausentes.
# 
# Se presenta un listado con las columnas con mayor número de valores ausentes encabezada por is_4wd, paint_color y odometer.

# ### Conclusiones y siguientes pasos
# 
# Cabe la posibilidad de que, al ser una plataforma de venta, la información faltante pudiera ser desconocida por el publicante o pudiera no ser observada como crítica o de peso para la venta y se decidió omitir.
# 
# Comenzaremos por estudiar los valores ausentes, buscar una explicación del porqué estos datos no existen, si su inexistencia afecta a la distribución o a la relevancia de los datos, así como la posiblidad de eliminarlos.
# 
# En caso negativo, alternativas de reemplazo para estos datos ausentes.
# 
# Una vez hecho esto, se establecerá un tipo de variable que sea adecuado y congruente con el tipo de información contenida.

# ## Tratar los valores ausentes (si hay)

# ***Columna is_4wd***

# In[82]:


#Revisando la distribución de valores de la variable, se observa variable dicotómica
df1["is_4wd"].describe()


# In[83]:


#Paneo de los datos, vista general
print(df1["is_4wd"].head(10))
print()
df1["is_4wd"].tail(10)


# Se obseva que es una variable que tiene datos dicotómicos, es decir, sólo tiene dos valores. El valor 1 que indica que el modelo de vehículo ingresado si tiene tracción en las cuatro llantes, podemos llamarle ***True***, y ***NaN*** en caso contrario.
# 
# Una vez dicho esto, se decide cambiar el tipo de variable a booleana, cambiando los datos iguales a 1.0 por ***True***, y sustituyendo los datos ausentes por ***False***.

# In[84]:


"""
Se crea una nueva variable df2, esta contendra el DataFrame con variables cambiadas y con datos completos y enriquecidos.
"""

df2 = df1.copy()


# In[85]:


#Se ejecuta el rellenado de datos, si es ausente se cambia por False, si no es ausente se cambia por False
df2.loc[df2["is_4wd"].isna() == False, "is_4wd"] = True
df2.loc[df2["is_4wd"].isna() == True, "is_4wd"] = False
df2["is_4wd"]


# In[86]:


#Se confirma que en la variable is_4wd no hay valores ausentes
df2.info()


# ***Columna paint_color***

# In[87]:


#Paneo inicial de la variable, se observan valores ausentes
print(df2["paint_color"].head(10))
print()
df2["paint_color"].tail(10)


# In[88]:


#Revisión de la frecuencia con la que se observa cada respuesta en la variable
df2["paint_color"].value_counts()


# Confirmamos que no hay respuestas repetidas dentro de paint_color.
# 
# Ahora cambiaremos nuestros valores nulos por valores de color blanco ya que es el color con mayor representación en la muestra. Esta medida se pretende que sea menos agresiva contra los datos que eliminarlos ya que sería una porcentaje considerable de los datos que se eliminarían ***(17.99%)***.

# In[89]:


#Cambiando valores ausentes por "unknown"
df2.loc[df2["paint_color"].isna() == True, "paint_color"] = "unknown"
df2.head()


# In[90]:


"""
Se confirma que el cambio se ejecuto correctamente.
"""

df2["paint_color"].value_counts()


# In[91]:


#Se confirma que la variable paint_color no tiene valores ausentes
df2.info()


# ***Columna odometer***

# In[92]:


#Primer paneo de la variable odometer
print(df2["odometer"].head(10))
print()
df2["odometer"].tail(10)


# In[93]:


#Revisando la distribución de la variable
df2["odometer"].describe()


# Se cambiarán los datos ausentes con la mediana de los valores debido a que este cambio no afectará significativamente la distribución. 

# In[94]:


#Generando tabla dinámica para observar el millaje mediano por el tipo de condition del vehículo
table_odometer = df2.pivot_table(index='condition', values='odometer', aggfunc='median')
table_odometer


# In[95]:


#Codificando función que reemplaza el millaje ausente con respecto a la tabla dinámica antes mencionada
def replace_odometer(df):
    df.loc[(df["odometer"].isna() == True) & (df["condition"] == "excellent"), "odometer"] = table_odometer["odometer"][0]
    df.loc[(df["odometer"].isna() == True) & (df["condition"] == "fair"), "odometer"] = table_odometer["odometer"][1]
    df.loc[(df["odometer"].isna() == True) & (df["condition"] == "good"), "odometer"] = table_odometer["odometer"][2]
    df.loc[(df["odometer"].isna() == True) & (df["condition"] == "like new"), "odometer"] = table_odometer["odometer"][3]
    df.loc[(df["odometer"].isna() == True) & (df["condition"] == "new"), "odometer"] = table_odometer["odometer"][4]
    df.loc[(df["odometer"].isna() == True) & (df["condition"] == "salvage"), "odometer"] = table_odometer["odometer"][5]


# In[96]:


#Se ejecuta la función previamente codificada
replace_odometer(df2)
df2


# In[97]:


#Revisando la distribución de la variable odometer
df2["odometer"].describe()


# In[98]:


"""
Impresión de la información general del DataFrame para corroborar que la variable odometer ha sido modificada y no cuenta
con valores ausentes
"""
df2.info()


# ***Columna cylinders***

# In[99]:


#Impresión de la distribución de la variable cylinders
df2["cylinders"].describe()


# In[100]:


#Revisión de la frecuenca con que aparece cada respuesta en la varible
df2["cylinders"].value_counts()


# Se cambiarán los datos ausentes con la mediana de los valores debido a que este cambio no afectará significativamente la distribución. En específico la distribución de los cuartiles, mínimo y máximo.

# In[101]:


#Generación de tabla dinámica para obtener el tipo de cilindraje más común dependiendo el modelo del vehículo
table_cylinders = df2.pivot_table(index='model', values='cylinders', aggfunc=pd.Series.mode)
table_cylinders.columns = ["cylinders_def"]
table_cylinders


# In[102]:


#Reemplazando los valores ausentes por el valor más común dependiendo el modelo
df2 = df2.merge(table_cylinders, how = "left", on="model")
df2.loc[df2["cylinders"].isna(), "cylinders"] = df2.loc[df2["cylinders"].isna(), "cylinders_def"].copy()
df2 = df2.drop(columns = "cylinders_def")
df2.info()


# ***Columna model_year***

# In[103]:


#Primer paneo de la variable model_year
print(df2["model_year"].head(10))
print()
df2["model_year"].tail(10)


# In[104]:


#Impresión de la distribución de la variable model_year
df2["model_year"].describe()


# Para el caso del modelo de auto (model_year), es una variable tan importante y significativa para la determinación del precio de venta, por lo que se decide modificar el valor dependiendo del modelo y su valor más común.

# In[105]:


#Generando tabla dinámica para obtener el año más común dependiendo del modelo del vehículo
table_model_year = df2.pivot_table(index='model', values='model_year', aggfunc=pd.Series.mode)
table_model_year.columns = ["model_year_def"]
table_model_year


# In[106]:


"""
Existen algunas respuestas que el modelo más común esta empatado entre dos años, esto genera una respuesta en la tabla dinámica
tipo Serie, se elige tomar el modelo más antiguo para reemplazar estas variables, esto nos ayudará a tener un diagnóstico más
conservador del precio dependiendo del año del vehículo
"""
table_model_year["model_year_def"]["jeep grand cherokee laredo"] = 2006.0
table_model_year["model_year_def"]["kia sorento"] = 2011.0
table_model_year["model_year_def"]["nissan versa"] = 2012.0
table_model_year["model_year_def"]["subaru impreza"] = 2008.0
table_model_year = table_model_year.astype("int64")
table_model_year


# In[107]:


#Reemplazando los valores ausentes por el valor más común recibido en la tabla dinámica table_model_year
df2 = df2.merge(table_model_year, how = "left", on="model")
df2.loc[df2["model_year"].isna(), "model_year"] = df2.loc[df2["model_year"].isna(), "model_year_def"].copy()
df2 = df2.drop(columns = "model_year_def")
df2.info()


# ## Corregir los tipos de datos

# In[108]:


#Corrigiendo el tipo de datos por uno más congruente a los datos observados en la variable
df2["model_year"] = df2["model_year"].astype("int32")
df2["cylinders"] = df2["cylinders"].astype("int32")
df2["date_posted"] = pd.to_datetime(df2["date_posted"], format = "%Y-%m-%d")


# In[109]:


#Confirmando la modificación del tipo de datos
df2.info()


# ## Enriquecer datos

# In[110]:


"""
Se agregan las siguientes columnas:

year_posted : Año en que se publicó el anuncio
month_posted : Mes en que se publicó el anuncio
weekday_posted : Día de la semana en que se publicó el anuncio
vehicule_age : Edad del vehículo
"""

df2["year_posted"] = pd.DatetimeIndex(df2["date_posted"]).year
df2["month_posted"] = pd.DatetimeIndex(df2["date_posted"]).month
df2["weekday_posted"] = df2["date_posted"].dt.weekday
df2["vehicule_age"] = df2["year_posted"] - df2["model_year"]
df2.head()


# In[111]:


"""
Se agrega la columna odometer_mean, la cual tiene el propósito de mostrar el uso promedio (millaje) del vehículo por 
cada año de vida
"""

df2["odometer_mean"] = df2["odometer"].copy()#creando columna odometer_mean con valores de odometer
df2.loc[df2["model_year"] != df2["year_posted"], "odometer_mean"] = df2["odometer"] / df2["vehicule_age"]
#cambiando los valores donde no se hace infinito por el promedio. Donde daba infinito, ya se arreglo el problema con la primera línea
df2.sort_values(by = "odometer_mean", ascending = False).head()


# De acuerdo a lo acontecido en el dataframe inicial estudiado en los primeros pasos, en la fase de inicialización, observamos que al tratarse de una plataforma de apoyo al área de ventas, la información faltante en cuanto a datos ausentes  puede deberse a desconocimiento de parte del publicante, alguna estrategía relacionada a la venta que lo llevará a ocultar ciertos datos que fueran importantes durante la negociación o pudiese ser observada como no crítica para el proceso de la venta y el publicante la decidió omitir.
# 
# Tenemos varias variables con datos ausentes como son is_4wd, paint_color, odometer, cylinders y model_year.
# 
# Para la columna is_4wd, se decidió hacer cambiar los valores por los valores booleanos True o False, esta decisión se tomó por la naturaleza dicotómica de los datos, esta naturaleza nos permite trabajar de manera más sencilla con los valores booleanos antes mencionados.
# 
# En la columna paint_color, se requiere un tratamiento diferente, como no podemos eliminar los datos ya que son demasiados y esta variable puede ser importante para el estudio del precio, se decide cambiar los valores ausentes por "unknown", esto con el propósito de poder estudiar a futuro, si se requiere, el impacto de esta variable desconocida vs el precio.
# 
# Las variables odometer, cylinders y model_year, requirieron modificar su valor ya que teníamos tanto valores ausentes como valores atipicos, por lo que primero se hizo una categorización basada en los valores y se cambio el valores dependiendo el modelo, el año o la condición, según sea el caso, y cambió ya sea por la media aritmética, la moda o la mediana.

# In[112]:


# Revisando la distribución de respuestas de la variable condition
df2["condition"].value_counts()


# In[113]:


"""
Reemplazando la variable condition por valores númericos a través de una función, esto hará más sencillo el análisis.

Nueva clasificación
new        -> 5
like new   -> 4
excellent  -> 3
good       -> 2
fair       -> 1
salvage    -> 0
"""

df2.loc[df2["condition"] == "new","condition"] = 5
df2.loc[df2["condition"] == "like new","condition"] = 4
df2.loc[df2["condition"] == "excellent","condition"] = 3
df2.loc[df2["condition"] == "good","condition"] = 2
df2.loc[df2["condition"] == "fair","condition"] = 1
df2.loc[df2["condition"] == "salvage","condition"] = 0

df2["condition"].value_counts()


# In[114]:


#Modificando el tipo de datos por uno más congruente con los datos modificados
df2["condition"] = df2["condition"].astype(int)
df2.info()


# ## Comprobar datos limpios

# In[115]:


# Se imprime la información general sobre el DataFrame

df2.info()


# In[116]:


# Paneo de una muestra de los datos

df2.head(5)


# ## Estudiar parámetros principales
# 
# Los parámetros son:
# - Precio
# - Los años del vehículo cuando el anuncio se colocó
# - Millaje
# - Número de cilindros
# - Estado

# In[117]:


#Generando función para la creación de histogramas para la revisión de parámetros principales
def graphics(serie, cajas = 50, tamano = (20, 10)):
    print(serie.describe())
    return serie.hist(bins = cajas, 
                      legend = True,
                      figsize = tamano
                     )


# In[118]:


#Histograma de la variable price
graphics(df2["price"], 50)


# Con lo observado en el histograma anterior, podemos inferir que ***hay datos atípicos*** en la variable, ya que nos alarga hasta 350,000 los valores. Esto requiere un estudio posterior, aunque cabe la posibilidad que no sean datos atípicos, si no que tengamos una gran dispersión de los precios debido a los segmentos encontrados en el DataFrame.

# In[119]:


#
graphics(df2["vehicule_age"], 50)


# Con lo observado en el histograma anterior, podemos inferir que ***hay datos atípicos*** en la variable, ya que nos alarga hasta 100 los valores. Esto requiere un estudio posterior. Parece díficil que haya vehículos con 100 años de antigüedad.

# In[120]:


#
graphics(df2["odometer"], 30)


# Con lo observado en el histograma anterior, podemos inferir que ***hay datos atípicos*** en la variable, ya que nos alarga hasta 1,000,000 los valores. Esto requiere un estudio posterior. No parece lógico que tengamos vehículos con un millón de millas.

# In[121]:


#
graphics(df2["cylinders"], [1,3,5,7,9,11,13])


# Con lo observado en el histograma anterior, podemos inferir que ***no hay datos atípicos*** en la variable, tenemos frecuencias relacionadas a datos normales del cilindraje de lso vehículos.

# In[122]:


#
graphics(df2["condition"], 5)


# Con lo observado en el histograma anterior, podemos inferir que ***no hay datos atípicos*** en la variable, tenemos frecuencias relacionadas a datos normales del tipo de condición, en este caso, la mayoría de los autos tienen como condición fair, good o excellent, esto es lógico dado que es una página de vehículos seminuevos.

# ## Estudiar y tratar valores atípicos
# 
# [Con los resultados anteriores, determina qué columnas pueden contener valores atípicos y crea un DataFrame sin esos valores atípicos. Pista: los valores atípicos se pueden identificar tras definir el límite inferior/superior para el rango normal de valores.]

# In[123]:


# Determinación los límites inferiores para valores atípicos para la variable odometer

print(df2["odometer"].describe())
df2["odometer"].plot(kind = "box", title = "Boxplot by Odometer", figsize = (4, 6))
plt.show()
odometer_iqr = df2["odometer"].quantile(0.75) - df2["odometer"].quantile(0.25)
odometer_lower_limit = df2[df2["odometer"] < (df2["odometer"].quantile(0.25) - 1.5 * odometer_iqr)]
odometer_lower_limit


# In[124]:


# Determinación los límites inferiores para valores atípicos para la variable vehicule_age

print(df2["vehicule_age"].describe())
df2["vehicule_age"].plot(kind = "box", title = "Boxplot by vehicule_age", figsize = (4, 6))
plt.show()
vehicule_age_iqr = df2["vehicule_age"].quantile(0.75) - df2["vehicule_age"].quantile(0.25)
vehicule_age_lower_limit = df2[df2["vehicule_age"] < (df2["vehicule_age"].quantile(0.25) - 1.5 * vehicule_age_iqr)]
vehicule_age_lower_limit


# In[125]:


# Determinación los límites inferiores para valores atípicos para la variable price

print(df2["price"].describe())
df2["price"].plot(kind = "box", title = "Boxplot by price", figsize = (4, 6))
plt.show()
price_iqr = df2["price"].quantile(0.75) - df2["price"].quantile(0.25)
price_lower_limit = df2[df2["price"] < (df2["price"].quantile(0.25) - 1.5 * price_iqr)]
price_lower_limit


# In[126]:


# Determinación los límites superiores para valores atípicos para la variable odometer
odometer_upper_limit = df2[df2["odometer"] > (df2["odometer"].quantile(0.75) + 1.5 * odometer_iqr)]
odometer_upper_limit


# In[127]:


# Determinación los límites superiores para valores atípicos para la variable vehicule_age
vehicule_age_upper_limit = df2[df2["vehicule_age"] > (df2["vehicule_age"].quantile(0.75) + 1.5 * vehicule_age_iqr)]
vehicule_age_upper_limit


# In[128]:


# Determinación los límites superiores para valores atípicos para la variable price
price_upper_limit = df2[df2["price"] > (df2["price"].quantile(0.75) + 1.5 * price_iqr)]
price_upper_limit


# In[129]:


"""
Se almacena los datos sin valores atípicos en un DataFrame separado con el objetivo a posterior de poder hacer 
comparaciones entre DataFrames, en  caso de ser necesario.
"""

df3 = df2[(df2["odometer"] > df2["odometer"].quantile(0.25) - 1.5 * odometer_iqr) & 
         (df2["odometer"] < df2["odometer"].quantile(0.75) + 1.5 * odometer_iqr)]
df3 = df3[(df3["vehicule_age"] > df3["vehicule_age"].quantile(0.25) - 1.5 * vehicule_age_iqr) & 
         (df3["vehicule_age"] < df3["vehicule_age"].quantile(0.75) + 1.5 * vehicule_age_iqr)]
df3 = df3[(df3["price"] > df3["price"].quantile(0.25) - 1.5 * price_iqr) & 
         (df3["price"] < df3["price"].quantile(0.75) + 1.5 * price_iqr)]
df3


# ## Estudiar parámetros principales sin valores atípicos

# In[130]:


graphics(df2["odometer"], 50)


# In[131]:


graphics(df3["odometer"], 50)


# ***Comentarios sobre la variable odometer***
# 
# Se puede observar que se eliminaron los valores atipicos, nuestros valores en el DataFrame filtrado sin valores atípicos están más concentrados dentro de valores lógicos con valor máximo de 256K, muy diferente de los 990K que representaban los valores atípicos.
# 
# La forma del gráfico es similar en cuanto a distribución central pero al eliminar los valores atípicos tenemos una distribución más lógica y valores reales de media y mediana.

# In[132]:


graphics(df2["vehicule_age"], 50)


# In[133]:


graphics(df3["vehicule_age"], 50)


# ***Comentarios sobre la variable vehicule_age***
# 
# Se puede observar que se eliminaron los valores atipicos, nuestros valores en el DataFrame filtrado sin valores atípicos están más concentrados dentro de valores lógicos con valor máximo de 23, muy diferente de los 110 que representaban los valores atípicos. Esto suena mucho más lógico, ya que en caso contrario, tendríamos vehículos intentando ser vendidos con año de fabricación en la decada de 1910.
# 
# La forma del gráfico es similar en cuanto a distribución central pero al eliminar los valores atípicos tenemos una distribución más lógica y valores reales de media y mediana.

# In[134]:


graphics(df2["price"], 100)


# In[135]:


graphics(df3["price"], 100)


# ***Comentarios sobre la variable price***
# 
# Se puede observar que se eliminaron los valores atipicos, nuestros valores en el DataFrame filtrado sin valores atípicos están más concentrados dentro de valores lógicos con valor máximo de 347K, este resultado no es muy diferente de los 375K que representaba el valor máximo observado sin los valores atípicos. Esta variable si puede explicar este comportamiento, ya que tenemos vehículos de muchas gamas, con rangos de precios diferentes.
# 
# La forma del gráfico es similar en cuanto a distribución central pero al eliminar los valores atípicos tenemos una distribución más lógica y valores reales de media y mediana.

# ## Periodo de colocación de los anuncios

# In[136]:


#Obteniendo la distribución de la variable days_listed

print(df3["days_listed"].describe())
print()

#Calculando periodo de colocación más habitual, periodo mediano y periodo medio

print(f'Periodo de colocación más habitual: {df3["days_listed"].mode()}')
print(f'Mediana de días anunciados: {df3["days_listed"].median()}')
print(f'Media de días anunciados: {df3["days_listed"].mean()}')


# In[137]:


#Graficando días anuncios que salieron demasiado rápido y anuncios anormalmente largos

df3["days_listed"].plot(kind = "box", title = "Boxplot by Odometer", figsize = (4, 6))
plt.show()

#Obteniendo los anuncios que salieron demasiado rápido

days_listed_iqr = df3["days_listed"].quantile(0.75) - df3["days_listed"].quantile(0.25)
days_listed_lower_limit = df3[df3["days_listed"] < (df3["days_listed"].quantile(0.25) - 1.5 * days_listed_iqr)]
print(days_listed_lower_limit)


# In[138]:


#Obteniendo los anuncios que fueron anormalmente largos

days_listed_upper_limit = df3[df3["days_listed"] > (df3["days_listed"].quantile(0.75) + 1.5 * days_listed_iqr)]
print(f'Cantidad de anuncios que fueron anormalmente largos: {len(odometer_upper_limit)}')
print(f'Relación anuncios que fueron anormalmente largos: {len(odometer_upper_limit) / len(df3["days_listed"])}')


# In[139]:


#Generando histograma variable days_listed

graphics(df3["days_listed"], 100) 


# ***Comentarios sobre la variable days_listed***
# 
# Podemos observar que tenemos muchos valores anormalmente largos, esto con la simple observación del diagrama de bigote y cajas. Estos días anormalmente largos están causando una desviación importante en las medidas de tendencia central como es la mediana y la media, que están muy separadas de la moda (18). 
# 
# En cuanto a la cantidad de días anormalmente largos, observamos que se presentan 923 anuncios (***1.92%***) del total de anuncios registrados.
# 
# El estudio del histograma nos da evidencia de como se distribuyen los datos, al tener esta cola del diagrama anormalmente larga y con tanta separación entre el valor máximo 271, el valor más común, le media y la mediana.

# ## Precio promedio por cada tipo de vehículo

# In[140]:


#Generando tabla dinámica que muestre el precio promedio y la cantidad de anuncios por cada tipo de vehículos
pt_model = df3.pivot_table(index = ["type"], 
                values = "price", 
                aggfunc = ["count", "mean"], 
                ).sort_values(by = [('count', 'price')], ascending = False)
pt_model.columns = ["count_price","mean_price"]
pt_model = pt_model.sort_values(by="count_price", ascending=False)
pt_model


# In[141]:


#Graficando tabla dinámica anterior
pt_model.plot(title = "Número de anuncios vs Precio", 
              y = "count_price", 
              style = "o-",
              grid = True, 
              figsize = (18, 6)
             )


# ***Comentarios sobre la relación entre el precio y la cantidad de anuncios vs el tipo de vehículo***
# 
# Los dos tipos más anunciados de vehículos son sedan y SUV, con marcadas diferencias vs el resto de vehículos. Se tomarán estos datos para los cálculos de la siguiente sección.

# ## Factores de precio

# In[142]:


#Paneo del DataFrame

df3.head()


# In[143]:


#Generando dos DataFrames, uno con vehículos sedan y otro con vehículos SUV
df3_sedan = df3[df3["type"] == "sedan"]
df3_suv = df3[df3["type"] == "SUV"]


# In[144]:


#Fitlrando por color para observar cuantos anuncios hay de cada color en el DataFrame de sedan y de suv.
print(df3_sedan["paint_color"].value_counts())
print()
df3_suv["paint_color"].value_counts()


# In[145]:


#Eliminano del DataFrame valores desconocidos, custom y todos aquellos sin un mínimo de 50 anuncios para el DataFrame de sedan
df3_sedan_paint_color = df3_sedan[(df3_sedan["paint_color"] != "purple") & 
                                  (df3_sedan["paint_color"] != "yellow") & 
                                  (df3_sedan["paint_color"] != "orange")
                     ]

#Eliminano del DataFrame valores desconocidos y todos aquellos sin un mínimo de 50 anuncios para el DataFrame de suv
df3_suv_paint_color = df3_suv[(df3_suv["paint_color"] != "purple") & 
                              (df3_suv["paint_color"] != "yellow")
                 ]


# In[146]:


#Genereando una función para la impresión del diagrama de caja y bigotes
def graphic_box(df, serie1, serie2):
    df.boxplot(column = serie1, 
               by = serie2,
               figsize = (16, 10),
               grid = True,
               rot = 90,
               fontsize = 10
              )
    plt.suptitle(f'Diagrama de caja {serie1} vs {serie2}')
    plt.show()
    
#Mostrando el diagrama de caja y bigotes del color por tipo de vehículo (sedan)
graphic_box(df3_sedan_paint_color, "price", "paint_color")


# In[147]:


#Mostrando el diagrama de caja y bigotes del color por tipo de vehículo (suv)
graphic_box(df3_suv_paint_color, "price", "paint_color")


# ***Comentarios acerca de la dependencia del precio vs paint_color***
# 
# De acuerdo a los modelos más anunciados (SUV y sedan), podemos observar que, en ambos casos, los colores que tienen un mayor efecto en el precio son el color blanco y rojo, y en general, el resto de colores se ordenan de forma similar, con mínimas diferencias en el precio medio.

# In[148]:


#Fitlrando por color para observar cuantos anuncios hay de cada color en el DataFrame de sedan y de suv.
print(df3_sedan["transmission"].value_counts())
print()
df3_suv["transmission"].value_counts()


# In[149]:


#Mostrando el diagrama de caja y bigotes del tipo de transmisión por tipo de vehículo (sedan)
graphic_box(df3_sedan, "price", "transmission")


# In[150]:


#Mostrando el diagrama de caja y bigotes del tipo de transmisión por tipo de vehículo (sedan)
graphic_box(df3_suv, "price", "transmission")


# ***Comentarios acerca de la dependencia del precio vs transmission***
# 
# De acuerdo a los modelos más anunciados (SUV y sedan), podemos observar diferencia entre los precios de venta más altos conseguidos, en el caso de las SUV, el precio promedio más alto es para transmisión manual y para sedan, transmisión automática.

# In[151]:


it_cols = ["vehicule_age", "odometer_mean", "condition"]

def graphic_scatter(df, yvar):
    for i in it_cols:
        df.plot(x = i, 
            y = yvar, 
            kind = "scatter",
            grid = True,
            alpha = 0.2,
            figsize = (16, 5)
        )
        print(f'Correlación de Pearson {i} vs {yvar} : {df[i].corr(df[yvar])}')

#Graficando para los vehículos del tipo sedan
graphic_scatter(df3_sedan, "price")


# In[152]:


#Graficando para los vehículos del tipo SUV
graphic_scatter(df3_suv, "price")


# ***Comentarios sobre gráficas y correlaciones price vs vehicule_age, price vs odometer_mean y price vs condition***
# 
# De las correlaciones, observamos una correlación positiva para las relaciones entre el precio y condition y el precio y odometer_mean para ambos tipos de carro (sedan y SUV). En cuanto al resultado de odometer_mean, es sorpresivo, no parece muy lógico que el precio del vehículo incremente a medida que tenemos mayor millaje promedio por año, pero la relación se asume debil por el valor observado en ambos tipos de carro.
# 
# En cuanto a la variable condition, en ambos tipos de vehículo (sedan y SUV), hace mucho sentido, ya que a mayor valores numérico de condition, el estado del vehículo es mejor. ***Es importante recordar que hicimos un cambio en el tipo de variable para una categorización más sencilla***, pero aunque los datos son numéricos, es una variable categórica.
# 
# En cuanto a la relación negativa observada con la variable vehicule_age, suena congruente que a mayor edad del vehículo, el precio sea menor y por el valor de la correlación de Pearson, se asume una relación medianamente fuerte, por lo que, de las tres variables antes estudiadas, es la que mayor influencia tendrá en el precio, esta conclusión se observa en ambos tipos de vehículo (sedan y SUV)

# ## Conclusión general

# Como en cualquier proyecto, la importancia del preprocesamiento de datos es fundamental, rememorando la frase ***"basura entra, basura sale"***, comenzamos el proyecto haciendo una exploración inicial de los datos, primero con un estudio acerca de los valores ausentes en la data del proyecto.
# 
# Observado esto, nos dimos cuenta que las variables is_4wd,paint_color, odometer, cylinders y model_year tenían dentro del DataFrame, datos ausentes que había que analizar como iba a ser su tratamiento.
# 
# ***Tratamiento de la variable is_4wd***
# 
# Observamos una característica dicotómica de la variable, así como que se observó que los valores ausentes eran congruentes con el valor 0, es decir, si había un 1 como respuesta, el vehículo tiene tracción en las cuatro ruedas, en caso contrario, encontrabamos un NaN, por lo que se decide reemplazar los valores de 1 con True y los valores de ausentes con False.
# 
# ***Tratamiento de la variable paint_color***
# 
# Esta variable tenía peculiaridades, similares a las que se observan en las variables odometer, cylinders y model_year, esto es que, por el tipo de datos encontrados, no era posible reemplazarlos por un valor arbitrario o conocer el comportamiento de los datos con un paneo sencillo o con la distribución. Por lo que, el reemplazo de los valores ausentes requirió de un estudio más profundo para no afectar el estudio del caso.
# 
# En el caso de la variable mencionada, se decidió cambiar todos los valores ausentes por "unknown", esto para que pudieran reflejarse en los cálculos y análisis posteriores sin modificar lo conocido.
# 
# ***Tratamiento de las variables odometer, cylinders y model_year***
# 
# Estas variables, al ser numéricas, se podía reemplazar sus valores ausentes tomando en cuenta valores o medidas de tendencia central de cada una de ellas, por lo que se decide que para odometer, cylinders y model_year, se modificaría por los valores de la mediana, moda y moda, respectivamente, todo dependiendo del modelo que cada dato ausente tuviera.
# 
# Una vez terminado el proceso de tratamiento de valores ausentes, revisamos que los datos importados del archivo origen csv y leídos por python, se hayan interpretado de forma congruente con los valores que contienen.
# 
# ***Corrección del tipo de datos***
# 
# Se observa que las variables model_year, cylinders y date_posted, no tenían tipos de datos correctos y se modificaron a nuevos tipos más afines a los datos que representan como son entero para las primeras dos y datetime para el tercero.
# 
# Terminada la correción de tipo de datos, se revisa y se hace un enriquecimiento del DataFrame, esto es, agregar columnas o información relativa al DataFrame o procesada del mismo que nos facilite o haga más profundo nuestro posterior análisis.
# 
# ***Enriquecimiento de datos***
# 
# Por lo que se decide agregar algunas columnas relacionadas a date_posted, como fueron el año, el mes y el día en que se publicó el anuncio. También se agrego la edad de cada vehículo que era una sustracción entre el año de fabricación y el año que se publicó el anuncio.
# 
# Teniendo esta nueva columna, se genera una columna que determinará el millaje medio de cada vehículo, haciendo una razón entre el millaje y la edad del vehículo.
# 
# Se hizo una reclasificación de los datos contenidos en la variable condition, esto era para hacer posible hacer operaciones, en caso de ser necesario, y para facilitar el diagramado de la variable.
# 
# ***Conclusiones generales***
# 
# Una vez estudiados y analizados también valores atípicos de las variables en los parámetros principales, observamos que los anuncios permanecen aproximadamente 39 días publicados previo a la venta, es un indicador de la eficiencia de nuestra propuesta de valor como sitio de venta, ***se deben generar condiciones y estrategías relacionadas a bajar este valor que es clave para el éxito y crecimiento de nuestra propuesta comercial y de producto***. Haciendo una investigación somera, el sitio iSeeCars, relacionado a EEUU, establece que el tiempo promedio de venta de un auto seminuevo es de 68.9 días en 2020, por lo que nuestra propuesta de valor como página puede ser evidente, pero no hay que dormirse en nuestros laureles.
# 
# ***Liga del dato***
# 
# https://www.univision.com/carros/ranking-de-carros/los-carros-que-mas-tiempo-tardan-en-venderse-en-estados-unidos-fotos
# 
# Ahora, tenemos algunos datos interesantes de nuestro estudio, observamos que los tipos de vehículos más vendidos son los de tipo sedan y SUV, y que los factores de precio más impactantes son, en orden descendendete, la edad del vehículo, el millaje promedio por año y la condition del vehículo, siendo la última de relación positiva y la primera de relación negativa. 
# 
# En cuanto a los colores, el blanco y el negro son los colores más vendidos en nuestro sitio, siendo el blanco el mayor con un 23.9% del parque vehícular, por lo que no es sorpresivo los datos encontrados.
# 
# ***Liga del dato***
# 
# https://siempreauto.com/cuales-son-los-colores-de-autos-mas-populares-en-los-estados-unidos/#:~:text=Aqu%C3%AD%20dejamos%20la%20lista%20de,23.9%20%25%20de%20todos%20los%20veh%C3%ADculos.&text=Los%20autos%20sin%20escala%20de,el%20azul%20en%20el%20sexto.
