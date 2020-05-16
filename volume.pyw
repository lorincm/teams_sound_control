from tkinter import * 
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

window = Tk(className=" TVN")
window.geometry("200x150")
window.resizable(False, False)
window.iconbitmap('volume.ico')

var = DoubleVar()
scale = Scale( window, variable = var, orient=HORIZONTAL, sliderrelief='flat', from_=0, to=100, highlightthickness=20) #command = setSound(var)
scale.set(50)
scale.pack(fill=X, anchor=CENTER, pady=20)

def setSound():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process and session.Process.name() == "Teams.exe":
            tmp1=float(scale.get())/float(100.0)
            volume.SetMasterVolume(tmp1, None)
    window.after(200, setSound)

window.after(500, setSound)
window.mainloop()

#the pyw file extension prevents the useless cmd window to pop up
