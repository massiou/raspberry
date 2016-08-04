#/bin/sh


# Update repos
sudo apt-get update
sudo apt-get install -y

# fstab mount
mounted_hdd=$(cat /etc/fstab | grep -o "^/dev/sda1")
mounting_point="/mnt/HDD"
if [ -z ${mounted_hdd}  ]
then
    echo "Adding /dev/sda1 mounting point to fstab ..."
    sudo mkdir -p ${mounting_point}
    sudo echo "/dev/sda1 ${mounting_point} auto,nofail defaults" >> /etc/fstab
else
    echo "/dev/sda1 already mounted in fstab"
fi
