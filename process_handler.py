from utils import start_process
from os import kill, getpid
import signal

class ProcessHandler():
    def __init__(self):
        self.processes = []
        return

    def start(self, name, process):
        self.processes.append({"pid": start_process(name, process), "name":name})
        return

    def stop(self, name):
        for proc in self.processes:
            if proc['name'] == name:
                kill(int(name['pid']), signal.SIGTERM)
        return

    def kill(self, pid):
        kill(int(pid), signal.SIGTERM)
        return pid

    def last(self):
        return self.processes[len(self.processes) - 1]
    
    def close(self):
        if len(self.processes):
            last_proc = self.processes[len(self.processes) - 1]
            kill(int(last_proc['pid']), signal.SIGTERM)
            del self.processes[len(self.processes) - 1]
        return

process_handler = ProcessHandler()
