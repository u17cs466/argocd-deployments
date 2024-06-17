import pandas as pd

# Define the file paths
file1 = 'file1.xlsx'
file2 = 'file2.xlsx'

def compare_excel_files(file1, file2):
    # Read the Excel files
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)

    # Ensure both DataFrames have the same shape by aligning them
    df1, df2 = df1.align(df2, join='outer', axis=1)
    df1, df2 = df1.align(df2, join='outer', axis=0)
    
    # Compare the DataFrames
    comparison_values = df1.eq(df2)

    # Check if there are any differences
    if comparison_values.all().all():
        return "The two Excel files have the same data."
    else:
        return "The two Excel files do not have the same data."

# Compare the files
compare_result = compare_excel_files(file1, file2)
print(compare_result)
