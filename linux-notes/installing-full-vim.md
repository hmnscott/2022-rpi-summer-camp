# Install Full Vim

1. View list of enabled and disabled features of currently installed version of vim.
```bash
$ vi --version # or
$ vim --version
```

2. Remove default installation of vim, vim-tiny.
```bash
$ sudo apt remove vim-tiny # or
$ sudo apt remove --assume-yes vim-tiny
```

3. Update apt's package list.
```bash
$ sudo apt update
```

4. Install full version of vim.
```bash
$ sudo apt install vim # or
$ sudo apt install --assume-yes vim
```

5. Check if package successfully installed.
```bash
$ vim --version
```
