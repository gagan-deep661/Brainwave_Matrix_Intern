# Brainwave Matrix Intern Projects – Phishing Link Scanner & Password Strength Checker

Welcome to the **Brainwave Matrix Intern Projects** repository! This repository includes two cybersecurity tools developed as part of my internship with **Brainwave Matrix Solutions**: the **Phishing Link Scanner** and **Password Strength Checker**. These Python-based solutions provide practical tools to enhance user security by identifying suspicious URLs and encouraging strong password practices.

---

## 🔍 Project 1: Phishing Link Scanner

The **Phishing Link Scanner** is a Python program designed to analyze URLs and identify potentially malicious links based on common phishing characteristics. Phishing attacks often involve deceptive URLs to trick users into providing sensitive information. This tool inspects URLs based on common phishing patterns and performs a reachability check, helping users assess if a URL might be risky.

### 🛠️ Key Features
- **Pattern Detection**: Identifies common phishing indicators, such as:
  - IP addresses in URLs.
  - Uncommon top-level domains (e.g., `.tk`, `.ml`, `.ga`).
  - Suspicious characters like hyphens or `@` symbols.
  - Nested subdomains (e.g., `example.phish.com`).
- **Reachability Check**: Verifies if the URL is accessible, as non-existent or unreachable URLs may signal a phishing attempt.


## 🔍 Project 2: Password Strength Checker
This tool evaluates the strength of passwords based on length, complexity, and uniqueness. Built in Python on Kali Linux.

### 🛠️ Key Features
- Length check (8+ characters)
- Complexity check (uppercase, lowercase, numbers, special characters)
- Common password detection
