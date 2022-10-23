<div align="center">
  <h1>Ingeniería de datos con Python, Cloud & Data Sourcing</h1>
</div>

<div align="center"> 
  <img src="https://miro.medium.com/max/501/1*XzNcxsUYugJu2SB2SEOf3w.jpeg" width="">
</div>
Fuente de imagen miro.medium.com

# Presentacion

Mi nombre es **Jonathan Garcia** Ingeniero en telecomunicaciones por la UNIVERSIDAD TECNOLOGICA DE MEXICO, actualmente lidero el equipo analistas de KPI's y SLA's en Altán Redes, una compañia encargada de desarrollar una red de telecomunicaciones a gran escala, desde mis inicios laborales he tenido la necesidad de gestionar la informacion en ficheros de excel, lo que ha hecho que ocasionalmente se tengan perdidas de datos o que su manipulacion se compleja, es por esto que como apasionado de la tecnologia estoy en un proceso de transicion para desarrollar proyectos de ingenieria de datos y ciencia de datos, este catalogo de proyectos busca mostrar mis habilidades en el campo de la ingenieria de datos bajo el siguiente pipeline.

<div align="left">
  <h4>1.- Captura</h4>
  <h4>2.- Almacenamiento</h4>
  <h4>3.- Procesamiento</h4>
  <h4>4.- Uso del dato</h4>
  <h4>5.- Analitica</h4>
  <h4>6-. Publicacion</h4>
  <h4>7.- Archivado</h4>
</div>

# Introducción
 El desarrollo de estos proyectos busca poder plasmar los conocimientos obtenidos y que sean una guia para los cientificos de datos e ingenieros de datos con poca experiencia y que buscan ideas distintas para desarrollar sus proyectos
 
# Objetivos del repositorio
<div align="left">
<h3>Desarrollar proyectos que involucren el ciclo de vida de la ingeniera de datos a traves de herramientas locales y en la nube como</h3>
<ul style="list-style-type:square">
<li>AWS Cloud</li>
<li>Azure</li>
<li>Google Cloud</li>
<li>Owncloud</li>
<li>Jupyter Notebooks</li>
<li>Apache airflow</li>
<li>SQL</li>
<li>Bussines Intelligence (Power BI, Tableau,Qlick Sense etc.)</li>  
</ul>
</div>

# Tabla de contenido 
### Desde la introduccion hasta ETL, se ha tomado el resumen de francomanca93 https://github.com/francomanca93

- [Introducción](#Introducción)
    - [Introducción al curso](#Introducción-al-curso)
    - [¿Qué es la Ciencia e Ingeniería de Datos?](#¿Qué-es-la-Ciencia-e-Ingeniería-de-Datos?)
    - [Roles](#Roles)
    - [Configuración del ambiente](#Configuración-del-ambiente)
    - [Jupyter Notebooks](#Jupyter-Notebooks)
    - [Profundizando en tipos de datos](#Profundizando-en-tipos-de-datos)
    - [Fuentes de datos](#Fuentes-de-datos)
    - [ETL](#ETL)

## Introducción
En este curso vamos a explorar cuál es el proceso que se sigue en la **ingeniería de datos**. Obtener obtener datos y datasets del mundo real de diferentes fuentes y lugares. Casi siempre estos datos vienen en un formato o estructura que no esta lista para el **análisis** adecuado.

La ingeniería de datos se preocupan principalmente por implementar los **pipelines** que permiten automatizar la obtención de datos y su posterior limpieza para que otros profesionales de los datos(científicos de datos o expertos en machine learning) puedan realizar su labor. **Son la primera parte de la cadena**.

Podrás entender el día a día de un ingeniero de datos y cómo colabora con el resto del equipo.

### ¿Qué es la Ciencia e Ingeniería de Datos?

La Ciencia de Datos es la disciplina que se encarga de extraer conocimiento de los datos disponible. Casi siempre cuando te realizas una pregunta sobre datos estas fuentes se encuentran escondidas, ocultas o de difícil acceso. A nuestro alrededor hay datos en tu computadora, mesa, reloj, etc.

Los datos están por todas partes.

La Ciencia de datos es multidisciplinaria. A diferencia de muchos otros ámbitos profesionales dentro del mundo de la tecnología cuando hablamos de un científico de datos es una persona que sabe de matemáticas, ingeniería de software y sabe de negocios.

Se apoya en: 
- **Computer science**. Las computadoras son la mejor herramienta para procesar datos. Se apoya de: 
    - Algoritmos
    - Estructura de datos
    - Visualizaciones que nos puede dar la computadora.
    - Conectar varias computadoras en paralelo en la nube, 
    - Programación.
- **Matemática estadística**
    - Regresiones
    - Inferencias
    - Identificación de variables y relación de variables.
- Tener **conocimiento del dominio**
    - Preguntar los correcto
    - Interpretar datos correctamente en función a las preguntas que hagamos.

<div align="center"> 
  <img src="https://datos.gob.es/sites/default/files/datosgobes/equipos_datos_1.png" width="">
</div>

Herramientas donde se auxilia:

- Bases de Datos
    - SQL (MySQL, Postgres, etc.)
    - NoSQL (Cassandra, Spark, etc.)
- Análisis de texto y procesamiento de lenguaje natural (NLP)
- Análisis de redes
- Análisis numérico de datos y minado de datos
- Visualización de datos
    - No permite contar historias
    - Analizar rapidamente
    - Los humanos somos mas eficientes analizando datos gráficos.
- Machine learning e Inteligencia Artificial
- Análisis de señales digitales. 
    - Análisis de datos en tiempo real. 
- Análisis de datos en la nube (Big Data). Data center que podemos utilizar eficientemente para procesar grandes cantidades de datos

### Roles

Existen por lo menos tres diferentes roles para tener un pipeline completo de ciencia de datos. Este curso trata sobre el primer rol:

- **Data engineer**: Se encarga de obtener los datos, Limpiarlos y estructurarlos para posterior análisis, crear pipelines de análisis automatizado, utilización de herramientas en la nube, análisis descriptivo de los datos.

- **Data scientist**: Una vez tiene los datos se encarga de generar el análisis matemático de ellos, encontrar las relaciones entre las variables, las correlaciones, las causas y por último genera los modelos predictivos y prescriptivos.

- **Machine Learning engineer**: Se encarga de llevar las predicciones a escala, de subirlos a la nube y allí generar muchas predicciones. Se encarga de mantener la calidad del modelo.

<div align="center"> 
  <img src="https://miro.medium.com/max/1200/1*FMwKyF0I9nh3DG0ft8nKvg.png" width="">
</div>

### Configuración del ambiente

[**Anaconda**](https://www.anaconda.com/) es una instalación de Python que ya trae preinstalado todos los paquetes necesarios para tu labor en la Ciencia de Datos, tiene más de **1400 paquetes**. Nos permite configurar ambientes virtuales para poder utilizar diferentes versiones de nuestros paquetes.

- Para conocer la versión y saber que lo tenemos instalado: 

`conda --version`

- Para ver todos los comandos que podemos usar usamos:

`conda --help` 

- Para ver una lista de todos los paquetes que Anaconda instaló.

`conda list` 


Una buena práctica es generar un **ambiente virtual** por cada proyecto, los ambientes virtuales nos permiten generar varios proyectos con diferentes versiones de la librería sin generarnos errores de compatibilidad. Tradicionalmente en Python se utiliza virtualenv

`conda create --name nombre_entorno`

- Instalar librerias:

`$ conda install nombre_libreria`

- En este caso usaremos las siguientes librerias:
  - **beautifulsoup4** = parsear y manipular HTML
  - **requests** = generar solicitudes a la web
  - **numpy** = análisis numéricos de nuestros datos
  - **pandas** = analizar, modificar, transformar datos y generar análisis descriptivos sobre los mismos
  - **matplotlib** = generar visualizaciones de nuestros datos
  - **yaml** =archivo similar a Json, permite generar algunas configuraciones

Al instalar las librerias se instalan dependendias para que estas funcionen.

- Para activar el ambiente que acabamos de crear: 

`conda activate nombre_entorno`

- Para salir 

`conda deactivate`

- Para ver una lista de los ambientes virtuales que tenemos:

`$ conda info --envs` o tambien `$ conda env list`

- Para ver todos paquetes de nuestro entorno virtual:

`$ conda list -n nombre_entorno`

- Para eliminar nuestro entorno virtual con todos nuestros paquetes

`$ conda remove --name nombre_entorno --all`

### Jupyter Notebooks

Algo interesante que tenemos con Anaconda es que nos trae [Jupyter Notebooks](https://jupyter.org/).

Jupyter Notebooks es un entorno de programación en el cual podemos mezclar ejecución de código en vivo, visualizaciones y añadir markdown.

- Para inicializar nuestro servidor de jupyter:

`$ jupyter notebook`

Jupyter Notebook tiene diferentes tipos de celdas en las cuales podemos escribir código o markdown. Si queremos ejecutar nuestro código hacemos `ctrl + enter` y si queremos ejecutar y añadir una nueva celda `shift + enter`.

- `ESC`: dentro de una celda entrar al modo de navegación. (el borde izquierdo de la celda se resalta en azul)
- `K`: mover hacia arriba
- `J`: mover hacia abajo
- `B`: Agregar nueva celda
- `M`: Convertir en MarkDown
- `P`: Acceder a la línea de comando
- `DD`: Eliminar Celda

Jupyter Notebook tiene dos modalidades, la modalidad de edición y navegación.

### Profundizando en tipos de datos

Los datos vienen en muchas formas y estas formas las podemos clasificar de diferentes maneras, permitiéndonos poder aplicar técnicas distintas a cada uno de los tipos de datos.

- Los primeros datos son los primitivos.
`int, str, bool, float, hex, oct, datetime, objetos especiales`

Tenemos otras clasificaciones como los datos estructurados, semi estructurados y no estructurados.

- Los **estructurados** son los más fáciles de acceder a su información.
  - Bases de datos
  - Data warehouse
- Los **semis estructurados** donde podemos usar las APIs
  - json API's
  - Datos tabulares (csv, excel)
- Los **No estructurados** son la mayoría de los datos que te vas a encontrar en tu desarrollo profesional.
  - HTML
  - Texto libre
  - Imagenes, audios, videos
  - Datos científicos

<div align="center"> 
  <img src="https://www.salesforce.com/content/dam/blogs/mx/2020/data-lakesxdata-warehouses-mx.jpg" width="80%">
</div>

### Fuentes de datos

- **Web**

Es una mina enorme con datos financieros, de startups, del clima, precipitación fluvial, astronómicos, de negocios, etc.


- **APIs**

Endpoints que viven en la web y nos devuelven JSON. Por ejemplo, la API de twitter, google, facebook.

Todas las [API's de google](https://console.cloud.google.com/apis/library) que este nos ofrece.

- **User Analytics**

Son el comportamiento del usuario dentro de nuestra aplicaciones, algo similar a los que nos ofrece Google Analytics.

- **IoT**

El [IoT o Internet of Things](https://es.wikipedia.org/wiki/Internet_de_las_cosas) Se ha vuelto una mina espectacular en los últimos años. Como automóviles, sensores en edificios y todo aquello que se pueda conectar a internet. 

En los siguientes enlaces podemos encontrar gran cantidad de datset asi como tambien un buscado de estos desarrollado por google.

- [Dataset Search de Google](https://datasetsearch.research.google.com/)
- [Data Word](https://data.world/)
- [Kaggle](https://www.kaggle.com/)

### ETL

**ETL = Extract Transform Load**

Los procesos ETL son un término estándar que se utiliza para referirse al movimiento y transformación de datos. Se trata del proceso que permite a las organizaciones mover datos desde múltiples fuentes, reformatearlos y cargarlos en otra base de datos (denominada data mart o data warehouse) con el objeto de analizarlos. También pueden ser enviados a otro sistema operacional para apoyar un proceso de negocio.

Si separamos por puntos cada uno haría lo siguiente:
- **Extract**: Es el proceso de lectura de datos de diversas fuentes

  - Base de datos
  - CRM
  - Archivos CSV
  - Datasets públicos

- **Transform**: En este momento cuando nosotros tenemos que transformar los datos, tenemos que identificar datos faltantes o datos erróneos o una edad negativa. En esta etapa donde tenemos que identificar todos los problemas y solucionarlos.

  - Limpieza
  - Estructurado
  - Enriquecimiento.

- **Load**: Una vez transformados debemos insertarlos en el data warehouse

  - Depende del tipo de solución que se haya escogido

<div align="center"> 
  <img src="https://content.altexsoft.com/media/2020/03/etl-pipeline.png" width="">
</div>
