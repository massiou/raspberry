#/bin/bash


# Update repos
sudo apt-get update
sudo apt-get install -y

# fstab mount
mounted_hdd = $(cat /etc/fstab | grep "/dev/sda1")
if [ echo ${mounted_hdd} == "" ]
then
    echo "Adding /dev/sda1 mounting point to fstab ..."
    sudo mkdir -p /mnt/disque_dur
    sudo echo "/dev/sda1 /mnt/HDD auto,nofail defaults" >> /dev/fstab
else
    echo "/dev/sda1 already mounted in fstab"
fi
