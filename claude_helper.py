import os
from dotenv import load_dotenv
from anthropic import Anthropic, APIError

load_dotenv()

def ask_claude(prompt, model="claude-sonnet-4-5-20250929", max_tokens=2048):
    """
    Send a prompt to Claude and return the response with error handling.
    """
    try:
        client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
        
        message = client.messages.create(
            model=model,
            max_tokens=max_tokens,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        return message.content[0].text
    
    except APIError as e:
        return f"API Error: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"