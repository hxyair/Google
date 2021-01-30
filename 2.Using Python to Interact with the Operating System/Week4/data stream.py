
import subprocess
subprocess.call('dir', shell=True)

subprocess.run(['cmd.exe', '/c', 'dir'])#dir is a command in cmd.exe, which means you want to do:
