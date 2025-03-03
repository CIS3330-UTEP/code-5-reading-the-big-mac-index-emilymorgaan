import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

df['year'] = pd.to_datetime(df['date']).dt.year

def get_big_mac_price_by_year(year,country_code):
    data = df[(df['year'] == year) & (df['iso_a3'] == country_code)]
    return round(data['dollar_price'].mean(), 2)

def get_big_mac_price_by_country(country_code):
    data = df[df['iso_a3'] == country_code]
    return round(data['dollar_price'].mean(), 2) 

def get_the_cheapest_big_mac_price_by_year(year):
    data = df[df['year'] == year]
    return data.nsmallest(1, 'dollar_price')[['name', 'iso_a3', 'dollar_price']].values[0] 

def get_the_most_expensive_big_mac_price_by_year(year):
    data = df[df['year'] == year]
    return data.nlargest(1, 'dollar_price')[['name', 'iso_a3', 'dollar_price']].values[0]

if __name__ == "__main__":
    while True:
        print("\nBig Mac Index Menu:")
        print("1. Get price by year and country")
        print("2. Get average price by country")
        print("3. Get cheapest price by year")
        print("4. Get most expensive price by year")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == '1':
            year = int(input("Enter year: "))
            country_code = input("Enter country code (e.g., ARG): ").upper()
            price = get_big_mac_price_by_year(year, country_code)
            print(f"Big Mac price in {country_code} in {year}: ${price}" if price else "No data found.")

        elif choice == '2':
            country_code = input("Enter country code (e.g., ARG): ").upper()
            price = get_big_mac_price_by_country(country_code)
            print(f"Average price in {country_code}: ${price}" if price else "No data found.")

        elif choice == '3':
            year = int(input("Enter year: "))
            result = get_the_cheapest_big_mac_price_by_year(year)
            if len(result) > 0:
                print(f"Cheapest: {result[0]} ({result[1]}) - ${result[2]}")
            else:
                print("No data found.")


        elif choice == '4':
            year = int(input("Enter year: "))
            result = get_the_most_expensive_big_mac_price_by_year(year)
            if len(result) > 0:
                print(f"Most expensive: {result[0]} ({result[1]}) - ${result[2]}")
            else:
                print("No data found.")

        elif choice == '5':
            print("Later!")
            break

        else:
            print("Invalid choice, try again.")