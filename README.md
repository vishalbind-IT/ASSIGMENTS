# Fetch Users from Public API

This Python script fetches a list of users from a public API and displays selected user details in a readable format.

##  Features
- Fetches data using a GET request to `https://jsonplaceholder.typicode.com/users`
- Displays each user's:
  - Name
  - Username
  - Email
  - City (from `address.city`)
- Handles API errors gracefully
- **Bonus:** Filters and prints only users whose city name starts with the letter **S**

##  Requirements
- Python 3.x
- `requests` library

##  Installation
Clone the repository and install dependencies:
```bash
git remote add origin https://github.com/vishalbind-IT/ASSIGMENTS.git
cd fetch-users-api
pip install requests
