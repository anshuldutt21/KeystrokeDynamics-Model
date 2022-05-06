import csv
from csv import writer
import subprocess
from otp_validation import check_otp_validation
from timestamp_records import update_timestamp_records

 
# Model for Keystrok Dynamics based password authentication
print("Hello, welcome to Keystroke Dynamics based User-Identification model.")
print("...")
print("Are you a pre-registered user? (Y/N)")
 
model_begin_flag = True
registered_user = False
new_user = False
temp_time_stamp = []

def collect_timing_data():
    temp_data = []
    #collect and process timing data
    temp_data = subprocess.check_output(["python3", "timestamp_collection.py"], encoding='utf-8').split()
    i = 0
    while (i<len(temp_data)):
        temp_data[i] = temp_data[i][:-1]
        i+=1
    temp_data[0] = temp_data[0][1:]
    return temp_data
 
while model_begin_flag:
    val = input("->")
    if (val == "Y"):
        print("Great, please login into the model...")
        registered_user = True
        break
    elif (val == "N"):
        print("Glad to see you here, please sign up first...")
        new_user = True
        break
    else:
        print("Please type either Y or N...")

#register new user
if (new_user):
    username = input("username: ")
    email = input("email: ")
    print("password: ")
    register_timing_list = []
    temp = []
    temp = collect_timing_data()
    register_timing_list.append(temp)
    password = input("")
    count = 4
    while (count>0):
        print("Re-enter password (",count, "times):")
        next_password = ""
        temp = []
        temp = collect_timing_data()
        next_password = input()
        if(next_password != password):
            print("Passwords dont match. Type again,")
        elif(next_password == password):
            count = count - 1
            register_timing_list.append(temp)

    
    #add user details to user_login_data
    temp_user_details = [username, email, password]
    with open('user_login_data.csv', 'a', newline='') as f_object:  
        writer_object = writer(f_object)
        writer_object.writerow(temp_user_details)
        f_object.close()

    #add user timing data to timestamp_data
    for i in register_timing_list:
        update_timestamp_records(username, i)

    print("User created successfully!\n...")
    print("You can now login,")
    registered_user = True

#login existing user
if (registered_user):
    username = input("username: ")
    print("password: ")
    temp_data = collect_timing_data()
    password = input("")
    print("sample timing data:",temp_data)
    user_pass_match_key = False

    #check if the username/password exists in database
    filename = open('user_login_data.csv', 'r')
    file = csv.DictReader(filename)
    current_users = []
    for row in file:
        current_users.append(row['username'])
    if username in current_users:
        filename = open('user_login_data.csv', 'r')
        file = csv.DictReader(filename)
        for row in file:
            if row['username'] == username:
                if row['password'] == password:
                    print("User found and password verified!")
                    user_pass_match_key = True
                else:
                    print("password incorrect!..Please try again.")
    else:
        print("username not found!..register to create a new user.")

    #check if the user is authentic using timestamp
    if (user_pass_match_key):
        print("Based on keystroke patterns the model will now check if user is trully valid...\n...")
        trust_score= float(input("Model output score >>:"))
        if (trust_score>=0.7 and trust_score<=1):
            print("Validation successfull. Logged in!")
            update_timestamp_records(username, temp_data)
        elif (trust_score>=0.3 and trust_score<0.7):
            print("\nThe system is not sure if the user is authentic...")
            print("An One-Time Password has been sent to the registered email-id.")
            otp_key = check_otp_validation(username)
            OTP = input("Please enter the otp to continue >>: ")
            if (OTP == otp_key):
                print("User verified!\nSuccessfully logged in!")
            else:
                print("OTP entered is wrong. Please try again.")

        elif (trust_score<0.3 and trust_score>0):
            print("User timing patterns and recorded data doesn't match.")
            print("...\nPlease try again.")
        else:
            print("Internal model error with output..")

else:
    print("Error with model initialization")