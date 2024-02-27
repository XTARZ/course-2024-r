
## 虚拟机环境配置

1. 安装VMWare宿主软件
2. 安装FileZilla（方便和宿主机交换文件）
3. 下载Ubtuntu18 镜像    
   x64架构  https://releases.ubuntu.com/jammy/ubuntu-22.04.4-live-server-amd64.iso  
   Arm架构 https://cdimage.ubuntu.com/releases/22.04/release/ubuntu-22.04.4-live-server-arm64.iso


### 设置并启动虚拟机

1. 新建虚拟机，选择「稍后安装系统」
2. 选择安装位置，记得新建文件夹再安装
3. 系统选择 `Linux - Ubuntu 64`
4. 在列表中点击刚才创建的虚拟机，点击「编辑虚拟机设置」
5. 选择DVD 驱动器，使用ISO文件，选择之前下载的ISO镜像
6. 将虚拟机开机
   
### 新系统的设置

虚拟机开机后，需要对系统进行设置

> 以下内容针对不同网络环境需要进行自行斟酌

#### `Ubuntu` 使用清华镜像源
https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/

#### `Conda` 使用清华镜像源
https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/

#### `pip` 使用清华镜像源
https://mirrors.tuna.tsinghua.edu.cn/help/pypi/


### 安装 R

```bash
# update indices
sudo apt update -qq
# install two helper packages we need
sudo apt install --no-install-recommends software-properties-common dirmngr
# add the signing key (by Michael Rutter) for these repos
# To verify key, run gpg --show-keys /etc/apt/trusted.gpg.d/cran_ubuntu_key.asc 
# Fingerprint: E298A3A825C0D65DFD57CBB651716619E084DAB9
wget -qO- https://cloud.r-project.org/bin/linux/ubuntu/marutter_pubkey.asc | sudo tee -a /etc/apt/trusted.gpg.d/cran_ubuntu_key.asc
# add the R 4.0 repo from CRAN -- adjust 'focal' to 'groovy' or 'bionic' as needed
sudo add-apt-repository "deb https://cloud.r-project.org/bin/linux/ubuntu $(lsb_release -cs)-cran40/"
```

```bash
sudo apt install --no-install-recommends r-base
```

### 安装 Anaconda（Miniconda）

官方仓库 https://repo.anaconda.com/  
清华镜像 https://mirrors.tuna.tsinghua.edu.cn/anaconda/

根据自己的需求下载安装程序，然后以当前用户运行
```bash
bash installer_name.sh # 这里是刚刚下载的安装包文件名
```

### 生成 SSH KEY

终端中运行

```bash
# 默认使用 RSA 算法密钥
ssh-keygen

# 也可以使用更强大简洁的 ED25519 算法，但某些旧系统（openSSH <6.5 ）可能不支持
ssh-keygen -t ed25519
```
回答安装程序提出的几个问题，没有特殊需求一般保持默认。  
生成的公钥文件位于 `.ssh/id_rsa.pub`
> 实际生成的文件默认以 `id_algorithm.pub` 命名，如果使用 `ed25519` 则会命名为 `id_ed25519.pub`

终端中运行

```bash
cat .ssh/id_rsa.pub
```

可以显示公钥内容

将公钥添加到Github的个人公钥列表中 https://github.com/settings/keys 

接着在终端中输入

```bash
git config --global user.name XTARZ
git config --global user.email i@xtarz.cn
```

其中，`XTARZ` 和 `i@xtarz.cn` 分别是 Github 的用户名和邮箱




### 克隆所需代码库

记得使用ssh连接地址



## Linux 常用指令

```bash
cd #（change directory）更改目录
   # cd <dir-name>

mkdir # 创建目录
     # mkdir <dir-name>
touch # 创建文件，Windows下使用 ni
cp # 复制文件
   # cp <source> <target>
mv # 移动（重命名）文件
   # mv <source> <target>
rm # 删除文件
ls # 显示当前目录下的文件
```

Linux 常用目录

```bash
cd / #根目录
cd ~ #家目录（主目录）
cd . #当前目录
cd .. # 上层目录
```
