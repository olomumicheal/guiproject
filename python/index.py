import tkinter as tk
import tkinter.font as tkFont
import time


def navbar(self, page):
    page = page
    timerBtn = tk.Button(self.master, text='Timer', command=lambda: timers(self, page))
    timerBtn.place(x=0, y=550, width=333, height=50)

    ClockBtn = tk.Button(self.master, text='Clock', command=lambda: clocks(self, page))
    ClockBtn.place(x=333, y=550, width=333, height=50)

    stopWatchBtn = tk.Button(self.master, text='Stop Watch', command=lambda: stopWatchs(self, page))
    stopWatchBtn.place(x=666, y=550, width=333, height=50)


def timers(self, page):
    if page != 'Timer':
        self.master.destroy()
        root = tk.Tk()
        app = timer(root)


def clocks(self, page):
    if page != 'Clock':
        self.master.destroy()
        root = tk.Tk()
        app = clock(root)


def stopWatchs(self, page):
    if page != 'StopWatch':
        self.master.destroy()
        root = tk.Tk()
        app = stopWatch(root)


class timer():
    def __init__(self, master):
        self.master = master
        self.master.title("Clock Clone")
        self.master.geometry("999x600")

        self.place()

    def place(self):
        self.hoursLabel = tk.Label(self.master, text='Hours')
        self.hoursLabel.place(x=220, y=200)

        self.hoursEntry = tk.Entry(self.master)
        self.hoursEntry.place(x=200, y=200, width=20)

        self.hoursUpArrow = tk.Button(self.master, text="\N{UPWARDS BLACK ARROW}",
                                      command=lambda: self.change('hours', 'Up'))
        self.hoursUpArrow.place(x=201, y=170)

        self.hoursDownArrow = tk.Button(self.master, text="\N{DOWNWARDS BLACK ARROW}",
                                        command=lambda: self.change('hours', 'Down'))
        self.hoursDownArrow.place(x=201, y=225)

        self.minsLabel = tk.Label(self.master, text='Minutes')
        self.minsLabel.place(x=520, y=200)

        self.minsEntry = tk.Entry(self.master)
        self.minsEntry.place(x=500, y=200, width=20)

        self.minsUpArrow = tk.Button(self.master, text="\N{UPWARDS BLACK ARROW}",
                                     command=lambda: self.change('mins', 'Up'))
        self.minsUpArrow.place(x=501, y=170)

        self.minsDownArrow = tk.Button(self.master, text="\N{DOWNWARDS BLACK ARROW}",
                                       command=lambda: self.change('mins', 'Down'))
        self.minsDownArrow.place(x=501, y=225)

        self.secondsLabel = tk.Label(self.master, text='Seconds')
        self.secondsLabel.place(x=820, y=200)

        self.secondsEntry = tk.Entry(self.master)
        self.secondsEntry.place(x=800, y=200, width=20)

        self.secondsUpArrow = tk.Button(self.master, text="\N{UPWARDS BLACK ARROW}",
                                        command=lambda: self.change('sec', 'Up'))
        self.secondsUpArrow.place(x=801, y=170)

        self.secondsDownArrow = tk.Button(self.master, text="\N{DOWNWARDS BLACK ARROW}",
                                          command=lambda: self.change('sec', 'Down'))
        self.secondsDownArrow.place(x=801, y=225)

        self.cancelButton = tk.Button(self.master, text='Cancel', command=self.cancel)
        self.cancelButton.place(x=150, y=400)

        self.startButton = tk.Button(self.master, text='Start', command=self.start)
        self.startButton.place(x=750, y=400)

        navbar(self, 'Timer')

    def change(self, time, change):
        changeable = 0
        if time == 'hours':
            changeable = self.hoursEntry.get()
        elif time == 'mins':
            changeable = self.minsEntry.get()
        elif time == 'sec':
            changeable = self.secondsEntry.get()

        if changeable == '':
            changeable = 0
        else:
            changeable = int(changeable)

        if time == 'hours':
            if change == 'Up':
                changeable += 1
            else:
                if changeable > 0:
                    changeable -= 1
            self.hoursEntry.delete(0, tk.END)
            self.hoursEntry.insert(0, str(changeable))
        elif time == 'mins':
            if change == 'Up' and changeable < 60:
                changeable += 1
            else:
                if changeable > 0:
                    changeable -= 1
            self.minsEntry.delete(0, tk.END)
            self.minsEntry.insert(0, str(changeable))
        elif time == 'sec':
            if change == 'Up' and changeable < 60:
                changeable += 1
            else:
                if changeable > 0:
                    changeable -= 1
            self.secondsEntry.delete(0, tk.END)
            self.secondsEntry.insert(0, str(changeable))

    def cancel(self):
        self.place()
        self.TimeLabel.place_forget()

    def start(self):
        self.hours = self.hoursEntry.get()
        self.mins = self.minsEntry.get()
        self.seconds = self.secondsEntry.get()

        if self.hours == '':
            self.hours = '00'
        if self.mins == '':
            self.mins = '00'
        if self.seconds == '':
            self.seconds = '00'

        self.hours = int(self.hours)
        self.mins = int(self.mins)
        self.seconds = int(self.seconds)

        self.hoursLabel.place_forget()
        self.hoursEntry.place_forget()
        self.hoursUpArrow.place_forget()
        self.hoursDownArrow.place_forget()
        self.minsLabel.place_forget()
        self.minsEntry.place_forget()
        self.minsUpArrow.place_forget()
        self.minsDownArrow.place_forget()
        self.secondsLabel.place_forget()
        self.secondsEntry.place_forget()
        self.secondsUpArrow.place_forget()
        self.secondsDownArrow.place_forget()

        fontStyle = tkFont.Font(family="Lucida Grande", size=50)
        Time = str(self.hours) + ':' + str(self.mins) + ':' + str(self.seconds)

        self.TimeLabel = tk.Label(self.master, text=Time, font=fontStyle)
        self.TimeLabel.place(x=380, y=200)
        self.on = True
        self.timer(Time)

    def timer(self, Time):
        time.sleep(1)
        self.seconds -= 1
        if self.seconds <= 0:
            if self.mins > 0:
                self.seconds = 60
                self.mins -= 1
            else:
                if self.hours >= 1:
                    self.mins = 59
                    self.seconds = 60
                    self.hours -= 1
                else:
                    self.on = False

        Time = str(self.hours) + ':' + str(self.mins) + ':' + str(self.seconds)
        self.TimeLabel.config(text=Time)

        if self.on == True:
            self.timer(Time)


class clock():
    def __init__(self, master):
        self.master = master
        self.master.title("Clock Clone")
        self.master.geometry("999x600")

        navbar(self, 'Clock')


class stopWatch():
    def __init__(self, master):
        self.master = master
        self.master.title("Clock Clone")
        self.master.geometry("999x600")

        navbar(self, 'StopWatch')


root = tk.Tk()
app = timer(root)
root.mainloop()