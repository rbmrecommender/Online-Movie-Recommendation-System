from timeit import default_timer

class Timer(object):
    #Timer class
    
    def __init__(self):
        self._timer = default_timer
        self._interval = 0
        self.running = False

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.stop()

    def __str__(self):
        return "{:0.4f}".format(self.interval)

    def start(self):
        #Start the timer
        
        self.init = self._timer()
        self.running = True

    def stop(self):
        #Stop the timer. Calculate the interval in seconds.
        
        self.end = self._timer()
        try:
            self._interval = self.end - self.init
            self.running = False
        except AttributeError:
            raise ValueError( "Timer has not been initialized: use start() or the contextual form with Timer() as t:" )

    @property
    def interval(self):
        #Get time interval in seconds
        
        if self.running:
            raise ValueError("Timer has not been stopped, please use stop().")
        else:
            return self._interval
