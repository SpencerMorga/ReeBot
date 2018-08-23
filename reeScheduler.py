import sys
import os
import threading
import time
from datetime import datetime

class ReeScheduler:
    
    class _ScheduleStruct:
        def __init__(self, interval, function, *argc, **argv):
            self.interval = interval
            self.running = False
            self.function = function
            self.argc = argc
            self.argv = argv
            self.timer = None
        def _run(self):
            self.running = False
            self.start()
            self.function(*self.argc, **self.argv)
        def start(self):
            if not self.running:
                self.timer = threading.Timer(self.interval, self._run)
                self.running = True
                self.timer.start()
        def stop(self):
            self.timer.cancel()
            self.running = False

    def __init__(self):
        self.schedules = dict()
        self.CONST_SCHEDULE_DIR = 'schedules'
        self.CONST_DATE_FORMAT = '%Y-%m-%d %H:%M:%S.%f'
    
    def stop_running_schedules(self):
        for key, value in self.schedules.items():
            print('Starting %s' % key)
            value.stop()

    def parse_schedule_file(self, fileName):
        if not os.path.exists(fileName):
            return None
        with open(fileName, "r") as f:
            data = f.readlines()
            name = data[0]
            dateString = data[1]
            intervalTime = int(data[2])
            storedTime = datetime.strptime(dateString[0:-1], self.CONST_DATE_FORMAT)
        print('Parsed schedule file %s %d %s' % (name, intervalTime, dateString))
        return (name, intervalTime, storedTime)

    def load_saved_schedules(self):
        scheduleFiles = os.listdir(self.CONST_SCHEDULE_DIR)
        
        print (scheduleFiles)
        
        for fileName in scheduleFiles:
            filePath = os.path.join(self.CONST_SCHEDULE_DIR, fileName)
            schedule = self.parse_schedule_file(filePath)
            self.schedules[schedule[0]] = self._ScheduleStruct(schedule[1], self.test1) # TODO: using test function for now
        
        for key, value in self.schedules.items():
            print('Starting %s' % key)
            value.start()

    def set_schedule(self, scheduleName, timeInterval, callbackFunction):
        fileName = os.path.join(self.CONST_SCHEDULE_DIR, scheduleName)
        if not os.path.exists(fileName):
            print("File/Dir does not exist")
            os.makedirs(os.path.dirname(fileName), exist_ok=True)
            with open(fileName, "w") as f:
                f.write('') # just create the file, dont write anything yet
        with open(fileName, "r+") as f:
            f.write("%s\n%s\n%d" % (scheduleName, datetime.now(), timeInterval))

    def test1(self):
        print("test1")

    def test2(self):
        print("test2")

    def test3(self):
        print("test3")
        



#test = ReeScheduler()
#test.set_schedule("test", 4, None) # TODO: Can we store what function to call?
#test.set_schedule("test2", 2, None)
#test.load_saved_schedules()
