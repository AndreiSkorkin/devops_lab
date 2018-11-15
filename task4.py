import configparser
import datetime
import json
import psutil
import time
cfg = configparser.ConfigParser()
cfg.read('settings.cfg')
period = (cfg.get('common', 'period'))
out = (cfg.get('common', 'output'))
counter = 1


class Psuinf(object):

    def CPU(self):
        return str(psutil.cpu_percent(interval=1))

    def available_memory(self):
        return str(psutil.virtual_memory().available / (1024 * 1024))

    def used_memory(self):
        return str(psutil.virtual_memory().used / (1024 * 1024))

    def read(self):
        return str(psutil.disk_io_counters().read_bytes)

    def received(self):
        return str((psutil.net_io_counters().bytes_recv) / (1024 * 1024))


class WriteInfo(Psuinf):

    def infojson(self):
        get_data = {
            '1': Psuinf.CPU(self),
            '2': Psuinf.available_memory(self),
            '3': Psuinf.used_memory(self),
            '4': Psuinf.read(self),
            '5': Psuinf.received(self)}
        get_data['CPU load, %'] = get_data.pop('1')
        get_data['Available memory, Mb'] = get_data.pop('2')
        get_data['Used memory, Mb'] = get_data.pop('3')
        get_data['Read bytes, b'] = get_data.pop('4')
        get_data['Network_received, Mb'] = get_data.pop('5')
        return get_data

    def TXT(self):
        counter = 1
        while True:
            now = datetime.datetime.now()
            CPUload = Psuinf.CPU(self)
            memusage = Psuinf.available_memory(self)
            vmemusage = Psuinf.used_memory(self)
            IOinfo = Psuinf.read(self)
            network = Psuinf.received(self)
            file = open(out, "a+")
            file.write("SNAPSHOT ")
            file.write(str(counter) + ':  ')
            file.write(now.strftime("%Y-%m-%d %H:%M:%S  "))
            file.write('CPU: ' + str(CPUload) + ' %   ')
            file.write('available memory: ' + memusage + ' Mb   ')
            file.write('used memory: ' + vmemusage + ' Mb   ')
            file.write('read: ' + str(IOinfo) + ' b  ')
            file.write('received: ' + network + ' Mb\n')
            file.close()
            time.sleep(int(period))
            counter += 1

    def JSON(self):
        get_status = {}
        counter = 1
        while True:
            now = datetime.datetime.now()
            get_status["Snapshot"] = "SNAPSHOT" + str(counter)
            get_status["timestamp"] = str(now.strftime("%Y-%m-%d %H:%M:%S  "))
            get_status["status"] = WriteInfo.infojson(self)
            output_file = open(out, "a")
            output_file.write(json.dumps(get_status) + "\n\n")
            output_file.close()
            get_status.clear()
            time.sleep(int(period))
            counter += 1

    def outputis(self):
        if out == "output.txt":
            WriteInfo.TXT(self)
        if out == "output.json":
            WriteInfo.JSON(self)


t = WriteInfo()
t.outputis()
