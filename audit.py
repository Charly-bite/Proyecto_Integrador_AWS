import boto3
import json
from datetime import datetime, timedelta

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")

def prune_dict(d, keys_to_keep):
    if not isinstance(d, dict):
        return d
    return {k: d[k] for k in keys_to_keep if k in d}

def save_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, default=json_serial)

def main():
    # Set up clients
    region = 'us-east-1'
    ec2_client = boto3.client('ec2', region_name=region)
    s3_client = boto3.client('s3', region_name=region)
    cw_client = boto3.client('cloudwatch', region_name=region)

    vpc_id = 'vpc-0982e3e343bf75089'
    instance_id = 'i-0b72112bacb2de241'
    sg_id = 'sg-000307f07c1070e22'
    bucket_name = 'proyecto-integrador-archivos-69181'

    # 1. VPC Evidence
    print(f"Fetching VPC {vpc_id}...")
    vpc_response = ec2_client.describe_vpcs(VpcIds=[vpc_id])
    if vpc_response['Vpcs']:
        vpc = vpc_response['Vpcs'][0]
        vpc_pruned = prune_dict(vpc, ['VpcId', 'State', 'CidrBlock', 'IsDefault'])
        save_json(vpc_pruned, 'vpc_evidence.txt')

    print(f"Fetching Subnets for VPC {vpc_id}...")
    subnets_response = ec2_client.describe_subnets(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])
    if subnets_response['Subnets']:
        subnets_pruned = [prune_dict(sn, ['SubnetId', 'VpcId', 'CidrBlock', 'State', 'AvailabilityZone']) for sn in subnets_response['Subnets']]
        save_json(subnets_pruned, 'subnets_evidence.txt')

    # 2. EC2 Evidence
    print(f"Fetching EC2 {instance_id}...")
    ec2_response = ec2_client.describe_instances(InstanceIds=[instance_id])
    if ec2_response['Reservations'] and ec2_response['Reservations'][0]['Instances']:
        instance = ec2_response['Reservations'][0]['Instances'][0]
        instance_pruned = prune_dict(instance, ['InstanceId', 'InstanceType', 'State', 'PublicIpAddress', 'PrivateIpAddress', 'VpcId', 'SubnetId'])
        instance_pruned['State'] = instance_pruned.get('State', {}).get('Name', 'unknown')
        save_json(instance_pruned, 'ec2_evidence.txt')

    # 3. Security Group Evidence
    print(f"Fetching SG {sg_id}...")
    sg_response = ec2_client.describe_security_groups(GroupIds=[sg_id])
    if sg_response['SecurityGroups']:
        sg = sg_response['SecurityGroups'][0]
        sg_pruned = prune_dict(sg, ['GroupId', 'GroupName', 'VpcId', 'IpPermissions'])
        save_json(sg_pruned, 'sg_evidence.txt')

    # 4. S3 Evidence (Public Access Block & Encryption)
    print(f"Fetching S3 {bucket_name}...")
    s3_evidence = {'BucketName': bucket_name}
    try:
        pab_response = s3_client.get_public_access_block(Bucket=bucket_name)
        s3_evidence['PublicAccessBlockConfiguration'] = pab_response.get('PublicAccessBlockConfiguration', {})
    except Exception as e:
        s3_evidence['PublicAccessBlockConfiguration'] = str(e)

    try:
        enc_response = s3_client.get_bucket_encryption(Bucket=bucket_name)
        s3_evidence['ServerSideEncryptionConfiguration'] = enc_response.get('ServerSideEncryptionConfiguration', {})
    except Exception as e:
        s3_evidence['ServerSideEncryptionConfiguration'] = str(e)

    save_json(s3_evidence, 's3_evidence.txt')

    # 5. CloudWatch Evidence
    print(f"Fetching CloudWatch metrics for {instance_id}...")
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(hours=1)

    cw_response = cw_client.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
        StartTime=start_time,
        EndTime=end_time,
        Period=300,
        Statistics=['Average']
    )

    cw_evidence = {
        'InstanceId': instance_id,
        'MetricName': 'CPUUtilization',
        'RecentDatapoints': []
    }

    if cw_response.get('Datapoints'):
        # sort by timestamp and take the last 3 for brevity
        datapoints = sorted(cw_response['Datapoints'], key=lambda x: x['Timestamp'])[-3:]
        for dp in datapoints:
            cw_evidence['RecentDatapoints'].append({
                'Timestamp': dp['Timestamp'].isoformat(),
                'AverageCPU': round(dp['Average'], 2)
            })
    else:
        cw_evidence['RecentDatapoints'] = 'No recent datapoints available.'

    save_json(cw_evidence, 'cloudwatch_evidence.txt')

    print("Audit data collected successfully.")

if __name__ == '__main__':
    main()
