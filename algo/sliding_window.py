# implement stop and wait
# how to do: 
# create 2 threads
# call each thread from previous one
# pass parameter

import threading
import queue
import time
import random
import operator
from functools import partial

start_time = time.time()
data = queue.Queue()
ack = queue.Queue()
data_reach = queue.Queue()
probability_of_recv = 0.5

def curr_time(rd=2):
    return round(time.time() - start_time, rd)

def sender_data(to_send, lat=0.25):
    def send_func():
        data.put(to_send)

    threading.Timer(lat, send_func).start()
    print("Sender:: Sent {} at {}".format(to_send, round(time.time() - start_time, 2)))

def sender_task():
    data_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", None]
    all_acks = []
    window = [0, 1, 2, 3]       # initialize window
    while all_acks.__len__() < data_list.__len__() - 1:
        sent_time = time.time()
        new_window = list(window)
        for to_send_num in window:
            sender_data({
                'data': data_list[to_send_num],
                'seq': to_send_num
            })
            # watch for acknowledgements and update window
            while not ack.empty():
                recv_ack = ack.get()
                # remove value from new window
                new_window.remove(recv_ack)
                all_acks.append(recv_ack)
                print("Sender:: Received ack {} at {}".format(recv_ack, curr_time()))
        
        # wait for timeouts
        while new_window.__len__() != 0 and time.time() - sent_time < 1.0:
            # collect acknowledgments
            while not ack.empty():
                recv_ack = ack.get()
                # remove value from new window
                new_window.remove(recv_ack)
                all_acks.append(recv_ack)
                print("Sender:: Received ack {} at {}".format(recv_ack, curr_time()))

        all_acks = sorted(all_acks)
        window = list(range(len(data_list)))
        for temp_ack in all_acks:
            window.remove(temp_ack)
        while window[-1] - window[0] >= 4:
            window.pop()

def receiver_ack(to_send, lat=0.25):
    def send_func():
        ack.put(to_send)

    threading.Timer(lat, send_func).start()
    print("Receiver:: Sent ack {} at {}".format(to_send, curr_time()))

def receiver_task():
    received_chunks = []
    while True:
        if not data.empty():
            # consume data
            recv_data = data.get()
            if random.random() > probability_of_recv:
                print("Dropped :: {} at {}".format(recv_data, curr_time()))
                continue
 
            print("Receiver:: Received {} at {}".format(recv_data['data'], curr_time()))

            # send ack
            receiver_ack(recv_data['seq'])
            # ack.put(recv_data['seq'])
            # print("Receiver:: Sent ack {} at {}".format(recv_data['seq'], round(time.time() - start_time, 2)))
            # time.sleep(0.025)
        pass

sender = threading.Thread(target=sender_task)
receiver = threading.Thread(target=receiver_task)

sender.start()
receiver.start()
while sender.is_alive() or receiver.is_alive():
    continue
