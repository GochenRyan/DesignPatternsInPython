import simplefactory

if __name__ == '__main__':
   oPer = simplefactory.CSimpleFactory.CreateOperate("/")
   oPer.SetNumberA(666)
   oPer.SetNumberB(2333)
   print oPer.GetResult()