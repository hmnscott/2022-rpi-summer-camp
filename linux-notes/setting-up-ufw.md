# Setting up ufw

## Links
* [Setting up ufw](https://pimylifeup.com/raspberry-pi-ufw/)

## Commands
Set up ufw.
```bash
sudo apt update

sudo apt install ufw

sudo ufw enable

sudo ufw status
```

Set up ufw and allow ssh traffic.
```bash
sudo apt update
sudo apt full-upgrade

sudo apt install ufw

sudo ufw allow 22

sudo ufw limit 22

sudo ufw show added

sudo ufw enable

sudo ufw status
```