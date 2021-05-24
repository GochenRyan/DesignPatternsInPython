import operation

class CSimpleFactory(object):
	@classmethod
	def CreateOperate(cls, sOperate):
		if sOperate == "+":
			oOper = operation.CAdd()
		elif sOperate == "-":
			oOper = operation.CSub()
		elif sOperate == "*":
			oOper = operation.CMul()
		elif sOperate == "/":
			oOper = operation.CDiv()
		else:
			oOper = operation.COperation()
		return oOper