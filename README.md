 #  Sistema De Reservas para el gimnasio de la Universidad De Medellín

El presente archivo describe el diseño e implementación de un sistema de reservas para el gimnasio de la Universidad de Medellín. El sistema tiene como objetivo mejorar el proceso actual de reserva, que es incómodo y lento para los estudiantes y el personal, ya que, Los estudiantes y el personal deben ir físicamente al bloque 2 o enviar un correo con 24 horas de anticipación para solicitar una reserva. Además, algunos incluso se ven obligados a llegar a las 6 AM del día anterior para asegurar su turno.


![image](https://github.com/Alcaraz5678/ProyectoGym/assets/159556883/bbc8cd95-abb7-4167-a0ef-8c91fbeb9ae1)


Sabiendo lo anterior, nuestro sistema funciona de la siguiente forma:

Al momento de iniciar sesión los usuarios se autentican en el sistema utilizando su número de identificación, el sistema verifica que este registrado en Universidad De Medellín, después el sistema le muestra el menú principal al usuario donde este elije la opción que necesita.

Cuando el usuario desea reservar, elije la opción realizar reserva en el menú, después selecciona la fecha y hora en la que desea usar el gimnasio. El sistema verifica la disponibilidad de horarios para esa fecha. El usuario selecciona un horario disponible y confirma su reserva,
luego el sistema muestra la información de la reserva

El usuario puede cancelar su reserva desde el sistema. El sistema solicita al usuario confirmar la cancelación. El sistema le confirmaría la cancelación con una notificación, El sistema define un límite de usuarios en el gimnasio por hora. El sistema muestra la disponibilidad de cupos en tiempo real. El sistema no permite reservar un horario si se ha superado el límite de capacidad.
El usuario también puede ver un historial de sus reservas en el sistema. El historial de reservas incluye la fecha, hora y estado
Cada estudiante tiene un calendario personalizado en el sistema. El calendario muestra las reservas del estudiante El estudiante puede ver la disponibilidad del gimnasio en el calendario. 
El gimnasio ofrece una variedad de retos a los usuarios. Los usuarios pueden elegir los retos que desean completar, luego se muestra información del reto seleccionado. 
