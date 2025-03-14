import os
import glob
from datetime import datetime
from pippa_db import PippaDB

def read_md_content(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    return content

def main():
    # Initialize the database
    db = PippaDB()
    
    # Get all dataset files - works with both protocol/ and protocol-public/ structures
    dataset_path = "../*/datasets/**/*.md"
    dataset_files = glob.glob(dataset_path, recursive=True)
    
    print(f"Found {len(dataset_files)} dataset files")
    
    # Process each file
    for file_path in dataset_files:
        print(f"\nProcessing: {file_path}")
        content = read_md_content(file_path)
        
        # Add to database with metadata
        entry = f"[Dataset Entry from {os.path.basename(file_path)}]\n\n{content}"
        db.add(entry)
        print("Added to database")

if __name__ == "__main__":
    main() 