import csv


"""

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
true_label

"""

labels = ["pass", "fail", "Unknown" "topic_marker"]

with open("adversarial_testing.csv") as csvfile:
    with open("converted.csv", "w") as csvConv:
        reader = csv.reader(csvfile, delimiter=",")
        writer = csv.writer(csvConv, delimiter=",", lineterminator="\n")

        for i, row in enumerate(reader):
            if i == 0:
                row[7] = "patient_input"
                row[2] = "machine_input"
                row[4] = "true_label"
            if row[4] == "Unknown" or row[4] == "topic_marker":
                continue
            if row[4] == "pass":
                row[4] = 1
            elif row[4] == "fail":
                row[4] = 0
            converted_row = [row[7], row[2].strip(), row[4]]
            writer.writerow(converted_row)

csvfile.close()
csvConv.close()
