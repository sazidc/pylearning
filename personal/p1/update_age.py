from csv_modifer import modify_csv 
# Define a transformation function that increments age by 1
def increment_age(row):
    if 'Age' in row:
        row['Age'] = str(int(row['Age']) + 1)

# Call the function on a CSV file
modify_csv('input.csv', 'output.csv', increment_age)
