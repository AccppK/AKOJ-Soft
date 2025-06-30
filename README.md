<center><h1>AKOJ-Soft，快速、免费的创建你的下载站</h1></center>
## 部署方式
<s>先点这个![image](https://github.com/user-attachments/assets/35d36b1d-09a9-499b-a442-3b426b085379)
</s>
### 使用 Github Pages
在您的本地运行“git clone https://github.com/AccppK/AKOJ.git”，克隆本仓库。
找到“soft”文件夹，将您需要上传的文件放入其文件夹。
在克隆的文件夹中，运行"python js.py"，前提是您的系统应当安装了Python，如果没有请前往官网下载最新版的python。
运行完后，您应当看到处理的项目个数回馈，在当前目录下，将生成software.json文件。
在Github创建一个新的仓库，并且配置好Git连接。
确保一切就绪（连接到你的仓库），使用git命令上传文件到您的仓库：
```bash
git add .
git push
```
然后点击Settings，左边栏点击“Pages”，在Branch配置中，从None更改为main，文件夹改为/(root)，点击Save，等待2分钟后，刷新即可看见下载库。
您也可以在“Custom domain”配置您的域名。
