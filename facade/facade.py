# -*- coding: utf-8 -*-

import subsystem

class CFacade(object):
	def __init__(self):
		self.m_oSystemOne = subsystem.CSubSystemOne()
		self.m_oSystemTwo = subsystem.CSubSystemTwo()
		self.m_oSystemThree = subsystem.CSubSystemThree()
		self.m_oSystemFour = subsystem.CSubSystemFour()

	def MethodA(self):
		print "----方法组A----"
		self.m_oSystemOne.MethodOne()
		self.m_oSystemTwo.MethodTwo()
		self.m_oSystemFour.MethodFour()

	def MethodB(self):
		print "----方法组B----"
		self.m_oSystemThree.MethodThree()