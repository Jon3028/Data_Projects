<div align="center">
  <h1>Spark for big data</h1>
</div>

<div align="center"> 
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Apache_Spark_logo.svg/1200px-Apache_Spark_logo.svg.png" width="40%">
</div>
Headline: El resumen de este proyecto se ha obtenido del curso de SPARK de Udacity https://learn.udacity.com/courses/ud2002

# Introduccion

SPARK es una de las herramientas mas populares para el analisis de BIG DATA, sin embargo existen otro tipo de tecnologias como Hadoop que es una tecnologia un poco mas antigua, sin embargo sigue siendo usada por grandes empresas. Spark generalmente es mas rapido en comparacion con Hadoop lo que lo ha posicionado en estos ultimos años como la herramienta mas popular.

Existen algunas otras herramientas para la manipulacion de BIG DATA, cada una con sus propios casos de uso, por ejemplo tenemos Apache Cassadra y SQL queries como Presto, sin embargo Spark continua siendo la herramienta mas popular para el analisis de grandes cantidades de datos.

<h3>A continuacion algunos puntos del proposito del desarrollo de este proyecto</h3>
<div align="left">
  <h4>1.- ¿Que es BIG Data?</h4>
  <h4>2.- Revision del hardware detras de BIG DATA</h4>
  <h4>3.- Introduccion a los sistemas distribuidos</h4>
  <h4>4.- Una breve historia de Spark y Big Data</h4>
  <h4>5.- Casos comunes del uso de Spark</h4>
  <h4>6-. Otras tecnologias en el ecosistema del BIG Data</h4>
</div>

# Conceptos

- [¿Que_es_Big_Data?](#¿Que_es_Big_Data?)
- [Numeros_que_todos_deben_conocer](#Numeros)
- [Hardware_CPU](#Hardware_CPU)
- [Hardware_Memoria](#Hardware_Memory)
- [Hardware_Almacenamiento](#Hardware_Storage)
- [Hardware_Red](#Hardware_Network)
- [Hardware_Key_Ratios](#Hardware_Key_Ratios)
- [Datos_Pequeños](#Datos_Pequeños)
- [Datos_Enormes_BIG](#Datos_Enormes_BIG)
- [Datos_Promedio](#Datos_Promedio)
- [Datos_ditribuidos](#Datos_ditribuidos)
- [Ecositema_Haddop](#Ecositema_Haddop)
- [Map_Reduce](#Map_Reduce)
- [Hadoop_Map_reduce_demo](#Hadoop_Map_reduce_demo)
- [Spark_Cluster](#Spark_Cluster)
- [Spark_casos_uso](#Spark_casos_uso)
- [Resumen](#Resumen)

### ¿Qué es Big Data?
<div align="center"> 
  <img src="https://datasciencedegree.wisconsin.edu/wp-content/uploads/2015/05/4-Vs-of-big-data-1024x629.jpg" width="%">
</div>

Una interpretación popular de big data se refiere a conjuntos de datos extremadamente grandes. Un informe del Instituto Nacional de Estándares y Tecnología definió los grandes datos como "conjuntos de datos extensos, principalmente en las características de volumen, velocidad y/o variabilidad, que requieren una arquitectura escalable para un almacenamiento, manipulación y análisis eficientes". Algunos han definido big data como una cantidad de datos que supera un petabyte, un millón de gigabytes.

<h3>ANumeros_que_todos_deben_conocer</h3>
<div align="left">
  <h4>CPU = 04 nano segundos</h4>
  <h4>Memoria = 100 nano segundos</h4>
  <h4>Almacenamiento = 16 micras de segundo</h4>
  <h4>Red = 150 mili segundos</h4>
</div>


#### CPU (Unidad Central de Procesamiento)
La CPU es el "cerebro" de la computadora. Cada proceso en su computadora es eventualmente manejado por su CPU. Esto incluye cálculos y también instrucciones para los demás componentes del cálculo.

#### Memoria (RAM)
Cuando su programa se ejecuta, los datos se almacenan temporalmente en la memoria antes de enviarse a la CPU. La memoria es un almacenamiento efímero: cuando su computadora se apaga, los datos en la memoria se pierden.

#### Almacenamiento (SSD o disco magnético)
El almacenamiento se utiliza para mantener datos durante largos períodos de tiempo. Cuando se ejecuta un programa, la CPU indicará a la memoria que cargue temporalmente datos del almacenamiento a largo plazo.

#### Red (LAN o Internet)
La red es la puerta de entrada para cualquier cosa que necesite que no esté almacenada en su computadora. La red podría conectarse a otras computadoras en la misma habitación (una red de área local) o a una computadora en el otro lado del mundo, conectada a través de Internet.


