# Desarrollo del Proyecto Integrador - Implementación en la Nube (AWS)

## 4.1.2 Objetivos
**a) Objetivo General:** Diseñar e implementar una arquitectura en la nube segura, escalable y centralizada para la gestión, almacenamiento y procesamiento de información crítica de la organización, mitigando riesgos de pérdida de datos y accesos no autorizados.

**b) Objetivos Específicos:**
1. Desplegar una infraestructura de red segura (VPC) que aísle los componentes internos de los públicos.
2. Implementar un servidor de cómputo (EC2) de alta disponibilidad para alojar la aplicación principal.
3. Asegurar el almacenamiento de archivos del sistema en la nube (S3) mediante cifrado nativo y bloqueo de acceso público.
4. Establecer políticas estrictas de seguridad mediante IAM y Security Groups siguiendo el principio de menor privilegio.

**c) Usuarios o actores del sistema:**
- **Usuario final:** Interactúa con la aplicación web desplegada en el servidor.
- **Administrador del sistema:** Encargado de la configuración, mantenimiento y despliegue en AWS.
- **Auditor de seguridad (Ej. Rol ProyectoAuditor):** Encargado de revisar accesos, monitorear métricas y validar el cumplimiento normativo (solo lectura).

---

## 4.1.3 Activos que manejará el sistema
El sistema gestionará archivos operativos, documentos internos de la empresa, registros de usuarios y bitácoras de acceso.
- **Nivel de sensibilidad:** Alto, debido a la naturaleza confidencial de los documentos internos.
- **Riesgos asociados:** Fuga de información por accesos mal configurados, pérdida de datos por falla de hardware o eliminación accidental.
- **Requerimientos:** Cifrado en reposo y tránsito, respaldos diarios (Snapshots) y almacenamiento altamente durable.

---

## 4.1.4 Justificación del uso de la nube
El uso de servicios en la nube de AWS permite implementar una solución robusta sin necesidad de adquirir ni mantener infraestructura física propia (CapEx a OpEx). Se beneficia de la escalabilidad instantánea (pago por uso de la instancia EC2), disponibilidad garantizada por la infraestructura global de AWS, respaldos automatizados mediante EBS Snapshots, y un control de acceso centralizado y auditable a través de AWS IAM.

---

## 4.1.5 Alcance técnico del proyecto
**Incluye (Implementado de forma práctica):**
- Diseño de arquitectura con red virtual propia (Amazon VPC).
- Despliegue de instancia de cómputo (Amazon EC2).
- Almacenamiento seguro de objetos (Amazon S3 con AES-256).
- Control de accesos (AWS IAM).
- Seguridad de red (Security Groups).
- Monitoreo básico detallado (CloudWatch).

**No incluye (Presentado de forma simulada/conceptual debido a costos):**
- Base de datos relacional gestionada (Amazon RDS).
- Balanceador de carga elástico (ALB).
- Auto Scaling Groups.

---

## 4.2.1 Identificación de servicios en la nube
Los servicios de AWS seleccionados para construir esta arquitectura son:
- **Servicio de cómputo:** Amazon EC2 (`t2.micro`).
- **Servicio de almacenamiento:** Amazon S3.
- **Servicio de base de datos:** Amazon RDS (Simulado).
- **Red virtual:** Amazon VPC (Virtual Private Cloud) con Internet Gateway.
- **Control de accesos:** AWS IAM (Identity and Access Management).
- **Seguridad:** Security Groups (Firewalls virtuales).
- **Monitoreo:** Amazon CloudWatch.
- **Respaldo:** Amazon EBS Snapshots.

---

## 4.2.3 Descripción de componentes
- **Amazon VPC (`vpc-0982e3e343bf75089`):** Proporciona una red aislada lógicamente donde se despliegan los recursos. Reduce el riesgo de ataques directos a nivel de red.
- **Amazon EC2 (`i-0b72112bacb2de241`):** Servidor virtual que aloja la aplicación. Procesa las peticiones de los usuarios web.
- **Amazon S3 (`proyecto-integrador-archivos-69181`):** Almacenamiento de archivos y documentos con bloqueo perimetral total y cifrado por defecto (AES256). Reduce el riesgo de pérdida o fuga de datos masiva.
- **AWS IAM:** Gestiona los permisos. Se creó el usuario `ProyectoAuditor` con políticas de solo lectura para auditar sin riesgo de modificaciones accidentales.
- **Security Groups (`sg-000307f07c1070e22`):** Actúa como firewall virtual de la instancia EC2, permitiendo únicamente tráfico en los puertos 22 (SSH), 80 (HTTP) y 443 (HTTPS).

---

## 4.2.4 Configuración básica de seguridad
Se implementó un enfoque de **Defensa en Profundidad**:
1. **Identidad (IAM):** Creación del usuario `ProyectoAuditor` aplicando el principio de menor privilegio mediante la política `ReadOnlyAccess`.
2. **Red (Security Groups):** El acceso al servidor EC2 está restringido al Security Group `WebServerSG`. No se abrieron puertos innecesarios.
3. **Datos (S3):** El bucket de almacenamiento cuenta con "Block Public Access" habilitado en su totalidad. Toda la información almacenada en el bucket S3 se cifra automáticamente en reposo utilizando `SSE-S3 (AES-256)`.

---

## 4.2.5 Plan de respaldo y recuperación
- **Qué se respaldará:** Los volúmenes EBS asociados a la instancia EC2 y los archivos en S3.
- **Frecuencia (RPO - 24 horas):** Snapshots de EBS diarios programados durante ventanas de mantenimiento nocturnas.
- **Almacenamiento:** Los Snapshots de EBS se almacenan automáticamente en la infraestructura redundante de AWS S3 gestionada por AWS.
- **Recuperación (RTO - 2 horas):** En caso de falla, se lanzará una nueva instancia EC2 a partir del Snapshot más reciente, o se restaurará el volumen afectado.

---

## 4.2.6 Monitoreo y auditoría
- Se activó el **Monitoreo Detallado de CloudWatch** en la instancia EC2 (`i-0b72112bacb2de241`).
- **Métricas importantes:** Utilización de CPU (`CPUUtilization`), comprobaciones de estado (`StatusCheckFailed`), y tráfico de red entrante/saliente.
- **Auditoría:** Se utiliza AWS IAM para identificar usuarios. A nivel conceptual, se propone AWS CloudTrail para registrar todas las llamadas a las API de AWS realizadas dentro de la cuenta, detectando cambios anómalos en la configuración.

---

## 4.2.7 Elementos implementados y elementos simulados

| Elemento | Implementado | Simulado | Justificación |
| :--- | :---: | :---: | :--- |
| VPC y Subredes | Sí | No | Necesario para aislar la red de la instancia EC2. |
| EC2 (Servidor) | Sí | No | Desplegado usando la capa gratuita (`t2.micro`). |
| Amazon S3 | Sí | No | Se creó el bucket con políticas de cifrado y bloqueo público. |
| IAM y Security Groups | Sí | No | Críticos para la seguridad fundamental del proyecto. |
| RDS (Base de datos) | No | Sí | Se documentó su necesidad, pero genera costos fuera de capa gratuita. |
| CloudWatch | Sí | No | Se habilitaron métricas detalladas para la instancia EC2. |
| Load Balancer | No | Sí | Arquitectura de un solo nodo para ahorrar créditos/costos. |

---

## 4.3.5 / 4.4 Plan de Continuidad y Riesgos

### Identificación y Clasificación de Riesgos
| Riesgo | Probabilidad | Impacto | Nivel de Riesgo |
| :--- | :---: | :---: | :---: |
| Falla del servidor (Caída de EC2) | Media | Alto | Alto |
| Acceso no autorizado a S3 por mala configuración | Baja | Alto | Medio |
| Pérdida de llaves SSH (`ProyectoKeyPair.pem`) | Media | Medio | Medio |
| Ataque DDoS contra la IP pública de EC2 | Baja | Alto | Medio |
| Filtración de credenciales IAM | Baja | Alto | Alto |

### Escenarios de Falla (Respuesta)
1. **Falla del Servidor EC2 (Hardware subyacente de AWS):** 
   - *Respuesta:* CloudWatch emitirá alerta de `StatusCheckFailed`. El administrador detendrá e iniciará la instancia para que AWS la migre a hardware sano, o restaurará desde el último Snapshot EBS.
2. **Eliminación accidental de un archivo en S3:** 
   - *Respuesta:* Habilitar versionamiento en S3 (conceptual). Restaurar la versión anterior del archivo.
3. **Compromiso de credenciales del Auditor:** 
   - *Respuesta:* Desactivar o rotar inmediatamente las `Access Keys` del usuario IAM involucrado y auditar sus acciones recientes en CloudTrail.
