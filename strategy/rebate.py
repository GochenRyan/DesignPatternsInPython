import base

class CCashRebate(base.CCashBase):
	def __init__(self, fRebate):
		self.m_fRebate = fRebate

	def AcceptCash(self, fCash):
		return fCash * self.m_fRebate