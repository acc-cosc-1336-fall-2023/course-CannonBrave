import tkinter
import time
import math
import clock

TIME_ZONES = {"Atlantic Standard Time": -4, "Eastern Standard Time": -5, "Central Standard Time": -6 ,
              "Mountain Standard Time": -7, "Pacific Standard Time": -8, "Alaska Standard Time": -9 ,
              "Hawaii Standard Time": -10, "Samoa Standard Time": -11, "Greenwich Mean Time": 0 ,
              "British Summer Time": 1, "Central European Time": 1, "Eastern European Time": 2 ,
              "Charlie Time(Mid East)": 3, "Delta Time(Mid East": 4, "Australia Western Standard Time": 8
             }

class Clock(object):

    def __init__(self, tk, zone=None, **kargs):
        self.width = 200
        self.height = 200

        self.internal_frame = tkinter.Frame(tk, borderwidth=3, relief=tkinter.GROOVE)

        self.canvas = tkinter.Canvas(self.internal_frame, width= self.width, height = 250)
        self.canvas.grid()

        self.canvas.after(300, self.refresh)

        if time.daylight:
            dlt = time.altzone
        else:
            dlt = time.timezone

        self.diff = dlt #TIME_ZONES[zone]

        self.local_offset = self.diff
        self.now = time.time()          # Allow fast-forwarding
        self.interval = 500

        self.var = tkinter.StringVar(self.internal_frame)
        self.var.set('local')
        option = tkinter.OptionMenu(self.internal_frame, self.var, *TIME_ZONES)
        option.grid(sticky='ew')
        self.internal_frame.grid(**kargs)
        self.time_scale = 1

        def callback(*args):
            self.diff = TIME_ZONES[self.var.get()]

        self.var.trace("w", callback)
        self.var.set(zone)

    def refresh(self, forced=False):
        '''Redraw the clock. If forced is True, display it now. If forced is
        False, register a redraw for later.'''

        self.now = self.now + self.interval / 1000 * self.time_scale
        self.canvas.delete(tkinter.ALL)

        self.draw_clock_rim()
        self.draw_tick_marks()
        self.draw_clock_face()
        self.hands_colour = "black" if self.hour < 12 else "white"

        self.draw_hour_hand()
        self.draw_minute_hand()
        self.draw_second_hand()
        self.draw_larger_tick_marks()
        self.draw_time_text()

        if not forced:
            self.canvas.after(self.interval, self.refresh)

    def draw_clock_rim(self):
        self.canvas.create_oval(10, 10, self.width - 10,
                                self.height - 10, width=2, fill="#334455")

    def draw_tick_marks(self):
        for i in range(0, 12):
            angle = math.radians(i / 12 * 360)
            outer_length = 90
            inner_length = 80

            self.canvas.create_line(
                math.cos(angle) * inner_length + self.width / 2,
                math.sin(angle) * inner_length + self.width / 2,
                math.cos(angle) * outer_length + self.width / 2,
                math.sin(angle) * outer_length + self.width / 2,
                fill='white', width=3
            )

    def draw_clock_face(self):
        # Draw a light or dark face depending on whether it's before noon or
        # after.
        utc_hour = (clock.get_hours_since_midnight(self.now)) % 24

        self.hour = clock.time_from_utc(self.diff, utc_hour)
        self.canvas.create_oval(15, 15, self.width - 15, self.height - 15,
                                width=2, fill="#e0e8ff" if self.hour < 12 else "#334")

    def draw_hour_hand(self):
        hours_angle = (self.hour % 12) / 12 * 360
        self._draw_hand(hours_angle, 30, arrow=tkinter.FIRST,
                        arrowshape=(50, 2, 2), fill=self.hands_colour)
        self._draw_hand(hours_angle + 180, 5, fill=self.hands_colour)

    def _draw_hand(self, degrees, length, **kw):
        '''Draw a clock hand on this Clock at angle degrees length pixels
        long. kw contains information about the hand colour and shape of
        the hand.'''

        angle = math.radians(degrees - 90)

        self.canvas.create_line(self.width / 2, self.height / 2,
                                math.cos(angle) * length + self.width / 2,
                                math.sin(angle) * length + self.width / 2,
                                **kw)

    def draw_minute_hand(self):
        self.minutes = clock.get_minutes((self.now))
        minutes_angle = self.minutes / 60 * 360

        if clock.time_from_utc(0, self.diff) % 1 == 0.5:
            minutes_angle += 180
        elif clock.time_from_utc(0, self.diff) % 1 == 0.75:
           minutes_angle += 270

        self._draw_hand(minutes_angle, 30, arrow=tkinter.FIRST,
                        arrowshape=(80, 2, 2), fill=self.hands_colour)
        self._draw_hand(minutes_angle + 180, 5, fill=self.hands_colour)


    def draw_second_hand(self):
        self.seconds = clock.get_seconds(self.now)
        seconds_angle = self.seconds / 60 * 360

        self._draw_hand(seconds_angle, 70, fill='red',
                        width=2, arrow=tkinter.FIRST, arrowshape=(70, 9, 2))

        self._draw_hand(seconds_angle + 180, 18, fill='red',
                        arrow=tkinter.LAST, arrowshape=(8, 5, 5), width=2)

        self._draw_hand(seconds_angle + 180, 20, fill='red')
    
    def draw_larger_tick_marks(self):
        '''
        Draw the four larger tick marks at noon, 3, 6, and 9.
        '''

        for i in range(0, 12, 3):
            angle = math.radians(i / 12 * 360)
            outer_length = 90
            inner_length = 70
            self.canvas.create_line(
                math.cos(angle) * inner_length + self.width / 2,
                math.sin(angle) * inner_length + self.width / 2,
                math.cos(angle) * outer_length + self.width / 2,
                math.sin(angle) * outer_length + self.width / 2,
                width=5
            )

    def draw_time_text(self):
        self.canvas.create_text(95, 225, text=clock.get_time(int(self.hour), int(self.minutes),
                                                      int(self.seconds), 24), fill="red")
            


        
