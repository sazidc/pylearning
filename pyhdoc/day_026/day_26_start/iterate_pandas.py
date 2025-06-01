# Iterate over a Pandas DataFrame
import pandas

student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}
student_data_frame = pandas.DataFrame(student_dict)
for index, row in student_data_frame.iterrows():
    # print(row.student)
    print(row.student)
    if row.student == "Angela":
        print(row.score)