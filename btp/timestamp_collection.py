from pynput import keyboard
from pynput.keyboard import Key, Listener
import time
 
down_time = []
up_time = []
down_down_time = []
up_down_time = []
hold_time = []
final_list = []
ff = []
 
def on_key_release(key):
    time_taken_up = round(time.time() - t, 5)
    up_time.append(time_taken_up)
    if len(down_time)>0:
        hold_time.append(round(up_time[-1]-down_time[-1],5))
 
def on_key_press(key):
    time_taken_down = round(time.time() - t, 5)
    if len(down_time)>0:
        down_down_time.append(round(time_taken_down-down_time[-1], 5))
    if len(up_time)>0:
        up_down_time.append(round(time_taken_down-up_time[-1],5))
    down_time.append(time_taken_down)
 
    if key == Key.enter:
        time_stamp_list = alterList(down_time, up_time)
        i = 0
        while i<len(hold_time):
            final_list.append(hold_time[i])
            final_list.append(down_down_time[i])
            final_list.append(up_down_time[i])
            i+=1
        print(final_list)
        listener.stop()
        return final_list
 
def alterList(list1, list2):
    return [sub[item] for item in range(len(list2))
                    for sub in [list1, list2]]


t = time.time()

with keyboard.Listener(on_release = on_key_release, on_press = on_key_press) as listener:
    listener.join()