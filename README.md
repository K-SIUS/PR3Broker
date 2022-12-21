# PR3Broker
PR3_ BROKER: Ander Sarrión Martín.
A pub/sub communication based on sockets

Para que este modelo acepte múltiples conexiones. He tenido el mismo problema en la práctica de sockets1.
O bien ejecutar múltiples threads, 1 para cada cliente. O bien cambiar el puerto de cada cliente.
Esto no ejecuta porque todos los clientes tienen la misma IP, al ser todos ejecutados desde el mismo pc.
En la teoría, una conexión se identifica por un puerto y una IP distintiva, dándose la posibilidad de que alguno de estos se repita entre conexiones.
Para nuestro caso, si lo que queremos es que acepte múltiples conexiones desde una misma IP, deberemos implementar un mecanismo que vaya actualizando la asignación de puertos de las conexiones entrantes.

Dado que me ha resultado imposible hacerlo mediante if y else, he optado por utilizar try/catch, y reaccionar al error. Haciendo que cuando se dé el error de que el puerto esté en uso, aumentar el valor de puerto y conectarlo a ese puerto.
De esta manera, el cliente suscriptor se conecta a la espera sin que el programa ni el broker lo eche. 
A pesar de todo, y no entiendo el por qué, la ejecución no es perfecta pues los nuevos puertos de clientes suscriptores conectados no sé con quién hacen conexión, pero nunca les llega el mensaje del publicador. Incluso si la conexión con el primer suscriptor se cae, los otros suscriptores no reciben ningún mensaje, es como si su conexión via UDP nunca pudiera recibir paquetes, y no sé por qué es debido. He probado a realizar una llamada de broadcast a todos los clientes subscriptores cada vez que llegara el contenido del publicador, pero tampoco me funcionaba correctamente. Así que he optado por dejarlo tal cual así, pues según lo comentado con mis compañeros de clase, parece ser un error recurrente, y que no se pretendía trabajar en este ejercicio.
