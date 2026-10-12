from openai import OpenAI, RateLimitError, AuthenticationError
from dotenv import load_dotenv
import os

print("Program Started")

load_dotenv()#load .env file

api_key = os.getenv("OPENAI_API_KEY")

print("Current Directory:", os.getcwd())

if api_key:
    print("API Key Loaded Successfully")
else:
    print("API Key Not Found")
    exit()

try:
    client = OpenAI(api_key=api_key)
    print("OpenAI Client Created\n")
except Exception as e:
    print("Failed to Create Client")
    print(e)
    exit()

INPUT_PRICE = 0.000005
OUTPUT_PRICE = 0.000015

def ask_ai(prompt):

    print("\nSending Request...")
    print("Prompt:", prompt[:50])

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=300,
        )

        print("Response Received")

        answer = response.choices[0].message.content

        input_tokens = response.usage.prompt_tokens
        output_tokens = response.usage.completion_tokens
        total_tokens = response.usage.total_tokens

        cost = (
            input_tokens * INPUT_PRICE +
            output_tokens * OUTPUT_PRICE
        )

        return {
            "success": True,
            "prompt": prompt,
            "answer": answer,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "total_tokens": total_tokens,
            "cost": cost
        }

    except AuthenticationError:

        print("Invalid API Key")

        return {
            "success": False,
            "answer": "Authentication Failed",
            "input_tokens": 0,
            "output_tokens": 0,
            "total_tokens": 0,
            "cost": 0
        }

    except RateLimitError:

        print("API Quota Exceeded")
        print("Check Billing / Credits")

        return {
            "success": False,
            "answer": "Quota Exceeded",
            "input_tokens": 0,
            "output_tokens": 0,
            "total_tokens": 0,
            "cost": 0
        }

    except Exception as e:

        print("Unexpected Error")
        print(e)

        return {
            "success": False,
            "answer": str(e),
            "input_tokens": 0,
            "output_tokens": 0,
            "total_tokens": 0,
            "cost": 0
        }

tasks = [
    "Explain recursion in simple terms.",
    "Write a haiku about programming.",
    "List 5 Python best practices.",
    """
    Fix this code:

    def divide(a,b):
        return a/b

    print(divide(10,0))
    """,
    "Translate 'Hello, how are you?' into 5 languages."
]

grand_total = 0

for i, task in enumerate(tasks, start=1):

    print("\n" + "=" * 60)
    print(f"TASK {i}")
    print("=" * 60)

    result = ask_ai(task)

    if result["success"]:

        print("\nPROMPT:")
        print(result["prompt"])

        print("\nRESPONSE:")
        print(result["answer"])

        print("\nTOKEN USAGE")
        print("Input Tokens :", result["input_tokens"])
        print("Output Tokens:", result["output_tokens"])
        print("Total Tokens :", result["total_tokens"])

        print(f"Cost: ${result['cost']:.6f}")

        grand_total += result["cost"]

    else:

        print("\nRequest Failed")
        print("Reason:", result["answer"])

print("\n" + "=" * 60)
print("TOTAL COST")
print("=" * 60)
print(f"${grand_total:.6f}")

print("\nProgram Finished")