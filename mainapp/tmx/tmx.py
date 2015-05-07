class Tmx(object):

    """class wrapped around Elementtree to represent Translation Memory
     in TMX format"""

    def __init__(self, filename=''):
        self.trans_units = []
        #custom properties for a translation memory
        self.properties = dict()
        #obligatory attributes for a translation memory
        self.attributes = dict()
        if filename:
            self.tmx = ET.parse(filename).getroot()
            if self.tmx.tag != 'tmx':
                raise AttributeError("Not valid TMX")
            self.trans_units = [TU(tu) for tu in self.tmx.iter(tag="tu")]
            self.attributes.update(self.tmx.find('header').attrib)

            for prop in self.tmx[0].findall('prop'):
                self.properties[prop.attrib['type']] = prop.text

    def get_version(self):
        '''retrieves version of TMX file'''
        if 'version' in self.tmx.attrib:
            return self.tmx.attrib['version']

    def __len__(self):
        '''gets number of translation units'''
        return len(self.trans_units)

    def __getitem__(self, number):
        '''access to the items on the list'''
        if number > len(self.trans_units):
            raise IndexError("list index out of range")
        return self.trans_units[number]

    def next(self):
        """generator to go through all TU segments"""
        for trans_unit in self.trans_units:
            yield trans_unit.toxml()

    def save(self, filename):
        '''saves translation memory as TMX file'''
        tmx = ET.Element('tmx')
        print(tmx)
        header = ET.SubElement(tmx, 'header')
        header.attrib.update(self.attributes)
        print(header)
        for key, value in self.properties.items():
            prop = ET.SubElement(header, 'prop')
            prop.attrib['type'] = key
            prop.text = value
        body = ET.SubElement(tmx, 'body')
        print(body)
        for tuv in self.trans_units:
            body.append(tuv.toxml())
        print(tmx)
        ET.ElementTree(tmx).write(
            filename,
            xml_declaration=True,
            encoding='UTF-8')