import threading

class myThread(threading.Thread):
    def __init__(self,threadid, chr, num):
        # super(myThread, self).__init__()
        # can use the above as well to call the base class constructor
        threading.Thread.__init__(self)
        self.threadid= threadid
        self.chr=chr
        self.num = num
        
    def run(self):
        threading.Lock.acquire()
        while self.num>0:
            print (self.chr, end="")
            self.num-=1
        threading.Lock.release()

th1Obj = myThread(1,'a',2000)
th2Obj = myThread(2,'b',3000)

th1Obj.start()
th2Obj.start()
