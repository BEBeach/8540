import json
import re
import csv

# Regular expressions for hashtags and URLs
hashtag_pattern = re.compile(r'#\w+')
url_pattern = re.compile(r'https?://\S+')

# Open the JSON file for reading and the CSV and JSON files for writing
with open('tweets.json', 'r') as json_file, open('output_id.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Writing header row in CSV file, now including "ID" column
    csv_writer.writerow(['ID', 'Hashtags', 'URLs'])
    
    # Initialize an empty list to hold the data dictionaries for JSON output
    extracted_data_for_json = []
    
    # Process each line in the JSON file
    for line in json_file:
        tweet = json.loads(line)
        tweet_id = tweet.get('id', '')  # Extract the ID
        full_text = tweet.get('full_text', '')
        
        # Find all hashtags and URLs in the full_text
        hashtags = hashtag_pattern.findall(full_text)
        urls = url_pattern.findall(full_text)
        
        # Write the extracted information to the CSV file, including the ID
        csv_writer.writerow([tweet_id, ', '.join(hashtags), ', '.join(urls)])
        
        # Append the data to the list for JSON output, including the ID
        extracted_data_for_json.append({
            'ID': tweet_id,
            'Hashtags': hashtags,
            'URLs': urls
        })

# Write the extracted data to a JSON file
with open('extracted_data_id.json', 'w') as output_json_file:
    json.dump(extracted_data_for_json, output_json_file, indent=4)

print('Extraction completed and saved to output.csv and extracted_data.json.')
