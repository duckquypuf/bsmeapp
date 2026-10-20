import ssl
import pandas as pd
ssl._create_default_https_context = ssl._create_unverified_context

sheet_id = "1oTXNazg0q_ztCSXsV4Vm1fDpTJURkD_5X4hDgvcefZs"
def useless_function():
  print("virat is a germ")

def get_google_sheet(sheet_id):
  url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"

  df_raw = pd.read_csv(url, header=None)

  # Find the row index where 'Home Team' or 'Date' appears
  header_row_index = None
  #for idx, row in df_raw.iterrows():
    #if "Home Team" in row.values or "Date" in row.values:
      #header_row_index = idx
      #break

  if header_row_index is not None:
    # Re-read the CSV using the correct header row
    df = pd.read_csv(url, skiprows=header_row_index)
  else:
    # Fallback if not found
    df = pd.read_csv(url)

  # Clean up any empty unnamed columns or rows
  df = df.loc[:, ~df.columns.str.contains("^Unnamed")]
  df = df.dropna(how="all")

  print("--- Successfully Loaded Columns ---")
  print(df.columns.tolist())
  return df


# 1. Get the cleaned DataFrame
df = get_google_sheet(sheet_id)

# 2. Now this will work because 'Outcome' exists!
results = df
#results = df[df["Outcome"] == "Home Win"]

print("\n--- Home Wins Results ---")
print(results.head())