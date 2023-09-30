import requests
from bs4 import BeautifulSoup

# Function to validate subscription packages for a country
def validate_subscription_packages(country):
    url = f"https://subscribe.stctv.com/{country}-ar?"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find subscription packages
    packages = soup.find_all('div', class_='package')
    results = []

    # Extract package details
    for package in packages:
        package_type = package.find('div', class_='package-type').text.strip()
        package_price = package.find('div', class_='package-price').text.strip()
        package_currency = package.find('div', class_='package-currency').text.strip()
        results.append(f"Type: {package_type}\tPrice: {package_price}\tCurrency: {package_currency}")

    return results

# List of countries to validate
countries = ['sa', 'bh', 'kw']

# Validate subscription packages for each country
results = []
for country in countries:
    country_results = validate_subscription_packages(country)
    results.extend(country_results)

# results to a notepad file
with open('subscription_packages.txt', 'w', encoding='utf-8') as file:
    for result in results:
        file.write(result + '\n')

print("Validation completed. Results have been saved to subscription_packages.txt.")