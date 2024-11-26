import pandas as pd

def process_file(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Print descriptive statistics
    print(f"Descriptive statistics for {file_path}:")
    print(df.describe())
    print("\n")

def main():
    files = ['data_1.csv', 'data_2.csv', 'data_3.csv']
    
    for file in files:
        process_file(file)

if __name__ == "__main__":
    main()