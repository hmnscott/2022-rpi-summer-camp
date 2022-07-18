# Linux Crash Course - Managing Users

[Managing Users (Learn Linux Crash Course video)](https://www.youtube.com/watch?v=19WOD84JFxA)

```shell
# adds user without home directory on some distros
sudo useradd {username}

ls -l /home

cat /etc/passwd

cat /etc/passwd | wc -l

cat /etc/default/useradd

sudo userdel {username}

# add user with home directory
sudo useradd -m {username}

# remove user and home directory
sudo userdel -r {username}

# change password for current user
passwd

# change password for another user
sudo passwd {username}

# create system user
sudo useradd -r {system username}

# display password file
# must use sudo
sudo cat /etc/shadow
```