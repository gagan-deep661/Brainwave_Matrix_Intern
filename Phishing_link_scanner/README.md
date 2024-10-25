# Phishing Link Scanner
The **Phishing Link Scanner** is a Python program that inspects URLs based on common phishing patterns and reachability checks, assisting users in identifying potentially unsafe links before accessing them.

## 🛠️ Features

- **Pattern Detection**: Uses regular expressions to detect suspicious characteristics in URLs, such as:
  - IP addresses in URLs
  - Uncommon top-level domains (e.g., `.tk`, `.ml`, `.ga`)
  - Use of hyphens or `@` symbols
  - Nested subdomains (e.g., `example.phish.com`)
  
- **Reachability Check**: Validates if the URL is accessible, since non-existent or unreachable URLs may indicate phishing attempts.

### Prerequisites

Ensure Python 3 and `pip` are installed on your system. Install the `requests` library, which is required for URL reachability checks.

```bash
pip install requests
