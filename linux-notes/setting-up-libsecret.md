# Setting up libsecret

```bash
# install libsecret
sudo apt install libsecret-1-0 libsecret-1-dev

# go to libsecret directory
cd /usr/share/doc/git/contrib/credential/libsecret/

# compile libsecret
sudo make

# configure git to use libsecret as credential helper
git config --global credential.helper /usr/share/doc/git/contrib/credential/libsecret/git-credential-libsecret
```