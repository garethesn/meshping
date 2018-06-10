from twisted.internet import task
from twisted.internet import reactor

timeout = 30.0 # Sixty seconds

def doWork():
    print "Did a thing..."
    pass

l = task.LoopingCall(doWork)
l.start(timeout) # call every sixty seconds

reactor.run()
