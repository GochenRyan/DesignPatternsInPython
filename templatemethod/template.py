class CAbstract(object):
	def primitiveOperation1(self):
		pass

	def primitiveOperation2(self):
		pass

	def TemplateMethod(self):
		self.primitiveOperation1()
		self.primitiveOperation2()