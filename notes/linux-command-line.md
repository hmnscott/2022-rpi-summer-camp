# Notes on the Linux Command Line

## The Care and Feeding of Your Raspberry Pi

Use the following commands to upgrade installed packages.

**Attention.** There may be notices saying packages have changed from "stable" (or something) to "old stable". Type "y" to accept the changes.

```
# Update package information
sudo apt update

# Install available upgrades
sudo apt upgrade
```

Some packages will be held back during an upgrade due to a change in the package's dependencies. To update these packages use the following command.
```
sudo apt dist-upgrade
```

To clean up install
```
sudo apt autoremove
```


Check which Raspbian version you are currently running.
```
cat /etc/os-release
```

