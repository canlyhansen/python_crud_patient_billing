Python CRUD Application for Patient Billing Management System

A comprehensive Python application for managing patient billing data with Create, Read, Update, and Delete (CRUD) operations.

## Business Understanding

This project caters to the healthcare administration domain, specifically addressing the need to manage patient billing records efficiently in clinics or small hospitals. Patient billing data plays a crucial role in tracking medical expenses, monitoring patient status (In/Out), and supporting financial reporting for daily operations.

**Benefits:**

* Improved billing data accuracy and consistency
* Streamlined patient record management for cashiers/admin staff
* Faster retrieval of patient information during service
* Enhanced decision-making through summary statistics and bill tracking
* Reduced risk of manual recording errors

**Target Users:**

This application is designed for cashiers or administrative staff in healthcare facilities to facilitate their daily tasks related to managing patient registration numbers, billing amounts, patient status, and basic demographic data.

## Features

* **Create:**
    * Add new patient records with details:
      1. Registration number
      2. Name
      3. Birthdate
      4. Sex
      5. Bill
      6. Status
    * Input validation ensures:
      - Unique and numeric registration numbers
      - Correct birthdate format (YYYY-MM-DD)
      - Valid bill values and categorical inputs
* **Read:**
    * View all patient records in a formatted table
    * Search patient by:
      - Registration number (exact match)
      - Name keyword (case-insensitive)
    * Sorting feature to display patients by highest bill
* **Update:**
    * Update patient information based on registration number
    * Editable fields:
      1. Registration Number
      2. Name
      3. Birthdate
      4. Sex
      5. Status
    * Flexible bill update options:
      1. Add to existing bill
      2. Replace bill with new value
    * Confirmation step before saving changes
* **Delete:**
    * Remove one or multiple patients using registration numbers
    * Supports batch deletion using comma-separated input (e.g., 001,002,003)
    * Confirmation prompt before deletion to prevent accidental removal
* **Security:**
    * Simple login authentication for a single cashier user
    * Ensures only authorized staff can access and modify patient billing data
* **Reporting:**
    * Display summary statistics:
      1. Total number of patients
      2. Total accumulated bills
    * View patients sorted by highest billing amount for quick financial insights

## Installation

1. **Prerequisites:**
    * Python 3.10 or higher
    * No external libraries required (pure Python standard library)

2. **Installation:**
    ```bash
    git clone https://github.com/canlyhansen/python_crud_patient_billing.git
    cd python_crud_patient_billing

## Usage

1. **Run the application:**
    ```bash
    python main.py
    ```

2. **Login**
   Use the cashier credentials (as defined in the program) to access the system.
   
3. **CRUD Operations:**
    * **Create:** Add a new patient record with validated inputs.
    * **Read:** Display all patients or search by registration number or name.
    * **Update:** Modify patient information and billing details with confirmation.
    * **Delete:** Remove one or multiple patient records safely with confirmation prompts.

## Data Model
This project utilizes a Python list of dictionaries to represent patient billing data. Each patient record contains the following fields:
   * Registration Number: (string) – Unique numeric identifier for each patient
   * Name: (string) – Patient’s full name
   * Birthdate: (string) – Date of birth in YYYY-MM-DD format
   * Sex: (string) – Gender of the patient (M/F)
   * Bill: (integer) – Total billing amount for the patient
   * Status: (string) – Patient status (In/Out) indicating admission state

## Contributing
We welcome contributions to this project! Please feel free to open a pull request, send it to canlyhansen@gmail.com or submit an issue if you encounter any problems or have suggestions for improvements.

