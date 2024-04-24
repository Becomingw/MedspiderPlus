# MedspiderPlus<img src="https://image-1307946721.cos.ap-shanghai.myqcloud.com/logo.png" alt="logo" style="zoom: 25%;" />

## 1.图示🧬：

<img src="https://image-1307946721.cos.ap-shanghai.myqcloud.com/20240424213005.png" style="zoom:33%;" />

## 2.简介📝：
简体中文 | [English](./README_en.md)

与[Medspider](https://github.com/Becomingw/Med-Spider)相似。该项目是一个基于Python的GUI（Tkinter）工具，旨在通过让ChatGPT提供的关键词，从PubMed数据库中检索相关文献并提供免费文献的PDF下载。相比自己给关键词（写正则表达式），ChatGPT更擅长这一任务，你要做的就是给它一个你想要了解的领域🤓！

相比Medspider **支持更多AI模型**：

- GPT3.5Turbo
- GPT4
- GeminPro
- ChatGLM4
- 自定义模型：其他通过oneapi进行转发的模型 及 OpneAI所有模型

**更美观的界面**：

使用PyQt5 开发，使用[qt_material](https://qt-material.readthedocs.io/en/latest/index.html)美化包，其实美化还有很大提升空间🤫。

**更流畅**：

在pyqt的加持下，加入了更合理的多线程，提升软件运行流畅程度🥳。

**更安全**：

提供了随机代理池与自定义代理（暂未加入），允许自行选择关闭或开启😌。

**更直观**：

从日志直接观察程序运行情况与参数设置情况，从表格预览直接查看表格的前4行的内容，不再需要打开excel文件确认情况。

**可下载更多文章**：

后续有时间将更新直接从出版商处下载文献（cookie法),。

目前已支持：AHA杂志社（大善人🤤，大部分期刊都是解锁的）

**去除所有翻译功能**：

后续有时间将利用MedSpider的表格做个大的，机翻不仅不能带来什么好处，还增加程序冗余与报错。如确实需要翻译，可到excel中一行公式直接翻译（具有问Bing🥱）

### 3.使用📇：

#### 3.1.安装：

**常规方法📔**

请提前安装`Python>=3.10`（建议如此）

1. 克隆该项目到本地

```bash
git clone https://github.com/Becomingw/MedSpiderPlus.git
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

**简易方法**📖：

下载release的Medspider+.7z文件，解压后，双击`run.vsb`即可运行。

#### 3.2.使用及注意事项：

1.操作顺序尽量遵循：填写研究内容-->设置搜索相关设置-->设置AI相关（先填写你需要填写的项目，后进行选择）--> 设置网络代理-->运行搜索-->下载文献；

2.研究内容的填写没啥特别的，只要你愿意，可以塞一段引言啥的进去，相比上一代能收的东西更宽泛。但是，容易产生0搜索，理论上使用GPT4效果会好于其他。如果你不想使用AI协助，**那你的填写内容应该为全英文的搜索正则**。(所以你也可以去弄个更好的检索词丢进这个里面😁)

3.没有搜索文献，不要点下载（保证有Medspider+.xlsx文件再进行下载）；

4.本程序所有产生的文件都是覆盖写，所以你懂的😊（该另存记得另存）；

5.网络代理的随机代理有时候不是很稳定，产生网络报错属于正常。如果你的文献数量不大，可以裸连下载。；

6.不建议大批量下载，本程序本质是一个爬虫，所以也你懂的😇。

### 4. 其他🧪：

1.程序的核心程序都在utils.py内，用户可以自行优化其中的Prompt，加入更多下载的程序等；

2.外观程序在main.py的最低端，可以自行切换喜欢的主题，支持的主题https://github.com/UN-GCPDS/qt-material

3.本程序的UI文件为Med.UI,可以自行丢进QtDesigner中重新设计，但是注意修改对应的main的内容。

4.其他就自行探索吧。

5.希望能有人:star:,以及PR









