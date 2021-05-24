import base

class CCashReturn(base.CCashBase):
	def __init__(self, fCondition, fReturn):
		self.m_fCondition = fCondition
		self.m_fReturn = fReturn

	def AcceptCash(self, fCash):
		if fCash >= self.m_fCondition:
			fRealCash = fCash - int(fCash / self.m_fCondition) * self.m_fReturn
		else:
			fRealCash = fCash
		return fRealCash