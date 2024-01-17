import requests

def get_dashboard_ids(api_key, app_key):
    # Datadog API endpoint for listing dashboards
    endpoint = "https://api.datadoghq.com/api/v1/dashboard"

    # Set up headers with API and Application keys
    headers = {
        "Content-Type": "application/json",
        "DD-API-KEY": api_key,
        "DD-APPLICATION-KEY": app_key
    }

    # Make the API request to get a list of dashboards
    response = requests.get(endpoint, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the response JSON and extract dashboard IDs
        dashboards = response.json().get("dashboards", [])
        dashboard_ids = [dashboard["id"] for dashboard in dashboards]
        return dashboard_ids
    else:
        # Print an error message if the request was not successful
        print(f"Error: {response.status_code}")
        return []

# Example usage
if __name__ == "__main__":
    # Replace with your Datadog API and Application keys
    api_key = "d4866e715297856d50a9c07b23f2cb06"
    app_key = "3d1e18e801186c04a5519e94625eb0d4b5ac6fac"

    dashboard_ids = get_dashboard_ids(api_key, app_key)
    print("Dashboard IDs:", dashboard_ids)
