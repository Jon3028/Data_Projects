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
- [Ecositema_Haddop](#Ecositema_Haddop)
- [Map_Reduce](#Map_Reduce)
- [Hadoop_Map_reduce_demo](#Hadoop_Map_reduce_demo)
- [Spark_Cluster](#Spark_Cluster)
- [Spark_casos_uso](#Spark_casos_uso)
- [Resumen](#Resumen)

## ¿Qué es Big Data?
<div align="center"> 
  <img src="https://datasciencedegree.wisconsin.edu/wp-content/uploads/2015/05/4-Vs-of-big-data-1024x629.jpg" width="%">
</div>

Una interpretación popular de big data se refiere a conjuntos de datos extremadamente grandes. Un informe del Instituto Nacional de Estándares y Tecnología definió los grandes datos como "conjuntos de datos extensos, principalmente en las características de volumen, velocidad y/o variabilidad, que requieren una arquitectura escalable para un almacenamiento, manipulación y análisis eficientes". Algunos han definido big data como una cantidad de datos que supera un petabyte, un millón de gigabytes.

<h3>Numeros que todos deben conocer</h3>
<div align="center">
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

##  Hardware CPU
El CPU de hardware siver para calcular matematicamente cuanta memoria necesitara el procesamiento de la informacion
<br></br>
$$ {(600 tweets/second)x(200 bytes/tweets)= 1.2 Million bytes/second} $$

##  Hardware Memoria

Eficente, Costosa y Efimera

Se tienen dos problemas con la memoria

- 1.- Volatilidad: cuando se apaga el servicio de nuestras maquinas es comun que pedamos informacion
- 2.- Costosa : Es muy costoso tener mucha memoria.

Muchas compañias gastaban mucha plata por esta memoria,sin embargo como estrategia de multiples empresas de cloud como google, es que distribuyeros esta caga con Hardware "volatil".

Al conectar este grupo de computadoras en un sustema distribuido, le dieron el termino a cada unas las maquinas como un NODO, estos arreglos realizados por Google fue parte de la idea para el desarrollo de Spark

<div align="center"> 
  <img src="https://hpe-developer-portal.s3.amazonaws.com/uploads/media/2020/6/image6-1593757021829.png" width="%">
</div>

##  Hardware Almacenamiento

Cuando se usan discos magneticos o tipo SSD, puede ser una opcion mas economica pero que tiene un gran peso en la perdida de velocidad, ya que la informacion tarda mucho mas en procesarse.

Por ejemplo, procesar 1 hora de tweets (4.3 G) nos llevaria aprox.

<table class="default">
  <tr>
    <td>Memoria</td>
    <td>SSD</td>
    <td>Disco Magnetico</td>
  </tr>
  <tr>
    <td>30 ms</td>
    <td>0.5s</td>
    <td>4s</td>
  </tr>
</table>

Aparente no es mucho tiempo, pero cuando se tienen billones de operaciones a realizar, esto juega un papel importante. Es la razon del nacimiento de Spark, evitar este tipo de problemas.

##  Hardware de red

Aun cuando hemos tenido avances importantes en el desarrollo de hardware, continuamos con un bajo desarrollo en la velocidades de conexion que pueden tener algunos nodos o equipos, 

Debido a esto los sistemas distribuidos tratan de minimizar esto con un concepto llamado **Shufflin data back**, que no es mas que dividir la informacion entre los nodos del cluster y repartirla para que su procesamiento sea mas simple

##  Hardware Key Ratios

<table class="default">
  <tr>
    <td>CPU</td>
    <td>Memoria</td>
    <td>SSD</td>
    <td>Red</td>
  </tr>
  <tr>
    <td>200x mas rapido que una memoria</td>
    <td>15x mas rapido que un SSD</td>
    <td>20x mas rapido que una red</td>
    <td>Tu red dependera en que rancho vivas</td>
  </tr>
</table>

##  Datos pequeños
Cuando no tienes cantidades enormes para procesamiento es conveniente usar python para su procesamiento.

##  Datos enormes BIG
Spark fue diseñado para trabajar con clusters y nodos, esto con el proposito de distribuir la carga de trabajo, cuando tenemos que trabajar con grandes volumenes de datos, es conveniente usar Spark para estas tareas

## Datos promedio
Si tus datos son tan enormes como el tamañan de la memoria RAM de tu laptop, entonces puedes analizar esa informacion con una computadora simple, las librerias de Pandas pueden leer los datos completos del disco dentro de la memoria, si los datos a manipular son tan enormes como el tamaño de tu disco duro, entonces el programa no funcionara.

Un truco para para poder usar Python en grandes volumenes de datos, es particionar la informacion y dividirla.

#### Truco
Poniendo como ejemplo un archivo donde necesitamos separar los artistas de una base de datos, podriamos particionar el archivo en dos el primero de la A-M y el segundo de N-Z

nota: A un alto nivel, la computación distribuida implica varias CPU, cada una con su propia memoria. La computación paralela utiliza varias CPU que comparten la misma memoria.

## Hadoop Ecosystem


**Hadoop:** un ecosistema de herramientas para el almacenamiento de big data y el análisis de datos. Hadoop es un sistema más antiguo que Spark, pero muchas empresas todavía lo utilizan. La principal diferencia entre Spark y Hadoop es cómo usan la memoria. Hadoop escribe resultados intermedios en el disco, mientras que Spark intenta mantener los datos en la memoria siempre que sea posible. Esto hace que Spark sea más rápido para muchos casos de uso.

**Hadoop MapReduce:** un sistema para procesar y analizar grandes conjuntos de datos en paralelo.

**Hadoop YARN:** un administrador de recursos que programa trabajos en un clúster. El administrador realiza un seguimiento de los recursos informáticos disponibles y luego asigna esos recursos a tareas específicas.

Sistema de archivos distribuidos de Hadoop (HDFS): un sistema de almacenamiento de big data que divide los datos en fragmentos y los almacena en un grupo de computadoras.

A medida que Hadoop maduró, se desarrollaron otras herramientas para facilitar el trabajo con Hadoop. Estas herramientas incluyen:

Apache Pig: un lenguaje similar a SQL que se ejecuta sobre Hadoop MapReduce
Apache Hive: otra interfaz similar a SQL que se ejecuta sobre Hadoop MapReduce
A menudo, cuando alguien habla de Hadoop en términos generales, en realidad está hablando de Hadoop MapReduce. Sin embargo, Hadoop es más que solo MapReduce. En la siguiente parte de la lección, aprenderá más sobre cómo funciona MapReduce.

**¿Cómo se relaciona Spark con Hadoop?**
Spark, es otro marco de big data. Spark contiene bibliotecas para análisis de datos, aprendizaje automático, análisis de gráficos y transmisión de datos en vivo. Spark es generalmente más rápido que Hadoop. Esto se debe a que Hadoop escribe resultados intermedios en el disco, mientras que Spark intenta mantener los resultados intermedios en la memoria siempre que sea posible.

El ecosistema de Hadoop incluye un sistema de almacenamiento de archivos distribuido llamado HDFS (Sistema de archivos distribuido de Hadoop). Spark, por otro lado, no incluye un sistema de almacenamiento de archivos. Puede usar Spark además de HDFS, pero no es necesario. Spark también puede leer datos de otras fuentes, como Amazon S3.

**Transmisión de datos**
La transmisión de datos es un tema especializado en big data. El caso de uso es cuando desea almacenar y analizar datos en tiempo real, como publicaciones de Facebook o tweets de Twitter.

Spark tiene una biblioteca de transmisión llamada Spark Streaming, aunque no es tan popular ni rápida como otras bibliotecas de transmisión. Otras bibliotecas de transmisión populares incluyen Storm y Flink.
