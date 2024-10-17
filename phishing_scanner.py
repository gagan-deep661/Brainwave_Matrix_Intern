import re
import requests
from urllib.parse import urlparse

# Function to validate a URL format
def validate_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

# Check for common phishing URL patterns using regex
def detect_suspicious_url(url):
    # Example suspicious patterns (this can be extended)
    suspicious_patterns = [
        re.compile(r"http://\d+\.\d+\.\d+\.\d+"),  # IP address in URL
        re.compile(r"-"),  # URLs with hyphens are sometimes suspicious
        re.compile(r"\.tk|\.ml|\.ga|\.cf|\.gq"),  # Uncommon or free top-level domains (TLDs)
        re.compile(r"@"),  # URLs with @ symbol might be phishing
        re.compile(r"https?://.*\..*\..*")  # Nested subdomains (e.g., phish.example.com)
    ]
    
    for pattern in suspicious_patterns:
        if pattern.search(url):
            return True
    return False

# Check if URL resolves to an IP address or domain (non-existent domains may indicate phishing)
def check_url_reachable(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return "URL is reachable and returns a valid response."
        else:
            return f"URL returned status code: {response.status_code}. Might be suspicious."
    except requests.exceptions.RequestException:
        return "URL is unreachable. Could be suspicious."

# Main function to scan the URL
def scan_url(url):
    if not validate_url(url):
        return f"Invalid URL format: {url}"

    if detect_suspicious_url(url):
        return f"Suspicious URL detected based on pattern analysis: {url}"
    
    # Check if URL is reachable
    return check_url_reachable(url)

# Main script
if __name__ == "__main__":
    url = input("Enter a URL to scan: ")
    
    # Scan the URL using pattern and reachability checks
    result = scan_url(url)
    print(result)
