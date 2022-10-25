# Hilos
#### INTRODUCCIÓN
El servicio de películas en linea día a día llega a ser una herramienta útil para aquellas personas quienes desean conocer información acerca de alguna película. Puede que en internet haya muchos sitios web donde te de esa información, sin embargo para el usuario es algo molesto buscar la página de mejor conveniencia y suele entrar al primer sitio web que aparece.

Esta situación ya no será un problema ya que se presentará más adelante un programa que permite la busqueda de peliculas donde te dará el único resultado deseado, asi como la información más relevante de la pelicula. Es un proceso más rápido y confiable.
#### METODOLOGÍA
**Programación concurrente**

Hace referencia a las técnicas de programación que son utilizadas para expresar la concurrencia entre tareas y solución de los problemas de comunicación y sincronización entre procesos. La programación concurrente es la ejecución simultánea de múltiples tareas interactivamente. Estas tareas pueden ser un conjunto de procesos o hilos de ejecución creados por un único programa. Las tareas se pueden ejecutar en una sola CPU (multiprogramación), en varios procesadores, o en una red de computadores distribuidos.

La programación concurrente no es más que la forma en la cual podemos resolver ciertas problemáticas de forma concurrente, es decir, ejecutando múltiples tareas a la misma vez y no de forma secuencial.En un programa concurrente las tareas puede continuar sin la necesidad que otras comiencen o finalicen.
#### RESULTADOS

#Aspectos teoricos de hilos.

Un hilo es una unidad básica de utilización de CPU, la cual contiene un id de hilo, su
propio program counter, un conjunto de registros, y una pila; que se representa a nivel
del sistema operativo con una estructura llamada TCB (thread control block).
Los hilos comparten con otros hilos que pertenecen al mismo proceso la sección de
código, la sección de datos, entre otras cosas. Si un proceso tiene múltiples hilos, puede
realizar más de una tarea a la vez (esto es real cuando se posee más de un CPU).
Un hilo es el proceso del sistema operativo con características distintas de las de un proceso normal:

Los hilos existen como subconjuntos de los procesos.
Los hilos comparten memoria y recursos.
Los hilos ocupan una dirección diferente en la memoria

Ventajas de usar hilos
• Respuesta: el tiempo de respuesta mejora, ya que el programa puede
continuar ejecutándose, aunque parte de él esté bloqueado.
• Compartir recursos: los hilos comparten la memoria y los recursos del
proceso al que pertenecen, por lo que se puede tener varios hilos de
ejecución dentro del mismo espacio de direcciones.
• Economía: Es más fácil la creación, cambio de contexto y gestión de
hilos que de procesos.
• Utilización múltiples CPUs: permite que hilos de un mismo proceso
ejecuten en diferentes CPUs a la vez. En un proceso mono-hilo, un
proceso ejecuta en una única CPU, independientemente de cuantas tenga
disponibles.
