# 📦 Infra Lab – Full Installation Guide (Ubuntu 22.04)

## 1️⃣ Update System

sudo apt update && sudo apt upgrade -y

---

## 2️⃣ Install Virtualization (KVM + Libvirt)

sudo apt install -y \
  qemu-kvm \
  libvirt-daemon-system \
  libvirt-clients \
  bridge-utils \
  virtinst \
  libvirt-dev \
  build-essential

sudo systemctl enable --now libvirtd
sudo usermod -aG libvirt,kvm $USER

# IMPORTANT: logout/login or reboot after this step

---

## 3️⃣ Install Vagrant (Official Package)

wget https://releases.hashicorp.com/vagrant/2.4.1/vagrant_2.4.1-1_amd64.deb
sudo apt install -y ./vagrant_2.4.1-1_amd64.deb

vagrant --version

---

## 4️⃣ Install Vagrant Libvirt Plugin

vagrant plugin install vagrant-libvirt
vagrant plugin list

---

## 5️⃣ Download Ubuntu 22.04 Vagrant Box

vagrant box add generic/ubuntu2204
vagrant box list

---

## 6️⃣ Create Lab Folder

mkdir -p ~/infra-lab
cd ~/infra-lab

touch Vagrantfile template.env .env
echo ".env" >> .gitignore

---

## 7️⃣ Start Lab

vagrant up --provider=libvirt

---

## 8️⃣ Useful Commands

# SSH into node
vagrant ssh node1

# Stop all VMs (frees RAM)
vagrant halt

# Destroy lab (full rebuild)
vagrant destroy -f

---

## Notes

• Boxes are stored in ~/.vagrant.d/boxes/
• The box is downloaded only once
• When VMs are halted, RAM is freed
• Reboot required after adding user to libvirt/kvm group
