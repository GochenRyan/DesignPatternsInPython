# -*- coding: utf-8 -*-

import template

class CConcreteA(template.CAbstract):
	def primitiveOperation1(self):
		print "具体类A方法1实现"

	def primitiveOperation2(self):
		print "具体类A方法2实现"


class CConcreteB(template.CAbstract):
	def primitiveOperation1(self):
		print "具体类B方法1实现"

	def primitiveOperation2(self):
		print "具体类B方法2实现"