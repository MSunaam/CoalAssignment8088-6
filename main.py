from commands import *
from Register_Instances import *
from Memory_Instances import *

AL.input(5)
BL.input(2)
# mem['0'].input(5)
OR(3, 'al', 'bl')
AL.printContent()
# mem['0'].printMemory()
