from lxml import etree

if __name__ == '__main__':
    # s = "1.0798057866830962e+02"
    # aa = "107.9846"
    # print(s)
    # print(aa)
    # print(float(s), float(aa))
    # print(round(float(aa), 2))

    parserRight = etree.XMLParser(remove_blank_text=True)
    xmlRight = etree.parse("C:/Users/Administrator/Desktop/ss/hzzzxz_sm14(1).xodr", parserRight)
    rightRoot = xmlRight.getroot()  # 获取根节点
    #
    # t = "-1.2715896858959216e+01"
    # s = "1.0798057866830962e+02"
    #
    # plusFlag = t.find("+")
    # print(plusFlag)
    #
    # fsFlagS = s.find("-")
    # fsFlagT = t.find("-")
    # substrS = 4
    # substrT = 4
    # if fsFlagT < 0:
    #     substrT = 4
    #     txx = t[0:substrT]
    # else:
    #     substrT = 5
    #     txx = t[0:substrT]
    #
    # if fsFlagS < 0:
    #     substrS = 4
    #     sxx = s[0:substrS]
    # else:
    #     substrS = 5
    #     sxx = s[0:substrS]
    #
    # txxf = float(txx)
    # sxxf = float(sxx)
    #
    # t1 = txxf - 0.01
    # t2 = txxf + 0.01
    # s1 = sxxf - 0.01
    # s2 = sxxf + 0.01
    #
    # ss1 = str(s1) + s[substrS:]
    # ss2 = str(s2) + s[substrS:]
    # tt1 = str(t1) + t[substrT:]
    # tt2 = str(t2) + t[substrT:]

    # objectList = rightRoot.xpath(
    #     "//OpenDRIVE/road[@id='14002']/objects/object[@id='24' and @s>'" + ss1 + "' and @s<'" + ss2 + "']")
    # objectList = rightRoot.xpath(
    #     "//OpenDRIVE/road[@id='14002']/objects/object[@s>'" + ss1 + "' and @s<'" + ss2 + "' and @t>'" + tt1 + "' and @t<'" + tt2 + "']")
    objectList = rightRoot.xpath(
        "//OpenDRIVE/road[@id='14002']/objects/object[contains(@name ,'SgRMArrowStraight')]")

    print(len(objectList))
