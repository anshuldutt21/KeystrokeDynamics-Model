# import csv  

# header = ['username', 'email', 'password']
# data = ['ayush', 'ayushshr@gmail.com', 'a123']

# with open('users.csv', 'w', encoding='UTF8') as f:
#     writer = csv.writer(f)

#     # write the header
#     writer.writerow(header)

#     # write the data
#     writer.writerow(data)

import csv  

header = ['username', 'sessionId', 'reg', 'avg_HT', 'avg_DD', 'avg_UD', 'std_dev_HD', 'std_dev_DD', 'std_dev_UD']
data = ['ayush', '1', '1', '0.1', '0.1', '0.1', '0.1', '0.1', '0.1']

with open('timestamp_data.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    writer.writerow(data)
