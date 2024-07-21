import json

def clean_transcript(transcript_data):
    """
    Clean up the transcript data and format it into readable text.
    
    Parameters:
    - transcript_data: List of dictionaries containing transcript segments.
    
    Returns:
    - Formatted transcript as a single string.
    """
    # Initialize an empty string to hold the cleaned transcript
    cleaned_text = ""
    
    # Iterate over each segment in the transcript data
    for segment in transcript_data:
        # Extract the text from each segment
        text = segment['text']
        
        # Skip segments that are not meaningful (e.g., "[Music]")
        if text.strip() and text != "[Music]":
            cleaned_text += text + " "
    
    # Remove extra spaces and format the text
    cleaned_text = cleaned_text.strip()
    
    return cleaned_text

# Example transcript data (in JSON format)
transcript_json = '''
[{"text": "[Music]", "start": 0.0, "duration": 14.65}, {"text": "we're no strangers to", "start": 18.8, "duration": 7.239}, {"text": "love you know the rules and so do", "start": 21.8, "duration": 7.84}, {"text": "I I full commitments while I'm thinking", "start": 26.039, "duration": 5.201}, {"text": "of", "start": 29.64, "duration": 5.88}, {"text": "you wouldn't get this from any other guy", "start": 31.24, "duration": 8.2}, {"text": "I just want to tell you how I'm", "start": 35.52, "duration": 7.84}, {"text": "feeling got to make you understand Never", "start": 39.44, "duration": 6.759}, {"text": "Going To Give You Up never going to let", "start": 43.36, "duration": 6.359}, {"text": "you down never going to run around and", "start": 46.199, "duration": 7.441}, {"text": "desert you never going to make you cry", "start": 49.719, "duration": 6.401}, {"text": "never going to say goodbye never going", "start": 53.64, "duration": 7.12}, {"text": "to tell a lie and hurt you", "start": 56.12, "duration": 7.84}, {"text": "we've known each other for so", "start": 60.76, "duration": 6.56}, {"text": "long your heart's been aching but your", "start": 63.96, "duration": 6.64}, {"text": "to sh to say it inside we both know", "start": 67.32, "duration": 5.2}, {"text": "what's been going", "start": 70.6, "duration": 6.04}, {"text": "on we know the game and we're going to", "start": 72.52, "duration": 8.88}, {"text": "playing and if you ask me how I'm", "start": 76.64, "duration": 7.96}, {"text": "feeling don't tell me you're too my you", "start": 81.4, "duration": 6.32}, {"text": "see Never Going To Give You Up never", "start": 84.6, "duration": 6.199}, {"text": "going to let you down never to run", "start": 87.72, "duration": 6.679}, {"text": "around and desert you never going to", "start": 90.799, "duration": 7.28}, {"text": "make you cry never going to say goodbye", "start": 94.399, "duration": 7.841}, {"text": "never going to tell a lie and hurt you", "start": 98.079, "duration": 6.601}, {"text": "never going to give you up never going", "start": 102.24, "duration": 5.44}, {"text": "to let you down never going to run", "start": 104.68, "duration": 6.64}, {"text": "around and desert you never going to", "start": 107.68, "duration": 7.52}, {"text": "make you cry never going to sing goodbye", "start": 111.32, "duration": 7.52}, {"text": "going to tell a lie and hurt", "start": 115.2, "duration": 6.64}, {"text": "you", "start": 118.84, "duration": 3.0}, {"text": "give", "start": 121.96, "duration": 2.32}, {"text": "you give", "start": 125.24, "duration": 6.639}, {"text": "you going to give going to give", "start": 127.64, "duration": 8.2}, {"text": "you going to give going to give", "start": 131.879, "duration": 8.161}, {"text": "you we've known each other for so", "start": 135.84, "duration": 7.52}, {"text": "long your heart's been aching but you're", "start": 140.04, "duration": 6.88}, {"text": "too sh to say inside we both know what's", "start": 143.36, "duration": 5.12}, {"text": "been going", "start": 146.92, "duration": 5.8}, {"text": "on we the game and we're going to play", "start": 148.48, "duration": 9.28}, {"text": "it I just want to tell you how I'm", "start": 152.72, "duration": 8.92}, {"text": "feeling got to make you understand Never", "start": 157.76, "duration": 6.72}, {"text": "Going To Give You Up never going to let", "start": 161.64, "duration": 6.44}, {"text": "you down never going to run around and", "start": 164.48, "duration": 7.479}, {"text": "desert you never going to make you cry", "start": 168.08, "duration": 6.36}, {"text": "never going to say goodbye never going", "start": 171.959, "duration": 6.681}, {"text": "to tell you my and Hurt You Never Going", "start": 174.44, "duration": 5.96}, {"text": "To Give You Up", "start": 178.64, "duration": 4.239}, {"text": "never going to let you down never going", "start": 180.4, "duration": 6.68}, {"text": "to run around and desert you never going", "start": 182.879, "duration": 8.161}, {"text": "to make you C never going to say goodbye", "start": 187.08, "duration": 5.32}, {"text": "never going to", "start": 191.04, "duration": 5.6}, {"text": "tell and Hur You Never Going To Give You", "start": 192.4, "duration": 7.28}, {"text": "Up never going to let you down never", "start": 196.64, "duration": 7.319}, {"text": "going to run around and desert you never", "start": 199.68, "duration": 7.35}, {"text": "going to make you going to", "start": 203.959, "duration": 4.721}, {"text": "[Music]", "start": 207.03, "duration": 3.97}, {"text": "goodbye", "start": 208.68, "duration": 5.32}, {"text": "and", "start": 211.0, "duration": 3.0}]
'''

# Load transcript data from JSON
transcript_data = json.loads(transcript_json)

# Clean up and format the transcript
formatted_text = clean_transcript(transcript_data)

# Print the formatted transcript
print(formatted_text)
