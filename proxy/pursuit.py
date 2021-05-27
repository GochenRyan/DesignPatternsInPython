# -*- coding: utf-8 -*-

class CPursuit(object):
	def __init__(self):
		self.m_oGirl = None

	def SetGirl(self, oGirl):
		self.m_oGirl = oGirl

	def GiveFlowers(self):
		print "{}, 送你鲜花".format(self.m_oGirl.GetName())