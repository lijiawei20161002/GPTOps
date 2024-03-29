import os
import pandas as pd

# Define the directory containing the .txt files
directory = '../data series/aws/'

# List to hold data from each file
data_frames = []

# Iterate through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        # Construct the full file path
        file_path = os.path.join(directory, filename)
        
        # Read the spot prices from the file, skipping the header
        df = pd.read_csv(file_path, usecols=[1], header=0)
        
        # Rename the column to the filename (without .txt extension)
        df.columns = [filename[:-4]]
        
        # Append the DataFrame to our list
        data_frames.append(df)

# Concatenate all DataFrames horizontally
combined_df = pd.concat(data_frames, axis=1)

# Define the output file name
output_file_path = os.path.join(directory, 'combined_spot_prices.txt')

# Save the combined DataFrame to a new .txt file
combined_df.to_csv(output_file_path, sep='\t', index=False)
