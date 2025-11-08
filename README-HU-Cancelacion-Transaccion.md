Diagrama de Secuencia - Cancelación de Transacción (Draw.io)

Descripción

Este repositorio contiene un diagrama en formato Draw.io que muestra la secuencia de pasos cuando un funcionario desde la pantalla "Histórico de transacciones" en el tab "Pendientes" solicita la cancelación de una transacción.

Archivo

- `HU-Cancelacion-Transaccion-Secuencia.drawio`: Diagrama de secuencia en formato Draw.io (XML). Abra con https://app.diagrams.net/ o con la aplicación de escritorio Draw.io.

Resumen del flujo

1. El funcionario está en la pantalla "Histórico de transacciones" (tab "Pendientes").
2. En un registro con opción de "Cancelar" el funcionario hace clic en esa opción.
3. Se muestra un modal de confirmación con: ícono de alerta, título "¿Deseas realizar la cancelación de la transacción?", texto "Vas a cancelar la transacción. No se puede deshacer" y acciones: "Confirmar" y "Cancelar" además del botón de cerrar.
4. Si el usuario cancela o cierra el modal, no hay cambios en el histórico.
5. Si confirma, el sistema envía la solicitud al Servicio de Transferencias.
6. El servicio valida condiciones (tipo de cliente, tipo de transacción, estado de la solicitud). La opción de cancelar está habilitada solamente para los casos indicados (persona natural: TI, BZLC, cheques; empresa: TI, BZLC, Cheques, BHDIB, Pago TC, Pago préstamo) y sólo si el estado es Ingresada, Pendiente de aprobación o Devuelta.
7. Si la validación pasa, la transferencia se actualiza a "Revocada por cliente" y se notifica al BackOffice para mover la transferencia a la bandeja y al histórico (tab "Realizadas").
8. Si tenía aprobaciones pendientes (estado "Pendiente de aprobación"), se cancelan los procesos de aprobación y desaparece de la pantalla "Pendientes de Aprobación".
9. Se registra la auditoría con: usuario, IP, fecha y hora, tipo de acción (cancelación).
10. Al finalizar, se muestra mensaje al usuario "Tu cancelación ha sido realizado" con texto "Puedes validar en el histórico de transacciones" y un botón "Entendido" que cierra el modal y redirige al histórico de transacciones (tab Pendientes), donde la transacción ya no se visualizará.
11. Si se produce un error al cancelar, se muestra el modal con título "No pudimos realizar la cancelación" y texto "Inténtalo más tarde" con botón "Entendido" que al cerrarlo muestra el formulario diligenciado con la opción de estado "Revocado por cliente".

Recomendaciones

- El diagrama incluye actores: Funcionario (Usuario), Pantalla BEL - Histórico, Servicio de Transferencias, BackOffice, Registro Auditoría.
- Cuando lo abra, puede editar los textos y agregar notas o detalles técnicos (por ejemplo, endpoints, eventos del bus o nombres de la tabla de auditoría) directamente en Draw.io.

Control de versiones

- Fecha de creación: 2025-10-22
- Autor: Generado automáticamente (ajustar metadatos si es necesario)

Contacto

Si desea que convierta esto a un diagrama PNG o SVG o que agregue más detalles técnicos (nombres de APIs, payloads, ejemplo de log de auditoría), indíquelo y lo agrego.