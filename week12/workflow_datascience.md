1. Tema/Hipótesis 
2. Datos - ¿Existen suficientes datos? 
    2.1 Conseguir más datos
3. EDA: (creación de semilla)
    * Si se precisa crear baseline, pasar a \\7. haciendo los pasos básicos de EDA para que sea posible.

    3.0. Data Wrangling
    3.1. Visualizar los datos / comprender los datos
    Data Mining
    3.2. Limpiar datos: NaN, duplicados, eliminar columnas no relevantes,...
    3.3. Encoder/get_dummies
    3.4. Normalizar [-1, 1], Scalar media = 0, var = 1
    3.5. Outliers
    3.6. Añadir columnas (mediana, media, varianza, covarianza...) / generar rangos (pd.cut)
    3.7. Reducción de la dimensionalidad, PCA, T-sne (...)
    \\3.8. Eliminar columnas conileanes*
    3.9. Repetir proceso hasta diferentes versiones.
4. Creación del conjunto de entrenamiento y de test
5. Elegir el modelo y parámetros (GridSearch opcional)
6. Entrenar el modelo (X_train): 
    6.1 Entrenar con todos los datos sin cross validation
    6.2 Cross validation normal (warm_start=True)
    6.3 Cross validation poco a poco (partiendo en pequeños trozos)(warm_start)  
\\7. Creación del modelo baseline entrenado (este modelo es simplemente el modelo de partida para futuras comparaciones). Lo primero que habría que hacer a nivel teórico crear un baseline para tener una referencia. Nos tenemos que quedar con un score para poder comparar.
    7.1 Repetir 3,4,5,6 eligiendo un modelo mejor.
8. Sacar el score con el conjunto de test
    8.1 volver al punto 2/3 para intentar encontrar la mejor relación de los datos
9. Si nuestro score es correcto y tenemos la necesidad de probar nuestro modelo para el mayor conjunto de datos, sería conveniente probar nuestras modificaciones y algoritmo con diferentes semillas aleatorias para comprobar el rendimiento real de nuestro modelo.
10. Entrenar con todos los datos (X).
11. Guardamos el modelo
12. Usar el modelo en producción (desplegar el modelo)
13. Monitorizar el modelo