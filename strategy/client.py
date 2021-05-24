import context

if __name__ == '__main__':
    oContext = context.CContext("80%off")
    print oContext.GetResult(600)
    oContext = context.CContext("300to100")
    print oContext.GetResult(666)