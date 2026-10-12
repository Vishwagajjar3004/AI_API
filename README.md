# AI_API
AI API Calls Project
The application:

Loads an API key from a .env file
Creates an OpenAI client
Sends multiple prompts to an AI model
Receives AI-generated responses
Tracks token usage
Calculates approximate API costs
Handles common API errors gracefully
Features

1. Environment Variables
The API key is stored securely in a .env file instead of being hardcoded in the source code.

2. OpenAI API Integration
The project uses the OpenAI Python SDK to send prompts and receive responses.
Model used:
gpt-4o-mini

3. Multiple AI Tasks
The application performs the following tasks:
Explain recursion in simple terms
Write a haiku about programming
List 5 Python best practices
Fix a buggy Python code snippet
Translate a sentence into 5 languages

4. Token Usage Tracking
For every request, the application records:
Input Tokens
Output Tokens
Total Tokens
This helps understand how API billing works.

5. Cost Estimation
The application calculates an approximate API cost based on token usage.
Formula:
Cost = (Input Tokens × Input Price) + (Output Tokens × Output Price)

6. Error Handling
The application handles common errors:
Authentication Error
Occurs when the API key is invalid.
