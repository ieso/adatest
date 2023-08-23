import csv


'''

----- BEFORE ----

[blank column (id)]
topic
input
output
label
labeler
description
model score
author
query

----- AFTER ----

patient_input
machine_input
label

'''

with open('new.csv') as csvfile:
    with open("converted.csv", "w") as csvConv:
        reader = csv.reader(csvfile, delimiter=',')
        writer = csv.writer(csvConv, delimiter=',')
        
        for i, row in enumerate(reader):
            converted_row = [row[7], row[2].strip(), row[4]]
            writer.writerow(converted_row)
        
csvfile.close()
csvConv.close()