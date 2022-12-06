import tkinter as tk
from MainCode import stringToFunction, machineCodes
from Register_Instances import *
from Memory_Instances import *

window = tk.Tk()
window.title("MicroProcessor Emulator")
window.geometry('600x550')

# Global String
codeString = ''
# Label Register
labelRegister = tk.Label(window, text='Registers')
labelRegister.grid(row=0, column=0, padx=2, pady=2, sticky="NW")
# RegisterAX
labelAX = tk.Label(window, text='AX Register')
labelAX.grid(row=1, column=0, padx=2, pady=2)
labelAXData = tk.Label(window, text=''.join([str(x) for x in AX.getData()]))
labelAXData.grid(row=1, column=1, padx=2, pady=2)
# RegisterBX
labelBX = tk.Label(window, text='BX Register')
labelBX.grid(row=2, column=0, padx=2, pady=2)
labelBXData = tk.Label(window, text=''.join([str(x) for x in BX.getData()]))
labelBXData.grid(row=2, column=1, padx=2, pady=2)
# RegisterCX
labelCX = tk.Label(window, text='CX Register')
labelCX.grid(row=3, column=0, padx=2, pady=2)
labelCXData = tk.Label(window, text=''.join([str(x) for x in CX.getData()]))
labelCXData.grid(row=3, column=1, padx=2, pady=2)
# RegisterDX
labelDX = tk.Label(window, text='DX Register')
labelDX.grid(row=4, column=0, padx=2, pady=2)
labelDXData = tk.Label(window, text=''.join([str(x) for x in DX.getData()]))
labelDXData.grid(row=4, column=1, padx=2, pady=2)
# RegisterDS
labelDS = tk.Label(window, text='DS Register')
labelDS.grid(row=5, column=0, padx=2, pady=2)
labelDSData = tk.Label(window, text=''.join([str(x) for x in DS.getData()]))
labelDSData.grid(row=5, column=1, padx=2, pady=2)
# RegisterES
labelES = tk.Label(window, text='ES Register')
labelES.grid(row=6, column=0, padx=2, pady=2)
labelESData = tk.Label(window, text=''.join([str(x) for x in ES.getData()]))
labelESData.grid(row=6, column=1, padx=2, pady=2)
# RegisterCS
labelCS = tk.Label(window, text='CS Register')
labelCS.grid(row=7, column=0, padx=2, pady=2)
labelCSData = tk.Label(window, text=''.join([str(x) for x in CS.getData()]))
labelCSData.grid(row=7, column=1, padx=2, pady=2)
# RegisterSS
labelSS = tk.Label(window, text='SS Register')
labelSS.grid(row=8, column=0, padx=2, pady=2)
labelSSData = tk.Label(window, text=''.join([str(x) for x in SS.getData()]))
labelSSData.grid(row=8, column=1, padx=2, pady=2)


def overWriteLabels():
    # AX
    labelAXData = tk.Label(window, text=''.join(
        [str(x) for x in AX.getData()]))
    labelAXData.grid(row=1, column=1, padx=2, pady=2, sticky="NW")
    # BX
    labelBXData = tk.Label(window, text=''.join(
        [str(x) for x in BX.getData()]))
    labelBXData.grid(row=2, column=1, padx=2, pady=2, sticky="NW")
    # CX
    labelCXData = tk.Label(window, text=''.join(
        [str(x) for x in CX.getData()]))
    labelCXData.grid(row=3, column=1, padx=2, pady=2, sticky="NW")
    # DX
    labelDXData = tk.Label(window, text=''.join(
        [str(x) for x in DX.getData()]))
    labelDXData.grid(row=4, column=1, padx=2, pady=2, sticky="NW")
    # DS
    labelDSData = tk.Label(window, text=''.join(
        [str(x) for x in DS.getData()]))
    labelDSData.grid(row=5, column=1, padx=2, pady=2, sticky="NW")
    # ES
    labelESData = tk.Label(window, text=''.join(
        [str(x) for x in ES.getData()]))
    labelESData.grid(row=6, column=1, padx=2, pady=2, sticky="NW")
    # CS
    labelCSData = tk.Label(window, text=''.join(
        [str(x) for x in CS.getData()]))
    labelCSData.grid(row=7, column=1, padx=2, pady=2, sticky="NW")
    # SS
    labelSSData = tk.Label(window, text=''.join(
        [str(x) for x in SS.getData()]))
    labelSSData.grid(row=8, column=1, padx=2, pady=2, sticky="NW")
    # Memory 0
    labelMemory0 = tk.Label(window, text=''.join(
        [str(x) for x in mem['0'].getData()]))
    labelMemory0.grid(row=1, column=6, padx=2, pady=2, sticky="NW")
    # Memory 1
    labelMemory1 = tk.Label(window, text=''.join(
        [str(x) for x in mem['1'].getData()]))
    labelMemory1.grid(row=2, column=6, padx=2, pady=2, sticky="NW")
    # Memory 2
    labelMemory2 = tk.Label(window, text=''.join(
        [str(x) for x in mem['2'].getData()]))
    labelMemory2.grid(row=3, column=6, padx=2, pady=2, sticky="NW")
    # Memory 3
    labelMemory3 = tk.Label(window, text=''.join(
        [str(x) for x in mem['3'].getData()]))
    labelMemory3.grid(row=4, column=6, padx=2, pady=2, sticky="NW")
    # Memory 4
    labelMemory4 = tk.Label(window, text=''.join(
        [str(x) for x in mem['4'].getData()]))
    labelMemory4.grid(row=5, column=6, padx=2, pady=2, sticky="NW")
    # Memory 5
    labelMemory5 = tk.Label(window, text=''.join(
        [str(x) for x in mem['5'].getData()]))
    labelMemory5.grid(row=6, column=6, padx=2, pady=2, sticky="NW")
    # Memory 6
    labelMemory6 = tk.Label(window, text=''.join(
        [str(x) for x in mem['6'].getData()]))
    labelMemory6.grid(row=7, column=6, padx=2, pady=2, sticky="NW")
    # Memory 7
    labelMemory7 = tk.Label(window, text=''.join(
        [str(x) for x in mem['7'].getData()]))
    labelMemory7.grid(row=8, column=6, padx=2, pady=2, sticky="NW")
    # Memory 8
    labelMemory8 = tk.Label(window, text=''.join(
        [str(x) for x in mem['8'].getData()]))
    labelMemory8.grid(row=9, column=6, padx=2, pady=2, sticky="NW")
    # Memory 9
    labelMemory9 = tk.Label(window, text=''.join(
        [str(x) for x in mem['9'].getData()]))
    labelMemory9.grid(row=10, column=6, padx=2, pady=2, sticky="NW")
    # Memory A
    labelMemoryA = tk.Label(window, text=''.join(
        [str(x) for x in mem['A'].getData()]))
    labelMemoryA.grid(row=11, column=6, padx=2, pady=2, sticky="NW")
    # Memory B
    labelMemoryB = tk.Label(window, text=''.join(
        [str(x) for x in mem['B'].getData()]))
    labelMemoryB.grid(row=12, column=6, padx=2, pady=2, sticky="NW")
    # Memory C
    labelMemoryC = tk.Label(window, text=''.join(
        [str(x) for x in mem['C'].getData()]))
    labelMemoryC.grid(row=13, column=6, padx=2, pady=2, sticky="NW")
    # Memory D
    labelMemoryD = tk.Label(window, text=''.join(
        [str(x) for x in mem['D'].getData()]))
    labelMemoryD.grid(row=14, column=6, padx=2, pady=2, sticky="NW")
    # Memory E
    labelMemoryE = tk.Label(window, text=''.join(
        [str(x) for x in mem['E'].getData()]))
    labelMemoryE.grid(row=15, column=6, padx=2, pady=2, sticky="NW")
    # Memory F
    labelMemoryF = tk.Label(window, text=''.join(
        [str(x) for x in mem['F'].getData()]))
    labelMemoryF.grid(row=16, column=6, padx=2, pady=2, sticky="NW")


# User Input
labelL1 = tk.Label(window, text="Please Enter Assembly Command:")
labelL1.grid(row=0, column=3, padx=2, pady=2, sticky='W')

code = tk.Entry(window, justify=tk.LEFT, width=25, borderwidth=1)
# code.config(highlightbackground = "red")
code.grid(row=1, column=3, padx=2, pady=2, sticky='W')


def acceptCode():

    machineCodes.clear()
    codeString = (code.get())
    errorMsg = stringToFunction(codeString, machineCodes)
    if errorMsg is not None:
        labelCode = tk.Label(window, text=errorMsg, fg='red')
        labelCode.grid(row=3, column=3, padx=2, pady=2)
    else:
        opcodeOutput = tk.Label(
            window, text=machineCodes.returnCode(), bg='black', fg='white', width=30)
        opcodeOutput.grid(row=4, column=3, columnspan=2,
                          rowspan=3, padx=2, pady=2)
        # Refresh Labels
        overWriteLabels()
        code.delete(0,tk.END)


acceptCode = tk.Button(window, text='Execute', command=acceptCode)
acceptCode.grid(row=2, column=3, padx=2, pady=2)

# Memory
labelMemory = tk.Label(window, text='Memory')
labelMemory.grid(row=0, column=5, padx=2, pady=2, sticky='W')
# Memory 0
labelMemory0 = tk.Label(window, text='0th Location')
labelMemory0.grid(row=1, column=5, padx=2, pady=2, sticky='W')
labelMemory0Data = tk.Label(window, text=''.join(
    [str(x) for x in mem['0'].getData()]))
labelMemory0Data.grid(row=1, column=6, padx=2, pady=2, sticky='W')
# Memory 1
labelMemory1 = tk.Label(window, text='1st Location')
labelMemory1.grid(row=2, column=5, padx=2, pady=2, sticky='W')
labelMemory1Data = tk.Label(window, text=''.join(
    [str(x) for x in mem['1'].getData()]))
labelMemory1Data.grid(row=2, column=6, padx=2, pady=2, sticky='W')
# Memory 2
labelMemory2 = tk.Label(window, text='2nd Location')
labelMemory2.grid(row=3, column=5, padx=2, pady=2, sticky='W')
labelMemory2Data = tk.Label(window, text=''.join(
    [str(x) for x in mem['2'].getData()]))
labelMemory2Data.grid(row=3, column=6, padx=2, pady=2, sticky='W')
# Memory 3
labelMemory3 = tk.Label(window, text='3rd Location')
labelMemory3.grid(row=4, column=5, padx=2, pady=2, sticky='W')
labelMemory3Data = tk.Label(window, text=''.join(
    [str(x) for x in mem['3'].getData()]))
labelMemory3Data.grid(row=4, column=6, padx=2, pady=2, sticky='W')
# Memory 4
labelMemory4 = tk.Label(window, text='4th Location')
labelMemory4.grid(row=5, column=5, padx=2, pady=2, sticky='W')
labelMemory4Data = tk.Label(window, text=''.join(
    [str(x) for x in mem['4'].getData()]))
labelMemory4Data.grid(row=5, column=6, padx=2, pady=2, sticky='W')
# Memory 5
labelMemory5 = tk.Label(window, text='5th Location')
labelMemory5.grid(row=6, column=5, padx=2, pady=2, sticky='W')
labelMemory5Data = tk.Label(window, text=''.join(
    [str(x) for x in mem['5'].getData()]))
labelMemory5Data.grid(row=6, column=6, padx=2, pady=2, sticky='W')
# Memory 6
labelMemory6 = tk.Label(window, text='6th Location')
labelMemory6.grid(row=7, column=5, padx=2, pady=2, sticky='W')
labelMemory6Data = tk.Label(window, text=''.join(
    [str(x) for x in mem['6'].getData()]))
labelMemory6Data.grid(row=7, column=6, padx=2, pady=2, sticky='W')
# Memory 7
labelMemory7 = tk.Label(window, text='7th Location')
labelMemory7.grid(row=8, column=5, padx=2, pady=2, sticky='W')
labelMemory7Data = tk.Label(window, text=''.join(
    [str(x) for x in mem['7'].getData()]))
labelMemory7Data.grid(row=8, column=6, padx=2, pady=2, sticky='W')
# Memory 8
labelMemory8 = tk.Label(window, text='8th Location')
labelMemory8.grid(row=9, column=5, padx=2, pady=2, sticky='W')
labelMemory8Data = tk.Label(window, text=''.join(
    [str(x) for x in mem['8'].getData()]))
labelMemory8Data.grid(row=9, column=6, padx=2, pady=2, sticky='W')
# Memory 9
labelMemory9 = tk.Label(window, text='9th Location')
labelMemory9.grid(row=10, column=5, padx=2, pady=2, sticky='W')
labelMemory9Data = tk.Label(window, text=''.join(
    [str(x) for x in mem['9'].getData()]))
labelMemory9Data.grid(row=10, column=6, padx=2, pady=2, sticky='W')
# Memory A
labelMemoryA = tk.Label(window, text='A Location')
labelMemoryA.grid(row=11, column=5, padx=2, pady=2, sticky='W')
labelMemoryAData = tk.Label(window, text=''.join(
    [str(x) for x in mem['A'].getData()]))
labelMemoryAData.grid(row=11, column=6, padx=2, pady=2, sticky='W')
# Memory B
labelMemoryB = tk.Label(window, text='B Location')
labelMemoryB.grid(row=12, column=5, padx=2, pady=2, sticky='W')
labelMemoryBData = tk.Label(window, text=''.join(
    [str(x) for x in mem['B'].getData()]))
labelMemoryBData.grid(row=12, column=6, padx=2, pady=2, sticky='W')
# Memory C
labelMemoryC = tk.Label(window, text='C Location')
labelMemoryC.grid(row=13, column=5, padx=2, pady=2, sticky='W')
labelMemoryCData = tk.Label(window, text=''.join(
    [str(x) for x in mem['C'].getData()]))
labelMemoryCData.grid(row=13, column=6, padx=2, pady=2, sticky='W')
# Memory D
labelMemoryD = tk.Label(window, text='D Location')
labelMemoryD.grid(row=14, column=5, padx=2, pady=2, sticky='W')
labelMemoryDData = tk.Label(window, text=''.join(
    [str(x) for x in mem['D'].getData()]))
labelMemoryDData.grid(row=14, column=6, padx=2, pady=2, sticky='W')
# Memory E
labelMemoryE = tk.Label(window, text='E Location')
labelMemoryE.grid(row=15, column=5, padx=2, pady=2, sticky='W')
labelMemoryEData = tk.Label(window, text=''.join(
    [str(x) for x in mem['E'].getData()]))
labelMemoryEData.grid(row=15, column=6, padx=2, pady=2, sticky='W')
# Memory F
labelMemoryF = tk.Label(window, text='F Location')
labelMemoryF.grid(row=16, column=5, padx=2, pady=2, sticky='W')
labelMemoryFData = tk.Label(window, text=''.join(
    [str(x) for x in mem['F'].getData()]))
labelMemoryFData.grid(row=16, column=6, padx=2, pady=2, sticky='W')


window.mainloop()
