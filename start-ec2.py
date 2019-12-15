import boto3

getInstances = boto3.client('ec2')

def start_the_instances():
    TaggedInstance = getInstances.describe_instances(
        Filters=[
            {
                'Name': 'tag:script',
                'Values': [
                    'givemerest'
                    ]
                }
            ]
        )

    instancelist = []
    for reservation in (TaggedInstance["Reservations"]):
        for instance in reservation["Instances"]:
            instancelist.append(instance["InstanceId"])

    for InstanceId in instancelist:
        print("This instances is going to start: " + InstanceId)
        start_ec2 = getInstances.start_instances(
            InstanceIds=[
                InstanceId
            ]
        )
        instance_status=getInstances.describe_instances(
            InstanceIds=[
                InstanceId
            ]
        )
        print(start_ec2)
        print(instance_status)

start_the_instances();
