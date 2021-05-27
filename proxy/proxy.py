# -*- coding: utf-8 -*-

class CProxy(object):
	def __init__(self, oGirl):
		import pursuit
		self.m_oPursuit = pursuit.CPursuit()
		self.m_oPursuit.SetGirl(oGirl)

	def GiveFlowers(self):
		self.m_oPursuit.GiveFlowers()