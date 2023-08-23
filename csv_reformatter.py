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

output_labels = {"acceptable": 1, "unacceptable": 0}
rev_output_labels = {"acceptable": 0, "unacceptable": 1}
labels = ["pass", "fail", "Unknown" "topic_marker"]

duplicate_checker = []

with open("adversarial_testing.csv") as csvfile:
    with open("adversarial_testing_formatted.csv", "w") as csvConv:
        reader = csv.reader(csvfile, delimiter=",")
        writer = csv.writer(csvConv, delimiter=",", lineterminator="\n")

        for i, row in enumerate(reader):
            if i == 0:
                patient_input = "patient_input"
                machine_input = "machine_input"
                true_label = "true_label"
            else:
                patient_input = row[7]
                machine_input = row[2].strip()

            if (
                row[4] == "Unknown"
                or row[4] == "topic_marker"
                or not row[3]
                or machine_input in duplicate_checker
                or "bin" in row[1]
                or "ignore" in row[6] # just put ignore in topic description to not count towards dataset
            ):
                continue

            if row[4] == "pass":
                true_label = output_labels[row[3]]

            elif row[4] == "fail":
                true_label = rev_output_labels[row[3]]

            converted_row = [patient_input, machine_input, true_label]
            writer.writerow(converted_row)
            duplicate_checker.append(machine_input)

csvfile.close()
csvConv.close()
