# security_functions.py

def check_sensitive_data_exposure(data):
    sensitive_keywords = ['password', 'secret', 'key', 'token', 'api_key']
    for keyword in sensitive_keywords:
        if keyword in data.lower():
            return f"Sensitive data exposure detected: {keyword} found in the data."
    return "No sensitive data exposure detected."

def input_validation(input_data):
    # Implement input validation logic based on your requirements
    # This could include checks for SQL injection, XSS, etc.
    # For simplicity, let's check for alphanumeric characters only.
    if not input_data.isalnum():
        return "Input validation failed. Only alphanumeric characters are allowed."
    return "Input validation successful."

def check_security_vulnerabilities(code):
    # Implement security vulnerability checks based on your requirements
    # For simplicity, let's check for the use of eval() function.
    if 'eval(' in code:
        return "Security vulnerability detected: 'eval' function used in the code."
    return "No security vulnerabilities detected."

def check_file_permissions(filepath):
    # Implement file permission checks based on your requirements
    # For simplicity, let's check if the file has read and write permissions.
    import os
    if os.access(filepath, os.R_OK | os.W_OK):
        return "File has read and write permissions."
    return "File does not have sufficient permissions."

def encrypt_data(data):
    # Implement data encryption logic based on your requirements
    # For simplicity, let's use a basic XOR encryption.
    key = 0x5A
    encrypted_data = ''.join(chr(ord(char) ^ key) for char in data)
    return encrypted_data
