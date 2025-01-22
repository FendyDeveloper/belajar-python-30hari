import csv
import os
from datetime import datetime


class StudentDatabase:
    def __init__(self, database_file="students.csv"):
        self.database_file = database_file
        self._create_file_if_not_exists()

    def _create_file_if_not_exists(self):
        """Create the CSV file with headers if it doesn't exist"""
        if not os.path.exists(self.database_file):
            with open(self.database_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['NIM', 'Name', 'Created Date', 'Last Updated'])

    def _validate_nim(self, nim):
        """Validate NIM format"""
        return nim.isdigit() and len(nim) >= 5

    def _validate_name(self, name):
        """Validate name format"""
        return len(name.strip()) >= 2 and name.replace(' ', '').isalpha()

    def add_student(self, nim, name):
        """Add a new student to the database"""
        try:
            # Validate input
            if not self._validate_nim(nim):
                return False, "Invalid NIM format. NIM should be numeric and at least 5 digits."

            if not self._validate_name(name):
                return False, "Invalid name format. Name should contain only letters and be at least 2 characters."

            # Check if NIM already exists
            if self._student_exists(nim):
                return False, "Student with this NIM already exists."

            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(self.database_file, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([nim, name.title(), current_time, current_time])
            return True, "Student added successfully!"
        except Exception as e:
            return False, f"Error adding student: {str(e)}"

    def view_students(self):
        """View all students in the database"""
        try:
            with open(self.database_file, 'r') as file:
                reader = csv.DictReader(file)
                students = list(reader)

                if not students:
                    return False, "No students found in the database."

                return True, students
        except FileNotFoundError:
            return False, "Database file not found."
        except Exception as e:
            return False, f"Error viewing students: {str(e)}"

    def _student_exists(self, nim):
        """Check if a student with given NIM exists"""
        try:
            with open(self.database_file, 'r') as file:
                reader = csv.DictReader(file)
                return any(row['NIM'] == nim for row in reader)
        except FileNotFoundError:
            return False

    def update_student(self, nim, new_name):
        """Update student information"""
        try:
            if not self._validate_name(new_name):
                return False, "Invalid name format. Name should contain only letters and be at least 2 characters."

            temp_file = "temp_database.csv"
            updated = False

            with open(self.database_file, 'r') as file, \
                    open(temp_file, 'w', newline='') as temp:
                reader = csv.DictReader(file)
                fieldnames = ['NIM', 'Name', 'Created Date', 'Last Updated']
                writer = csv.DictWriter(temp, fieldnames=fieldnames)
                writer.writeheader()

                for row in reader:
                    if row['NIM'] == nim:
                        row['Name'] = new_name.title()
                        row['Last Updated'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        updated = True
                    writer.writerow(row)

            os.replace(temp_file, self.database_file)

            if updated:
                return True, "Student updated successfully!"
            return False, "Student with given NIM not found."
        except Exception as e:
            return False, f"Error updating student: {str(e)}"

    def delete_student(self, nim):
        """Delete a student from the database"""
        try:
            temp_file = "temp_database.csv"
            deleted = False

            with open(self.database_file, 'r') as file, \
                    open(temp_file, 'w', newline='') as temp:
                reader = csv.DictReader(file)
                fieldnames = ['NIM', 'Name', 'Created Date', 'Last Updated']
                writer = csv.DictWriter(temp, fieldnames=fieldnames)
                writer.writeheader()

                for row in reader:
                    if row['NIM'] == nim:
                        deleted = True
                    else:
                        writer.writerow(row)

            os.replace(temp_file, self.database_file)

            if deleted:
                return True, "Student deleted successfully!"
            return False, "Student with given NIM not found."
        except Exception as e:
            return False, f"Error deleting student: {str(e)}"


def main():
    db = StudentDatabase()

    while True:
        print("\n=== Student Management System ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        try:
            choice = input("\nEnter your choice (1-5): ")

            if choice == "1":
                nim = input("Enter NIM: ")
                name = input("Enter Name: ")
                success, message = db.add_student(nim, name)
                print(message)

            elif choice == "2":
                success, result = db.view_students()
                if success:
                    print("\n=== List of Students ===")
                    print(f"{'NIM':<10} {'Name':<20} {'Created Date':<20} {'Last Updated':<20}")
                    print("-" * 70)
                    for student in result:
                        print(
                            f"{student['NIM']:<10} {student['Name']:<20} {student['Created Date']:<20} {student['Last Updated']:<20}")
                else:
                    print(result)

            elif choice == "3":
                nim = input("Enter NIM to update: ")
                new_name = input("Enter new Name: ")
                success, message = db.update_student(nim, new_name)
                print(message)

            elif choice == "4":
                nim = input("Enter NIM to delete: ")
                success, message = db.delete_student(nim)
                print(message)

            elif choice == "5":
                print("Thank you for using Student Management System. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break
        except Exception as e:
            print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()