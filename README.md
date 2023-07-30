# Waqas_Hospital_System_V1_tkinter_in_python
Hospital Management System using Tkinter for GUI. Allows managing patient info, prescriptions, and medication details. Features data entry, update, and deletion. Utilizes local MySQL database for storage. User-friendly interface for easy navigation.
Features
Add new patient records
View and update patient details
Create and manage prescriptions
Medication information and dosages
Search and filter patient data
User-friendly GUI for easy navigation
Requirements
Python (>=3.6)
Tkinter (usually included in Python installations)
MySQL Connector (MySQL Connector/Python) - Install using: pip install mysql-connector-python
Installation
Clone the repository: git clone https://github.com/waqasahmad713/Waqas-hospital-system.git
Navigate to the project directory: cd hospital-management
Install the required dependencies as mentioned in the "Requirements" section above.
Create a MySQL database named hospital_data and set up the necessary tables. You can use the database_setup.sql script provided in the repository.
Update the database connection details in the code (Hospital class) to match your MySQL server credentials.
Usage
Run the application: python hospital.py
The Hospital Management System GUI will open.
Add new patient information by filling in the details and clicking the "Prescription" button to enter prescription information.
Use the "Prescription data" button to save the entered data to the database.
Use the "Update" and "Delete" buttons to modify or remove existing patient records.
Use the search and filter options to find specific patient data.
Contributing
Pull requests and bug reports are welcome. For major changes, please open an issue first to discuss what you would like to change.

Acknowledgments
The project uses Tkinter for the graphical user interface.
The MySQL Connector/Python is used for database connectivity.
Contact
For any inquiries or questions, please email us at waqaskhanwaqas713@gmail.com.
