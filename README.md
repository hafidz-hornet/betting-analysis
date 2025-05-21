# Casino User Data Extraction Tool

This repository contains utilities for extracting and analyzing user data related to casino mentions from a MySQL database.

## Contents

- app.py - Queries a database for users with "casino" mentions and exports results to CSV
- csv_rows.py - Utility script to count the number of rows in the generated CSV file
- .env - Configuration file for database connection (excluded from git)

## Setup

1. Clone the repository
2. Install the required dependencies:

```bash
pip install pandas sqlalchemy pymysql python-dotenv
```

3. Create a .env file with your database credentials:

```
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=your_host
DB_PORT=your_port
DB_DATABASE=your_database
```

## Usage

### Extracting User Data

Run the main script to query the database and generate a CSV file:

```bash
python app.py
```

This will:
- Connect to the database using credentials from the .env file
- Execute a query to find users with "casino" in their profile information
- Save the results to casino_users.csv

### Counting Rows

To count the number of data rows in the generated CSV:

```bash
python csv_rows.py
```

## Data Structure

The extracted data includes the following fields:
- `user_id`
- `nickname`
- `introduction`
- `short_introduction`
- `created_at`

## Note

The CSV files are excluded from version control to avoid committing potentially sensitive user data.
