# PhishGuard - Basic Security Tool

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Project](https://img.shields.io/badge/Type-Security%20Tool-darkgreen)
![Level](https://img.shields.io/badge/Difficulty-Basic-yellow)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## About the Project  

PhishGuard is a simple command-line tool developed in Python to identify potential phishing attempts.  
It focuses on two main checks:  
- Detecting risky keywords in emails  
- Identifying suspicious domain similarities  

The project demonstrates how basic logic can be applied to improve security awareness.

---

## Functional Modules  

### Email Risk Detection (Task-1)
- Accepts email content as input  
- Searches for predefined phishing keywords  
- Returns a warning if any risky word is found  

**Keywords used:**  
urgent, verify, password, bank, click  

---

### Domain Similarity Detection (Task-2)
- Accepts two domain names  
- Converts both to lowercase  
- Applies normalization for common character substitutions:
  - 0 → o  
  - 1 → l  
  - 3 → e  
  - @ → a  

- Checks:
  - Direct match after normalization  
  - Base domain similarity (before ".")  

---

## Sample Run  

### Email Check  

Input:  
Enter email text: Please verify your bank account urgently  

Output:  
Warning: This email may be risky  

---

### Domain Check  

Input:  
Enter first domain: g00gle.com  
Enter second domain: google.com  

Output:  
Suspicious domain  

---

Input:  
Enter first domain: test.com  
Enter second domain: demo.com  

Output:  
Domain looks safe  

---

### Task 3: Short Answer

## Use Cases
1.I think this system can be used in email to check if a message is safe.

2.It can also be used in browsers to warn about fake websites.

3.We can build it as a website to check links.

4.It is useful for companies to protect users.

Overall, it helps avoid phishing attacks.

---

## Technical Approach  

- Uses string operations for text processing  
- Applies normalization to reduce character-based spoofing  
- Uses conditional checks to classify results  
- Keeps logic simple and readable  

---

## Limitations  

- Keyword-based detection may not cover advanced phishing cases  
- Domain comparison is rule-based and not highly accurate  
- No real-time validation with external sources  

---

## Possible Enhancements  

- Add more advanced phishing patterns  
- Implement similarity scoring  
- Integrate with web interface  
- Use AI/ML models for better detection  

---

## Conclusion  

PhishGuard provides a basic understanding of how phishing detection works using simple programming techniques.  
It can be extended into a more advanced system with additional logic and real-world integrations.

---

## Author  

[Your Friend’s Name]


### Task 3: Short Answer

## Use Cases
1.I think this system can be used in email to check if a message is safe.

2.It can also be used in browsers to warn about fake websites.

3.We can build it as a website to check links.

4.It is useful for companies to protect users.

Overall, it helps avoid phishing attacks.
