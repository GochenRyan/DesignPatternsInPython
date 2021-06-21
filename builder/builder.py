# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod, abstractproperty
import product

class CBuilder(object):
	__metaclass__ = ABCMeta

	@abstractproperty
	def product(self):
		pass

	@abstractmethod
	def producePartA(self):
		pass

	@abstractmethod
	def producePartB(self):
		pass

	@abstractmethod
	def producePartC(self):
		pass

class CConcreteBuilder(CBuilder):
	def __init__(self):
		self.m_oProduct = product.CProduct()

	@property
	def product(self):
		return self.m_oProduct

	def producePartA(self):
		self.m_oProduct.add("partA")

	def producePartB(self):
		self.m_oProduct.add("partB")

	def producePartC(self):
		self.m_oProduct.add("partC")