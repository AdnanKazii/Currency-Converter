# Made by Adnan Kazi

import requests

def fetch_exchange_rates(api_url):
    response = requests.get(api_url)
    
    if response.status_code != 200:
        print(f"Failed to fetch data: HTTP {response.status_code}")
        return {}
    
    if not response.headers.get("Content-Type", "").startswith("application/json"):
        print("Invalid response format (not JSON).")
        return {}
    
    data = response.json()
    
    if "rates" in data:
        return data["rates"]
    else:
        print("Unexpected response format (missing 'rates').")
        return {}

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j][1] > key[1]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

def convert_currency(amount, rates):
    converted = [(currency, round(amount * rate, 2)) for currency, rate in rates.items()]
    return converted

def display_sorted_conversions(sorted_conversions):
    print("\nSorted Currency Conversions:")
    print("=" * 40)
    for currency, value in sorted_conversions:
        print(f"{currency}: {value}")

def main():
    api_url = "https://open.er-api.com/v6/latest/CAD"
    print("Fetching exchange rates...")
    rates = fetch_exchange_rates(api_url)
    
    if rates:
        print("\nEnter the amount in CAD to convert: ", end="")
        amount_input = input().strip()
        
        if amount_input.replace('.', '', 1).isdigit() and amount_input.count('.') <= 1:
            amount = float(amount_input)
        else:
            print("Invalid input. Please enter a numeric value.")
            return
        
        print("\nConverting currency...")
        conversions = convert_currency(amount, rates)
        
        print("\nSorting converted values using Insertion Sort...")
        sorted_conversions = insertion_sort(conversions)
        
        display_sorted_conversions(sorted_conversions)
    else:
        print("No data to process.")


if __name__ == "__main__":
    main()