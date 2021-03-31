import os
import random
from shutil import copyfile
from datetime import datetime

def makePack(size,source,destination):
    arr = os.listdir(source)
    random.seed(datetime.now())
    print(arr)
    random.shuffle(arr)
    print(arr)
    if not os.path.exists(destination):
        os.makedirs(destination) 
    for x in range(size):
        card = arr.pop()
        copyfile(source + card, destination +card)