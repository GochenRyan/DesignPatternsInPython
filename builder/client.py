# -*- coding: utf-8 -*-

import builder
import director

if __name__ == '__main__':
	oDirector = director.CDirector()
	oBuilder = builder.CConcreteBuilder()
	oDirector.builder = oBuilder
	oDirector.buildMinProduct()
	oBuilder.product.printParts()

	oBuilder = builder.CConcreteBuilder()
	oDirector.builder = oBuilder
	oDirector.buildMaxProduct()
	oBuilder.product.printParts()

	# 无需Director
	oBuilder = builder.CConcreteBuilder()
	oBuilder.producePartB()
	oBuilder.producePartC()
	oBuilder.product.printParts()