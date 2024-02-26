import json
import re

# REGEX
hashtag_pattern = re.compile(r'#\w+')
url_pattern = re.compile(r'https?://\S+')

# Read JSON
with open('tweets.json', 'r') as json_file, open('hashtags_and_urls.txt', 'w') as text_file:
    # Process each line
    for line in json_file:
        tweet = json.loads(line)
        full_text = tweet.get('full_text', '')
        
        # Find hashtags and urls
        hashtags = hashtag_pattern.findall(full_text)
        urls = url_pattern.findall(full_text)
        
        # Write hashtag to .txt
        for hashtag in hashtags:
            text_file.write(hashtag + '\n')
        
        # Write url to .txt
        for url in urls:
            text_file.write(url + '\n')

print('Extraction completed and saved to hashtags_and_urls.txt.')

