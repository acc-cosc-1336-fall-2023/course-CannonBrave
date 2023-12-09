from tkinter import Frame
from tkinter import Button
import clock_gui

class MainFrame(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.canvases = []
        for x in range(4):
            self.canvases.append(clock_gui.Clock(self,
                              zone=['Eastern Standard Time', 'Central Standard Time',
                                    'Mountain Standard Time', 'Pacific Standard Time'][x], row=0, column=x))

        Button(self, text='Slow motion',
                   command=self.slow).grid(row=3, column=0)

        Button(self, text='Normal speed',
                   command=self.normal_speed).grid(row=3, column=1)

        Button(self, text='Fast forward',
                   command=self.speed).grid(row=3, column=2)

    def slow(self):
        '''Halve the speed of the clocks.'''
        for canvas in self.canvases:
            canvas.time_scale /= 2
            canvas.refresh(forced=True)

    def normal_speed(self):
        '''Set the speed of the clocks back to normal.'''
        for canvas in self.canvases:
            canvas.time_scale = 1
            canvas.refresh(forced=True)

    def speed(self):
        '''Double the speed of the clocks.'''
        for canvas in self.canvases:
            canvas.time_scale *= 2
            canvas.refresh(forced=True)