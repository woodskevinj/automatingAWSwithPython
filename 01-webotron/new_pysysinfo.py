# very short script to reuse pysysinfo_func_2 code
from pysysinfo_func_2 import disk_func
import subprocess

def tmp_space():
    tmp_usage = "du"
    tmp_arg = "-sh"
    path = "/tmp"
    print("Space used in /tmp directory")
    subprocess.call([tmp_usage, tmp_arg, path])
