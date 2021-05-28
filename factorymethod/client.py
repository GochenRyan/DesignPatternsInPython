# -*- coding: utf-8 -*-

import factory

if __name__ == '__main__':
	oFactory = factory.CUndergraduateFactory()
	oStu = oFactory.CreateLeifeng()
	oStu.BuyRice()
	oStu.Sweep()
	oStu.Wash()