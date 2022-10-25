<div align="center">
  <h1>Spark for big data</h1>
</div>

<div align="center"> 
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Apache_Spark_logo.svg/1200px-Apache_Spark_logo.svg.png" width="40%">
</div>
Headline: El resumen de este proyecto se ha obtenido del curso de SPARK de la plataforma Udacity https://learn.udacity.com/courses/ud2002

# 01_Introduccion al poder de Spark

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

## Conceptos

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

<div align="center"> 
  <h3>Ecosistema Hadoop</h3>
  <img src="https://static.packt-cdn.com/products/9781788995092/graphics/assets/a64fec28-e2b2-42f0-96cf-098fe8385316.png" width="%">
</div>

### MapReduce

MapReduce es una técnica de programación para manipular grandes conjuntos de datos. "Hadoop MapReduce" es una implementación específica de esta técnica de programación.

La técnica funciona dividiendo primero un gran conjunto de datos y distribuyéndolos en un clúster. En el paso del mapa, cada dato se analiza y convierte en un par (clave, valor). Luego, estos pares clave-valor se barajan en el clúster para que todas las claves estén en la misma máquina. En el paso de reducción, los valores con las mismas claves se combinan entre sí.

Si bien Spark no implementa MapReduce, puede escribir programas Spark que se comporten de manera similar al paradigma map-reduce.

<div align="center"> 
  <h3>Diagrama Map Reduce</h3>
  <img src="https://www.guru99.com/images/Big_Data/061114_0930_Introductio1.png" width="%">
</div>

### MapReduce_practice
Revisar las practicas del repositorio

### Spark Cluster

Exiten distintas maneras de correr Spark, 


<table class="default">
  <tr>
    <td>Modo local</td>
    <td>Cluster Manager</td>
  </tr>
  <tr>
    <td>Para este caso, realmente no tenemos computacion distribuida, esta opcion es ideal para apender la sintaxys y prototipar proyectos pesonales</td>
    <td>La gestion de cluster es un proceso separado que momnitorea los recursos disponibles, asi mismo se asegura que todas las maquinas estan trbajando de manera adecuada</td>
  </tr>
</table>

Adicional existen de modos de clusters

<table class="default">
  <tr>
    <td>Standalone</td>
    <td>YARN</td>
    <td>Mesos</td>
  </tr>
  <tr>
    <td>Esta opcion es la instalacion local</td>
    <td>Yarn es necesario cuando estamos trabajando en un cluster con el equipo de trabajo</td>
    <td>Corre en cada nodo y provee aplicaciones (Hadoop,Yarn,Spark,Kafka) independientes a cada nodo</td>
  </tr>
</table>

### Casos de uso SPARK




<div align="left">
<h3>Aquí hay algunos recursos sobre diferentes casos de uso de Spark:</h3>
<ul style="list-style-type:square">
<li>Análisis de datos</li>
<li>Aprendizaje automático</li>
<li>Streaming</li>
<li>Analisis de datos</li>
</ul>
</div>

**No siempre necesitas Spark**
Spark está diseñado para grandes conjuntos de datos que no caben en una computadora. Pero no necesita Spark si está trabajando en conjuntos de datos más pequeños. En los casos de conjuntos de datos que pueden caber en su computadora local, existen muchas otras opciones que puede usar para manipular datos, tales como:

AWK: una herramienta de línea de comandos para manipular archivos de texto
R: un lenguaje de programación y un entorno de software para la computación estadística
Python PyData Stack, que incluye pandas, Matplotlib, NumPy y scikit-learn entre otras bibliotecas

A veces, aún puede usar pandas en una sola máquina local, incluso si su conjunto de datos es solo un poco más grande que la memoria. Los pandas pueden leer datos en fragmentos. Dependiendo de su caso de uso, puede filtrar los datos y escribir las partes relevantes en el disco.

Si los datos ya están almacenados en una base de datos relacional como MySQL o Postgres, puede aprovechar SQL para extraer, filtrar y agregar los datos. Si desea aprovechar pandas y SQL simultáneamente, puede usar bibliotecas como SQLAlchemy, que proporciona una capa de abstracción para manipular tablas SQL con expresiones generativas de Python.

La biblioteca de Python Machine Learning más utilizada es scikit-learn. Tiene una amplia gama de algoritmos para clasificación, regresión y agrupamiento, así como utilidades para el preprocesamiento de datos, el ajuste fino de los parámetros del modelo y la prueba de sus resultados. Sin embargo, si desea utilizar algoritmos más complejos, como el aprendizaje profundo, deberá buscar más. TensorFlow y PyTorch son paquetes actualmente populares.


**Limitaciones de Spark**
La latencia de Spark Streaming es de al menos 500 milisegundos, ya que opera en microlotes de registros, en lugar de procesar un registro a la vez. Las herramientas de transmisión nativas como Storm, Apex o Flink pueden reducir este valor de latencia y pueden ser más adecuadas para aplicaciones de baja latencia. Flink y Apex también se pueden usar para el cálculo por lotes, por lo que si ya los está usando para el procesamiento de transmisiones, no es necesario agregar Spark a su pila de tecnologías.

Otra limitación de Spark es su selección de algoritmos de aprendizaje automático. Actualmente, Spark solo admite algoritmos que escalan linealmente con el tamaño de los datos de entrada. En general, el aprendizaje profundo tampoco está disponible, aunque hay muchos proyectos que integran Spark con Tensorflow y otras herramientas de aprendizaje profundo.

**Hadoop contra Spark**
El ecosistema Hadoop es una tecnología un poco más antigua que el ecosistema Spark. En general, Hadoop MapReduce es más lento que Spark porque Hadoop escribe datos en el disco durante los pasos intermedios. Sin embargo, muchas grandes empresas, como Facebook y LinkedIn, comenzaron a usar Big Data temprano y construyeron su infraestructura en torno al ecosistema de Hadoop.

Si bien Spark es excelente para algoritmos iterativos, no hay mucho aumento de rendimiento en comparación con Hadoop MapReduce cuando se realiza un conteo simple. La migración del código heredado a Spark, especialmente en cientos de nodos que ya están en producción, podría no valer la pena por el pequeño aumento de rendimiento.

**Más allá de Spark para almacenar y procesar Big Data**
Tenga en cuenta que Spark no es un sistema de almacenamiento de datos y que hay varias herramientas además de Spark que se pueden usar para procesar y analizar grandes conjuntos de datos.

A veces tiene sentido usar el poder y la simplicidad de SQL en big data. Para estos casos se ha desarrollado una nueva clase de bases de datos, conocidas como NoSQL y NewSQL.

Por ejemplo, es posible que escuche acerca de los sistemas de almacenamiento de bases de datos más nuevos, como HBase o Cassandra. También hay motores SQL distribuidos como Impala y Presto. Muchas de estas tecnologías utilizan una sintaxis de consulta con la que probablemente ya esté familiarizado en función de sus experiencias con Python y SQL.

# 02_Data Wrangling con Spark

<div align="left">
<h3> Objetivos de aprendizaje</h3>
<ul style="list-style-type:square">
<li>Wrangling data con Spark</li>
<li>Programacion funcional</li>
<li>Lectura y escritura de informacion</li>
<li>Ambiente de Spark y APIs de Spark</li>
<li>RDD (Resilient Distributed Dataset) API</li>
</ul>
</div>

**Programacion funcional vs Programacion de procedimiento**

Actualmente existen distintos motores de programacion para trabajar con Spark, algunos de ellos son Scala, Java, R & Python, sin embargo para el proposito de este desarollo usaremos Python en las practicas **PySpark**

Python por su naturaleza tiene un ciclo de programacion de procedimeinto, lo que limita que se ejecute una funcion a la vez, sin emabrgo con Spark tenemos una programacion funcional, donde divide la informacion en distintos clusters y nodos y al termino de la ejecucion de la informacion la une y suma.

**Funciones limpias (Pure funtions)**

Cuando trabajamos con programación funcional buscamos hacer uso de las funciones puras.
Estas funciones son aquellas retornan un valor, el cual depende de los parámetros de entrada, y no se observan ningún efecto secundario.

Ejemplo de función pura

`def doble_de_la_suma(x,y):`

`return (x+y)/2`


Ejemplo de una función impura

`miLista = [0,1]`

`def funcion_impura(valor):`

`    miLista.append(valor)`

`funcion_impura(231)`

`print(miLista)`

Esta función anterior es considerada impura debido a que tiene un efecto secundario. Modifica la lista (miLista) como factor externo.

** DAGs en SPARK**

Apache Spark combina un sistema de computación distribuida a través de clusters de ordenadores con una manera sencilla y elegante de escribir programas. Fue creado en la Universidad de Berkeley en California y es considerado el primer software de código abierto que hace la programación distribuida realmente accesible a los científicos de datos.

Es sencillo entender Spark si lo comparamos con su predecesor, MapReduce, el cual revolucionó la manera de trabajar con grandes conjuntos de datos ofreciendo un modelo relativamente simple para escribir programas que se podían ejecutar paralelamente en cientos y miles de máquinas al mismo tiempo. Gracias a su arquitectura, MapReduce logra prácticamente una relación lineal de escalabilidad, ya que si los datos crecen es posible añadir más máquinas y tardar lo mismo.

Spark mantiene la escalabilidad lineal y la tolerancia a fallos de MapReduce, pero amplía sus bondades gracias a varias funcionalidades: DAG y RDD.

<div align="center"> 
  <img src="https://media.geeksforgeeks.org/wp-content/uploads/20210618181920/dag6-660x478.JPG" width="%">
</div>

DAG (Grafo Acíclico Dirigido) es un grafo dirigido que no tiene ciclos, es decir, para cada nodo del grafo no hay un camino directo que comience y finalice en dicho nodo. Un vértice se conecta a otro, pero nunca a si mismo.

Spark soporta el flujo de datos acíclico. Cada tarea de Spark crea un DAG de etapas de trabajo para que se ejecuten en un determinado cluster. En comparación con MapReduce, el cual crea un DAG con dos estados predefinidos (Map y Reduce), los grafos DAG creados por Spark pueden tener cualquier número de etapas. Spark con DAG es más rápido que MapReduce por el hecho de que no tiene que escribir en disco los resultados obtenidos en las etapas intermedias del grafo. MapReduce, sin embargo, debe escribir en disco los resultados entre las etapas Map y Reduce.

Gracias a una completa API, es posible programar complejos hilos de ejecución paralelos en unas pocas líneas de código.

**Funciones MAP & Lambdas**

