from Packer import makePack
from datetime import datetime

for x in range(10):
    makePack(5, "./My Cards/", "./pack"+str(x+1)+"/") 