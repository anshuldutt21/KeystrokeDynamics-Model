import imp
import statistics
import csv
from csv import writer

#functions to calculate mean and standard deviation of data
def calculate_mean(listA):
    return statistics.mean(listA)

def calculate_std_dev(listA):
    return statistics.stdev(listA)

#function to read the recorded timing data and process further
def averaged_timestamps(timing_list):
    hold_time = []
    down_down_time = []
    up_down_time = []
    length = len(timing_list)
    i = 0
    while (i<length):
        hold_time.append(timing_list[i])
        down_down_time.append(timing_list[i+1])
        up_down_time.append(timing_list[i+2])
        i+=3

    new_hold_time = [float(n) for n in hold_time]
    new_down_down_time = [float(n) for n in down_down_time]
    new_up_down_time = [float(n) for n in up_down_time]

    avg_time_list = []
    avg_time_list.append(round(calculate_mean(new_hold_time),5))
    avg_time_list.append(round(calculate_mean(new_down_down_time), 5))
    avg_time_list.append(round(calculate_mean(new_up_down_time), 5))
    avg_time_list.append(round(calculate_std_dev(new_hold_time), 5))
    avg_time_list.append(round(calculate_std_dev(new_down_down_time), 5))
    avg_time_list.append(round(calculate_std_dev(new_up_down_time), 5))
    return avg_time_list

#add a row to dataset
def add_user_row(listA):
    with open('timestamp_data.csv', 'a', newline='') as f_object:  
        writer_object = writer(f_object)
        writer_object.writerow(listA)
        f_object.close()

#delete the first row with given username from dataset
def delete_user_row(username):
    with open("timestamp_data.csv", newline="") as f:
        reader = csv.reader(f)
        index = 0
        updated_list = []
        for row in reader:
            if (row[0] == username and index == 0):
                index =1
            else:
                updated_list.append(row)

    with open('timestamp_data.csv', 'w', newline='') as f_object:  
        writer_object = writer(f_object)
        writer_object.writerows(updated_list)
        f_object.close()

# add timing details to timestamp_records
def update_timestamp_records(username, timing_data):
    final_processed_list = []
    final_processed_list.append(username)
    final_processed_list.append('1')
    final_processed_list.append('1')
    avg_time_list = averaged_timestamps(timing_data)
    final_processed_list = final_processed_list + avg_time_list

    user_data_count = 0
    filename = open('timestamp_data.csv', 'r')
    file = csv.DictReader(filename)
    for row in file:
        if (row['username'] == username):
            user_data_count+=1

    if (user_data_count>25):
        delete_user_row(username)
        add_user_row(final_processed_list)
    else:
        add_user_row(final_processed_list)
