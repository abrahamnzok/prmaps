# PRM2 : Rapport TD1 - GEOMARKETING
___

###### TEAM 6


## 1. Language (Python)

Pour réaliser la carte, nous avons utilisé le language de programation **python**. Python est connu pour permettre l'écriture de programme avec le moins de ligne de code possible. Il identifie et associe automatiquement les types de données et suit une structure d'imbrication basée sur l'indentation. 

Globalement, la langue est facile à utiliser et prend moins de temps à coder. Il n'y a pas non plus de limitation au traitement des données.

[Voir plus d'informations sur les fichiers geojson](https://medium.com/@sumit.arora/what-is-geojson-geojson-basics-visualize-geojson-open-geojson-using-qgis-open-geojson-3432039e336d)

## 2. Collecte, traitements et analyse des données

##### 1. Collecte
Pour dessiner la carte, nous avons opté pour un type de fichier particulier de type `.geojson`. GeoJSON est un format d’encodage des structures de données géographiques, qui utilise la notation JSON (JavaScript Object Notation). 

En termes simples, GeoJSON offre un format simple pour représenter des entités géographiques simples, ainsi que leurs attributs non spatiaux. 

source des données: https://github.com/gregoiredavid/france-geojson

##### 2. Traitement

Nous avons utilisé deux trois libraries de python pour le traitement de ces données. 

> * **Geopandas**: geopandas facilite la manipulation des données spatiales en python. Elle permet également de faire des tracés à partir de ces mêmes données. 
> 
> * **Pandas** : pandas est une bibliothèque Open Source fournissant des structures de données hautes performances, ainsi que des outils d'analyse des données. Nous l'avons essentiellement utilisés pour la manipulation de collections et pour la lecture de certains fichiers
> 
> * **Pydash**: Pydash est une librairie qui hérite ses fonctionnalités d'une librairie Javascript nommée [lodash](https://lodash.com/). Elle permet de gérer les collections, les tableaux et executer certaines tâches, nous avons utiliser cette librairie pour ne pas réimplementer nous même certaines tâches.
> 
> * **Matplotlib** : Matplotlib est un module python pour la création de graphiques et d'objets, principalement pour la création de visualisations de données. Nous l'avons utilisé pour créer les différents axes et les différentes couches de notre carte à savoir `la couche basse`, `la couche mediane` et `la couche haute`.
> 
> * **shapely** : Shapely nous a permis de créer des objets géométriques galbés. Par exemple, les points qui représentent communes. 


[Voir plus sur Geopandas](http://geopandas.org/), 
[Voir plus sur Matplotlib](https://matplotlib.org/),
[Voir plus sur Pydash](https://pydash.readthedocs.io/en/latest/),
[Voir plus sur Pandas](https://pandas.pydata.org/),
[Voir plus sur Shapely](https://pypi.org/project/Shapely/)

##### 3. Analyse

###### i. Règle syntaxique
Pour réaliser la carte, nous sommes basés sur des fichiers de règles syntaxiques pour les différentes communes. 

Nous avons également établie un algorithme qui prend un entrée le nom d'une commune, les règles qui relèvent de langue oc, et celle d'oeil. Cette algorithme retourne une variable linguiste qui permet de déterminer à partir d'un nom de communes si cette dernière relèvent de la langue d'oc ou d'oil.

La determination de cette valeur se fait en analysant certains critères (préfixe et suffixe) sur les noms de communes. 



##### ii. Tracés et différentes couches.

Pour dessiner la couche basse, il faut lire le fichiers communes.geojson et appeler une méthode de geopandas qui dessine les différents objets geometry contenus dans la collection. Le fichier communes.geojson est disponible dans la répéertoire github fournit à la fin du rapport. 

Pour tracer les points des différentes communes, nous avons décider de créer des collections intermédiaires qui contiendront les objets **geometry** des communes qui relèvent de la langue d'`oic` et celle de la langue d'`oil`. 

Une fois que nous avons ces collections, nous pouvons les déssiner dans différents plans mais aussi dans un même plan. C'est pour cette raison que nous disposons de plusieurs cartes.

