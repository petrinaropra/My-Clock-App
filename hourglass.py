from kivy.config import Config
Config.set('graphics', 'resizable', False)
from kivy.app import App
import pytz
from datetime import datetime
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from playsound import playsound  
from time import strftime

Window.size = (400, 400)

class HourglassApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    sw_started = False
    sw_seconds = 0

    alarm_time = " "
    
    def on_start(self):
        Clock.schedule_interval(self.update, 0)  
        	  
    def update(self, nap):
        if self.sw_started:
            self.sw_seconds += nap

        self.root.ids.time.text = strftime('[size=60][font=GOTHICB.ttf]%I[/font]:%M %p[/size]\n %a, %B %d')
        
        
        m, s = divmod(self.sw_seconds, 60)
        self.root.ids.stopwatch.text = ('%02d:%02d.[size=40]%02d[/size]' %
                                        (int(m), int(s), int(s * 100 % 100)))
                                        
        if self.alarm_time == strftime('%I:%M %p'):
            #print(strftime('%S'))
            if strftime('%S') == '00' and strftime('%S') != '10':
                self.root.ids.hi.text = '[size=60]Wake Up![/size]'
                self.sound = SoundLoader.load('C:/Users/Able Valued Client/Downloads/Alarm Clock_alarm.wav')
                self.sound.play()
               
        current_time=strftime("[size=30]%H:%M:%S[/size]")
        self.root.ids.okay.text= "[size=30]Local Time[/size]"
        self.root.ids.okay1.text=current_time
        
        
        home = pytz.timezone("Asia/Tokyo")
        local_time=datetime.now(home)
        current_time1= local_time.strftime("%H:%M:%S")
        self.root.ids.okay2.text= "Tokyo"
        self.root.ids.okay3.text=current_time1
        
        
        home = pytz.timezone("Australia/Sydney")
        local_time=datetime.now(home)
        current_time2=local_time.strftime("%H:%M:%S")
        self.root.ids.okay4.text= "Sydney"
        self.root.ids.okay5.text=current_time2
        
        home = pytz.timezone("America/New_York")
        local_time=datetime.now(home)
        current_time3= local_time.strftime("%H:%M:%S")
        self.root.ids.okay6.text= "New York"
        self.root.ids.okay7.text=current_time3
        
        """
        home = pytz.timezone("Europe/Madrid")
        local_time=datetime.now(home)
        current_time=strftime("%H:%M:%S")
        self.root.ids.okay12.text= "Madrid"
        self.root.ids.okay13.text=current_time
        """
          
            
    def start_stop(self):
        self.root.ids.start_stop.text = 'Start' if self.sw_started else 'Stop'
        self.sw_started = not self.sw_started

    def reset(self):
        if self.sw_started:
            self.root.ids.start_stop.text = 'Start'
            self.sw_started = False

        self.sw_seconds = 0
        
    def press(self, alarm_time):
        if len(alarm_time) != 8:
            self.root.ids.hi.text = "Invalid time format!\nTry add a zero before the hour \nif it's less than 10 and or add PM/AM"    
        else:
            if int(alarm_time[0:2]) > 12:
                self.root.ids.hi.text = "Invalid HOUR format! Please try again..."
            elif int(alarm_time[3:5]) > 59:
                self.root.ids.hi.text = "Invalid MINUTE format! Please try again..."
            else:
                self.alarm_time = alarm_time
                self.root.ids.hi.text = "Setting the alarm now..."
                 
if __name__ == '__main__':
    
    HourglassApp().run()
