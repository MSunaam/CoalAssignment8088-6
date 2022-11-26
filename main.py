from Register import Register

AX = Register("AX", True)
AX.setData(4000)
AX.printContent()
print(AX.getHigh())
print(AX.getLow())
print(AX.getLow())
print(AX.getHigh())
