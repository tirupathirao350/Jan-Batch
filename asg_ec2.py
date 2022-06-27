import boto3 


asg_client = boto3.client('autoscaling',aws_access_key_id=acc_key,aws_secret_access_key=sec_key,region_name='us-west-2')
ec2_client = boto3.client('ec2',aws_access_key_id=acc_key,aws_secret_access_key=sec_key,region_name='us-west-2')

asg = "YOUR_ASG_NAME"
instance_ids = [] # List to hold the instance-ids
 
 
def get_creds():
     """
     """


def describe_asg():
    """
    """
    asg_response = asg_client.describe_auto_scaling_groups(AutoScalingGroupNames=[asg])
    
    return asg_response


def get_ec2_id(asg_response):
    """
    """
    for i in asg_response['AutoScalingGroups']:
        for k in i['Instances']:
            instance_ids.append(k['InstanceId'])
    return instance_ids


def create_ami(instance_ids):
    """
    """
    for ec2_id in instance_ids:
        ec2_resp = ec2_client.create_image(InstanceId=ec2_id, NoReboot=True, Name="AMI-"+ec2_id)
        ec2_resp['ImageId']
        print(f"AMI Creation started for ec2 instance {ec2_id}")
        print(f"New AMI Id {ec2_resp['ImageId']}")