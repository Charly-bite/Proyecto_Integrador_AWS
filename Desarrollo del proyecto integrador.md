Desarrollo del proyecto
integrador

 Diseño inicial de la

arquitectura en la nube

4.2.1. Definición del problema

Describir de manera técnica la necesidad, limitación o riesgo que
se busca resolver mediante una solución basada en computación
en la nube.

 Debe incluir:

▪ Contexto general del problema.

▪ Situación actual.

▪ Limitaciones del esquema actual.

▪ Consecuencias de no atender el problema.

▪ Justificación de por qué la nube puede apoyar en su solución.

 Idea de referencia sin desarrollar; el equipo debe crear y ampliar su propio

planteamiento: (Una organización “x” requiere centralizar el acceso a información
crítica, pero actualmente los datos se encuentran dispersos en equipos locales, sin
control de acceso, respaldo automatizado ni disponibilidad garantizada.)

4.1.2 Objetivos

a) Objetivo General: Establecer el propósito principal del
proyecto, indicando qué se busca lograr con la
implementación de la solución en la nube.

b) Objetivos específicos (min. 3) Definir acciones concretas
que permitan alcanzar el objetivo general. (Ejem: Identificar
los servicios en la nube necesarios para el funcionamiento
del sistema)

c) Usuarios o actores del sistema: iIdentificar quiénes
interactuarían con la solución y qué rol cumplirían dentro del
sistema.

Debe considerar: Usuario final, administrador del sistema,
responsable de seguridad, responsable de operación o
monitoreo, cliente, área o institución beneficia

4.1.3 Activos que manejará el sistema

 Describir los datos, recursos o activos digitales que serán

procesados, almacenados o protegidos dentro de la solución.

 Debe incluir:

▪ Tipo de información.

▪ Nivel de sensibilidad.

▪ Riesgos asociados.

▪ Requerimientos de almacenamiento.

▪ Necesidades de respaldo y recuperación.

 Idea de referencia sin desarrollar; el equipo debe crear y ampliar su propio

planteamiento: (El sistema manejará registros de usuarios, documentos internos,
bitácoras de acceso y archivos operativos, por lo que se requiere aplicar controles de
confidencialidad, integridad y disponibilidad.)

 .

4.1.4 Justificación del uso de la nube

Explicar técnicamente por qué la solución propuesta se beneficiaría
de una arquitectura en la nube.

Debe relacionarse con:

 Escalabilidad, alta disponibilidad, reducción de infraestructura local,

Seguridad administrada, respaldo y recuperación, monitoreo,
acceso remoto controlado, pago por uso o uso de capa gratuita.

Idea de referencia sin desarrollar; el equipo debe crear y ampliar su propio planteamiento: (El
uso de servicios en la nube permite implementar una solución con mayor disponibilidad,
respaldos automatizados, control de acceso centralizado y capacidad de crecimiento sin
necesidad de adquirir infraestructura física propia.)

 .

4.1.5 Alcance técnico del proyecto

Delimitar qué incluirá y qué no incluirá la propuesta.

Debe indicar:

Debe indicar:

 Servicios considerados.

 Funciones principales.

 Medidas de seguridad mínimas.

 Elementos que se harán de forma práctica.

 Elementos que se presentarán de forma simulada o conceptual.

Idea de referencia sin desarrollar; el equipo debe crear y ampliar su propio planteamiento: (El
proyecto incluirá el diseño de una arquitectura con red virtual, instancia de cómputo,
almacenamiento, base de datos, control de accesos, respaldo y monitoreo. Los elementos
que no puedan implementarse dentro de la capa gratuita serán documentados mediante
simulación técnica.)

 .

4.1.5 Alcance técnico del proyecto

Delimitar qué incluirá y qué no incluirá la propuesta.

Debe indicar:

 Debe indicar:

 Servicios considerados.

 Funciones principales.

 Medidas de seguridad mínimas.

 Elementos que se harán de forma práctica.

 Elementos que se presentarán de forma simulada o conceptual.

Idea de referencia sin desarrollar; el equipo debe crear y ampliar su propio planteamiento: (El
proyecto incluirá el diseño de una arquitectura con red virtual, instancia de cómputo,
almacenamiento, base de datos, control de accesos, respaldo y monitoreo. Los elementos
que no puedan implementarse dentro de la capa gratuita serán documentados mediante
simulación técnica.)

 .

Diseño inicial de la
arquitectura en la nube

4.2.1 Identificación de servicios en la nube

 El equipo deberá identificar los servicios necesarios para construir

la solución propuesta.

 Debe identificar los servicios requeridos

▪ Servicio de cómputo.

▪ Servicio de almacenamiento.

▪ Servicio de base de datos.

▪ Red virtual.

▪ Control de accesos.

▪ Seguridad.

▪ Monitoreo.

▪ Respaldo y recuperación.

▪ Balanceo de carga o escalabilidad, si el proyecto lo requiere.

 .

4.2.2 Identificación de servicios en la nube

Necesidad técnica

Servidor virtual

Almacenamiento de archivos

Base de datos

Red virtual

Control de usuarios y permisos

Monitoreo

Auditoría

Respaldo

Seguridad perimetral

Servicio sugerido

EC2

S3

RDS o MySQL en EC2

VPC

IAM

CloudWatch

CloudTrail

Snapshots o backups

Security Groups

Nota: Idea de referencia sin desarrollar; el equipo debe crear y ampliar su propio
planteamiento

4.2.3 Descripción de componentes
Después del diagrama, el equipo deberá explicar cada componente
utilizado.

Por cada componente debe indicar:

 Nombre del servicio.

 Función dentro del proyecto.

 Información que procesa o protege.

 Relación con otros componentes.

 Riesgo que ayuda a reducir.

Idea de referencia sin desarrollar; el equipo debe crear y ampliar su propio
planteamiento: Amazon S3: se utilizará para almacenar documentos o archivos del
sistema. Este servicio permite guardar objetos de forma escalable y aplicar permisos
de acceso mediante políticas. Ayuda a reducir el riesgo de pérdida de información
al permitir versionamiento y respaldo.

4.2.4 Configuración básica de seguridad

El equipo deberá proponer las medidas de seguridad para proteger
la solución

 Debe incluir:

▪ Usuarios y roles. Principio de menor privilegio. Reglas de acceso.
Seguridad de red. Cifrado de información. Respaldo. Monitoreo
de eventos. Registro de actividad.

 Idea de referencia sin desarrollar; el equipo debe crear y ampliar su propio

planteamiento: Se configurarán usuarios mediante IAM, asignando permisos mínimos
según el rol. El acceso al servidor se restringirá mediante Security Groups, permitiendo
únicamente los puertos necesarios. La información almacenada deberá contar con
mecanismos de respaldo y, cuando sea posible, cifrado en reposo y en tránsito.

 .

4.2.5 Plan de respaldo y recuperación

El equipo deberá definir cómo se protegerá la información ante
pérdida, error humano, falla técnica o incidente de seguridad.

Debe incluir:

Qué información se respaldará.

Cada cuánto se haría el respaldo.

Dónde se almacenaría.

Cómo se recuperaría.

Qué pasaría si el sistema falla.

Tiempo estimado de recuperación.

 Palabras Claves: (Backup. Snapshot. Recuperación ante desastres. Alta disponibilidad.

RPO. RTO..)

 .

4.2.6 Monitoreo y auditoría

El equipo deberá indicar cómo se supervisará la solución

Debe Explicar:

▪ Qué eventos se van a monitorear.

▪ Qué métricas son importantes.

▪ Qué alertas podrían configurarse.

▪ Qué registros permitirían auditar accesos o cambios

▪ . Cómo se detectaría una actividad anómala.

 Idea de referencia sin desarrollar; el equipo debe crear y ampliar su propio

planteamiento (Se propone utilizar CloudWatch para monitorear uso de CPU, memoria,
disponibilidad del servicio y posibles fallas. También se puede utilizar CloudTrail para
registrar acciones realizadas por usuarios dentro de la cuenta.)

 .

4.2.7 Elementos implementados y elementos simulados

El equipo deberá distinguir qué partes de la arquitectura fueron
implementadas realmente y cuáles fueron simuladas o
documentadas.

 .

Elemento

VPC

EC2

RDS

CloudWatch

Balanceador de
carga

Implementa
do

Simulado

Justificación

Sí

Sí

No

Sí

No

No

No

Sí

No

Sí

Se creó una red
virtual básica

Se usó instancia
gratuita

Se documentó
por posible costo

Se revisaron
métricas básicas

Se simuló por
limitaciones de
capa gratuita

4.2.8 Diagrama de arquitectura
Representa como somo se conectan los componentes
principales del sistema (puedes usar Draw.io, diagrams.net, Lucidchart,
Canva, Figma)
Ejemplo:

4.2.9 Seguridad integrada en la arquitectura

 Aunque los controles de seguridad se desarrollan más en el punto
4.2.2, en el diseño arquitectónico ya deben aparecer ubicados.

▪ Deben señalar: (Dónde se aplican permisos, Qué componentes
quedan públicos y cuales privados.  Qué tráfico se permite.
Dónde se cifran datos.  Dónde se generan logs. Dónde se hacen
respaldos. Qué servicio monitorea la actividad.

Ejemplo:

 La base de datos no será pública. Solo aceptará conexiones desde el servidor de

aplicación. El almacenamiento tendrá políticas de acceso restringidas. Las
credenciales se gestionarán mediante usuarios y roles. El tráfico hacia la aplicación
utilizará HTTPS cuando sea posible. Las acciones administrativas serán registradas para
auditoría.

▪ .

4.2.10 Nivel de implementación:(real o simulado)

 Como puede haber limitaciones de capa gratuita, el equipo debe

indicar qué partes se implementarán realmente y cuáles se presentarán
de forma simulada o documentada.

Ejemplo:

Componente

EC2

S3

IAM

Security Groups

RDS

Load Balancer

Auto Scaling

CloudWatch

AWS Backup

Implementación

Real en capa gratuita

Real en capa gratuita

Real

Real

Opcional o simulado según créditos
disponibles

Simulado si genera costo

Simulado o documentado

Básico real

Simulado o documentado

Controles de seguridad en
la arquitectura

4.3.1 Identificación de activos a proteger
El equipo deberá identificar qué elementos de su proyecto requieren
protección.

Debe considerar:

 Información almacenada. Usuarios y credenciales. Servidores o servicios de

cómputo. Base de datos. Archivos o documentos. Red virtual. Respaldos. Logs o
bitácoras. Servicios de monitoreo.

Idea de referencia sin desarrollar; el equipo debe crear y ampliar su propio
planteamiento: El proyecto manejará registros de usuarios, documentos internos y
bitácoras de acceso, por lo que se consideran activos críticos la base de datos, el
almacenamiento de archivos, las credenciales de acceso y los respaldos.

4.3.2 Control de identidad y acceso
El equipo deberá definir cómo se administrarán los usuarios, permisos y
roles dentro de la solución

Debe incluir:

 Usuarios administrativos. Usuarios operativos. Roles o perfiles de acceso. Principio
de menor privilegio. Autenticación. Protección de credenciales. Separación de
permisos según responsabilidad.

Ejemplo:

4.3.3 Seguridad de red
El equipo deberá explicar cómo se protegerá la comunicación entre los
componentes de la arquitectura..

Debe considerar:

 VPC o red virtual.

 Subred pública/Subred privada.

 Security Groups, Reglas de firewall, Puertos permitidos.

 Restricción de acceso a base de datos.

 Separación entre componentes expuestos y componentes internos.

Ejemplo:

4.3.4 Monitoreo de seguridad
El equipo deberá definir cómo se detectarán eventos sospechosos, fallas o accesos
no autorizados.

Debe considerar:

 Métricas del sistema, Alertas, Logs de acceso.

 Registro de cambios, Eventos administrativos, Uso anormal de recursos.

 Intentos fallidos de acceso.

Ejemplo:

4.3.5 Auditoría y trazabilidad
El equipo deberá explicar cómo se conservará evidencia de las acciones realizadas
dentro del sistema o la cuenta de nube.

Debe considerar:

 Registro de accesos.

 Registro de cambios en la configuración.

 Identificación de usuarios que realizan acciones.

 Fecha y hora de eventos relevantes.

 Conservación de logs.

 Revisión periódica de actividad.

Ejemplo:

4.3.6 Respaldo seguro
El equipo deberá explicar cómo se conservará evidencia de las acciones realizadas
dentro del sistema o la cuenta de nube.

Debe considerar:

 Registro de accesos/ Registro de cambios en la configuración.

 Identificación de usuarios que realizan acciones.

 Fecha y hora de eventos relevantes/ Conservación de logs.

 Revisión periódica de actividad.

Ejemplo:

Plan de riesgos y
continuidad

4.4.1 Identificación de riesgos

El equipo deberá identificar al menos cinco riesgos técnicos del proyecto.

Ejemplo:

 Pérdida de información.

 Acceso no autorizado.

 Falla del servidor o servicio principal.

 Base de datos expuesta.

 Configuración incorrecta de permisos

4.4.2 Clasificación de riesgos

Cada riesgo deberá clasificarse por probabilidad e impacto.

Ejemplo:

Riesgo

Pérdida de
información

Acceso no
autorizado

Falla del servidor
principal

Probabilidad

Impacto

Nivel de riesgo

Media

Media

Media

Alto

Alto

Alto

Alto

Medio

Medio

4.3.3 Respaldo seguro
El equipo deberá explicar cómo se conservará evidencia de las acciones realizadas
dentro del sistema o la cuenta de nube.

Debe considerar:

 Registro de accesos/ Registro de cambios en la configuración.

 Identificación de usuarios que realizan acciones.

 Fecha y hora de eventos relevantes/ Conservación de logs.

 Revisión periódica de actividad.

Ejemplo:

4.3.4. RPO y RTO

El equipo deberá definir estos dos valores básicos:

Ejemplo:

Servicio

Base de datos

Aplicación web

Archivos

RPO

24 horas

24 horas

48 horas

RTO

4 horas

2 horas

6 horas

4.3.5. Escenarios de falla

El equipo deberá describir al menos tres escenarios de falla y cómo respondería.

Ejemplo:

Escenario

Acción de respuesta

Falla del servidor

Pérdida de datos

Revisar métricas, reiniciar servicio o
crear una nueva instancia

Restaurar desde el respaldo más
reciente

