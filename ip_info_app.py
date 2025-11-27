def get_ip_info():
    ip_data = {
        "ip": "158.62.34.183",
        "city": "Quezon City",
        "region": "Metro Manila",
        "country": "Philippines",
        "isp": "Globe Telecom Inc.",
        "asn": "AS132199",
        "lat": 14.6475,
        "lon": 121.0494
    }

    print("=== Your Public IP Information ===")
    for k, v in ip_data.items():
        print(f"{k}: {v}")
    print("\nProgram executed successfully!")

    return ip_data  


# ⭐ ADD THIS PART ⭐
if __name__ == "__main__":
    get_ip_info()

