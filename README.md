# MedspiderPlus<img src="https://image-1307946721.cos.ap-shanghai.myqcloud.com/logo.png" alt="logo" width=39;/>

## 1.图示🧬：

<img src="https://image-1307946721.cos.ap-shanghai.myqcloud.com/20240424213005.png" width=200 />

#### 更新：
2024.5.1 
- 使用更便捷的方式添加cookie法下载，添加cookie池功能；
- 添加sichub下载池（sci-hub.st、scihub.se）；
- 添加yaml配置文件，更轻易的配置默认配置（不用再每次启动都要再输一次apikey了🧐）；
- 添加kimi模型，并优化了所有模型的Prompt，出关键词更准确，更稳定。

2024.5.16
- 提供简易启动包（仅支持Windows）
- 修复一些已知BUG，优化逻辑结构
- 加入nature communication、European Radiology下载工具（各提供了一个cookie，过期后需要自行到浏览器获取，获取方式网上搜索）
- 允许自定义设置excel保存地址，允许自定义设置PDF保存地址

## 2.简介📝：
简体中文 | [English](./README_en.md)

**如果本程序对你有帮助，请给我一个免费的star🤗。**

与[Medspider](https://github.com/Becomingw/Med-Spider)相似。该项目是一个基于Python的GUI（Tkinter）工具，旨在通过让ChatGPT提供的关键词，从PubMed文献数据库中检索相关文献并提供免费文献的PDF下载。相比自己写检索关键词（写正则表达式），ChatGPT更擅长这一任务，你要做的就是给它一个你想要了解的领域🤓！

相比Medspider **支持更多AI模型**：

- GPT3.5Turbo
- GPT4
- GeminPro
- ChatGLM4
- Kimi
- 自定义模型及代理：其他通过oneapi进行转发的模型 及 OpneAI所有模型

**更美观的界面**：

使用PyQt5 开发，使用[qt_material](https://qt-material.readthedocs.io/en/latest/index.html)美化包，其实美化还有很大提升空间🤫。

**更流畅**：

在pyqt的加持下，加入了更合理的多线程，提升软件运行流畅程度🥳。

**更安全**：

提供了随机代理池与自定义代理（暂未加入），允许自行选择关闭或开启😌。

**更直观**：

从日志直接观察程序运行情况与参数设置情况，从表格预览直接查看表格的前4行的内容，不再需要打开excel文件确认情况。

**可下载更多文章**：

后续有时间将更新各出版社OA文献下载插件。

目前已支持：AHA（Stroke）、Nature Commmunication、 European Radiology

**去除所有翻译功能**：

后续有时间将利用MedSpider的表格做个大的，机翻不仅不能带来什么好处，还增加程序冗余与报错。

### 3.使用📇：

#### 3.1.安装：

**常规方法📔**

请提前安装`Python>=3.10`（建议如此）

1. 克隆该项目到本地

```bash
git clone https://github.com/Becomingw/MedspiderPlus.git
cd  MedspiderPlus
```

 2.安装依赖项

```bash
pip install -r requirements.txt #-i https://pypi.tuna.tsinghua.edu.cn/simple（国内用户可选）
```

 3.运行程序

```bash
python main.py
```

**简易方法**📖(推荐)：

下载[Release](https://github.com/Becomingw/MedspiderPlus/releases/tag/1.0)的网盘MedspiderPlus.zip文件（提供百度云与谷歌网盘下载），解压后，点击`Medspider.exe`即可运行，相关源码也同时包含在压缩文件夹内。exe文件由bat文件编译而来，可选择自行编译。

ps:未针对海外用户进行优化，如果出现报错，请自行解决🤗。

#### 3.2.使用及注意事项：

1.操作顺序尽量遵循：填写研究内容-->设置搜索相关设置-->设置AI相关（先填写你需要填写的项目，后进行选择）--> 设置网络代理-->运行搜索-->下载文献；

2.研究内容的填写没啥特别的，只要你愿意，可以塞一段引言啥的进去，相比上一代能收的东西更宽泛。但是，容易产生0搜索，理论上使用GPT4效果会好于其他。如果你不想使用AI协助，**那你的填写内容应该为全英文的搜索正则**。(所以你也可以去弄个更好的检索词丢进这个里面😁)

3.没有搜索文献，不要点下载（保证有Medspider+.xlsx文件再进行下载）；

4.本程序所有产生的文件都是覆盖写，所以你懂的😊（该另存记得另存）；

5.网络代理的随机代理有时候不是很稳定，产生网络报错属于正常。如果你的文献数量不大，可以裸连下载。；

6.不建议大批量下载，本程序本质是一个爬虫，所以也你懂的😇。

7.~~cookie.txt 内格式应符合json格式~~，现已整合进入`config.yaml`，你的excel保存地址，pdf保存地址都在yaml文件中设置这设置。
- 格式示例： excel_save_folder: E:\Medspider+ (冒号不可少，冒号前的内容不可更改，冒号后有一空格)

8.程序AI部分代理主要接入了来自DeepAIR深影的[GratAPI](https://api.surger.xyz)🎟️，一个基于OneAPI的免费代理。

9.程序的AI部分核心依赖于Openai库(不能使用最新版)，请一定按照`requirements.txt`中的依赖进行配置。

10.由于程序UI为响应式，因此运行时，窗口可能过小，导致部分功能被隐藏，请自行调整窗口大小。

### 4. 其他🧪：

1.程序的核心程序都在utils.py内，用户可以自行优化其中的Prompt，加入更多下载的程序等：
 - 1.1 下载程序现允许插件化加入， 你需要做的就是提供一个能从doi下载pdf的“方法”，并将它放入`cookie_download.py` 中.
 - 1.2 在`utils.py`文件开头设置你的下载程序对应的tag和程序名，具体见`utils.py`文件内的注释。
 - 每添加一个下载程序记得在`config.yaml`中设定对应的cookie,即使你的下载不需要cookie。

2.程序的UI文件为Med.UI,可以自行丢进QtDesigner中重新设计，但是注意修改对应的main的内容。

3.Enjoy it🥳。


### 5.免费程序，请不要用于商业或非法用途😁







