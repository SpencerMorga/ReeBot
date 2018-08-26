import sys
import os
import threading
import time
from datetime import datetime

class ReeScheduler:
    
    class _ScheduleStruct:
        def __init__(self, interval, firstInterval, function, *argc, **argv):
            self.interval = interval
            self.firstInterval = firstInterval
            self.running = False
            self.firstRun = True
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
                if self.firstRun:
                    self.timer = threading.Timer(self.firstInterval, self._run)
                    self.firstRun = False
                else:
                    self.timer = threading.Timer(self.interval, self._run)
                self.running = True
                self.timer.start()
        def stop(self):
            self.timer.cancel()
            self.running = False

    def __init__(self, globals):
        self.schedules = dict()
        self.CONST_SCHEDULE_DIR = 'schedules'
        self.CONST_DATE_FORMAT = '%Y-%m-%d %H:%M:%S.%f'
        self.globals = globals
    
    def stop_running_schedules(self):
        for key, value in self.schedules.items():
            value.stop()

    def parse_schedule_file(self, fileName):
        if not os.path.exists(fileName):
            return None
        with open(fileName, "r") as f:
            data = f.readlines()
            name = data[0][0:-1] # -1 to cut off newline char
            dateString = data[1][0:-1]
            intervalTime = int(data[2])
            
            functionStr = data[3]
            function = eval(functionStr, self.globals) # This function is magical
            if not function:
                raise NotImplementedError("Mthod %s not defined" % functionStr)

            storedTime = datetime.strptime(dateString, self.CONST_DATE_FORMAT)
        #print('Parsed schedule file %s %d %s %s' % (name, intervalTime, dateString, functionName))
        return (name, intervalTime, storedTime, function)

    def load_and_start_schedules(self):
        scheduleFiles = os.listdir(self.CONST_SCHEDULE_DIR)
                
        for fileName in scheduleFiles:
            filePath = os.path.join(self.CONST_SCHEDULE_DIR, fileName)
            schedule = self.parse_schedule_file(filePath)
            
            savedTime = schedule[2]
            timeDifference = datetime.now() - savedTime
            differenceInSeconds = timeDifference.total_seconds()
            firstInterval = schedule[1] - differenceInSeconds
            if firstInterval <= 0:
                firstInterval = 0
                self.set_schedule(schedule[0], schedule[1], schedule[3], True)
            
            self.schedules[schedule[0]] = self._ScheduleStruct(schedule[1], firstInterval, schedule[3])
        
        for key, value in self.schedules.items():
            value.start()

    # NOTE: callbackFunction cannot be async
    def set_schedule(self, scheduleName, timeInterval, callbackFunction, overwrite=True):
        fileName = os.path.join(self.CONST_SCHEDULE_DIR, scheduleName)
        fileCreated = False
        if not os.path.exists(fileName):
            # Path does not exist
            os.makedirs(os.path.dirname(fileName), exist_ok=True)
            with open(fileName, "w") as f:
                f.write("%s\n%s\n%d\n%s" % (scheduleName, datetime.now(), timeInterval, callbackFunction))
            fileCreated = True
        if not fileCreated and overwrite:
            with open(fileName, "r+") as f:
                f.write("%s\n%s\n%d\n%s" % (scheduleName, datetime.now(), timeInterval, callbackFunction))

    def dummyMethod(self):
        print("test1")
        



#test = ReeScheduler()
#test.set_schedule("test", 4, 'self.dummyMethod', False)
#test.load_and_start_schedules()
