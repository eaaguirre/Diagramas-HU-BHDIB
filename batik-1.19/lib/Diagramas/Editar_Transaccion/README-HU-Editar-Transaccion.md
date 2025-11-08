Diagrama de Secuencia - HU: Editar Transacción (BHDIB)

Resumen

Este diagrama muestra el flujo para consultar el detalle de una transacción desde la pantalla "Histórico de transacciones" (tab Pendientes), validar permisos, permitir la edición cuando corresponda, usar componente token (HU #833132), persistir cambios en BD, guardar histórico de modificaciones y registrar auditoría.

Archivos

- `editar_transaccion.puml`: Diagrama de secuencia PlantUML. Abra con PlantUML o generadores (VSCode PlantUML extension, PlantUML server) para exportar PNG/SVG.

Participantes clave

- Usuario (Funcionario)
- Interfaz (BEL - Histórico → Detalle)
- API Management (APIM)
- Microservicio de transacciones (`BHDIBP.MS.AccountTransactions`)
- Componente Token (CTA / 2FA)
- Approval Service (flujo de aprobaciones)
- DB (tabla Transactions)
- Historico_Cambios (tabla con cambios y metadata)
- Application Insights (telemetría / auditoría)

Puntos importantes implementados en el diagrama

- Los actores y participantes usan fondo blanco (skinparam actorBackgroundColor white y participantBackgroundColor white).
- Se valida permiso del usuario antes de mostrar opción "Modificar". Si sólo tiene permiso de visualización, no se muestra el botón Modificar.
- Reglas para permitir modificar: Estado (Pendiente de aprobación sin aprobaciones realizadas, o Devuelta); tipo de transacción según persona natural/jurídica según la HU.
- Al guardar, se valida formato/obligatoriedad; si pasa, se solicita token y luego se persisten los cambios en `Transactions`.
- Se guarda un registro en `Historico_Cambios` con el `username`, fecha/hora y detalle de cambios.
- Si corresponde, se reinicia el flujo de aprobaciones (Approval Service) y se actualizan registros de aprobaciones en BD.
- Se registra auditoría (AuditLog o Application Insights) con usuario, IP, fecha/hora y tipo de acción.
- Si ocurre error al consultar o guardar, se muestra el modal correspondiente y se hacen tracks en telemetry.

Cómo generar una imagen (opcional)

Con PlantUML instalado o la extensión de VSCode puedes renderizar el `.puml` a PNG/SVG. Ejemplo usando PlantUML local (requiere Java + plantuml.jar):

```powershell
# desde PowerShell en Windows
java -jar path\to\plantuml.jar d:\Repositorios\BANCO-BHD\Diagramas-HU-BHDIB\batik-1.19\lib\Diagramas\Editar_Transaccion\editar_transaccion.puml
```

Notas / seguimiento

- Si deseas que agregue payloads de ejemplo (JSON) para los endpoints `GET /transactions/{id}` y `PUT /transactions/{id}/update`, lo puedo añadir.
- Puedo también exportar y guardar PNG/SVG en la carpeta si lo deseas.

Fecha de creación: 2025-11-06

Si quieres ajustes (colores, layout, texto en español más corto o más técnico con nombres de tablas y campos), dime y lo adapto.