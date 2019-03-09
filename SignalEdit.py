from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from lxml import etree

from signalwin import Ui_SignalWin


class SignalEdit(QtWidgets.QWidget, Ui_SignalWin):
    def __init__(self):
        super(SignalEdit, self).__init__()
        self.setupUi(self)
        self.initEvent()

    def initEvent(self):
        self.signalAddBT.clicked.connect(self.signalAddEvent)
        self.signalDeleteBT.clicked.connect(self.signalDeleteEvent)
        self.saveSignalBT.clicked.connect(self.saveSignalEvent)
        self.objectAddBT.clicked.connect(self.objectAddEvent)
        self.objectDeleteBT.clicked.connect(self.objectDeleteEvent)
        self.saveObjectBT.clicked.connect(self.saveObjectEvent)

    def showWin(self, junctionID, linkID, fromroad, toroad):
        parser = etree.XMLParser(remove_blank_text=True)
        xml = etree.parse('yf_sample_data.xml', parser)
        self.root = xml.getroot()  # 获取根节点
        self.junctionID = junctionID
        self.linkID = linkID
        self.fromroad = fromroad
        self.toroad = toroad
        self.initWind()
        self.show()

    def initWind(self):
        self.initSignal()
        self.initObject()

    def initSignal(self):
        self.signalList = self.root.xpath(
            '//OpenDriveData/junction[@id="' + self.junctionID + '"]/links/link[@id="' + self.linkID + '"]/signals/signal')
        # 清空表格行
        while self.signalTable.rowCount() > 0:
            self.signalTable.removeRow(0)

        for signalIndex in range(0, len(self.signalList)):
            self.signalTable.insertRow(signalIndex)
            _signal = self.signalList[signalIndex]
            _id = _signal.xpath("@id")[0]
            _type = _signal.xpath("@type")[0]
            _subtype = _signal.xpath("@subtype")[0]
            _roadid = _signal.xpath("@roadid")[0]
            _s = _signal.xpath("@s")[0]
            _t = _signal.xpath("@t")[0]
            _h = _signal.xpath("@h")[0]
            # _reference = _signal.xpath("@reference")[0]
            _reference = _signal.xpath("@reference")[0] if len(_signal.xpath("@reference")) > 0 else ""
            self.signalTable.setItem(signalIndex, 0, QTableWidgetItem(_id))
            self.signalTable.setItem(signalIndex, 1, QTableWidgetItem(_type))
            self.signalTable.setItem(signalIndex, 2, QTableWidgetItem(_subtype))
            self.signalTable.setItem(signalIndex, 3, QTableWidgetItem(_roadid))
            self.signalTable.setItem(signalIndex, 4, QTableWidgetItem(_s))
            self.signalTable.setItem(signalIndex, 5, QTableWidgetItem(_t))
            self.signalTable.setItem(signalIndex, 6, QTableWidgetItem(_h))
            self.signalTable.setItem(signalIndex, 7, QTableWidgetItem(_reference))

    def initObject(self):
        self.objectList = self.root.xpath(
            '//OpenDriveData/junction[@id="' + self.junctionID + '"]/links/link[@id="' + self.linkID + '"]/objects/object')
        # 清空表格行
        while self.objectTable.rowCount() > 0:
            self.objectTable.removeRow(0)

        self.objectMaxId = 0
        for objectIndex in range(0, len(self.objectList)):
            self.objectTable.insertRow(objectIndex)
            _object = self.objectList[objectIndex]

            sr = _object.xpath("@sr")[0] if len(_object.xpath("@sr")) > 0 else ""
            st = _object.xpath("@st")[0] if len(_object.xpath("@st")) > 0 else ""
            sh = _object.xpath("@sh")[0] if len(_object.xpath("@sh")) > 0 else ""
            type = _object.xpath("@type")[0] if len(_object.xpath("@type")) > 0 else ""
            name = _object.xpath("@name")[0] if len(_object.xpath("@name")) > 0 else ""
            id = _object.xpath("@id")[0] if len(_object.xpath("@id")) > 0 else ""
            s = _object.xpath("@s")[0] if len(_object.xpath("@s")) > 0 else ""
            t = _object.xpath("@t")[0] if len(_object.xpath("@t")) > 0 else ""
            zOffset = _object.xpath("@zOffset")[0] if len(_object.xpath("@zOffset")) > 0 else ""
            validLength = _object.xpath("@validLength")[0] if len(_object.xpath("@validLength")) > 0 else ""
            orientation = _object.xpath("@orientation")[0] if len(_object.xpath("@orientation")) > 0 else ""
            length = _object.xpath("@length")[0] if len(_object.xpath("@length")) > 0 else ""
            width = _object.xpath("@width")[0] if len(_object.xpath("@width")) > 0 else ""
            height = _object.xpath("@height")[0] if len(_object.xpath("@height")) > 0 else ""
            hdg = _object.xpath("@hdg")[0] if len(_object.xpath("@hdg")) > 0 else ""
            pitch = _object.xpath("@pitch")[0] if len(_object.xpath("@pitch")) > 0 else ""
            roll = _object.xpath("@roll")[0] if len(_object.xpath("@roll")) > 0 else ""
            self.objectMaxId = max(self.objectMaxId, int(id))

            self.objectTable.setItem(objectIndex, 0, QTableWidgetItem(sr))
            self.objectTable.setItem(objectIndex, 1, QTableWidgetItem(st))
            self.objectTable.setItem(objectIndex, 2, QTableWidgetItem(sh))
            self.objectTable.setItem(objectIndex, 3, QTableWidgetItem(type))
            self.objectTable.setItem(objectIndex, 4, QTableWidgetItem(name))
            self.objectTable.setItem(objectIndex, 5, QTableWidgetItem(id))
            self.objectTable.setItem(objectIndex, 6, QTableWidgetItem(s))
            self.objectTable.setItem(objectIndex, 7, QTableWidgetItem(t))
            self.objectTable.setItem(objectIndex, 8, QTableWidgetItem(zOffset))
            self.objectTable.setItem(objectIndex, 9, QTableWidgetItem(validLength))
            self.objectTable.setItem(objectIndex, 10, QTableWidgetItem(orientation))
            self.objectTable.setItem(objectIndex, 11, QTableWidgetItem(length))
            self.objectTable.setItem(objectIndex, 12, QTableWidgetItem(width))
            self.objectTable.setItem(objectIndex, 13, QTableWidgetItem(height))
            self.objectTable.setItem(objectIndex, 14, QTableWidgetItem(hdg))
            self.objectTable.setItem(objectIndex, 15, QTableWidgetItem(pitch))
            self.objectTable.setItem(objectIndex, 16, QTableWidgetItem(roll))

    def signalAddEvent(self):
        rowCount = self.signalTable.rowCount()
        self.signalTable.insertRow(rowCount)
        self.initTableItemToEmptyStr(self.signalTable, rowCount)
        self.signalTable.setItem(rowCount, 1, QTableWidgetItem("1000001"))
        self.signalTable.setItem(rowCount, 2, QTableWidgetItem("-1"))
        self.signalTable.setItem(rowCount, 3, QTableWidgetItem(self.linkID))

    def signalDeleteEvent(self):
        currentRowIndex = self.signalTable.currentIndex().row()
        if currentRowIndex == -1:
            QMessageBox.information(self, "温馨提示", "请选择删除记录！", QMessageBox.Yes, QMessageBox.Yes)
            return
        model = self.signalTable.model()
        _id = model.data(model.index(currentRowIndex, 0))
        signals = self.root.xpath(
            '//OpenDriveData/junction[@id="' + self.junctionID + '"]/links/link[@id="' + self.linkID + '"]/signals')
        signal = signalList = self.root.xpath(
            '//OpenDriveData/junction[@id="' + self.junctionID + '"]/links/link[@id="' + self.linkID + '"]/signals/signal[@id="' + _id + '"]')
        if len(signals) > 0 and len(signal) > 0:
            signals[0].remove(signal[0])
        self.signalTable.removeRow(currentRowIndex)

    def saveSignalEvent(self):
        try:
            signalList = self.root.xpath(
                '//OpenDriveData/junction[@id="' + self.junctionID + '"]/links/link[@id="' + self.linkID + '"]/signals/signal')

            rowAllCount = self.signalTable.rowCount()
            model = self.signalTable.model()
            for i in range(0, rowAllCount):
                # _signalIndex = model.index(i, 0)
                # _val = model.data(_signalIndex)
                _id = model.data(model.index(i, 0))
                _type = model.data(model.index(i, 1))
                _subtype = model.data(model.index(i, 2))
                _roadid = model.data(model.index(i, 3))
                _s = model.data(model.index(i, 4))
                _t = model.data(model.index(i, 5))
                _h = model.data(model.index(i, 6))
                _reference = model.data(model.index(i, 7))

                print(_id, _type, _subtype, _roadid, _s, _t, _h, _reference)

                _signal = self.root.xpath(
                    '//OpenDriveData/junction[@id="' + self.junctionID + '"]/links/link[@id="' + self.linkID + '"]/signals/signal[@id="' + _id + '"]')

                if len(_signal) > 0:  # 该id在文本中存在
                    attrib = _signal[0].attrib
                    attrib["id"] = _id.strip()
                    attrib["type"] = _type.strip()
                    attrib["subtype"] = _subtype.strip()
                    attrib["roadid"] = _roadid.strip()
                    attrib["s"] = _s.strip()
                    attrib["t"] = _t.strip()
                    attrib["h"] = _h.strip()
                    if _reference != "":
                        attrib["reference"] = _reference.strip()

                else:  # signal不存在
                    _signals = self.root.xpath(
                        '//OpenDriveData/junction[@id="' + self.junctionID + '"]/links/link[@id="' + self.linkID + '"]/signals')
                    # attrib = {}
                    # attrib["id"] = _id
                    # attrib["type"] = _type
                    # attrib["subtype"] = _subtype
                    # attrib["roadid"] = _roadid
                    # attrib["s"] = _s
                    # attrib["t"] = _t
                    # attrib["h"] = _h
                    # if _reference != "":
                    #     attrib["reference"] = _reference

                    # element = Element("signal", attrib)
                    # if len(_signals) > 0:
                    #     _signals[0].append(element)
                    if len(_signals) > 0:
                        _signalnew = etree.SubElement(_signals[0], 'signal')
                        _signalnew.set("id", _id.strip())
                        _signalnew.set("type", _type.strip())
                        _signalnew.set("subtype", _subtype.strip())
                        _signalnew.set("roadid", _roadid.strip())
                        _signalnew.set("s", _s.strip())
                        _signalnew.set("t", _t.strip())
                        _signalnew.set("h", _h.strip())
                        if _reference != "" and _reference != None:
                            _signalnew.set("reference", _reference.strip())

            try:
                # 节点转为tree对象
                tree = etree.ElementTree(self.root)
                '''
                各个参数含义如下：
                1）第1个参数是xml的完整路径(包括文件名)；
                2）pretty_print参数是否美化代码；
                3）xml_declaration参数是否写入xml声明，就是我们看到xml文档第1行文字；
                4）encoding参数很明显是保存的编码。
                '''
                tree.write('yf_sample_data.xml', pretty_print=True, xml_declaration=True, encoding='utf-8')
                print('写入xml OK!')
                QMessageBox.information(self, "温馨提示", "写入xml成功！", QMessageBox.Yes, QMessageBox.Yes)
                # self.closeWin()
            except Exception as err:
                print('错误信息：{0}'.format(err))
                QMessageBox.information(self, "温馨提示", "写入xml失败！", QMessageBox.Yes, QMessageBox.Yes)
        except Exception as err:
            print('错误信息：{0}'.format(err))
            QMessageBox.information(self, "温馨提示", '错误信息：{0}'.format(err), QMessageBox.Yes, QMessageBox.Yes)

    def objectAddEvent(self):
        rowCount = self.objectTable.rowCount()
        self.objectTable.insertRow(rowCount)
        self.initTableItemToEmptyStr(self.objectTable, rowCount)
        sr = self.srLE.text().strip()
        st = self.stLE.text().strip()
        sh = self.shLE.text().strip()
        type = self.typeLE.text().strip()
        name = self.nameLE.text().strip()
        id = self.idLE.text().strip()
        s = self.sLE.text().strip()
        t = self.tLE.text().strip()
        zOffset = self.zOffsetLE.text().strip()
        validLength = self.validLengthLE.text().strip()
        orientation = self.orientationLE.text().strip()
        length = self.lengthLE.text().strip()
        width = self.widthLE.text().strip()
        height = self.heightLE.text().strip()
        hdg = self.hdgLE.text().strip()
        pitch = self.pitchLE.text().strip()
        roll = self.rollLE.text().strip()

        manualIndex = self.manualCBB.currentIndex()
        if manualIndex == 1:  # 0 否 1 是
            self.objectTable.setItem(rowCount, 0, QTableWidgetItem(sr))
            self.objectTable.setItem(rowCount, 1, QTableWidgetItem(st))
            self.objectTable.setItem(rowCount, 2, QTableWidgetItem(sh))

        self.objectTable.setItem(rowCount, 3, QTableWidgetItem(type))
        self.objectTable.setItem(rowCount, 4, QTableWidgetItem(name))
        self.objectMaxId = self.objectMaxId + 1
        self.objectTable.setItem(rowCount, 5, QTableWidgetItem(str(self.objectMaxId)))
        # self.objectTable.setItem(rowCount, 5, QTableWidgetItem(id))

        self.objectTable.setItem(rowCount, 6, QTableWidgetItem(s))
        self.objectTable.setItem(rowCount, 7, QTableWidgetItem(t))
        self.objectTable.setItem(rowCount, 8, QTableWidgetItem(zOffset))
        self.objectTable.setItem(rowCount, 9, QTableWidgetItem(validLength))
        self.objectTable.setItem(rowCount, 10, QTableWidgetItem(orientation))
        self.objectTable.setItem(rowCount, 11, QTableWidgetItem(length))
        self.objectTable.setItem(rowCount, 12, QTableWidgetItem(width))
        self.objectTable.setItem(rowCount, 13, QTableWidgetItem(height))
        self.objectTable.setItem(rowCount, 14, QTableWidgetItem(hdg))
        self.objectTable.setItem(rowCount, 15, QTableWidgetItem(pitch))
        self.objectTable.setItem(rowCount, 16, QTableWidgetItem(roll))

    def saveObjectEvent(self):
        objectList = self.root.xpath(
            '//OpenDriveData/junction[@id="' + self.junctionID + '"]/links/link[@id="' + self.linkID + '"]/objects/object')

        rowAllCount = self.objectTable.rowCount()
        model = self.objectTable.model()
        for i in range(0, rowAllCount):
            sr = model.data(model.index(i, 0))
            st = model.data(model.index(i, 1))
            sh = model.data(model.index(i, 2))
            type = model.data(model.index(i, 3))
            name = model.data(model.index(i, 4))
            id = model.data(model.index(i, 5))
            s = model.data(model.index(i, 6))
            t = model.data(model.index(i, 7))
            zOffset = model.data(model.index(i, 8))
            validLength = model.data(model.index(i, 9))
            orientation = model.data(model.index(i, 10))
            length = model.data(model.index(i, 11))
            width = model.data(model.index(i, 12))
            height = model.data(model.index(i, 13))
            hdg = model.data(model.index(i, 14))
            pitch = model.data(model.index(i, 15))
            roll = model.data(model.index(i, 16))

            object = self.root.xpath(
                '//OpenDriveData/junction[@id="' + self.junctionID + '"]/links/link[@id="' + self.linkID + '"]/objects/object[@id="' + id + '"]')

            if len(object) > 0:  # 该id在文本中存在
                attrib = object[0].attrib
                manualIndex = self.manualCBB.currentIndex()
                if manualIndex == 1:  # 0 否 1 是
                    if sr != None and sr != "":
                        attrib["sr"] = sr.strip()
                    if st != None and st != "":
                        attrib["st"] = st.strip()
                    if sh != None and sh != "":
                        attrib["sh"] = sh.strip()
                attrib["type"] = type.strip()
                attrib["name"] = name.strip()
                attrib["id"] = id
                attrib["s"] = s
                attrib["t"] = t
                attrib["zOffset"] = zOffset
                attrib["validLength"] = validLength
                attrib["orientation"] = orientation
                attrib["length"] = length
                attrib["width"] = width
                attrib["height"] = height
                attrib["hdg"] = hdg
                attrib["pitch"] = pitch
                attrib["roll"] = roll

            else:  # 不存在
                objects = self.root.xpath(
                    '//OpenDriveData/junction[@id="' + self.junctionID + '"]/links/link[@id="' + self.linkID + '"]/objects')
                if len(objects) > 0:
                    objectnew = etree.SubElement(objects[0], 'object')
                    manualIndex = self.manualCBB.currentIndex()
                    if manualIndex == 1:  # 0 否 1 是
                        if sr != None and sr != "":
                            objectnew.set("sr", sr.strip())
                        if st != None and st != "":
                            objectnew.set("st", st.strip())
                        if sh != None and sh != "":
                            objectnew.set("sh", sh.strip())
                    objectnew.set("type", type.strip())
                    objectnew.set("name", name.strip())
                    objectnew.set("id", id.strip())
                    objectnew.set("s", s.strip())
                    objectnew.set("t", t.strip())
                    objectnew.set("zOffset", zOffset.strip())
                    objectnew.set("validLength", validLength.strip())
                    objectnew.set("orientation", orientation.strip())
                    objectnew.set("length", length.strip())
                    objectnew.set("width", width.strip())
                    objectnew.set("height", height.strip())
                    objectnew.set("hdg", hdg.strip())
                    objectnew.set("pitch", pitch.strip())
                    objectnew.set("roll", roll.strip())

        try:
            # 节点转为tree对象
            tree = etree.ElementTree(self.root)
            '''
            各个参数含义如下：
            1）第1个参数是xml的完整路径(包括文件名)；
            2）pretty_print参数是否美化代码；
            3）xml_declaration参数是否写入xml声明，就是我们看到xml文档第1行文字；
            4）encoding参数很明显是保存的编码。
            '''
            tree.write('yf_sample_data.xml', pretty_print=True, xml_declaration=True, encoding='utf-8')
            print('写入xml OK!')
            QMessageBox.information(self, "温馨提示", "写入xml成功！", QMessageBox.Yes, QMessageBox.Yes)
            self.objectMaxId = max(self.objectMaxId, int(id))
            # self.closeWin()
        except Exception as err:
            print('错误信息：{0}'.format(err))
            QMessageBox.information(self, "温馨提示", "写入xml失败！", QMessageBox.Yes, QMessageBox.Yes)

    def objectDeleteEvent(self):
        currentRowIndex = self.objectTable.currentIndex().row()
        if currentRowIndex == -1:
            QMessageBox.information(self, "温馨提示", "请选择删除记录！", QMessageBox.Yes, QMessageBox.Yes)
            return
        model = self.objectTable.model()
        _id = model.data(model.index(currentRowIndex, 5))
        objects = self.root.xpath(
            '//OpenDriveData/junction[@id="' + self.junctionID + '"]/links/link[@id="' + self.linkID + '"]/objects')
        object = signalList = self.root.xpath(
            '//OpenDriveData/junction[@id="' + self.junctionID + '"]/links/link[@id="' + self.linkID + '"]/objects/object[@id="' + _id + '"]')
        if len(objects) > 0 and len(object) > 0:
            objects[0].remove(object[0])
        self.objectTable.removeRow(currentRowIndex)

    def initTableItemToEmptyStr(self, table, currentRow):
        for i in range(0, table.columnCount()):
            table.setItem(currentRow, i, QTableWidgetItem(""))
