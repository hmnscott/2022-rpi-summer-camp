# RPI Camp Syllabus

- [RPI Camp Syllabus](#rpi-camp-syllabus)
  - [Introduction to Raspberry Pi](#introduction-to-raspberry-pi)
    - [Updating software on the command line](#updating-software-on-the-command-line)
    - [Basic commands](#basic-commands)
    - [Creating files and directories](#creating-files-and-directories)
    - [Nano](#nano)
    - [Getting help on a command](#getting-help-on-a-command)
    - [Install cowsay, figlet, linuxlogo and add to .bashrc](#install-cowsay-figlet-linuxlogo-and-add-to-bashrc)
    - [Install htop, hwinfo, ncal](#install-htop-hwinfo-ncal)
    - [Install bsdgames](#install-bsdgames)
    - [Use the command line to solve Wordle](#use-the-command-line-to-solve-wordle)
    - [Add second user](#add-second-user)
    - [Change your password](#change-your-password)
  - [Linux](#linux)
    - [Create and add directory to PATH](#create-and-add-directory-to-path)
    - [Example python script](#example-python-script)
  - [Python](#python)
    - [Python challenges](#python-challenges)
    - [Python command line games](#python-command-line-games)
    - [Example games and game software](#example-games-and-game-software)
  - [Web Development](#web-development)
  - [Electronics](#electronics)
    - [Light LED with 9V battery](#light-led-with-9v-battery)
    - [Intruder alarm](#intruder-alarm)
    - [Blink LED with Raspberry Pi](#blink-led-with-raspberry-pi)
    - [Reaction Game](#reaction-game)

## Introduction to Raspberry Pi
* Short history of computers and Linux
* [How to install Raspbian](https://www.raspberrypi.com/software/)


### Updating software on the command line
```bash
# update repositories
sudo apt update

# upgrade installed software
sudo apt dist-upgrade
```

### Basic commands
```bash
cat
file

# find all text files in a directory
find . -name '*.txt'

less
```

### Creating files and directories
```shell
# create a directory called 'files'
mkdir files

# create a file called 'people.txt'
touch people.txt

# add text to file

# search for the name 'Mary' in the file
grep 'Mary' people.txt

# search for names that contain a 'P' in them
grep 'P' people.txt
```

### Nano
* [Linux Crash Course video on Nano](https://www.youtube.com/watch?v=DLeATFgGM-A)
* [Nano cheat sheet](https://www.nano-editor.org/dist/latest/cheatsheet.html)
* [It's FOSS - Nano cheat sheet](https://itsfoss.com/wp-content/uploads/2020/05/Nano-Cheat-Sheet.pdf)

```shell
# check to see if nano is installed
which nano

# open empty file
nano

# open a file called 'people.txt'
nano people.txt
```

* `^` = control key
* Save file with `^O`.
* Search within file with `^W`.
* Exit with `^X`.
* Cut line with `^K`.
* Paste line with `^U`.

### Getting help on a command
```shell
# example, getting help on `ls` command
man ls
whatis ls
curl cht.sh/ls
```

### Install cowsay, figlet, linuxlogo and add to .bashrc
```shell
# update
sudo apt update

# search for package
apt search cowsay
apt search figlet
apt search linuxlogo

# show description of package
apt show cowsay
apt show figlet
apt show linuxlogo

# install package
sudo apt install cowsay
sudo apt install figlet
sudo apt install linuxlogo

# check to see if packages are installed
which cowsay
which figlet

# try this
cowsay "hello $USER"
figlet "hello $USER"
linuxlogo -u

# list all available art types
cowsay -l

# try this
cowsay -f stegosaurus "hello"
```

Open .bashrc and add the following line at the end of file.
```
linuxlogo -u
cowsay "Hello"
```

Reload .bashrc file.
```shell
. ~/.bashrc
```

### Install htop, hwinfo, ncal
```bash
# check to see if packages are installed
which htop
which hwinfo
which ncal

# update repositories info
sudo apt update

# install packages if not already installed
sudo apt install htop
sudo apt install hwinfo
sudo apt install ncal

# try
cal 1752
```

### Install bsdgames
```shell
sudo apt update
apt search bsdgames
apt show bsdgames
sudo apt install bsdgames
```

### Use the command line to solve Wordle
[Solve Wordle using the Linux command line (web article)](https://opensource.com/article/22/1/word-game-linux-command-line#:~:text=Use%20the%20Linux%20grep%20and,favorite%20word%2Dbased%20guessing%20games.)

```shell
# copy all five letter words to a text file
grep '^[a-z][a-z][a-z][a-z][a-z]$' /usr/share/dict/words > words

# make a guess

# take out words that contain letters not in the word
grep -v '[cad]' words > words2

# save words that do contain a letter in the word
grep r words2 > words3

# search using letters in specific place or not in specific place
grep '..[^r].s' words3 > words4

# check number of lines in file
wc -l words4
```

### Add second user

### Change your password


## Linux
* Tab complete
* File and directory permissions
* Changing passwords
* User management
* Add second user

### Create and add directory to PATH
* Add local user bin directory
* Add path to local user bin directory

```shell
# create local user bin directory
mkdir ~/bin

# create script file in ~/bin

# make file executable 
chmod 755 {file name}  # or
chmod 700 {file name}

# add local user bin directory to path
# add this to .bash_rc
export PATH=$PATH:directory

# view path 
echo $PATH
```

### Example python script
Create a file.
```shell
touch ask_name.py
```

Add the following to the file.
```python
#!/usr/bin/env python3

name = input("Please enter your name: ")
print(f"Hello {name}")
```

Make the script executable and run the script.
```shell
chmod 755 ask_name.py
./ask_name.py
```

## Python
* Work through the Programming with Mosh cheat sheet

### Python challenges
* Write a program that asks a user for his or her name and greets the user.
* Write a function that multiplies two numbers that the user inputs.
* Write a program that adds all of the integers from 1 to 1000.
  * Try using a formula instead of brute force.
* Write a program that adds all of the integers from 1 to N. Let the user input N.
* Write a program that adds all multiples of 8 from 1 to 1000.
* Write a program that adds all multiples of 8 from 1 to N.
* Write a program that adds all multiples of a from 1 to N. Let the user input a and N.
* Write a program that prints out all numbers that are either multiples of 8 or multiples of 12 from 1 to 100.
* FizzBuzz challenge: Print integers from 1 to N. However, print "Fizz" if an integer is divisible by 3, print "Buzz" if an integer is divisible by 5, and print "FizzBuzz" if an integer is divisible by both 3 and 5.

```bash
# example output for fizzbuzz
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
```

* [First Project Euler challenge](https://projecteuler.net/problem=1)

### Python command line games
* [Guess the Number game](https://inventwithpython.com/invent4thed/chapter3.html)
* [Dragon Realm game](https://inventwithpython.com/invent4thed/chapter5.html)

* [Convert text to ascii art](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20)


### Example games and game software
* [80 Days](https://www.youtube.com/watch?v=D2CWdaJTikQ)
* [Ren'Py](https://www.renpy.org/) - visual novel game engine, uses python
* [Twine](https://twinery.org/)
* [Inky](https://www.inklestudios.com/ink/) - used to write 80 Days


## Web Development
* [Learn Web Development](https://developer.mozilla.org/en-US/docs/Learn)
* [w3schools](https://www.w3schools.com/)
* [Web Development Essentials](https://learning.lpi.org/en/learning-materials/030-100/)

## Electronics

### Light LED with 9V battery

From the book *Electronics for Kids* pg 78.


### Intruder alarm

From the book *Electronics for Kids* pg 11.


### Blink LED with Raspberry Pi

First project in Monk Makes kit.

### Reaction Game

Second chapter (pg 18) in the book *Simple Electronics with GPIO Zero*.