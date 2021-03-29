<div align="center">
    <img src="public\images\imagenIntecol.png"><img>
</div>

<h1 align="center">Nube de puntos de tanque de gas con vedo python</h1>

<p>
    <b>Realizado por:</b> Jaimen Aza
</p>

<p>Aquí, se presentan varios procedimientos que se pueden hacer a partir de una nube de puntos con extensión ply. La nube de puntos aquí presentada corresponde a un tanque de gas, al cual, se desea encontrar su diámetro y su altura.</p>

## Abrir nube de puntos 

Primero visualizaremos la nube de puntos tal cual es capturada por la cámara de Tiempo de Vuelo (ToF) Helios2 (ver figura 1). Esta nube de puntos retorna las coordenadas en unidades de milímetros.

<div align="center">
    <img src="public\images\nubePuntosSinModificaciones.png" width="600"><img>
    <p align="center"><b>Figura 1.</b> Nube de puntos inicial, sin modificaciones.</p>
</div>

## Transformación de nube de puntos a imagen de profundidad 

Comúnmente es típico tener una imagen de profundidad y transformarla a una nube de puntos 3D. En este caso será al contrario, a partir de una nube de puntos 3D se desea llegar a una imagen de profundidad. El resulta de muestra en la figura 2. 

<div align="center">
    <img src="public\images\pointCloud2image.png" width="500"><img>
    <p align="center"><b>Figura 2.</b> imagen de profundidad a partir de la nube de puntos 3D.</p>
</div>

## Segmentación del tanque de gas en la imagen de profundidad

Una vez se obtiene la imagen de profundidad, se desea segmentar el tanque de gas presentado en la imagen, para esto se detecta una circunferencia y se crea una máscara que elimina todo lo que esté afuera del círculo (ver figura 3).

<div align="center">
    <img src="public\images\segmentacionTanque2D.png" width="500"><img>
    <p align="center"><b>Figura 3.</b> Segmentación del tanque de gas en la imagen de profundidad.</p>
</div>

## Dibujar radio sobre la imagen 2D

Una vez detectado el círculo, se dibuja el radio y la longitud de este sobre la imagen ed profundidad, además se le asigna el falso color magma para efectos de visualización (ver figura 4).

<div align="center">
    <img src="public\images\radionTanqueEnImagen2D.png" width="500"><img>
    <p align="center"><b>Figura 4.</b> Radio del tanque de gas sobre la imagen de profundidad.</p>
</div>

## Segmentación del tanque de gas en la nube de puntos 3D

Con la máscara encontrada en la segmentación del tanque de gas en la imagen de profundidad, vamos a segmentar el tanque de gas sobre la nube de puntos 3D mostrada en la <b>figura 1</b>. El resultado de la segmentación de la nube de puntos se muestra en la figura 5.

<div align="center">
    <img src="public\images\segmentacionTanque3D.png"><img>
    <p align="center"><b>Figura 5.</b> Segmentanción del tanque en la nube de puntos 3D. En la izquierda, nube de puntos que no corresponden al tanque. A la derecha nube de puntos del tanque.</p>
</div>

## Calcular punto mínimo y máximo de la nube de puntos 

Ahora que tenemos el tanque de gas segmentado, se desea encontrar y dibujar sobre la nube de puntos el mínimo y el máximo valor de la nube, también se dibuja sobre la nube la distancia que existe entre estos dos puntos y el radio que se calculó anteriormente. Esto se muestre en la figura 6.

<div align="center">
    <img src="public\images\nubePuntosMinMax.png" width="400"><img>
    <p align="center"><b>Figura 6.</b> Nube puntos del tanque de gas con la distancia entre el mínimo punto y el máximo punto de la nube.</p>
</div>

## Proyección de la nube de puntos sobre el eje X 

Para calcular el ancho y el alto del tanque de gas se hace una proyección de la nube de puntos sobre el eje x, con esto se consigue un perfil de la nube (ver figura 7). 

<div align="center">
    <img src="public\images\proyeccionNubePuntos.png" width="400"><img>
    <p align="center"><b>Figura 7. </b>Altura y ancho de la proyección de la nube de puntos del tanque sobre el eje X.</p>
</div>


## Visualización de nube de puntos de varios tanques 

Para efectos de visualización, se hacen copias de la nube de puntos del tanque segmentada, se hace un desplazamiento a cada nube y luego se fusionan para mostrar una nube de puntos con varios tanques (ver figura 8).

<div align="center">
    <img src="public\images\nubePuntosVariosTanques.png" width="450"><img>
    <p align="center"><b>Figura 8.</b> Nube de puntos mostrando 6 tanques de gas.</p>
</div>

## instalar dependencias

```
pip install -r requirements.txt
```
