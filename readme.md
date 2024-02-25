
## 虚拟机环境配置

1. 安装VMWare宿主软件
2. 安装FileZilla（方便和宿主机交换文件）
3. 下载Ubtuntu18 镜像    
   x64架构  https://releases.ubuntu.com/jammy/ubuntu-22.04.4-live-server-amd64.iso  
   Arm架构 https://cdimage.ubuntu.com/releases/22.04/release/ubuntu-22.04.4-live-server-arm64.iso


**设置并启动虚拟机**

1. 新建虚拟机，选择「稍后安装系统」
2. 选择安装位置，记得新建文件夹再安装
3. 系统选择 `Linux - Ubuntu 64`
4. 在列表中点击刚才创建的虚拟机，点击「编辑虚拟机设置」
5. 选择DVD 驱动器，使用ISO文件，选择之前下载的ISO镜像
6. 将虚拟机开机
   
**新系统的设置**

虚拟机开机后，需要对系统进行设置

**生成SSH KEY**

终端中运行

```
ssh-keygen
```

生成的公钥文件位于 `.ssh/id_rsa.pub`

终端中运行

```
cat .ssh/id_rsa.pub
```

可以显示公钥内容

将公钥添加到Github的个人公钥列表中 https://github.com/settings/keys 

接着在终端中输入

```
git config --global user.name XTARZ
git config --global user.email i@xtarz.cn
```

其中，`XTARZ` 和 `i@xtarz.cn` 分别是Github的用户名和邮箱





## 克隆所需代码库

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
