import os
import sys
import time
import socket
from tkinter import *

def Printlabels3dig ():
    file = "temp.zpl"
    ip = ipi.get()
    port = porti.get()
    labels = labelsi.get()

    for x in range(0, labels):
        strx = str("%03d" % (x))
        stri = "^BXB,12,200^FO96,1325^FDSabcdef000_"+ strx +"_v^SF"
        stri2 = "^BXI,12,200^FO360,1325^FDSabcdef000_"+ strx +"_v^SF"
        stri3 = "^BXR,12,200^FO624,1325^FDSabcdef000_"+ strx +"_v^SF"
        stri4 = "^BXN,12,200^FO888,1325^FDSabcdef000_"+ strx +"_v^SF"
        stri5 = "^FO73,970^A0,54,0^FR^FB1055,1,0,C,0^FDSabcdef000_"+ strx +"_v^SF"

        with open("new def.zpl") as infile, open(file, 'w') as outfile:
            for line in infile:
                line = line.replace("^BXB,12,200^FO96,1325^FDSabcdef000_001_v^SF", stri)
                line = line.replace("^BXI,12,200^FO360,1325^FDSabcdef000_001_v^SF", stri2)
                line = line.replace("^BXR,12,200^FO624,1325^FDSabcdef000_001_v^SF", stri3)
                line = line.replace("^BXN,12,200^FO888,1325^FDSabcdef000_001_v^SF", stri4)
                line = line.replace("^FO73,970^A0,54,0^FR^FB1055,1,0,C,0^FDSabcdef000_001_v^SF", stri5)
                outfile.write(line)
        s = socket.socket()
        s.connect((ip, port))
        f = open(file, "rb")
        l = f.read(1024)
        while (l):
            s.send(l)
            l = f.read(1024)
        s.close()
        print("done")
        time.sleep(1)
    time.sleep(10)
    os.remove("temp.zpl")

def Createlabels3dig ():
    labels = labelsi.get()

    for x in range(0, labels):

        strx = str("%03d" % (x))
        stri = "^BXB,12,200^FO96,1325^FDSabcdef000_"+ strx +"_v^SF"
        stri2 = "^BXI,12,200^FO360,1325^FDSabcdef000_"+ strx +"_v^SF"
        stri3 = "^BXR,12,200^FO624,1325^FDSabcdef000_"+ strx +"_v^SF"
        stri4 = "^BXN,12,200^FO888,1325^FDSabcdef000_"+ strx +"_v^SF"
        stri5 = "^FO73,970^A0,54,0^FR^FB1055,1,0,C,0^FDSabcdef000_"+ strx +"_v^SF"
        out = "new" + strx + ".zpl"

        with open("new def.zpl") as infile, open(out, 'w') as outfile:
            for line in infile:
                line = line.replace("^BXB,12,200^FO96,1325^FDSabcdef000_001_v^SF", stri)
                line = line.replace("^BXI,12,200^FO360,1325^FDSabcdef000_001_v^SF", stri2)
                line = line.replace("^BXR,12,200^FO624,1325^FDSabcdef000_001_v^SF", stri3)
                line = line.replace("^BXN,12,200^FO888,1325^FDSabcdef000_001_v^SF", stri4)
                line = line.replace("^FO73,970^A0,54,0^FR^FB1055,1,0,C,0^FDSabcdef000_001_v^SF", stri5)
                outfile.write(line)

def createlabels():
    Createlabels3dig(labelsi)

def start():
    seq = seqi.get()
    if seq == 1:
        Printlabels3dig()
    elif seq == 2:
        Createlabels3dig()

master = Tk()

master.title("Python shipping label tool")
master.config(background="dark gray")
master.grid_columnconfigure(1, minsize=100)
ipi = StringVar()
porti = IntVar()
labelsi = IntVar()
progi = IntVar()
seqi = IntVar()

Title = Label(master, text="Python tool for printing unique shipping labels from a slam", bg="dark gray", font="Frutiger 18 bold")
Title.grid(row=1, column=2, columnspan=4)
ip_l = Label(master, text="Enter the ip address", bg="dark gray")
ip_l.grid(row=2, column=3)
port_l = Label(master, text="Enter the port number", bg="dark gray")
port_l.grid(row=3, column=3)
labels_l = Label(master, text="Enter the amount of required Labels", bg="dark gray")
labels_l.grid(row=4, column=3)

ip_e = Entry(master, textvariable = ipi)
ip_e.grid(row=2, column=4)
port_e = Entry(master, textvariable = porti)
port_e.grid(row=3, column=4)
labels_e = Entry(master, textvariable = labelsi)
labels_e.grid(row=4, column=4)

print_b = Radiobutton(master, text="print", variable=seqi, value=1, bg="dark gray")
print_b.grid(row=5, column=3)
create_b = Radiobutton(master, text="Create", variable=seqi, value=2, bg="dark gray")
create_b.grid(row=5, column=4)

startButton = Button(master, text="Start Script", command=start)
startButton.grid(row=6, column=5)
exitButton = Button(master, text="    Exit    ", command=sys.exit)
exitButton.grid(row=6, column=2)

#ip_e.grid(row=2, column=3)
#port_e.grid(row=2, column=8)
#titleFrame = Frame(master)
#titleFrame.grid(row=1, column=1)





#if create == "p":
#    printlabels(length)
#elif create == "c":
#    createlabels(length)
#else:
#    print("no p or c picked up, please try again, better luck next time")
master.mainloop()