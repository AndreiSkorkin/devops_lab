import configparser
import datetime
import psutil
import time
cfg = configparser.ConfigParser()
cfg.read('settings.cfg')
period = (cfg.get('common', 'period'))
out = (cfg.get('common', 'output'))
counter = 0


def info():
    '''This prints overall system data'''
    file = open(out, "a+")
    file.write("SNAPSHOT ")
    file.write(str(counter) + ':  ')
    file.write(now.strftime("%Y-%m-%d %H:%M:%S  "))
    file.write('CPU: ' + str(CPUload) + ' %   ')
    file.write('available memory: ' + str("%.2f" % memusage) + ' Mb   ')
    file.write('used memory: ' + str("%.2f" % vmemusage) + ' Mb   ')
    file.write('read: ' + str(IOinfo) + ' b  ')
    file.write('received: ' + str("%.4f" % network) + ' Mb\n')
    file.close()
    return


while True:
    now = datetime.datetime.now()
    CPUload = psutil.cpu_percent(interval=1)
    memusage = psutil.virtual_memory().available / (1024 * 1024)
    vmemusage = psutil.virtual_memory().used / (1024 * 1024)
    IOinfo = psutil.disk_io_counters().read_bytes
    network = psutil.net_io_counters().bytes_recv / (1024 * 1024)
    counter += 1
    time.sleep(int(period))
    info()
