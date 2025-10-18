# IPv4 and IPv6 Address Application
# Team Innovate - Project Activity 3: Social Coding

import requests

def get_ip_info():
    try:
        print("\nFetching your public IP information...\n")

        # Try to get data from the API
        response = requests.get("https://ipapi.co/json/", timeout=5)
        data = response.json()

        # If the API returns an error or rate limit message
        if "error" in data:
            raise Exception("API rate-limited or unavailable. Using mock data instead.")

    except Exception as e:
        print(f"Warning: {e}")
        # Mock data fallback (used when API is not reachable)
        data = {
            "ip": "49.145.23.11",
            "city": "Manila",
            "region": "Metro Manila",
            "country_name": "Philippines",
            "country_code": "PH",
            "org": "Globe Telecom",
            "asn": "AS4775",
            "latitude": "14.5995",
            "longitude": "120.9842"
        }

    # Display results (real or mock)
    print("=== Your Public IP Information ===")
    print(f"IPv4/IPv6 Address: {data.get('ip')}")
    print(f"City: {data.get('city')}")
    print(f"Region: {data.get('region')}")
    print(f"Country: {data.get('country_name')} ({data.get('country_code')})")
    print(f"Internet Service Provider: {data.get('org')}")
    print(f"ASN: {data.get('asn')}")
    print(f"Latitude: {data.get('latitude')}")
    print(f"Longitude: {data.get('longitude')}")
    print("\nProgram executed successfully!\n")

if __name__ == "__main__":
    get_ip_info()
