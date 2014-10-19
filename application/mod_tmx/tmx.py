import xml.etree.ElementTree as ET

class Tmx(object):
	"""class wrapped around Elementtree to represent Translation Memory in TMX format"""
	def __init__(self, filename):
		self.tmx = ET.parse(filename).getroot()
		if self.tmx.tag != 'tmx': raise(AttributeError("Not valid TMX"))
		header_temp = self.tmx[0].attrib
		self.header = dict()
		for prop in self.tmx[0].iter(tag='prop'):
			self.header[prop.attrib['type']]=prop.text
		self.header.update(header_temp)

		
		
	def get_version(self):
		if 'version' in self.tmx.attrib:
			return self.tmx.attrib['version']
	
	def get_header(self):
		return self.tmx[0].attrib
	
	def get_properties(self, element):
		properties = dict()
		for prop in element.iter(tag='prop'):
			properties[prop.attrib['type']]=prop.text
		return properties
	def len(self):
		return len(self.tmx.findall("./body/tu"))
	def next(self):
		"""generator to go through all TMX segments"""
		for tuv in self.tmx.iter(tag="tu"):
			segs = tuv.findall('./tuv/seg')
			yield (segs[0],segs[1])