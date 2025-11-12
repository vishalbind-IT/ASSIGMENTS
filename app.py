import requests  # Import the requests library for API calls

def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"  # API endpoint

    try:
        response = requests.get(url)  # Send GET request to the API
        response.raise_for_status()  # Check if the request was successful
        
        users = response.json()  # Convert response to JSON format

        if not users:  # Check if the user list is empty
            print("No users found.")
            return

        count = 1  # Initialize user counter
        for user in users:  # Loop through each user
            name = user.get('name')
            username = user.get('username')
            email = user.get('email')
            city = user.get('address', {}).get('city')

            # Bonus: Only show users from cities starting with 'S'
            if not city or not city.startswith('S'):
                continue

            # Print user details
            print(f"User {count}:")
            print(f"Name: {name}")
            print(f"Username: {username}")
            print(f"Email: {email}")
            print(f"City: {city}")
            print("-" * 25)
            count += 1 

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")  # Handle API errors

if __name__ == "__main__":
    fetch_users()  # Run the function

