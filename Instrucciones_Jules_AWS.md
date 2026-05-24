# Instrucciones de Auditoría y Documentación para Jules

Hola Jules, tu objetivo es ingresar a la consola de AWS, verificar la infraestructura desplegada, tomar capturas de pantalla como evidencia y finalmente armar el reporte final utilizando LaTeX.

---

## 1. Credenciales de Acceso (AWS Console)
Para tomar las capturas, debes ingresar a la Consola de Administración de AWS utilizando los siguientes datos:

- **URL de acceso:** `https://594161137071.signin.aws.amazon.com/console`
- **Account ID:** `594161137071`
- **Usuario IAM:** `ProyectoAuditor` *(Nota: Si aún no se ha generado una contraseña para este usuario, pide al administrador la contraseña temporal o utiliza la cuenta principal del proyecto).*
- **Contraseña:** `Proyecto123!Auditor`
- **Región:** Asegúrate de estar en la región **N. Virginia (`us-east-1`)** en la esquina superior derecha.

---

## 2. Paso a Paso y Objetivos de Captura

### Paso 1: Verificar la Red (Amazon VPC)
- **Objetivo:** Demostrar que la red virtual privada está desplegada para aislar los componentes.
- **Acción:** Ve al servicio **VPC**, selecciona "Your VPCs".
- **Captura 1 (`captura1_vpc.png`):** Toma un screenshot donde se vea la VPC creada con el ID `vpc-0982e3e343bf75089`.
- **Captura 2 (`captura2_subnets.png`):** Ve a la sección "Subnets" y toma un screenshot que muestre las subredes asociadas a esa VPC.

### Paso 2: Verificar Cómputo y Seguridad (Amazon EC2)
- **Objetivo:** Evidenciar la instancia web principal y sus reglas de firewall restrictivas.
- **Acción:** Ve al servicio **EC2**, entra a la sección "Instances".
- **Captura 3 (`captura3_ec2.png`):** Toma un screenshot de la instancia con ID `i-0b72112bacb2de241` en estado "Running".
- **Acción:** Selecciona la instancia, ve a la pestaña "Security" (o abre directamente "Security Groups").
- **Captura 4 (`captura4_sg.png`):** Toma un screenshot de las reglas Inbound (Entrada) del Security Group `sg-000307f07c1070e22` mostrando los puertos 22, 80 y 443 habilitados.

### Paso 3: Verificar Almacenamiento Seguro (Amazon S3)
- **Objetivo:** Comprobar que el almacenamiento está cifrado y estrictamente bloqueado al público.
- **Acción:** Ve al servicio **S3**, busca el bucket `proyecto-integrador-archivos-69181` y entra en él.
- **Captura 5 (`captura5_s3_public.png`):** En la pestaña "Permissions", toma un screenshot de la sección "Block public access" mostrando que todas las opciones de bloqueo están en "On".
- **Captura 6 (`captura6_s3_enc.png`):** En la pestaña "Properties", busca la sección "Default encryption" y toma un screenshot mostrando que el cifrado (AES-256) está habilitado.

### Paso 4: Verificar Monitoreo (Amazon CloudWatch)
- **Objetivo:** Demostrar que los recursos clave están siendo monitoreados para alta disponibilidad.
- **Acción:** Ve al servicio **CloudWatch**, navega a "Metrics" -> "All metrics" -> "EC2" -> "Per-Instance Metrics".
- **Captura 7 (`captura7_cloudwatch.png`):** Selecciona la métrica `CPUUtilization` para la instancia `i-0b72112bacb2de241` y toma un screenshot de la gráfica mostrada.

---

## 3. Generación del Reporte en LaTeX
Una vez que hayas guardado las 7 capturas de pantalla en la misma carpeta que tu proyecto de LaTeX, utiliza la siguiente plantilla base (por ejemplo, en un archivo `reporte.tex`) para generar el documento PDF.

```latex
\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[spanish]{babel}
\usepackage{graphicx}
\usepackage{geometry}
\usepackage{hyperref}

\geometry{a4paper, margin=2.5cm}

\title{\textbf{Reporte de Auditoría: Implementación de Infraestructura AWS}\\Proyecto Integrador}
\author{Auditor: Jules}
\date{\today}

\begin{document}

\maketitle

\section{Introducción}
El presente reporte evidencia la correcta implementación de la arquitectura en la nube sobre AWS, verificando de manera empírica el cumplimiento de los lineamientos de seguridad, redes y cómputo establecidos en el Proyecto Integrador.

\section{Evidencias de Implementación}

\subsection{1. Redes (Amazon VPC)}
El diseño de la red virtual fue aprovisionado para asegurar el correcto aislamiento de los recursos.
\begin{figure}[h!]
    \centering
    \includegraphics[width=0.8\textwidth]{captura1_vpc.png}
    \caption{Amazon VPC implementada (ID: vpc-0982e3e343bf75089).}
\end{figure}

\subsection{2. Cómputo y Seguridad (Amazon EC2 y Security Groups)}
Se desplegó un servidor web de alta disponibilidad. Sus accesos de red están limitados bajo el principio de menor privilegio.
\begin{figure}[h!]
    \centering
    \includegraphics[width=0.8\textwidth]{captura3_ec2.png}
    \caption{Instancia EC2 principal en ejecución (ID: i-0b72112bacb2de241).}
\end{figure}
\begin{figure}[h!]
    \centering
    \includegraphics[width=0.8\textwidth]{captura4_sg.png}
    \caption{Reglas de Security Group habilitando únicamente puertos HTTP, HTTPS y SSH.}
\end{figure}

\subsection{3. Almacenamiento Seguro (Amazon S3)}
El almacenamiento de objetos fue configurado con medidas robustas para prevenir la fuga de datos.
\begin{figure}[h!]
    \centering
    \includegraphics[width=0.8\textwidth]{captura5_s3_public.png}
    \caption{Bloqueo perimetral de acceso público activado exitosamente en S3.}
\end{figure}

\subsection{4. Monitoreo Activo (Amazon CloudWatch)}
Se validó la recolección de métricas detalladas del servidor para garantizar tiempos óptimos de respuesta a incidentes.
\begin{figure}[h!]
    \centering
    \includegraphics[width=0.8\textwidth]{captura7_cloudwatch.png}
    \caption{Gráfica de utilización de CPU monitoreada vía CloudWatch.}
\end{figure}

\section{Conclusión}
Tras la revisión de la consola de administración de AWS, se constata que los recursos de cómputo, almacenamiento y red fueron aprovisionados correctamente, incluyendo los controles de seguridad fundamentales (IAM, Security Groups y cifrado de S3).

\end{document}
```
