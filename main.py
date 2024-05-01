import random
import traceback
import webbrowser
import os
import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QObject, pyqtSignal, QThread
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QTextCursor
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from qt_material import apply_stylesheet

from finder import Gpt_finder  
from ui_mod import Ui_MainWindow  
from utils import get_proxy,read_yaml
root_path = os.path.dirname(os.path.realpath(__file__))


class Stream(QObject):
    newText = pyqtSignal(str)

    def write(self, text):
         self.newText.emit(str(text))

    def flush(self):
        pass

class Worker(QThread):
    finished = pyqtSignal(object)  # 可以根据需要发送不同类型的信号
    error = pyqtSignal(Exception)
    progress = pyqtSignal(int)  # 发射进度的信号

    def __init__(self, func, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        try:
            result = self.func(*self.args,**self.kwargs ,progress_callback=self.progress.emit)
            self.finished.emit(result)  # 任务完成后发出完成信号
        except Exception as e:
            self.error.emit(e)  # 发生错误时发出错误信号

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.gpt_finder = Gpt_finder()  # 创建 Gpt_finder 实例

        # 设置重定向输出
        self.stream = Stream(newText=self.onNewText)
        sys.stdout = self.stream

        # 连接 UI 控件事件
        self.pushButton.clicked.connect(self.run_search)
        self.pushButton_2.clicked.connect(self.download_papers)
        self.comboBox.currentIndexChanged.connect(self.change_model)
        self.comboBox_2.currentIndexChanged.connect(self.change_gpt_proxy)
        self.spinBox.valueChanged.connect(self.gpt_finder.set_year)
        self.spinBox_2.valueChanged.connect(self.gpt_finder.set_pages)
        self.checkBox_2.stateChanged.connect(self.toggle_use_ai)
        self.checkBox.stateChanged.connect(self.toggle_use_proxy)
        self.commandLinkButton.clicked.connect(self.open_website)

        # 其他初始设置
        self.gpt_finder.use_ai = self.checkBox_2.isChecked()
        self.gpt_finder.proxy = None
        self.gpt_finder.set_model(0)
        self.gpt_finder.set_year(1)
        self.gpt_finder.set_pages(10)
        self.gpt_finder.gpt_proxy = "https://api.surger.xyz/v1"


    def onNewText(self, text):
        self.textBrowser.moveCursor(QTextCursor.End)
        self.textBrowser.append(text)  # 在 QTextBrowser 控件中追加文本

    def toggle_use_ai(self, state):
        if state == Qt.Checked:
            self.gpt_finder.use_ai = True
            print("使用AI")
        else:
            self.gpt_finder.use_ai = False
            print("不使用AI")

    def toggle_use_proxy(self, state):
        if state == Qt.Checked:
            self.gpt_finder.proxy = get_proxy(random.choice([True,False]))
            print("已开启网络代理:",self.gpt_finder.proxy) 
        else:
            self.gpt_finder.proxy = False
            print("已关闭网络代理")

    def run_search(self):
        self.change_model()
        query = self.textEdit.toPlainText()  # 获取查询文本
        api_key = self.lineEdit_2.text()  # 获取 API Key
        self.progressBar.setValue(0)
        if "*****" in api_key:
            true_key = read_yaml(root_path+"/config.yaml")["api_key"]
        else:
            true_key = api_key
        QMessageBox.information(self, "查询状态", f"查询任务已开始，请稍候。\nAPI Key: {true_key} modle: {self.comboBox.currentText()}")
        self.worker = Worker(self.gpt_finder.find_reserch, query, true_key)
        self.worker.finished.connect(self.handle_search_result)
        self.worker.error.connect(self.handle_error)
        self.worker.progress.connect(self.progressBar.setValue)  # 更新进度条
        self.worker.finished.connect(self.update_table_view)
        self.worker.start()

    def handle_search_result(self, result):
        self.textBrowser.setText(str(result))

    def download_papers(self):
        self.progressBar.setValue(0)
        self.worker = Worker(self.gpt_finder.download_pdf)
        self.worker.finished.connect(self.handle_download_success)
        self.worker.error.connect(self.handle_error)
        self.worker.progress.connect(self.progressBar.setValue)  # 更新进度条
        self.worker.start()

    def handle_download_success(self):
        QMessageBox.information(self, "Success", "Papers downloaded successfully!")

    def handle_error(self, e):
        traceback.print_exc()
        QMessageBox.critical(self, "Error", str(e))

    def change_model(self):
        if self.comboBox.currentIndex()==5:
            self.gpt_finder.custom_model = self.lineEdit_4.text()
            print("已使用模型:",self.gpt_finder.custom_model)
        model = self.comboBox.currentIndex()
        self.gpt_finder.set_model(model)
        print("使用模型：",self.comboBox.currentText())
    
    def change_gpt_proxy(self):
        proxy_txt = self.lineEdit.text()
        idx = self.comboBox_2.currentIndex()
        if idx == 0:
            self.gpt_finder.gpt_proxy = False
        elif idx == 1:
            self.gpt_finder.proxy = "https://api.surger.xyz/v1"
        elif idx == 2:
            self.gpt_finder.proxy = proxy_txt
        else:
            self.gpt_finder.proxy = None
        print("模型代理:",self.gpt_finder.proxy)

    
    def load_excel_data(self, file_path):
        data = pd.read_excel(file_path)
        model = QStandardItemModel(4, data.shape[1]) 
        model.setHorizontalHeaderLabels(data.columns.tolist()) 

        # 遍历数据填充模型
        for row in range(4):
            for column in range(data.shape[1]):
                item = QStandardItem(str(data.iloc[row, column]))
                model.setItem(row, column, item)
        return model
    
    def update_table_view(self):
        self.setup_table_view_with_excel()

    def setup_table_view_with_excel(self):
        # 假设 Excel 文件路径已经定义
        model = self.load_excel_data(self.gpt_finder.excel_save_path)
        self.tableView.setModel(model)
        self.tableView.resizeColumnsToContents()
    
    def open_website(self):
        webbrowser.open('https://github.com/Becomingw/MedspiderPlus')

    def closeEvent(self, event):
        # 创建一个消息框，询问用户是否真的要关闭窗口
        reply = QMessageBox.question(self, '确认', '你确定要退出吗？',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            sys.stdout = sys.__stdout__  
            event.accept()  
        else:
            event.ignore()  

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    apply_stylesheet(app, theme='light_blue.xml')
    main_window.show()
    sys.exit(app.exec_())
