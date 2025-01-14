# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'group_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GroupInterface(object):
    def setupUi(self, GroupInterface):
        GroupInterface.setObjectName("GroupInterface")
        GroupInterface.resize(1066, 813)
        self.verticalLayout = QtWidgets.QVBoxLayout(GroupInterface)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(966, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.TitleLabel = TitleLabel(GroupInterface)
        self.TitleLabel.setProperty("pixelFontSize", 50)
        self.TitleLabel.setObjectName("TitleLabel")
        self.horizontalLayout.addWidget(self.TitleLabel)
        self.groupThemeButton = ToolButton(GroupInterface)
        self.groupThemeButton.setObjectName("groupThemeButton")
        self.horizontalLayout.addWidget(self.groupThemeButton)
        self.GitHubButton = ToolButton(GroupInterface)
        self.GitHubButton.setObjectName("GitHubButton")
        self.horizontalLayout.addWidget(self.GitHubButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.SimpleCardWidget = SimpleCardWidget(GroupInterface)
        self.SimpleCardWidget.setMinimumSize(QtCore.QSize(300, 0))
        self.SimpleCardWidget.setObjectName("SimpleCardWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.SimpleCardWidget)
        self.verticalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 5, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.SearchLineEdit = SearchLineEdit(self.SimpleCardWidget)
        self.SearchLineEdit.setObjectName("SearchLineEdit")
        self.horizontalLayout_4.addWidget(self.SearchLineEdit)
        self.createButton = ToolButton(self.SimpleCardWidget)
        self.createButton.setMinimumSize(QtCore.QSize(32, 32))
        self.createButton.setObjectName("createButton")
        self.horizontalLayout_4.addWidget(self.createButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.listWidget = ListWidget(self.SimpleCardWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.horizontalLayout_3.addWidget(self.SimpleCardWidget)
        self.SimpleCardWidget_2 = SimpleCardWidget(GroupInterface)
        self.SimpleCardWidget_2.setObjectName("SimpleCardWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.SimpleCardWidget_2)
        self.verticalLayout_4.setContentsMargins(-1, 2, 2, 2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.SimpleCardWidget_2)
        self.stackedWidget.setObjectName("stackedWidget")
        self.defaultPage = QtWidgets.QWidget()
        self.defaultPage.setObjectName("defaultPage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.defaultPage)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.LargeTitleLabel = LargeTitleLabel(self.defaultPage)
        self.LargeTitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LargeTitleLabel.setObjectName("LargeTitleLabel")
        self.verticalLayout_3.addWidget(self.LargeTitleLabel)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem2)
        self.createGroupButton = PrimaryPushButton(self.defaultPage)
        self.createGroupButton.setObjectName("createGroupButton")
        self.horizontalLayout_20.addWidget(self.createGroupButton)
        self.BodyLabel_3 = BodyLabel(self.defaultPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BodyLabel_3.sizePolicy().hasHeightForWidth())
        self.BodyLabel_3.setSizePolicy(sizePolicy)
        self.BodyLabel_3.setAlignment(QtCore.Qt.AlignCenter)
        self.BodyLabel_3.setObjectName("BodyLabel_3")
        self.horizontalLayout_20.addWidget(self.BodyLabel_3)
        self.joinByCodeButton = PrimaryPushButton(self.defaultPage)
        self.joinByCodeButton.setObjectName("joinByCodeButton")
        self.horizontalLayout_20.addWidget(self.joinByCodeButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_20)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.stackedWidget.addWidget(self.defaultPage)
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page1)
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.nameLabel = TitleLabel(self.page1)
        self.nameLabel.setObjectName("nameLabel")
        self.verticalLayout_6.addWidget(self.nameLabel)
        self.SimpleCardWidget_3 = SimpleCardWidget(self.page1)
        self.SimpleCardWidget_3.setMinimumSize(QtCore.QSize(0, 20))
        self.SimpleCardWidget_3.setObjectName("SimpleCardWidget_3")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.SimpleCardWidget_3)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, 2, -1, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.SubtitleLabel_6 = SubtitleLabel(self.SimpleCardWidget_3)
        self.SubtitleLabel_6.setObjectName("SubtitleLabel_6")
        self.horizontalLayout_9.addWidget(self.SubtitleLabel_6)
        self.announEditButton = ToolButton(self.SimpleCardWidget_3)
        self.announEditButton.setObjectName("announEditButton")
        self.horizontalLayout_9.addWidget(self.announEditButton)
        self.verticalLayout_12.addLayout(self.horizontalLayout_9)
        self.announcementLabel = CaptionLabel(self.SimpleCardWidget_3)
        self.announcementLabel.setObjectName("announcementLabel")
        self.verticalLayout_12.addWidget(self.announcementLabel)
        self.verticalLayout_6.addWidget(self.SimpleCardWidget_3)
        self.ElevatedCardWidget = ElevatedCardWidget(self.page1)
        self.ElevatedCardWidget.setObjectName("ElevatedCardWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.ElevatedCardWidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 3, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.IconWidget = IconWidget(self.ElevatedCardWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IconWidget.sizePolicy().hasHeightForWidth())
        self.IconWidget.setSizePolicy(sizePolicy)
        self.IconWidget.setMinimumSize(QtCore.QSize(80, 80))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("health_tracker/health_app_pyqt/resource/images/icon/step.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.IconWidget.setIcon(icon)
        self.IconWidget.setObjectName("IconWidget")
        self.horizontalLayout_6.addWidget(self.IconWidget)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.SubtitleLabel = SubtitleLabel(self.ElevatedCardWidget)
        self.SubtitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SubtitleLabel.setObjectName("SubtitleLabel")
        self.verticalLayout_7.addWidget(self.SubtitleLabel)
        self.BodyLabel = BodyLabel(self.ElevatedCardWidget)
        self.BodyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BodyLabel.setObjectName("BodyLabel")
        self.verticalLayout_7.addWidget(self.BodyLabel)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 3, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.IconWidget_4 = IconWidget(self.ElevatedCardWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IconWidget_4.sizePolicy().hasHeightForWidth())
        self.IconWidget_4.setSizePolicy(sizePolicy)
        self.IconWidget_4.setMinimumSize(QtCore.QSize(80, 80))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("health_tracker/health_app_pyqt/resource/images/icon/chronometer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.IconWidget_4.setIcon(icon1)
        self.IconWidget_4.setObjectName("IconWidget_4")
        self.horizontalLayout_7.addWidget(self.IconWidget_4)
        self.verticalLayout_10.addLayout(self.horizontalLayout_7)
        self.SubtitleLabel_4 = SubtitleLabel(self.ElevatedCardWidget)
        self.SubtitleLabel_4.setAlignment(QtCore.Qt.AlignCenter)
        self.SubtitleLabel_4.setObjectName("SubtitleLabel_4")
        self.verticalLayout_10.addWidget(self.SubtitleLabel_4)
        self.BodyLabel_4 = BodyLabel(self.ElevatedCardWidget)
        self.BodyLabel_4.setAlignment(QtCore.Qt.AlignCenter)
        self.BodyLabel_4.setObjectName("BodyLabel_4")
        self.verticalLayout_10.addWidget(self.BodyLabel_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, 3, -1, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.IconWidget_5 = IconWidget(self.ElevatedCardWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IconWidget_5.sizePolicy().hasHeightForWidth())
        self.IconWidget_5.setSizePolicy(sizePolicy)
        self.IconWidget_5.setMinimumSize(QtCore.QSize(80, 80))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("health_tracker/health_app_pyqt/resource/images/icon/calories.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.IconWidget_5.setIcon(icon2)
        self.IconWidget_5.setObjectName("IconWidget_5")
        self.horizontalLayout_8.addWidget(self.IconWidget_5)
        self.verticalLayout_11.addLayout(self.horizontalLayout_8)
        self.SubtitleLabel_5 = SubtitleLabel(self.ElevatedCardWidget)
        self.SubtitleLabel_5.setAlignment(QtCore.Qt.AlignCenter)
        self.SubtitleLabel_5.setObjectName("SubtitleLabel_5")
        self.verticalLayout_11.addWidget(self.SubtitleLabel_5)
        self.BodyLabel_5 = BodyLabel(self.ElevatedCardWidget)
        self.BodyLabel_5.setAlignment(QtCore.Qt.AlignCenter)
        self.BodyLabel_5.setObjectName("BodyLabel_5")
        self.verticalLayout_11.addWidget(self.BodyLabel_5)
        self.horizontalLayout_5.addLayout(self.verticalLayout_11)
        self.verticalLayout_6.addWidget(self.ElevatedCardWidget)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.cardWidget = CardWidget(self.page1)
        self.cardWidget.setMinimumSize(QtCore.QSize(250, 0))
        self.cardWidget.setObjectName("cardWidget")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.cardWidget)
        self.verticalLayout_13.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.StrongBodyLabel = StrongBodyLabel(self.cardWidget)
        self.StrongBodyLabel.setObjectName("StrongBodyLabel")
        self.verticalLayout_13.addWidget(self.StrongBodyLabel)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.IconWidget_6 = IconWidget(self.cardWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IconWidget_6.sizePolicy().hasHeightForWidth())
        self.IconWidget_6.setSizePolicy(sizePolicy)
        self.IconWidget_6.setMinimumSize(QtCore.QSize(30, 30))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("health_tracker/health_app_pyqt/resource/images/profile/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.IconWidget_6.setIcon(icon3)
        self.IconWidget_6.setObjectName("IconWidget_6")
        self.verticalLayout_14.addWidget(self.IconWidget_6)
        self.CaptionLabel = CaptionLabel(self.cardWidget)
        self.CaptionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CaptionLabel.setObjectName("CaptionLabel")
        self.verticalLayout_14.addWidget(self.CaptionLabel)
        self.horizontalLayout_10.addLayout(self.verticalLayout_14)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem6)
        self.verticalLayout_13.addLayout(self.horizontalLayout_10)
        self.StrongBodyLabel_2 = StrongBodyLabel(self.cardWidget)
        self.StrongBodyLabel_2.setObjectName("StrongBodyLabel_2")
        self.verticalLayout_13.addWidget(self.StrongBodyLabel_2)
        self.groupIDLabel = CaptionLabel(self.cardWidget)
        self.groupIDLabel.setObjectName("groupIDLabel")
        self.verticalLayout_13.addWidget(self.groupIDLabel)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.StrongBodyLabel_3 = StrongBodyLabel(self.cardWidget)
        self.StrongBodyLabel_3.setObjectName("StrongBodyLabel_3")
        self.horizontalLayout_11.addWidget(self.StrongBodyLabel_3)
        self.qrcodeButton = ToolButton(self.cardWidget)
        self.qrcodeButton.setObjectName("qrcodeButton")
        self.horizontalLayout_11.addWidget(self.qrcodeButton)
        self.verticalLayout_13.addLayout(self.horizontalLayout_11)
        self.StrongBodyLabel_4 = StrongBodyLabel(self.cardWidget)
        self.StrongBodyLabel_4.setObjectName("StrongBodyLabel_4")
        self.verticalLayout_13.addWidget(self.StrongBodyLabel_4)
        self.groupIDLabel_2 = CaptionLabel(self.cardWidget)
        self.groupIDLabel_2.setObjectName("groupIDLabel_2")
        self.verticalLayout_13.addWidget(self.groupIDLabel_2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem7)
        self.horizontalLayout_2.addWidget(self.cardWidget)
        self.horizontalLayout_2.setStretch(0, 8)
        self.horizontalLayout_2.setStretch(1, 2)
        self.stackedWidget.addWidget(self.page1)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.page2)
        self.horizontalLayout_19.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.nameLabel_2 = TitleLabel(self.page2)
        self.nameLabel_2.setObjectName("nameLabel_2")
        self.verticalLayout_8.addWidget(self.nameLabel_2)
        self.SimpleCardWidget_4 = SimpleCardWidget(self.page2)
        self.SimpleCardWidget_4.setMinimumSize(QtCore.QSize(0, 20))
        self.SimpleCardWidget_4.setObjectName("SimpleCardWidget_4")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.SimpleCardWidget_4)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setContentsMargins(-1, 2, -1, -1)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.SubtitleLabel_7 = SubtitleLabel(self.SimpleCardWidget_4)
        self.SubtitleLabel_7.setObjectName("SubtitleLabel_7")
        self.horizontalLayout_14.addWidget(self.SubtitleLabel_7)
        self.announEditButton_2 = ToolButton(self.SimpleCardWidget_4)
        self.announEditButton_2.setObjectName("announEditButton_2")
        self.horizontalLayout_14.addWidget(self.announEditButton_2)
        self.verticalLayout_17.addLayout(self.horizontalLayout_14)
        self.announcementLabel_2 = CaptionLabel(self.SimpleCardWidget_4)
        self.announcementLabel_2.setObjectName("announcementLabel_2")
        self.verticalLayout_17.addWidget(self.announcementLabel_2)
        self.verticalLayout_8.addWidget(self.SimpleCardWidget_4)
        self.ElevatedCardWidget_2 = ElevatedCardWidget(self.page2)
        self.ElevatedCardWidget_2.setObjectName("ElevatedCardWidget_2")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.ElevatedCardWidget_2)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setContentsMargins(-1, 3, -1, -1)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.IconWidget_2 = IconWidget(self.ElevatedCardWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IconWidget_2.sizePolicy().hasHeightForWidth())
        self.IconWidget_2.setSizePolicy(sizePolicy)
        self.IconWidget_2.setMinimumSize(QtCore.QSize(80, 80))
        self.IconWidget_2.setIcon(icon)
        self.IconWidget_2.setObjectName("IconWidget_2")
        self.horizontalLayout_16.addWidget(self.IconWidget_2)
        self.verticalLayout_9.addLayout(self.horizontalLayout_16)
        self.SubtitleLabel_2 = SubtitleLabel(self.ElevatedCardWidget_2)
        self.SubtitleLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.SubtitleLabel_2.setObjectName("SubtitleLabel_2")
        self.verticalLayout_9.addWidget(self.SubtitleLabel_2)
        self.BodyLabel_2 = BodyLabel(self.ElevatedCardWidget_2)
        self.BodyLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.BodyLabel_2.setObjectName("BodyLabel_2")
        self.verticalLayout_9.addWidget(self.BodyLabel_2)
        self.horizontalLayout_15.addLayout(self.verticalLayout_9)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setContentsMargins(-1, 3, -1, -1)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.IconWidget_8 = IconWidget(self.ElevatedCardWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IconWidget_8.sizePolicy().hasHeightForWidth())
        self.IconWidget_8.setSizePolicy(sizePolicy)
        self.IconWidget_8.setMinimumSize(QtCore.QSize(80, 80))
        self.IconWidget_8.setIcon(icon1)
        self.IconWidget_8.setObjectName("IconWidget_8")
        self.horizontalLayout_17.addWidget(self.IconWidget_8)
        self.verticalLayout_18.addLayout(self.horizontalLayout_17)
        self.SubtitleLabel_8 = SubtitleLabel(self.ElevatedCardWidget_2)
        self.SubtitleLabel_8.setAlignment(QtCore.Qt.AlignCenter)
        self.SubtitleLabel_8.setObjectName("SubtitleLabel_8")
        self.verticalLayout_18.addWidget(self.SubtitleLabel_8)
        self.BodyLabel_6 = BodyLabel(self.ElevatedCardWidget_2)
        self.BodyLabel_6.setAlignment(QtCore.Qt.AlignCenter)
        self.BodyLabel_6.setObjectName("BodyLabel_6")
        self.verticalLayout_18.addWidget(self.BodyLabel_6)
        self.horizontalLayout_15.addLayout(self.verticalLayout_18)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setContentsMargins(-1, 3, -1, -1)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.IconWidget_9 = IconWidget(self.ElevatedCardWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IconWidget_9.sizePolicy().hasHeightForWidth())
        self.IconWidget_9.setSizePolicy(sizePolicy)
        self.IconWidget_9.setMinimumSize(QtCore.QSize(80, 80))
        self.IconWidget_9.setIcon(icon2)
        self.IconWidget_9.setObjectName("IconWidget_9")
        self.horizontalLayout_18.addWidget(self.IconWidget_9)
        self.verticalLayout_19.addLayout(self.horizontalLayout_18)
        self.SubtitleLabel_9 = SubtitleLabel(self.ElevatedCardWidget_2)
        self.SubtitleLabel_9.setAlignment(QtCore.Qt.AlignCenter)
        self.SubtitleLabel_9.setObjectName("SubtitleLabel_9")
        self.verticalLayout_19.addWidget(self.SubtitleLabel_9)
        self.BodyLabel_7 = BodyLabel(self.ElevatedCardWidget_2)
        self.BodyLabel_7.setAlignment(QtCore.Qt.AlignCenter)
        self.BodyLabel_7.setObjectName("BodyLabel_7")
        self.verticalLayout_19.addWidget(self.BodyLabel_7)
        self.horizontalLayout_15.addLayout(self.verticalLayout_19)
        self.verticalLayout_8.addWidget(self.ElevatedCardWidget_2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem8)
        self.horizontalLayout_19.addLayout(self.verticalLayout_8)
        self.cardWidget_2 = CardWidget(self.page2)
        self.cardWidget_2.setMinimumSize(QtCore.QSize(250, 0))
        self.cardWidget_2.setObjectName("cardWidget_2")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.cardWidget_2)
        self.verticalLayout_15.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.StrongBodyLabel_5 = StrongBodyLabel(self.cardWidget_2)
        self.StrongBodyLabel_5.setObjectName("StrongBodyLabel_5")
        self.verticalLayout_15.addWidget(self.StrongBodyLabel_5)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.IconWidget_7 = IconWidget(self.cardWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IconWidget_7.sizePolicy().hasHeightForWidth())
        self.IconWidget_7.setSizePolicy(sizePolicy)
        self.IconWidget_7.setMinimumSize(QtCore.QSize(30, 30))
        self.IconWidget_7.setIcon(icon3)
        self.IconWidget_7.setObjectName("IconWidget_7")
        self.verticalLayout_16.addWidget(self.IconWidget_7)
        self.CaptionLabel_2 = CaptionLabel(self.cardWidget_2)
        self.CaptionLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.CaptionLabel_2.setObjectName("CaptionLabel_2")
        self.verticalLayout_16.addWidget(self.CaptionLabel_2)
        self.horizontalLayout_12.addLayout(self.verticalLayout_16)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem9)
        self.verticalLayout_15.addLayout(self.horizontalLayout_12)
        self.StrongBodyLabel_6 = StrongBodyLabel(self.cardWidget_2)
        self.StrongBodyLabel_6.setObjectName("StrongBodyLabel_6")
        self.verticalLayout_15.addWidget(self.StrongBodyLabel_6)
        self.groupIDLabel_3 = CaptionLabel(self.cardWidget_2)
        self.groupIDLabel_3.setObjectName("groupIDLabel_3")
        self.verticalLayout_15.addWidget(self.groupIDLabel_3)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.StrongBodyLabel_7 = StrongBodyLabel(self.cardWidget_2)
        self.StrongBodyLabel_7.setObjectName("StrongBodyLabel_7")
        self.horizontalLayout_13.addWidget(self.StrongBodyLabel_7)
        self.qrcodeButton_2 = ToolButton(self.cardWidget_2)
        self.qrcodeButton_2.setObjectName("qrcodeButton_2")
        self.horizontalLayout_13.addWidget(self.qrcodeButton_2)
        self.verticalLayout_15.addLayout(self.horizontalLayout_13)
        self.StrongBodyLabel_8 = StrongBodyLabel(self.cardWidget_2)
        self.StrongBodyLabel_8.setObjectName("StrongBodyLabel_8")
        self.verticalLayout_15.addWidget(self.StrongBodyLabel_8)
        self.groupIDLabel_4 = CaptionLabel(self.cardWidget_2)
        self.groupIDLabel_4.setObjectName("groupIDLabel_4")
        self.verticalLayout_15.addWidget(self.groupIDLabel_4)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem10)
        self.horizontalLayout_19.addWidget(self.cardWidget_2)
        self.horizontalLayout_19.setStretch(0, 8)
        self.horizontalLayout_19.setStretch(1, 2)
        self.stackedWidget.addWidget(self.page2)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.horizontalLayout_3.addWidget(self.SimpleCardWidget_2)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(GroupInterface)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(GroupInterface)

    def retranslateUi(self, GroupInterface):
        _translate = QtCore.QCoreApplication.translate
        GroupInterface.setWindowTitle(_translate("GroupInterface", "Form"))
        self.TitleLabel.setText(_translate("GroupInterface", "Group"))
        self.LargeTitleLabel.setText(_translate("GroupInterface", "Join a New Group"))
        self.createGroupButton.setText(_translate("GroupInterface", "Create a Group"))
        self.BodyLabel_3.setText(_translate("GroupInterface", "or"))
        self.joinByCodeButton.setText(_translate("GroupInterface", "Join by Group ID"))
        self.nameLabel.setText(_translate("GroupInterface", "Group Name"))
        self.SubtitleLabel_6.setText(_translate("GroupInterface", "📢 Announcement"))
        self.announcementLabel.setText(_translate("GroupInterface", "The group owner is too lazy, didn\'t write anything"))
        self.SubtitleLabel.setText(_translate("GroupInterface", "1"))
        self.BodyLabel.setText(_translate("GroupInterface", "Step Rank"))
        self.SubtitleLabel_4.setText(_translate("GroupInterface", "1"))
        self.BodyLabel_4.setText(_translate("GroupInterface", "Time Rank"))
        self.SubtitleLabel_5.setText(_translate("GroupInterface", "1"))
        self.BodyLabel_5.setText(_translate("GroupInterface", "Calories Rank"))
        self.StrongBodyLabel.setText(_translate("GroupInterface", "Group Members"))
        self.CaptionLabel.setText(_translate("GroupInterface", "You"))
        self.StrongBodyLabel_2.setText(_translate("GroupInterface", "Group ID"))
        self.groupIDLabel.setText(_translate("GroupInterface", "2000173"))
        self.StrongBodyLabel_3.setText(_translate("GroupInterface", "Group QRCode"))
        self.StrongBodyLabel_4.setText(_translate("GroupInterface", "Group ID"))
        self.groupIDLabel_2.setText(_translate("GroupInterface", "2000173"))
        self.nameLabel_2.setText(_translate("GroupInterface", "Group Name 2"))
        self.SubtitleLabel_7.setText(_translate("GroupInterface", "📢 Announcement"))
        self.announcementLabel_2.setText(_translate("GroupInterface", "The group owner is too lazy, didn\'t write anything"))
        self.SubtitleLabel_2.setText(_translate("GroupInterface", "1"))
        self.BodyLabel_2.setText(_translate("GroupInterface", "Step Rank"))
        self.SubtitleLabel_8.setText(_translate("GroupInterface", "1"))
        self.BodyLabel_6.setText(_translate("GroupInterface", "Time Rank"))
        self.SubtitleLabel_9.setText(_translate("GroupInterface", "1"))
        self.BodyLabel_7.setText(_translate("GroupInterface", "Calories Rank"))
        self.StrongBodyLabel_5.setText(_translate("GroupInterface", "Group Members"))
        self.CaptionLabel_2.setText(_translate("GroupInterface", "You"))
        self.StrongBodyLabel_6.setText(_translate("GroupInterface", "Group ID"))
        self.groupIDLabel_3.setText(_translate("GroupInterface", "2000184"))
        self.StrongBodyLabel_7.setText(_translate("GroupInterface", "Group QRCode"))
        self.StrongBodyLabel_8.setText(_translate("GroupInterface", "Group ID"))
        self.groupIDLabel_4.setText(_translate("GroupInterface", "2000184"))
from qfluentwidgets import BodyLabel, CaptionLabel, CardWidget, ElevatedCardWidget, IconWidget, LargeTitleLabel, ListWidget, PrimaryPushButton, SearchLineEdit, SimpleCardWidget, StrongBodyLabel, SubtitleLabel, TitleLabel, ToolButton
