# AWS CLI Implementation Plan - Proyecto Integrador

Este documento proporciona un plan paso a paso para automatizar el despliegue de la arquitectura en la nube (AWS) utilizando **AWS CLI**. El plan se basa en el alcance técnico definido en el documento del proyecto integrador, enfocándose en los elementos marcados como "Implementados" (VPC, EC2, IAM, S3, Security Groups y Monitoreo Básico).

## Requisitos Previos
1. Tener [AWS CLI instalado](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
2. Haber configurado credenciales con permisos de administrador (`aws configure`).
3. Herramientas de terminal (Bash/PowerShell).

---

## Fase 1: Redes (VPC, Subredes y Gateway)
El proyecto requiere una VPC que separe componentes expuestos e internos, implementando una subred pública (para EC2) y preparando una subred privada (para bases de datos, aunque RDS sea simulado).

```bash
# 1. Crear la VPC
VPC_ID=$(aws ec2 create-vpc --cidr-block 10.0.0.0/16 --query 'Vpc.VpcId' --output text)
echo "VPC creada: $VPC_ID"

# 2. Habilitar soporte DNS
aws ec2 modify-vpc-attribute --vpc-id $VPC_ID --enable-dns-support "{\"Value\":true}"
aws ec2 modify-vpc-attribute --vpc-id $VPC_ID --enable-dns-hostnames "{\"Value\":true}"

# 3. Crear Subred Pública (Para el servidor web)
PUB_SUBNET_ID=$(aws ec2 create-subnet --vpc-id $VPC_ID --cidr-block 10.0.1.0/24 --availability-zone us-east-1a --query 'Subnet.SubnetId' --output text)

# 4. Crear Subred Privada (Para componentes internos/RDS simulado)
PRIV_SUBNET_ID=$(aws ec2 create-subnet --vpc-id $VPC_ID --cidr-block 10.0.2.0/24 --availability-zone us-east-1b --query 'Subnet.SubnetId' --output text)

# 5. Crear Internet Gateway y adjuntarlo a la VPC
IGW_ID=$(aws ec2 create-internet-gateway --query 'InternetGateway.InternetGatewayId' --output text)
aws ec2 attach-internet-gateway --vpc-id $VPC_ID --internet-gateway-id $IGW_ID

# 6. Crear Tabla de Rutas Pública y configurar ruta a Internet
RT_ID=$(aws ec2 create-route-table --vpc-id $VPC_ID --query 'RouteTable.RouteTableId' --output text)
aws ec2 create-route --route-table-id $RT_ID --destination-cidr-block 0.0.0.0/0 --gateway-id $IGW_ID

# 7. Asociar Tabla de Rutas a la Subred Pública
aws ec2 associate-route-table --subnet-id $PUB_SUBNET_ID --route-table-id $RT_ID
```

---

## Fase 2: Seguridad (IAM y Security Groups)
Se aplicará el principio de menor privilegio, restringiendo el tráfico a puertos necesarios y gestionando los accesos.

```bash
# 1. Crear usuario IAM (Ejemplo: Administrador/Auditor)
aws iam create-user --user-name ProyectoAuditor

# 2. Asignar políticas de solo lectura (como ejemplo de permisos mínimos para auditoría)
aws iam attach-user-policy --user-name ProyectoAuditor --policy-arn arn:aws:iam::aws:policy/ReadOnlyAccess

# 3. Crear Security Group para el Servidor EC2 (Público)
SG_ID=$(aws ec2 create-security-group --group-name WebServerSG --description "Permitir HTTP, HTTPS y SSH" --vpc-id $VPC_ID --query 'GroupId' --output text)

# 4. Configurar Reglas Inbound (Ingreso)
# NOTA: Reemplazar YOUR_IP con tu IP real para mayor seguridad en el puerto 22.
aws ec2 authorize-security-group-ingress --group-id $SG_ID --protocol tcp --port 22 --cidr 0.0.0.0/0
aws ec2 authorize-security-group-ingress --group-id $SG_ID --protocol tcp --port 80 --cidr 0.0.0.0/0
aws ec2 authorize-security-group-ingress --group-id $SG_ID --protocol tcp --port 443 --cidr 0.0.0.0/0
```

---

## Fase 3: Almacenamiento Seguro (S3)
Crearemos un bucket para el almacenamiento de archivos del sistema. Contará con bloqueo de acceso público y cifrado habilitado.

```bash
# Definir un nombre de bucket único
BUCKET_NAME="proyecto-integrador-archivos-$(date +%s)"

# 1. Crear el Bucket S3
aws s3api create-bucket --bucket $BUCKET_NAME --region us-east-1

# 2. Bloquear acceso público (Seguridad perimetral)
aws s3api put-public-access-block \
    --bucket $BUCKET_NAME \
    --public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"

# 3. Habilitar cifrado por defecto (AES256)
aws s3api put-bucket-encryption \
    --bucket $BUCKET_NAME \
    --server-side-encryption-configuration '{"Rules": [{"ApplyServerSideEncryptionByDefault": {"SSEAlgorithm": "AES256"}}]}'
```

---

## Fase 4: Cómputo (EC2)
Lanzamiento de la instancia de cómputo en la subred pública que fungirá como el servidor principal.

```bash
# 1. Crear Key Pair para acceso SSH (se guardará en el directorio actual)
aws ec2 create-key-pair --key-name ProyectoKeyPair --query 'KeyMaterial' --output text > ProyectoKeyPair.pem
chmod 400 ProyectoKeyPair.pem

# 2. Lanzar la instancia EC2 (Capa gratuita - t2.micro con Amazon Linux 2023)
INSTANCE_ID=$(aws ec2 run-instances \
    --image-id ami-0c101f26f147fa7fd \
    --count 1 \
    --instance-type t2.micro \
    --key-name ProyectoKeyPair \
    --security-group-ids $SG_ID \
    --subnet-id $PUB_SUBNET_ID \
    --associate-public-ip-address \
    --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=ServidorPrincipalProyecto}]' \
    --query 'Instances[0].InstanceId' --output text)

echo "Instancia EC2 Creada: $INSTANCE_ID"
```

---

## Fase 5: Monitoreo (CloudWatch) y Respaldos (Snapshots)
Implementación de los controles de auditoría y plan de recuperación de desastres (RPO/RTO).

```bash
# 1. Habilitar monitoreo detallado en CloudWatch para la Instancia EC2
aws ec2 monitor-instances --instance-ids $INSTANCE_ID

# 2. Creación de un Respaldo (Snapshot) Seguro
# Esperar un momento a que la instancia se inicialice para obtener su volumen
VOLUME_ID=$(aws ec2 describe-instances --instance-ids $INSTANCE_ID --query 'Reservations[0].Instances[0].BlockDeviceMappings[0].Ebs.VolumeId' --output text)

# Crear Snapshot (Ejecutar esto como una tarea programada para cumplir con el RPO)
aws ec2 create-snapshot --volume-id $VOLUME_ID --description "Respaldo manual - Proyecto Integrador"
```

## Resumen del Entorno
Al finalizar este script, se habrán automatizado los siguientes puntos técnicos del documento:
- **4.2.2 y 4.2.7:** Creación real de VPC, EC2, IAM, SGs y S3.
- **4.2.4 y 4.3.3:** Configuración de seguridad a través de Security Groups y bloqueo perimetral en S3.
- **4.2.6 y 4.3.4:** Monitoreo con CloudWatch (Basic Metrics).
- **4.2.5:** Respaldo mediante EBS Snapshots.
