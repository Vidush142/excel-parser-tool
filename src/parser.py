import pandas as pd
import logging
import argparse
import os
import sys
from typing import List

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def filter_excel(input_path: str, output_path: str, keywords: List[str]) -> None:
    """
    Core logic to filter Excel data.
    """
    try:
        if not os.path.exists(input_path):
            logger.error(f"Input file not found: {input_path}")
            print(f"ERROR: File NOT found at {os.path.abspath(input_path)}")
            sys.exit(1)

        logger.info(f"Reading {input_path}...")
        df = pd.read_excel(input_path, engine='openpyxl')
        print(f"DEBUG: Successfully loaded {len(df)} rows.")

        # Create regex pattern from list
        pattern = '|'.join([str(k).strip() for k in keywords])
        
        logger.info(f"Filtering for: {keywords}")
        mask = df.astype(str).apply(
            lambda x: x.str.contains(pattern, case=False, na=False)
        ).any(axis=1)

        filtered_df = df[mask]

        logger.info(f"Saving {len(filtered_df)} matches to {output_path}...")
        filtered_df.to_excel(output_path, index=False, engine='openpyxl')
        logger.info("Process completed successfully.")

    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        sys.exit(1)

def main():
    # 1. Initialize the Parser
    parser = argparse.ArgumentParser(
        description="A CLI tool to filter large Excel files by keywords across all columns."
    )

    # 2. Define Arguments
    parser.add_argument(
        '-i', '--input', 
        required=True, 
        help="Path to the source Excel file (.xlsx)"
    )
    parser.add_argument(
        '-o', '--output', 
        default="filtered_output.xlsx", 
        help="Path for the filtered output file (default: filtered_output.xlsx)"
    )
    parser.add_argument(
        '-k', '--keywords', 
        nargs='+', 
        required=True, 
        help="Space-separated list of keywords to search for (e.g., -k term1 term2)"
    )

    # 3. Parse Arguments
    args = parser.parse_args()

    # 4. Execute
    filter_excel(args.input, args.output, args.keywords)

if __name__ == "__main__":
    main()