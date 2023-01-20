import os
import subprocess

os.chdir(r"D:\Z_portifolio\killo_portfolio")
cwd = os.getcwd()

# stats = subprocess.run(["git", "status"])
add = subprocess.run(["git", "add","."])
commit = subprocess.run(["git", "commit","-m","test for auto-git"])
stats = subprocess.run(["git", "status"])

print(add)
