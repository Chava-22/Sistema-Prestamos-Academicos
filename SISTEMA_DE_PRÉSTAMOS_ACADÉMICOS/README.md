# Sistema de Préstamos Académicos

Andrés Calderón
Programación Estructurada
Universidad de Especialidades Espíritu Santo (UEES)

## Objetivo del proyecto

Simular el proceso de préstamo de equipos tecnológicos dentro de una universidad (laptops, proyectores, etc.), aplicando los principios de la programación orientada a objetos: encapsulación, herencia, composición, abstracción y polimorfismo.

## Descripción general

El sistema permite registrar usuarios y equipos, realizar un préstamo, y procesar la devolución de un equipo calculando una multa cuando hay días de atraso. La multa no se cobra igual a todos los usuarios: depende del tipo de cliente que sea cada uno, y ese es justamente el punto central de esta entrega.

Un usuario puede ser cliente mayorista (representa a una facultad o departamento que solicita equipos en volumen, y recibe un 20% de descuento en la multa) o cliente minorista (un estudiante individual, con 5% de descuento). Ambos tipos comparten el mismo comportamiento base definido en una clase abstracta llamada Cliente, que obliga a que cualquier tipo de cliente sepa calcular su propio descuento a través del método calcularDescuento().

Lo importante aquí es que, al momento de cobrar la multa, el sistema no pregunta "¿este usuario es mayorista o minorista?" con un if. Simplemente le pide al cliente que calcule su descuento, y dependiendo de qué tipo de cliente sea realmente, la respuesta cambia. Eso es polimorfismo: mismo mensaje, comportamiento distinto según el objeto real.

## Clases del sistema

Persona guarda los datos básicos de cualquier persona (cédula, nombre, correo). Usuario hereda de Persona y añade la carrera, además de estar compuesto por un Cliente. Equipo representa el recurso físico que se presta. Prestamo une a un Usuario con un Equipo y controla todo el ciclo: el préstamo, la devolución y el cálculo de la multa que sea necesario. Cliente es la clase abstracta que da origen a ClienteMayorista y ClienteMinorista.

