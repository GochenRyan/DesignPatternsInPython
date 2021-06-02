from copy import copy, deepcopy

__all__ = ('CResume',)

class CWorkExperience(object):
	def __init__(self):
		self.m_sDate = ""
		self.m_sCompany = ""

	def SetDate(self, sDate):
		self.m_sDate = sDate

	def GetDate(self):
		return self.m_sDate

	def SetCompany(self, sCompany):
		self.m_sCompany = sCompany

	def GetCompany(self):
		return self.m_sCompany


class CResume(object):
	def __init__(self, sName):
		self.m_sName = sName
		self.m_oWorkExperience = CWorkExperience()

	def SetWorkExperience(self, sDate, sCompany):
		self.m_oWorkExperience.SetDate(sDate)
		self.m_oWorkExperience.SetCompany(sCompany)

	def __copy__(self):
		oWorkExperience = copy(self.m_oWorkExperience)
		new = self.__class__(self.m_sName)
		new.m_oWorkExperience = oWorkExperience
		new.__dict__.update(self.__dict__)
		return new

	def __deepcopy__(self, memodict={}):
		oWorkExperience = deepcopy(self.m_oWorkExperience, memodict)
		new = self.__class__(self.m_sName)
		new.m_oWorkExperience = oWorkExperience
		new.__dict__ = deepcopy(self.__dict__, memodict)
		return new

	def __str__(self):
		return "id: %s, name: %s, date: %s, company: %s" % (id(self), self.m_sName, self.m_oWorkExperience.GetDate(), self.m_oWorkExperience.GetCompany())
