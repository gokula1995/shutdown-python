import boto3
import sys


autoScalingGroupName = str(sys.argv[1])
aws_profile = str(sys.argv[2])
min_size = str(sys.argv[3])
desired_capacity = str(sys.argv[4])



print ("The Auto Scaling Group Name is : " + autoScalingGroupName)
print (" Profile is pointing to "+ aws_profile+ "Account" )
print ("The Minimum Instances to be run : " + min_size)
print ("The Desired instances to be run "+ desired_capacity)

#Selecting the Profile
profile = boto3.Session(profile_name=aws_profile)

autoScalingResponse = profile.client('autoscaling')

def autoScalingGroup():
    Response = autoScalingResponse.describe_auto_scaling_groups(
        AutoScalingGroupNames=[autoScalingGroupName]
        )
    desiredCapacity = Response['AutoScalingGroups'][0]['DesiredCapacity']
    maxInstances = Response['AutoScalingGroups'][0]['MaxSize']
    minInstances = Response['AutoScalingGroups'][0]['MinSize']
    return Response,desiredCapacity,maxInstances,minInstances

currentAutoScalingGroupDetails = autoScalingGroup()

print ("Current Desired Count is : " + str(currentAutoScalingGroupDetails[1]))
print ("Current Max Size is : " + str(currentAutoScalingGroupDetails[2]))
print ("Current Min Size is : " + str(currentAutoScalingGroupDetails[3]))

updateAutoScalingGroup = autoScalingResponse.update_auto_scaling_group(
    AutoScalingGroupName=autoScalingGroupName,
    MinSize=min_size,
    MaxSize=4,
    DesiredCapacity=desired_capacity
)

updatedAutoScalingGroupDetails = autoScalingGroup()

print ("Updated Desired Count is : " + str(updatedAutoScalingGroupDetails[1]))
print ("Updated Max Size is : " + str(updatedAutoScalingGroupDetails[2]))
print ("Updated Min Size is : " + str(updatedAutoScalingGroupDetails[3]))
