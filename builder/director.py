# -*- coding: utf-8 -*-

class CDirector(object):
	def __init__(self):
		self.m_oBuilder = None

	@property
	def builder(self):
		return self.m_oBuilder

	@builder.setter
	def builder(self, oBuilder):
		self.m_oBuilder = oBuilder

	def buildMinProduct(self):
		self.m_oBuilder.producePartA()

	def buildMaxProduct(self):
		self.m_oBuilder.producePartA()
		self.m_oBuilder.producePartB()
		self.m_oBuilder.producePartC()