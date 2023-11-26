# security_functions.py
import re
from cryptography.fernet import Fernet

def check_sensitive_data_exposure(data):
    sensitive_keywords = ['password', 'secret', 'key', 'token', 'api_key']
    for keyword in sensitive_keywords:
        if re.search(rf'\b{re.escape(keyword)}\b', data, flags=re.IGNORECASE):
            return f"Sensitive data exposure detected: '{keyword}' found in the data."
    return "No sensitive data exposure detected."

def input_validation(input_data):
    # Enhanced input validation to prevent common attacks
    if re.search(r'[^\w\s@.]+', input_data):
        return "Input validation failed. Invalid characters detected."
    return "Input validation successful."

def check_security_vulnerabilities(code):
    # Enhanced security vulnerability checks
    dangerous_functions = ['eval', 'exec', 'os.system', '__import__']
    for func in dangerous_functions:
        if func in code:
            return f"Security vulnerability detected: Dangerous function '{func}' used in the code."
    return "No security vulnerabilities detected."

def check_file_permissions(filepath):
    # Enhanced file permission checks
    import os
    try:
        with open(filepath, 'a'):
            pass
        return "File has read and write permissions."
    except PermissionError:
        return "File does not have sufficient permissions."

def encrypt_data(data, key):
    # Use Fernet symmetric key encryption for more secure data encryption
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data
