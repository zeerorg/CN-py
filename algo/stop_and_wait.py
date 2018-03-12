# implement stop and wait
# how to do: 
# create 2 threads
# call each thread from previous one
# pass parameter

import threading
import queue
import time
import random

start_time = time.time()
data = queue.Queue()
ack = queue.Queue()
probability_of_recv = 0.3

def sender_task():
    data_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", None]
    for chunk in data_list:
        time.sleep(0.1)
        data.put(chunk)
        print("Sent \"{}\" at {}".format(chunk, round(time.time() - start_time, 2)))
        sent_time = time.time()
        if chunk == None:
            break
        while ack.empty():
            if time.time() - sent_time > 0.25:
                # timeout, resend
                print("resent data: {}".format(chunk))
                time.sleep(0.1)
                data.put(chunk)
                sent_time = time.time()
            continue
        
        acknowledgment = ack.get()
        print("Received ack {} at {}".format(acknowledgment, round(time.time() - start_time, 2)))
        print()


def receiver_task():
    received_chunks = []
    while True:
        while data.empty():
            continue

        # If probability
        if random.random() > probability_of_recv:
            recv = data.get()
            if recv == None:
                break
            continue
        received_chunks.append(data.get())
        if received_chunks[-1] == None:
            break
        print("Received data \"{}\" at {}".format(received_chunks[-1], round(time.time() - start_time, 2)))
        print()
        time.sleep(0.1)
        ack.put(received_chunks.__len__())
        print("Sent ack {} at {}".format(received_chunks.__len__(), round(time.time() - start_time, 2)))

sender = threading.Thread(target=sender_task)
receiver = threading.Thread(target=receiver_task)

sender.start()
receiver.start()
while sender.is_alive() or receiver.is_alive():
    continue


