'''module for handling xml files in TMX format
TODO: some cleaner way to handling namespaces
'''
import xml.etree.ElementTree as ET
from collections import namedtuple
from hashlib import md5
import codecs


TMX_NAMESPACE = "{http://www.w3.org/XML/1998/namespace}"
LanguagePair = namedtuple('LanguagePair', ['source', 'target'])

def create_properties_dict(element):
    '''retrieves prop elements from TU'''
    properties = dict()
    for prop in element.findall('prop'):
        properties[prop.attrib['type']] = prop.text
    return properties

class TU(object):
    """TU - translation unit"""
    def __init__(self, tuv=''):

        self.source = ""
        self.target = ""
        #custom properties for a translation unit
        self.properties = dict()
        #obligatory attributes for a translation unit
        self.attributes = dict()
        self.language_pair = LanguagePair(source='', target='')
        if tuv:
            self.fromxml(tuv)

    def toxml(self):
        '''creates xml tuv element according to TMX specification
        TODO: does not preserve context information
        '''
        tuv = ET.Element('tu')
        tuv.attrib.update(self.attributes)
        for prop_name, prop_value in self.properties.items():
            prop = ET.SubElement(tuv, 'property')
            prop.attrib['type'] = prop_name
            prop.text = prop_value

        tu1 = ET.SubElement(tuv, 'tuv')
        tu1.attrib['xml:lang'] = self.language_pair[0]
        seg1 = ET.fromstring('<seg>{}</seg>'.format(self.source))
        tu1.append(seg1)

        tu2 = ET.SubElement(tuv, 'tuv')
        tu2.attrib['xml:lang'] = self.language_pair[1]
        seg2 = ET.fromstring('<seg>{}</seg>'.format(self.target))
        tu2.append(seg2)

        return tuv

    def fromxml(self, xml_tu):
        '''parses tuv element to read data'''

        if xml_tu and xml_tu.tag == 'tu':
            self.properties = create_properties_dict(xml_tu)
            self.attributes.update(xml_tu.attrib)

            list_tuv = xml_tu.findall('tuv')

            self.language_pair = LanguagePair(
                list_tuv[0].attrib['{}lang'.format(TMX_NAMESPACE)],
                list_tuv[1].attrib['{}lang'.format(TMX_NAMESPACE)])
            segments = xml_tu.findall('./tuv/seg')
            self.source = ET.tostring(
                segments[0],
                method='text',
                encoding='unicode')
            self.target = ET.tostring(
                segments[1],
                method='text',
                encoding='unicode')
        else: raise AttributeError('Not valid Translation Unit')

    def get_source_hash(self):
        '''calculates hash of the source text - used to detect repetitions'''
        return md5(codecs.encode(self.source)).hexdigest()

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

    def len(self):
        '''gets number of translation units'''
        return len(self.trans_units)
    def next(self):
        """generator to go through all TU segments"""
        for trans_unit in self.trans_units:
            yield trans_unit.toxml()
    def save(self, filename):
        '''saves translation memory as TMX file'''
        tmx = ET.Element('tmx')
        print (tmx)
        header = ET.SubElement(tmx,'header')
        header.attrib.update(self.attributes)
        print (header)
        for key, value in self.properties.items():
            prop = ET.SubElement(header, 'prop')
            prop.attrib['type']=key
            prop.text = value        
        body = ET.SubElement(tmx, 'body')
        print (body)
        for tuv in self.trans_units:
            body.append(tuv.toxml())
        print (tmx)
        ET.ElementTree(tmx).write(filename, xml_declaration=True, encoding='UTF-8')
        
