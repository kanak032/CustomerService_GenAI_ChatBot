import os
import xml.etree.ElementTree as ET
import pandas as pd
from tqdm import tqdm # A library to show a progress bar

def parse_single_xml(file_path):
    """
    Parses a single XML file and extracts only the question, answer, and question type.
    
    Args:
        file_path (str): The full path to the XML file.
        
    Returns:
        list: A list of dictionaries, where each dictionary contains the 
              question, answer, and qtype.
              Returns an empty list if the file cannot be parsed or is empty.
    """
    qa_pairs = []
    try:
        # Parse the XML file
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Find all 'QAPair' elements in the document
        for qa_pair_element in root.findall('.//QAPair'):
            question_element = qa_pair_element.find('Question')
            answer_element = qa_pair_element.find('Answer')
            
            # Ensure both question and answer tags exist and have text
            if question_element is not None and answer_element is not None:
                question = question_element.text or ""
                answer = answer_element.text or ""
                qtype = question_element.get('qtype') # Get the 'qtype' attribute
                
                qa_pairs.append({
                    'qtype': qtype,
                    'question': question.strip(),
                    'answer': answer.strip()
                })
                
    except ET.ParseError as e:
        print(f"Error parsing {file_path}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred with file {file_path}: {e}")
        
    return qa_pairs

def process_medquad_directory(root_dir):
    """
    Walks through a root directory, finds all XML files, parses them,
    and aggregates the results.
    
    Args:
        root_dir (str): The path to the root directory (e.g., 'MedQuAD').
        
    Returns:
        pandas.DataFrame: A DataFrame containing all the parsed Q&A data.
    """
    all_xml_files = []
    # os.walk recursively explores the directory tree
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.xml'):
                full_path = os.path.join(dirpath, filename)
                all_xml_files.append(full_path)
                
    if not all_xml_files:
        print(f"No XML files found in '{root_dir}'. Please check the directory path.")
        return pd.DataFrame()

    print(f"Found {len(all_xml_files)} XML files. Starting parsing...")
    
    all_qa_data = []
    # Use tqdm to show a nice progress bar during processing
    for xml_file in tqdm(all_xml_files, desc="Parsing XML files"):
        qa_data_from_file = parse_single_xml(xml_file)
        if qa_data_from_file:
            all_qa_data.extend(qa_data_from_file)
            
    # Convert the list of dictionaries to a pandas DataFrame for easy use
    df = pd.DataFrame(all_qa_data)
    return df

# --- Main Execution ---
if __name__ == "__main__":
    # Set the path to your main data folder
    # This script assumes the 'MedQuAD' folder is in the same directory
    # as this Python script.
    medquad_root_folder = 'MedQuAD'
    
    if not os.path.isdir(medquad_root_folder):
        print(f"Error: The directory '{medquad_root_folder}' was not found.")
        print("Please make sure the MedQuAD folder is in the same location as this script, or provide the full path.")
    else:
        # Process the directory and get the DataFrame
        medquad_df = process_medquad_directory(medquad_root_folder)
        
        if not medquad_df.empty:
            print("\n--- Parsing Complete! ---")
            print(f"Successfully extracted {len(medquad_df)} Q&A pairs.")
            
            # Display the first 5 rows of the resulting data
            print("\nSample of extracted data:")
            print(medquad_df.head())
            
            # Display summary information about the DataFrame
            print("\nData summary:")
            medquad_df.info()
            
            # --- Save the data to a JSON file ---
            output_json_path = 'medquad_parsed_data.json'
            try:
                # orient='records' creates a list of JSON objects.
                # indent=4 makes the JSON file human-readable.
                # force_ascii=False ensures correct encoding for non-English characters.
                medquad_df.to_json(output_json_path, orient='records', indent=4, force_ascii=False)
                print(f"\nSuccessfully saved all data to '{output_json_path}'")
            except Exception as e:
                print(f"\nCould not save data to JSON: {e}")

            # --- Save the data to a CSV file ---
            output_csv_path = 'medquad_parsed_data.csv'
            try:
                medquad_df.to_csv(output_csv_path, index=False, encoding='utf-8')
                print(f"Successfully saved all data to '{output_csv_path}'")
            except Exception as e:
                print(f"\nCould not save data to CSV: {e}")
