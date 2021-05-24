import base
import normal
import rebate
import cashreturn

class CContext(object):
	def __init__(self, sType):
		if sType == "normal":
			oCashStrategy = normal.CCashNormal()
		elif sType == "80%off":
			oCashStrategy = rebate.CCashRebate(0.8)
		elif sType == "300to100":
			oCashStrategy = cashreturn.CCashReturn(300, 100)
		else:
			oCashStrategy = base.CCashBase()

		self.m_oCashStrategy = oCashStrategy

	def GetResult(self, fCash):
		fRealCash = self.m_oCashStrategy.AcceptCash(fCash)
		return fRealCash