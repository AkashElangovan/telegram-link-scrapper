import re

def find_tradingview_links(input_file, output_file):
    # Open the input file with UTF-8 encoding
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Find all links related to https://www.tradingview.com/
    links = re.findall(r'https://www\.tradingview\.com/[^\s"]+', text)

    # Write the links into a new text file
    with open(output_file, 'w') as f:
        for link in links:
            f.write(link + '\n')

    print("Links related to 'https://www.tradingview.com/' have been extracted and saved to", output_file)

# Example usage:
input_file = r""  # Provide the path to your input text file
output_file = r""  # Provide the path where you want to save the output
find_tradingview_links(input_file, output_file)
