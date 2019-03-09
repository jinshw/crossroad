from lxml import etree

if __name__ == '__main__':
    # html = etree.parse('yf_sample_data.xml', etree.XMLParser())
    # result = html.xpath('//OpenDriveData/road')
    # # result = etree.tostring(html)  # 解析成字节
    # # print(type(html))
    # #     # print(type(result))
    # print(type(html))
    # print(type(result))
    # print(result)
    # print(result[0].xpath("@id"))
    #
    # list = html.xpath('//OpenDriveData/road/@id')
    # print(list)
    # list.sort()
    # print(list)
    parser = etree.XMLParser(remove_blank_text=True)
    xml = etree.parse('yf_sample_data.xml',parser)
    root = xml.getroot()  # 获取根节点

    # 获取属性
    print(root.items())  # 获取全部属性和属性值
    print(root.keys())  # 获取全部属性
    print(root.get('version', ''))  # 获取具体某个属性

    result = root.xpath('//OpenDriveData/road')
    print(type(root))
    print(type(result))
    print(result)
    print(result[0].xpath("@id"))

    list = root.xpath('//OpenDriveData/road/@id')
    print(list)
    list.sort()
    print(list)

    junction = etree.Element('junction')
    objects = etree.Element('objects')
    signals = etree.Element('signals')
    junction.append(objects)
    junction.append(signals)
    root.append(junction)
    junction.set("name","1111")
    junction.set("bbb","333")
    junction.set("aa","yyy")

    junction2 = etree.SubElement(root, 'junction', attrib={'id': '222',"name":"333","abc":"abc"})
    etree.SubElement(junction2, 'objects', attrib={'id': 'objects222', "name": "objects333"})
    etree.SubElement(junction2, 'signals', attrib={'id': 'signals222', "name": "signals333"})


    # 节点转为tree对象
    tree = etree.ElementTree(root)

    '''
    各个参数含义如下：
    1）第1个参数是xml的完整路径(包括文件名)；
    2）pretty_print参数是否美化代码；
    3）xml_declaration参数是否写入xml声明，就是我们看到xml文档第1行文字；
    4）encoding参数很明显是保存的编码。
    '''
    tree.write('testrtttt.xml', pretty_print=True, xml_declaration=True, encoding='utf-8')

