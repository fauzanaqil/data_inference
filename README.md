# Project Name

This project is a web application designed for data inference. It allows users to upload CSV/Excel files containing data, processes the uploaded data to infer and convert data types, and presents the inferred data types to the user. The backend of the application is built using Django, a Python web framework, while the frontend is developed using React.js, a JavaScript library for building user interfaces.

## Table of Contents

- [Project Name](#project-name)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Additional Notes](#additional-notes)
  - [Contributing](#contributing)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/fauzanaqil/data_inference.git

2. **Navigate to the project directory:**

   ```bash
   cd data_inference

3. **Set up the backend:**
   - Navigate to the *backend* directory:

   ```bash
   cd backend

   - Install Python dependencies using pip:

   ```bash
   pip install -r requirements.txt

4. **Set up the frontend:**

   - Navigate to the *frontend* directory:

   ```bash
   cd frontend

   - Install Node.js dependencies using npm (Node.js and npm required):

   ```bash
   npm install

## Usage

1. **Run the backend server:**

   - Navigate back to the root directory:

   ```bash
   cd ..

   - Start Django server:

   ```bash
   python manage.py runserver

2. **Navigate to the project directory:**

   - Navigate to the *frontend* directory if not already there:

   ```bash
   cd frontend

   - Start the React development server:

   ```bash
   npm start

3. **Access the application:**
   - Open your web browser and go to <http://localhost:8000> to view the application.

## Additional Notes

1. *Project Structure*: The project follows a typical Django project structure, with separate directories for the backend, frontend, and other resources.
2. *Frontend*: The frontend is built using React.js, a popular JavaScript library for building user interfaces. It communicates with the Django backend through API calls.
3. *Backend*: The backend is developed using Django, a high-level Python web framework. It handles file uploads, data processing, and serves the frontend application.
4. *File Uploads*: The application allows users to upload CSV files containing data. Ensure that the file upload mechanism is secure and handles errors gracefully.
5. *Data Processing*: After uploading a file, the backend processes the data to infer and convert data types. This functionality is implemented using Pandas, a powerful data manipulation library in Python.
6. *State Management*: React components manage their state to reflect changes in the application's UI. Ensure proper state management to prevent unexpected behavior.

## Contributing

1. Fork the project.
2. Create your feature branch: git checkout -b feature-name.
3. Commit your changes: git commit -m 'Add some feature'.
4. Push to the branch: git push origin feature-name.
5. Submit a pull request.