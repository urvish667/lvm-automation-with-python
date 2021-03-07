# lvm-automation-with-python
### This python script will help you do automate the Logical Volume Management
Let's see how it works. It has function called __check_available_disk()__ that will display the available disk on the system. Just this function and you will good to go.<br>
Now, Let go further inside it. I have created functions which will helps us to create __Physical Volumes__ and then it will create __Logical Groups__ with __Physical Volumes__<br>
__logical_group()__ functions helps to create __Logical Groups__. So, we just have to provide two arguments: __1. Number of devices, and 2. Name for Logical Group.__<br>
__partition()__ function helps to do partition in the group. It takes four arguments: __1. Size for partition (ex. 2G means 2GB), 2. Name for partition, 3. Name for Logical Volume, and 4. Folder name(mounted with)__ <br>
__extend_logical_group()__ function helps to extend the __Logical Groups__. It takes four arguments: __1. Number of Physical Volume, and 2. Logical Group name.__
