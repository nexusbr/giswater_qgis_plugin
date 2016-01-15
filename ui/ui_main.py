# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created: Tue Jan 05 13:31:36 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(414, 271)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 414, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuGiswater = QtGui.QMenu(self.menubar)
        self.menuGiswater.setObjectName(_fromUtf8("menuGiswater"))
        self.menuGo2Epa = QtGui.QMenu(self.menuGiswater)
        self.menuGo2Epa.setObjectName(_fromUtf8("menuGo2Epa"))
        self.menuAnalysis = QtGui.QMenu(self.menuGiswater)
        self.menuAnalysis.setObjectName(_fromUtf8("menuAnalysis"))
        self.menuEPA_results = QtGui.QMenu(self.menuAnalysis)
        self.menuEPA_results.setObjectName(_fromUtf8("menuEPA_results"))
        self.menuFlow_trace = QtGui.QMenu(self.menuAnalysis)
        self.menuFlow_trace.setObjectName(_fromUtf8("menuFlow_trace"))
        self.menuNetwork_configuration = QtGui.QMenu(self.menuGiswater)
        self.menuNetwork_configuration.setObjectName(_fromUtf8("menuNetwork_configuration"))
        self.menuNetwork_management = QtGui.QMenu(self.menuGiswater)
        self.menuNetwork_management.setObjectName(_fromUtf8("menuNetwork_management"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.tbInsert = QtGui.QToolBar(MainWindow)
        self.tbInsert.setObjectName(_fromUtf8("tbInsert"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.tbInsert)
        self.tbEdit = QtGui.QToolBar(MainWindow)
        self.tbEdit.setObjectName(_fromUtf8("tbEdit"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.tbEdit)
        MainWindow.insertToolBarBreak(self.tbEdit)
        self.actionJunction = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/giswater/icons/01.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionJunction.setIcon(icon)
        self.actionJunction.setObjectName(_fromUtf8("actionJunction"))
        self.actionNew_project = QtGui.QAction(MainWindow)
        self.actionNew_project.setObjectName(_fromUtf8("actionNew_project"))
        self.actionCopy_project_as = QtGui.QAction(MainWindow)
        self.actionCopy_project_as.setObjectName(_fromUtf8("actionCopy_project_as"))
        self.actionGiswater_interface = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/giswater/icons/23.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGiswater_interface.setIcon(icon1)
        self.actionGiswater_interface.setObjectName(_fromUtf8("actionGiswater_interface"))
        self.actionRun_simulation = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/giswater/icons/24.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRun_simulation.setIcon(icon2)
        self.actionRun_simulation.setObjectName(_fromUtf8("actionRun_simulation"))
        self.actionMove_node = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/giswater/icons/16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMove_node.setIcon(icon3)
        self.actionMove_node.setObjectName(_fromUtf8("actionMove_node"))
        self.actionDelete_node = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/giswater/icons/17.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete_node.setIcon(icon4)
        self.actionDelete_node.setObjectName(_fromUtf8("actionDelete_node"))
        self.actionCapture_raster_elevation = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/giswater/icons/18.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCapture_raster_elevation.setIcon(icon5)
        self.actionCapture_raster_elevation.setObjectName(_fromUtf8("actionCapture_raster_elevation"))
        self.actionResult_catalog = QtGui.QAction(MainWindow)
        self.actionResult_catalog.setObjectName(_fromUtf8("actionResult_catalog"))
        self.actionResult_selector = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/giswater/icons/25.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionResult_selector.setIcon(icon6)
        self.actionResult_selector.setObjectName(_fromUtf8("actionResult_selector"))
        self.actionSnapping_tolerance = QtGui.QAction(MainWindow)
        self.actionSnapping_tolerance.setObjectName(_fromUtf8("actionSnapping_tolerance"))
        self.actionNode_tolerance = QtGui.QAction(MainWindow)
        self.actionNode_tolerance.setObjectName(_fromUtf8("actionNode_tolerance"))
        self.actionTable_wizard = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/giswater/icons/21.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTable_wizard.setIcon(icon7)
        self.actionTable_wizard.setObjectName(_fromUtf8("actionTable_wizard"))
        self.actionUndo_wizard = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/giswater/icons/22.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo_wizard.setIcon(icon8)
        self.actionUndo_wizard.setObjectName(_fromUtf8("actionUndo_wizard"))
        self.actionOutfall = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/giswater/icons/02.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOutfall.setIcon(icon9)
        self.actionOutfall.setObjectName(_fromUtf8("actionOutfall"))
        self.actionDivider = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/giswater/icons/03.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDivider.setIcon(icon10)
        self.actionDivider.setObjectName(_fromUtf8("actionDivider"))
        self.actionStorage = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/giswater/icons/04.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStorage.setIcon(icon11)
        self.actionStorage.setObjectName(_fromUtf8("actionStorage"))
        self.actionFrom_node = QtGui.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/giswater/icons/26.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFrom_node.setIcon(icon12)
        self.actionFrom_node.setObjectName(_fromUtf8("actionFrom_node"))
        self.actionFrom_arc = QtGui.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/giswater/icons/27.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFrom_arc.setIcon(icon13)
        self.actionFrom_arc.setObjectName(_fromUtf8("actionFrom_arc"))
        self.actionEdit_arc = QtGui.QAction(MainWindow)
        self.actionEdit_arc.setIcon(icon5)
        self.actionEdit_arc.setObjectName(_fromUtf8("actionEdit_arc"))
        self.actionConnect_tool = QtGui.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/giswater/icons/20.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConnect_tool.setIcon(icon14)
        self.actionConnect_tool.setObjectName(_fromUtf8("actionConnect_tool"))
        self.menuGo2Epa.addAction(self.actionGiswater_interface)
        self.menuGo2Epa.addAction(self.actionRun_simulation)
        self.menuEPA_results.addAction(self.actionResult_catalog)
        self.menuEPA_results.addAction(self.actionResult_selector)
        self.menuFlow_trace.addAction(self.actionFrom_node)
        self.menuFlow_trace.addAction(self.actionFrom_arc)
        self.menuAnalysis.addAction(self.menuEPA_results.menuAction())
        self.menuAnalysis.addAction(self.menuFlow_trace.menuAction())
        self.menuNetwork_configuration.addAction(self.actionSnapping_tolerance)
        self.menuNetwork_configuration.addAction(self.actionNode_tolerance)
        self.menuNetwork_management.addAction(self.actionTable_wizard)
        self.menuNetwork_management.addAction(self.actionUndo_wizard)
        self.menuGiswater.addAction(self.actionNew_project)
        self.menuGiswater.addAction(self.actionCopy_project_as)
        self.menuGiswater.addAction(self.menuNetwork_configuration.menuAction())
        self.menuGiswater.addAction(self.menuNetwork_management.menuAction())
        self.menuGiswater.addAction(self.menuAnalysis.menuAction())
        self.menuGiswater.addAction(self.menuGo2Epa.menuAction())
        self.menubar.addAction(self.menuGiswater.menuAction())
        self.tbInsert.addAction(self.actionJunction)
        self.tbInsert.addAction(self.actionOutfall)
        self.tbInsert.addAction(self.actionDivider)
        self.tbInsert.addAction(self.actionStorage)
        self.tbEdit.addAction(self.actionMove_node)
        self.tbEdit.addAction(self.actionDelete_node)
        self.tbEdit.addAction(self.actionCapture_raster_elevation)
        self.tbEdit.addAction(self.actionEdit_arc)
        self.tbEdit.addAction(self.actionConnect_tool)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuGiswater.setTitle(_translate("MainWindow", "Giswater", None))
        self.menuGo2Epa.setTitle(_translate("MainWindow", "Go2Epa", None))
        self.menuAnalysis.setTitle(_translate("MainWindow", "Analysis", None))
        self.menuEPA_results.setTitle(_translate("MainWindow", "EPA results", None))
        self.menuFlow_trace.setTitle(_translate("MainWindow", "Flow trace", None))
        self.menuNetwork_configuration.setTitle(_translate("MainWindow", "Network configuration", None))
        self.menuNetwork_management.setTitle(_translate("MainWindow", "Network management", None))
        self.tbInsert.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.tbEdit.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionJunction.setText(_translate("MainWindow", "junction", None))
        self.actionJunction.setToolTip(_translate("MainWindow", "Insert Junction", None))
        self.actionNew_project.setText(_translate("MainWindow", "New network", None))
        self.actionCopy_project_as.setText(_translate("MainWindow", "Copy network as", None))
        self.actionGiswater_interface.setText(_translate("MainWindow", "Giswater interface", None))
        self.actionRun_simulation.setText(_translate("MainWindow", "Run simulation", None))
        self.actionMove_node.setText(_translate("MainWindow", "Move node", None))
        self.actionDelete_node.setText(_translate("MainWindow", "Delete node", None))
        self.actionCapture_raster_elevation.setText(_translate("MainWindow", "Capture raster elevation", None))
        self.actionResult_catalog.setText(_translate("MainWindow", "Result catalog", None))
        self.actionResult_selector.setText(_translate("MainWindow", "Result selector", None))
        self.actionSnapping_tolerance.setText(_translate("MainWindow", "Snapping tolerance", None))
        self.actionNode_tolerance.setText(_translate("MainWindow", "Node tolerance", None))
        self.actionTable_wizard.setText(_translate("MainWindow", "Table wizard", None))
        self.actionUndo_wizard.setText(_translate("MainWindow", "Undo wizard", None))
        self.actionOutfall.setText(_translate("MainWindow", "Outfall", None))
        self.actionDivider.setText(_translate("MainWindow", "Divider", None))
        self.actionDivider.setToolTip(_translate("MainWindow", "Insert Divider", None))
        self.actionStorage.setText(_translate("MainWindow", "Storage", None))
        self.actionStorage.setToolTip(_translate("MainWindow", "Insert Storage", None))
        self.actionFrom_node.setText(_translate("MainWindow", "From node", None))
        self.actionFrom_arc.setText(_translate("MainWindow", "From arc", None))
        self.actionEdit_arc.setText(_translate("MainWindow", "Edit arc", None))
        self.actionEdit_arc.setToolTip(_translate("MainWindow", "Edit arc", None))
        self.actionConnect_tool.setText(_translate("MainWindow", "Connect tool", None))
        self.actionConnect_tool.setToolTip(_translate("MainWindow", "Connect tool", None))

import resources_rc