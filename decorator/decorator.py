# -*- coding: utf-8 -*-
import component

class CFinery(component.CPerson):
	def __init__(self):
		super(CFinery, self).__init__()
		self.m_oComponent = None

	def Decorate(self, oComponent):
		self.m_oComponent = oComponent

	def Show(self):
		if self.m_oComponent:
			self.m_oComponent.Show()


class CTShirts(CFinery):
	def Show(self):
		print "大T恤",
		super(CTShirts, self).Show()

class CBigTrouser(CFinery):
	def Show(self):
		print "垮裤",
		super(CBigTrouser, self).Show()