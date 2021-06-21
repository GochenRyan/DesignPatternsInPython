# -*- coding: utf-8 -*-

class CProduct(object):
	def __init__(self):
		self.m_lPart = []

	def add(self, part):
		self.m_lPart.append(part)

	def printParts(self):
		print "Product parts:", self.m_lPart