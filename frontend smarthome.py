from backend import *
from tkinter import *

class SmartHomeSystem:
    def __init__(self):
        self.root = Tk()
        self.win = self.root
        self.root.title("Smart Home System")
        self.mainFrame = Frame(self.root)
        self.mainFrame.grid(column=0, row=0)
        self.devices = [
            "Smart Plug: Switched Off, Consumption Rate: 45",
            "Smart Plug: Switched Off, Consumption Rate: 45",
            "Smart Speaker: Streaming Service - Amazon, Status - Off"
        ]
        self.createWidgets()

    def createWidgets(self):
        rowNum = 0
        self.lblDeviceNames = []
        for info in self.devices:
            self.deviceFrame = Frame(self.mainFrame)
            self.deviceFrame.grid(column=0, row=rowNum+1)
            lblDeviceName = Label(self.deviceFrame, text=info)
            lblDeviceName.grid(column=0, row=rowNum+1, sticky="w")
            self.lblDeviceNames.append(lblDeviceName)

            btnToggle = Button(self.deviceFrame, text="Toggle", command=lambda index=self.lblDeviceNames.index(lblDeviceName), deviceName=lblDeviceName: self.toggleDevice(index, deviceName))
            btnToggle.grid(column=1, row=rowNum+1, sticky="w")

            btnEdit = Button(self.deviceFrame, text="Edit", command=lambda deviceName=lblDeviceName: self.editDevice(deviceName))
            btnEdit.grid(column=2, row=rowNum+1)

            btnDelete = Button(self.deviceFrame, text="Delete", command=lambda frame=self.deviceFrame: [frame.destroy(), self.deleteDevice(deviceName=lblDeviceName)])
            btnDelete.grid(column=3, row=rowNum+1)

            rowNum += 1

        btnAllOn = Button(self.mainFrame, text="Turn All On", command=self.turnAllOn)
        btnAllOn.grid(column=0, row=0, sticky="we")

        btnAllOff = Button(self.mainFrame, text="Turn All Off", command=self.turnAllOff)
        btnAllOff.grid(column=1, row=0, columnspan=4, sticky="we")

        btnAdd = Button(self.mainFrame, text="Add", command=self.addDevice)
        btnAdd.grid(column=0, row=rowNum+1, sticky="we")

    def toggleDevice(self, index, deviceName):
        current_status = deviceName.cget("text")
        new_status = "On" if "Off" in current_status else "Off"
        new_text = current_status.replace("Off", new_status).replace("On", new_status)
        deviceName.config(text=new_text)

    def editDevice(self, deviceName):
        print(f"Edit device: {deviceName.cget('text')}")

    def deleteDevice(self, deviceName):
        print(f"Delete device: {deviceName.cget('text')}")
        deviceName.master.destroy()

    def turnAllOn(self):
        for lblDeviceName in self.lblDeviceNames:
            self.toggleDevice(None, lblDeviceName)

    def turnAllOff(self):
        for lblDeviceName in self.lblDeviceNames:
            self.toggleDevice(None, lblDeviceName)

    def addDevice(self):
        print("Add device")

    def run(self):
        self.root.mainloop()

def main():
    system = SmartHomeSystem()
    system.run()

if __name__ == "__main__":
    main()

