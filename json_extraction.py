import json
import re
import csv

# Regex
hashtag_pattern = re.compile(r'#\w+')
url_pattern = re.compile(r'https?://\S+')

# Read from JSON
with open('tweets.json', 'r') as json_file, open('output_id.csv', 'w', newline='') as csv_file:
    # CSV writer creation
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['ID', 'Hashtags', 'URLs'])
    
    # JSON List
    extracted_data_for_json = []
    
    # Process JSON file
    for line in json_file:
        tweet = json.loads(line)
        tweet_id = tweet.get('id', '')  # Extract the ID
        full_text = tweet.get('full_text', '')
        
        # Apply regex to tweet text
        hashtags = hashtag_pattern.findall(full_text)
        urls = url_pattern.findall(full_text)
        
        # Write to CSV
        csv_writer.writerow([tweet_id, ', '.join(hashtags), ', '.join(urls)])
        
        # Update JSON list
        extracted_data_for_json.append({
            'ID': tweet_id,
            'Hashtags': hashtags,
            'URLs': urls
        })

# Write to JSON
with open('extracted_data_id.json', 'w') as output_json_file:
    json.dump(extracted_data_for_json, output_json_file, indent=4)

print('Extraction completed and saved to output.csv and extracted_data.json.')
