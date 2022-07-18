# Basic Linux Commands

* [The Linux Command Line](https://linuxcommand.org/index.php)
* [Description of directories](https://linuxcommand.org/lc3_lts0040.php)

## Package management

### Upgrading packages
```bash
# update apt repositories
sudo apt update

# view packages that can be upgraded
apt list --upgradable

# upgrade packages, does not upgrade dependencies ??
sudo apt upgrade

# upgrade packages, does upgrade dependencies ??
sudo apt full-upgrade

sudo apt dist-upgrade

# clean up upgrades
sudo apt autoremove
```

There may be notices saying packages have changed from "stable" (or something) to "old stable". Type "y" that you want to accept the changes.


### Installing and removing packages
```bash
# search for package
apt search {search term}

# show description of package
apt show {package name}

# install package
sudo apt install {package names}

# remove package
sudo apt remove {package name}
```

### Check to see if a package is installed
```bash
dpkg -l {package name}
# or
dpkg -l | grep {package name}
```

## Getting basic information
```bash
# display where command is located
which {command}

# display calendar of current month
cal

# display time and date
date

# display who is logged into your system
w
Who

# display username
whoami

# display hostname
hostname

# display ip address
hostname -I

# display network information
ifconfig
# or
ip address

# list system info
hostnamectl

# print working directory
pwd

# display environment variables
printenv

# display how long the system has been running
uptime

# display file systems and disk usage
df -h

# display free and used memory
free -h

# display hardware info
# not installed by default in raspbian
hwinfo

# check which Raspbian version you are currently running
cat /etc/os-release

# display processes
top

# display processes, cpu usage, memory usage
htop

# display users
cat /etc/passwd
```


## Foreground (fg) and background (bg)
```bash
# while in a program, send it to background
Ctrl+z

# put a program in background directly
{program name} &

# show all jobs running in background
jobs

# go to last job put in background
fg

# go to specific job in background
fg {job id}
```

## Getting help
```bash
# view man page for command
man {command}

# view one line description of command
whatis {command}

# view command cheat sheet on cht.sh
curl cht.sh/{command}

# built-in help
help -m {command}
```

## .bashrc file
Reload .bashrc file
```bash
source ~/.bashrc  # or
. ~/.bashrc
```

## Looking and Moving around
```bash
# display contents of directory
ls

# display contents of directory in long format
ls -l

# display contents of directory including hidden files
ls -a
ls -al

# display contents of directory in tree-like format
tree

# move to directory
cd {directory}

# move to home directory
cd
cd ~

# move to parent directory
cd ..

# move to root directory
cd /

# move to previous directory
cd -

# print working directory
pwd

# search for file in a directory
find {directory} -name {search pattern}

# search for all text files in current directory
find . -name "*.txt"
```

* `~` = home directory
* `.` = current directory
* `..` = parent directory
* tab completion

## File commands
```bash
# create new file
touch {file name}

# copy file
cp {/directory1/original_file} {/directory2/new_file}

# move file or rename file
mv {/directory1/original_file} {/directory2/new_file}

# delete file
rm {file}

# delete directory
rm -r {directory}

# forcibly delete directory
rm -rf {directory}

# create directory
mkdir {directory}

# display contents of a file
cat {file}

# display first 10 lines of a file
head {file}

# display last 10 lines of a file
tail {file}

# display 10 random lines of a file
shuf -n 10 {file}

# display line, word, and byte count of a file
wc

# display line count of a file
wc -l

# view file
less {file}

# display type of file
file {file}

# display lines in a file that match a pattern
grep {pattern} {file}
```

## Other
```bash
# print out text
echo "Hello"

# piping example
history | tail    # note, `tail history` does not work
history | grep apt
history | grep apt | wc -l
cat /etc/passwd | grep joe
```