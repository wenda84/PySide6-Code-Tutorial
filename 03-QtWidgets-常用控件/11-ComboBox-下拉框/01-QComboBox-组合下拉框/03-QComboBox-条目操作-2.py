import sys

from PySide6 import QtWidgets

"""
QComboBox 条目操作
提供了非常多方法来创建、插入、获取条目

默认情况下不允许用户编辑条目，但可以设置允许。用户编辑的条目的插入方式由插入策略控制
.setEditable(editable: bool)
.isEditable() -> bool
.setEditText(text: str)

插入策略控制着当用户创建了新的条目时该如何插入，QComboBox.InsertPolicy详情见下文
.setInsertPolicy(policy: QComboBox.InsertPolicy)
.insertPolicy() -> QComboBox.InsertPolicy


QComboBox.InsertPolicy 枚举值具体有如下数种：
https://doc.qt.io/qt-6/qcombobox.html#InsertPolicy-enum
QComboBox.NoInsert                  字符串不会被插入到combobox中
QComboBox.InsertAtTop               作为首条插入
QComboBox.InsertAtCurrent           替换当前条目
QComboBox.InsertAtBottom            插入到最后一条目之后
QComboBox.InsertAfterCurrent        在当前条目之后插入
QComboBox.InsertBeforeCurrent       在当前条目之前插入
QComboBox.InsertAlphabetically      按字母表顺序插入字符串至combobox

通过控制minimumContentsLength属性，限制最少字符数（默认为0）
.setMinimumContentsLength(characters: int)
.minimumContentsLength() -> int

还可以控制combobox中条目的最大数量（默认值为有符号整形的上限）、在屏幕上显示的最大数量（默认为10）
.setMaxCount(max: int)
.maxCount() -> int
.setMaxVisibleItems(max_items: int)
.maxVisibleItems() -> int

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QComboBox-条目操作")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""

        cbb = QtWidgets.QComboBox(self)
        cbb.move(200, 200)
        cbb.resize(400, 60)
        cbb.addItems([str(i) for i in range(100, 110)])  # 通过列表推导式快速添加多个条目

        # 允许用户编辑条目
        cbb.setEditable(True)

        # 设置插入策略
        # cbb.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        # cbb.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        # cbb.setInsertPolicy(QtWidgets.QComboBox.InsertAtCurrent)
        cbb.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        # cbb.setInsertPolicy(QtWidgets.QComboBox.InsertAfterCurrent)
        # cbb.setInsertPolicy(QtWidgets.QComboBox.InsertBeforeCurrent)
        # cbb.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)

        # 设置可编辑文本
        cbb.setEditText("000")  # 将当前文本设置为00,而不影响其他条目

        # 限制最小字符数
        cbb.setMinimumContentsLength(3)

        # 限制最大条目数，达到12条后无法再添加
        cbb.setMaxCount(12)

        # 每次只能显示5条条目，更多条目需要滚动显示
        cbb.setMaxVisibleItems(5)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
