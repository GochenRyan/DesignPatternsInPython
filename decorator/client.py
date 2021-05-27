# -*- coding: utf-8 -*-
import component
import decorator

if __name__ == '__main__':
	oFresnel = component.CPerson()
	oFresnel.SetName("菲涅尔")

	oTShirts = decorator.CTShirts()
	oBigTrouser = decorator.CBigTrouser()

	oTShirts.Decorate(oFresnel)
	oBigTrouser.Decorate(oTShirts)

	oBigTrouser.Show()