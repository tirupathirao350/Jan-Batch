import boto3 


# Region Autoscaling region
asg_client = boto3.client('autoscaling',aws_access_key_id=acc_key,aws_secret_access_key=sec_key,region_name='us-west-2')
ec2_client = boto3.client('ec2',aws_access_key_id=acc_key,aws_secret_access_key=sec_key,region_name='us-west-2')

# Autoscaling Group Name
asg = "" 
instance_ids = [] # List to hold the instance-ids
 

def describe_asg():
    """
    Function to describe the ASG
    """
    asg_response = asg_client.describe_auto_scaling_groups(AutoScalingGroupNames=[asg])
    
    return asg_response


def get_ec2_id(asg_response):
    """
    Function to get the Instances from the ASG
    """
    for i in asg_response['AutoScalingGroups']:
        for k in i['Instances']:
            instance_ids.append(k['InstanceId'])
    return instance_ids


def create_ami(instance_ids):
    """
    Create AMI for the specific Instance
    """
    for ec2_id in instance_ids:
        ec2_resp = ec2_client.create_image(InstanceId=ec2_id, NoReboot=True, Name="AMI-"+ec2_id)
        ami_id = ec2_resp['ImageId']
        print(f"AMI Creation started for ec2 instance {ec2_id}")
        print(f"New AMI Id {ami_id}")

if __name__ == "__main__":
    asg_resp = describe_asg()
    #print(asg_resp)
    ec2_id = get_ec2_id(asg_resp)
    print(ec2_id)
    #create_ami(ec2_id)