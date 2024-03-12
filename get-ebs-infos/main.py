import subprocess
import json
import xlsxwriter

command = "aws ec2 describe-volumes"
result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE)
volumes = json.loads(result.stdout)

instance_states = {}

instance_names = {}

command = "aws ec2 describe-instances"
result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE)
instances = json.loads(result.stdout)

for reservation in instances["Reservations"]:
    for instance in reservation["Instances"]:
        instance_id = instance["InstanceId"]
        instance_state = instance["State"]["Name"]
        instance_states[instance_id] = instance_state
        
        for tag in instance.get("Tags", []):
            if tag["Key"] == "Name":
                instance_names[instance_id] = tag["Value"]

workbook = xlsxwriter.Workbook('ebs_info.xlsx')
worksheet = workbook.add_worksheet()

columns = ["Tag Name", "Volume ID", "Instance ID", "EC2 State", "EC2 Tag Name", "Volume State", "Encryption", "KMS Key ID", "KMS Key Alias"]
for col_num, col_name in enumerate(columns):
    worksheet.write(0, col_num, col_name)

row = 1
for volume in volumes["Volumes"]:
    volume_id = volume["VolumeId"]
    volume_state = volume["State"]
    encrypted = volume["Encrypted"]
    kms_key_id = volume.get("KmsKeyId", "")
    instance_id = volume.get("Attachments", [{}])[0].get("InstanceId", "")
    ec2_state = instance_states.get(instance_id, "")
    ec2_tag_name = instance_names.get(instance_id, "")
    
    if kms_key_id:
        command = f"aws kms list-aliases --key-id {kms_key_id}"
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE)
        aliases = json.loads(result.stdout).get("Aliases", [])
        kms_key_alias = aliases[0]["AliasName"] if aliases else ""
    else:
        kms_key_alias = ""
    
    tag_name = ""
    for tag in volume.get("Tags", []):
        if tag["Key"] == "Name":
            tag_name = tag["Value"]
            break

    worksheet.write(row, 0, tag_name)
    worksheet.write(row, 1, volume_id)
    worksheet.write(row, 2, instance_id)
    worksheet.write(row, 3, ec2_state)
    worksheet.write(row, 4, ec2_tag_name)
    worksheet.write(row, 5, volume_state)
    worksheet.write(row, 6, encrypted)
    worksheet.write(row, 7, kms_key_id)
    worksheet.write(row, 8, kms_key_alias)
    row += 1

workbook.close()
