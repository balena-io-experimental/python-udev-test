
# https://pyudev.readthedocs.io/en/v0.14/api/monitor.html#pyudev.MonitorObserver
from pyudev import Context, Monitor, MonitorObserver
from time import sleep

context = Context()
monitor = Monitor.from_netlink(context)

monitor.filter_by(subsystem='input')

def print_device_event(action, device):
    print('background event {0}: {1}'.format(action, device))

observer = MonitorObserver(monitor, print_device_event, name='monitor-observer')
print('Starting obverver')
observer.start()

while True:
  sleep(600)
