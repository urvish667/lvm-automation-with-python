#lvm-automation
#importing libraries
import os
import subprocess as sp
import paramiko as pm

#check available drives
def check_available_disk():
	status, output = sp.getstatusoutput("lsblk")
	if status == 0:
		print(output)
	else:
		print("[x] Something went wrong!!")

#creating physical volumes
def logical_group(number, lv_name):
	cmd = "vgcreate "+lv_name
	for i in range(number):
		print("Enter device {0}: ".format(i+1), end="")
		drive = input()
		drive = "/dev/"+drive
		status, output = sp.getstatusoutput("pvcreate {0}".format(drive))
		if status != 0:
			print("[x] Enable to convert {0} to physical volume".format(drive))
		else:
			cmd+=(" "+drive)
		
	#creating logical volumes
	status, output = sp.getstatusoutput(cmd)
	if(status == 0):
		print("[✔] Logical volume has been created")
	else:
		print("[x] Unable to create logical volume!!")
		print(output)
		print()
		
#creates partitions
def partition(par_size, par_name, lv_name, folder_name):
	status, output = sp.getstatusoutput("lvcreate --size +{0} --name  {1} {2}".format(par_size, par_name, lv_name))
	if status != 0:
		print("[x] Unable to create partition!!")
		print(output)
		exit()
	else:
		print("[✔] Partition has been created")
	
	status, output = sp.getstatusoutput("mkfs.ext4 /dev/{0}/{1}".format(lv_name, par_name))
	if(status != 0):
		print("[x] Unable to formate drive!!")
		print(output)
		exit()
	else:
		print("[✔] Volume has been formatted")

	status, output = sp.getstatusoutput("mkdir /root/{0}".format(folder_name))
	if(status != 0):
		print("[x] Unable to create directory!!")
		print(output)
		exit()
	else:
		print("[✔] Directory has been created")
	
	status, output = sp.getstatusoutput("mount /dev/{0}/{1} /root/{2}".format(lv_name, par_name, folder_name))
	if(status != 0):
		print("[x] Unable to mount volume to directory!!")
		print(output)
		exit()
	else:
		print("[✔] Volume has been mounted to folder")	


#Add new physical drive to the existing group
def extend_logical_group(number, lv_name):
	cmd = "vgextend "+lv_name
	for i in range(number):
		print("Enter device {0}: ".format(i+1), end="")
		drive = input()
		drive = "/dev/"+drive
		status, output = sp.getstatusoutput("pvcreate {0}".format(drive))
		if status != 0:
			print("[x] Enable to convert {0} to physical volume".format(drive))
		else:
			cmd+=(" "+drive)
	
	status, output = sp.getstatusoutput(cmd)
	if(status == 0):
		print("[✔] Logical volume has been created")
	else:
		print("[x] Unable to create logical volume!!")
		print(output)
		print()
