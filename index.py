import os
import subprocess
import sys

os.chdir(r"D:\Z_portifolio\killo_portfolio")
cwd = os.getcwd()

# stats = subprocess.run(["git", "status"])
add = subprocess.run(["git", "add","."])
commit = subprocess.run(["git", "commit","-m","test for auto-git"])
stats = subprocess.run(["git", "status"])
# def execute(command):
#     subprocess.check_call(command, shell=True, stdout=sys.stdout, stderr=subprocess.STDOUT)


# output = execute("git status")

for line in stats.stdout:
    print(line.decode().strip())