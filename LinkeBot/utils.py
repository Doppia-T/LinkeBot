import time
import random


def random_nap():
    nap_time = random.randint(30, 300)
    time.sleep(nap_time)
