# Proyecto-Progra-2
# Proyecto-Progra-2: Análisis de Créditos y Datos Demográficos

## 👥 Integrantes del Grupo
Juan Sebastian Castro Castellanos
Juan Sebastian Pardo Quintero
- Andres Felipe Gomez Bejarano
Juan Esteban Gil 

---

## 📂 Explicación de la Estructura de los Datos
El dataset principal utilizado en este proyecto es `DATASET_proyecto_dic.xlsx`, el cual contiene información detallada sobre registros de solicitantes de crédito, abarcando variables demográficas, financieras y de vivienda. 

La estructura general se compone de:
* **Filas:** 1,000 registros (solicitudes evaluadas).
* **Columnas:** 9 variables principales que describen características numéricas y categóricas de los clientes.



## 📖 Diccionario de la Base de Datos

| Columna | Descripción (Info) | Tipo de Variable | Detalles |
| :--- | :--- | :--- | :--- |
| **Column1** | Representa la posición del registro de 1 a 1000 registros. | Numérica | - |
| **Age** | Representa la edad de cada solicitante en años, desde los 19 en adelante. | Numérica (Cuantitativa discreta) | Edad en años |
| **Sex** | Representa el género de las personas en male y female. | Categórica (Cualitativa nominal) | `male` y `female` (masculino y femenino) |
| **Job** | Representa el nivel laboral codificado de 0 a 3. | Categórica / Numérica (Cualitativa ordinal) | 0 = No residente ni cualificado<br>1 = Persona residente y no cualificada<br>2 = Trabajador cualificado<br>3 = Trabajador altamente cualificado |
| **Housing** | Situación de vivienda, indica la categoría de vivienda del solicitante. | Categórica (Cualitativa nominal) | `own` = vivienda propia<br>`rent` = renta<br>`free` = sin pago alquiler |
| **saving accounts** | Indica la categoría de ahorros del solicitante (con datos faltantes identificados). | Categórica (Cualitativa ordinal) | `little` = pocos ahorros<br>`moderate` = ahorros moderados<br>`quite rich` = ahorros relativamente altos<br>`rich` = ahorros altos |
| **Checking account** | Indica la categoría del saldo disponible en la cuenta corriente. | Categórica (Cualitativa ordinal) | `little` = saldo bajo<br>`moderate` = saldo moderado<br>`rich` = saldo alto |
| **Credit amount** | Indica la cantidad de dinero solicitada por el cliente. | Numérica (Cuantitativa continua) | No se especifica la moneda |
| **duration** | Duración del crédito en meses. | Numérica (Cuantitativa discreta) | Meses |
| **purpose** | Indica el propósito del crédito solicitado. | Categórica (Cualitativa nominal) | Diferentes categorías de préstamo |



