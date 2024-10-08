import time
import plyer
from plyer import notification
from windows_toasts import Toast, WindowsToaster
import tkinter as tk
from tkinter import ttk, messagebox
import winsound



class PomodoroTimer:
    #init will run as soon as a PomodoroTimer object is created
    def __init__(self, masterWindow):
        #
        self.masterWindow = masterWindow
        self.masterWindow.title("Pomodoro")
        self.masterWindow.geometry("600x600")

        fontSizeNorm = 100
        fontSizeLarge = 200

        # time display
        self.timerLabel = tk.Label(masterWindow, text= "0", font= ("Comic Sans MS", fontSizeNorm))
        self.timerLabel.pack()

        # button init
        self.startButton = tk.Button(masterWindow, text= "Start",font= fontSizeNorm, command=self.timer)
        self.startButton.pack()

        self.pauseButton = tk.Button(masterWindow, text= "Pause",font= fontSizeNorm, command=self.pause)
        self.pauseButton.pack(pady=10)

        exitButton = tk.Button(masterWindow, text= "Exit",font= fontSizeNorm + 30, command= self.exitFunction)
        exitButton.pack(pady=20)

        # timer init
        # self.workTime = 4*60*60
        # self.breakTime = 2*60*60
        self.workTime = 4
        self.breakTime = 2
        self.currentTime = self.breakTime

        self.ifBreak = True
        self.isRunning = True

        self.timer()

    def exitFunction(self):
        self.masterWindow.destroy()

    
    def timer(self):
        self.startButton.config(state=tk.DISABLED)
        if self.isRunning == True:
            #clock formating
            second = self.currentTime % 60
            minute = (self.currentTime // 60) % 60
            hour = self.currentTime // (60 * 60)
            #print ("running")
            if self.currentTime > -1:
                self.timerLabel.config(text=(str(hour) + ":" + str(minute) + ":"+ str(second)))
                self.currentTime -= 1
                self.masterWindow.after(1000, self.timer)
            elif self.currentTime == -1:
                if self.ifBreak == True:
                    send_notification("Pomo", "Break Over")
                    self.currentTime = self.workTime
                    self.ifBreak = False
                    self.startButton.config(state=tk.ACTIVE)
                    self.playSound()
                else:
                    send_notification("Pomo", "Work Over")
                    self.ifBreak = True
                    self.currentTime = self.breakTime
                    self.startButton.config(state=tk.ACTIVE)
                    self.playSound()
        elif self.isRunning == False:
            print("not running")

    def pause(self):
        if self.isRunning == True:
            # save current time
            self.pausedTime = self.currentTime
            self.isRunning = False
            self.pauseButton.config(text= "Paused")
            self.timer()

        elif self.isRunning == False:
            self.currentTime = self.pausedTime
            self.isRunning = True
            self.pauseButton.config(text= "Pause")
            self.timer()

    #plays the windows Ring03 sound
    def playSound(self):
        winsound.PlaySound("Ring03.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
            
        
# from message box            
# def send_notification(header = "Blank", messageToSend = "Blank"):
#     notification.notify(title= header, message=messageToSend, app_name= "pomo", timeout= 10)

# Send notifications via win10toast
def send_notification(header = "Blank", messageToSend = "Blank"):
    toaster = WindowsToaster(header)
    newToast = Toast()
    newToast.text_fields = [messageToSend]
    toaster.show_toast(newToast)
    

# create tkinter window and Pomodoro class obj
def main():
    mainWindow = tk.Tk()
    coolClass = PomodoroTimer(mainWindow)
    # keep the window up
    mainWindow.mainloop()


if __name__ == "__main__":
    main()