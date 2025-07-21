from bsedata.bse import BSE
b= BSE()
print(b) 
q = b.getQuote('534976')
print(q,'\n')
codelist = ["500116", "512573"]
for code in codelist:
    quote = b.getQuote(code)
    print (quote["companyName" ])
    print (quote["currentValue"])
    print (quote["updatedOn" ])

print('\n',b.topGainers())
print('\n',b.topLosers ())

import pandas as pd

# Path to the CSV file
file_path = "/Users/yashrajsakunde/Desktop/StocksProject/PythonCodes/EQT0.csv"

# Load the CSV file into a DataFrame
try:
    df = pd.read_csv(file_path)
    print("File loaded successfully!")
    print(df)  # Display the first few rows for verification
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")
    exit()

# List of Security Codes to search for
tickers = [
    '100087', '100112', '100228', '100251', '100253', '100290', '100295',
    '100312', '100425', '100440', '100477', '100483', '100547', '100790',
    '100850', '117334', '126371', '132134', '132400', '132477', '132488',
    '132522', '132541', '132977', '140005'
]

# Fetching matching rows based on Security Code
codes = []
for t in tickers:
    # Filter rows where 'Security Code' matches the ticker
    filtered_rows = df[df['Security Code'] == int(t)]  # Convert ticker to integer if necessary
    if not filtered_rows.empty:
        # Append the first matched row's 'Security Code' or any other column value
        codes.append(str(filtered_rows.iloc[0]['Security Code']))
    else:
        print(f"Security Code '{t}' not found in the DataFrame.")

# Output the fetched Security Codes
print("Fetched Security Codes:", codes)


