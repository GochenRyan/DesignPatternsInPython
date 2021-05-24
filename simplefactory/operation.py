class COperation(object):
	def __init__(self):
		self.m_iNumberA = 0
		self.m_iNumberB = 0

	def GetNumberA(self):
		return self.m_iNumberA

	def GetNumberB(self):
		return self.m_iNumberB

	def SetNumberA(self, iNumberA):
		self.m_iNumberA = iNumberA

	def SetNumberB(self, iNumberB):
		self.m_iNumberB = iNumberB

	def GetResult(self):
		return 0


class CAdd(COperation):
	def __init__(self):
		super(CAdd, self).__init__()

	def GetResult(self):
		return (self.m_iNumberA + self.m_iNumberB)

class CSub(COperation):
	def __init__(self):
		super(CSub, self).__init__()

	def GetResult(self):
		return (self.m_iNumberA - self.m_iNumberB)

class CMul(COperation):
	def __init__(self):
		super(CMul, self).__init__()

	def GetResult(self):
		return (self.m_iNumberA * self.m_iNumberB)

class CDiv(COperation):
	def __init__(self):
		super(CDiv, self).__init__()

	def GetResult(self):
		fResult = None
		try:
			fResult = float(self.m_iNumberA) / self.m_iNumberB
		except ZeroDivisionError as e:
			print "except: ", e
		return fResult
