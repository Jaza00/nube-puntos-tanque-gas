<div align="center">
    <img src="src\images\imagenIntecol.PNG"><img>
</div>

<h1 align="center">Nube de puntos de tanque de gas con vedo python<h1>

<p>
    <b>Realizado por:</b> Ing. Jaimen Aza
</p>

Aquí se presentan varios procedimientos que se pueden hacer a partir de una nube de puntos con extención ply. La nube de puntos aquí presentada corresponde a un tanque de gas, al cual se le desea encontrar su diametro y su altura. 

## Abrir nube de puntos 

Primero visualizaremos la nube de puntos tal cual es captura por la cámara de Tiempo de Vuelo (Tof) Helios2, esta nube de puntos retorna las coordenas de unidades de milímetros. 

## Transformación de nube de puntos a imagen de profundidad 

Comunmente es más tipico tener una imagen de profundidad y esta se transforma a una nube de puntos 3D. En este caso será al contrario, a partir de una nube de puntos 3D se desea llegar a una imagen de profundidad. El resulta de muestra en la imagen tal

## Segmetanción del cilindo en la imagen de profundidad

Una vez obtenida la imagen de profundidad, se desea segmentar el cilindro presentado en la imagen, para esto se detecta una circunferencia y se crea una máscara que elimina todo lo que esté afuera del circulo. 

## Dibujar radio sobre la imagen 2D

Una vez detectado el círculo, se dibuja el radio y la longitud de este sobre la imagen ed profundidad, además se le asigna el falso color viridis para efectos de visualización.

## Segmentación del cilindro en la nube de puntos 3D

Con la máscara encontrada en la segmentación del cilindro en la imagen de profundidad, se usa para segmentar el cilindro sobre la nube de puntos 3D, mostrada en la figura x y el resultado de la segemetanción se muestra en la figura tal

## Calcular punto mínimo y máximo de la nube de puntos 

Ahora que tenemos el cilindro segmentado, se desea encontrar y dibujar sobre la nube de puntos el mínimo el máximo valor de la nube, también se dibuja sobre la nube la distancia que existe entre estos dos puntos y el radio que se calculó anteriormente. 

## Proyección de la nube de puntos sobre el eje X 

Para calcular el ancho y el alto del cilindro se hace una proyección de la nube de puntos sobre el eje x, con esto se consigue un perfil de la nube. 

