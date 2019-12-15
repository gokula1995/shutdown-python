import boto3

getInstances = boto3.client('ec2')

def stop_the_instances():
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
        print("This instances is going to shutdown: " + InstanceId)
        stop_ec2 = getInstances.stop_instances(
            InstanceIds=[
                InstanceId
            ]
        )
        instance_status=getInstances.describe_instances(
            InstanceIds=[
                InstanceId
            ]
        )
        print(stop_ec2)
        print(instance_status)

stop_the_instances();
