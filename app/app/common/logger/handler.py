import os
import time
from logging.handlers import TimedRotatingFileHandler


class RayUserTimedRotatingFileHandler(TimedRotatingFileHandler):
    """ 适配多进程环境，继承TimedRotatingFileHandler，并重写rotate和doRollover """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def rotate(self, source, dest):
        """ 适配多进程环境，重写rotate """
        if not callable(self.rotator):
            if os.path.exists(source):
                try:
                    os.rename(source, dest)
                except PermissionError:
                    # 多进程环境下，如果文件正在被其他进程写入，则不去rename日志。
                    pass
        else:
            self.rotator(source, dest)

    def doRollover(self):
        """ 适配多进程环境，重写doRollover """
        if self.stream:
            self.stream.close()
            self.stream = None
        currentTime = int(time.time())
        dstNow = time.localtime(currentTime)[-1]
        t = self.rolloverAt - self.interval
        if self.utc:
            timeTuple = time.gmtime(t)
        else:
            timeTuple = time.localtime(t)
            dstThen = timeTuple[-1]
            if dstNow != dstThen:
                if dstNow:
                    addend = 3600
                else:
                    addend = -3600
                timeTuple = time.localtime(t + addend)
        dfn = self.rotation_filename(self.baseFilename + "." + time.strftime(self.suffix, timeTuple))
        # 判断目标日志是否存在，如果存在，则不做rotate操作，防止多进程环境下目标日志被覆盖。
        if not os.path.exists(dfn):
            self.rotate(self.baseFilename, dfn)
        if self.backupCount > 0:
            for s in self.getFilesToDelete():
                try:
                    os.remove(s)
                except FileNotFoundError:
                    # 多进程环境下，文件可能已被其他进程删除。
                    pass
        if not self.delay:
            self.stream = self._open()
        newRolloverAt = self.computeRollover(currentTime)
        while newRolloverAt <= currentTime:
            newRolloverAt = newRolloverAt + self.interval
        if (self.when == 'MIDNIGHT' or self.when.startswith('W')) and not self.utc:
            dstAtRollover = time.localtime(newRolloverAt)[-1]
            if dstNow != dstAtRollover:
                if not dstNow:
                    addend = -3600
                else:
                    addend = 3600
                newRolloverAt += addend
        self.rolloverAt = newRolloverAt


