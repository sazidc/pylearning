# Basic Python Program: Personal Diary Application

# Import necessary libraries
import json

# Class to represent a diary entry
class DiaryEntry:
    def __init__(self, date, content):
        self.date = date
        self.content = content

    def __str__(self):
        return f"Date: {self.date}\nContent: {self.content}\n"

# Function to add a new diary entry
def add_entry(entries):
    date = input("Enter the date (YYYY-MM-DD): ")
    content = input("Write your diary entry: ")
    entry = DiaryEntry(date, content)
    entries.append(entry)
    print("Diary entry added successfully!")

# Function to view all diary entries
def view_entries(entries):
    if not entries:
        print("No diary entries found.")
    else:
        for entry in entries:
            print(entry)

# Function to save entries to a file
def save_entries(entries, filename='diary_entries.json'):
    with open(filename, 'w') as file:
        json.dump([entry.__dict__ for entry in entries], file)
    print(f"Entries saved to {filename}.")

# Function to load entries from a file
def load_entries(filename='diary_entries.json'):
    try:
        with open(filename, 'r') as file:
            entries_data = json.load(file)
            return [DiaryEntry(**entry) for entry in entries_data]
    except FileNotFoundError:
        return []

# Main function to run the diary application
def main():
    entries = load_entries()
    
    while True:
        print("\n--- Personal Diary ---")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Save Entries")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_entry(entries)
        elif choice == '2':
            view_entries(entries)
        elif choice == '3':
            save_entries(entries)
        elif choice == '4':
            print("Exiting the diary application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Entry point of the program
if __name__ == "__main__":
    main()