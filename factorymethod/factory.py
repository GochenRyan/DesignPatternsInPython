# -*- coding: utf-8 -*-

class IFactory:
	def CreateLeifeng(self):
		pass

class CUndergraduateFactory(object, IFactory):
	def CreateLeifeng(self):
		import leifeng
		return leifeng.CUndergraduate()

class CVolunteerFactory(object, IFactory):
	def CreateLeifeng(self):
		import leifeng
		return leifeng.CVolunteer()