# -*- coding: utf-8 -*-

class CPerson(object):
	def __init__(self):
		self.m_sName = ""

	def SetName(self, sName):
		self.m_sName = sName

	def Show(self):
		print "装扮的{}".format(self.m_sName),
