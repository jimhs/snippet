[gitlab.install.deb](https://about.gitlab.com/installation/#debian)
[gitlab.https](https://docs.gitlab.com/omnibus/settings/nginx.html#enable-https)
```bash
sudo apt-get update # v
sudo apt-get install -y curl openssh-server ca-certificates # v
sudo apt-get install -y postfix # v
curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.deb.sh | sudo bash # v
sudo EXTERNAL_URL="http://gitlab.example.com" apt-get install gitlab-ee # x
```