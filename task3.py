import configparser
import datetime
import json
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


def infojson():
    get_data = {
        '1': str(psutil.cpu_percent(interval=1)),
        '2': str(psutil.virtual_memory().available / (1024 * 1024)),
        '3': str(psutil.virtual_memory().used / (1024 * 1024)),
        '4': str(psutil.disk_io_counters().read_bytes),
        '5': str((psutil.net_io_counters().bytes_recv) / (1024 * 1024))}
    get_data['CPU load, %'] = get_data.pop('1')
    get_data['Available memory, Mb'] = get_data.pop('2')
    get_data['Used memory, Mb'] = get_data.pop('3')
    get_data['Read bytes, b'] = get_data.pop('4')
    get_data['Network_received, Mb'] = get_data.pop('5')
    return get_data


if out == "output.txt":
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


if out == "output.json":
    get_status = {}
    counter = 1
    while True:
        now = datetime.datetime.now()
        get_status["Snapshot"] = "SNAPSHOT" + str(counter)
        get_status["timestamp"] = str(now.strftime("%Y-%m-%d %H:%M:%S  "))
        get_status["status"] = infojson()
        output_file = open(out, "a")
        output_file.write(json.dumps(get_status) + "\n\n")
        output_file.close()
        get_status.clear()
        counter += 1
        time.sleep(int(period))
