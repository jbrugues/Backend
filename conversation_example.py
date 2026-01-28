import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Start a conversation with context
conversation_history = [
    {"role": "user", "content": "I'm building a systematic trading system. What should I consider for data quality?"},
]

# First message
response1 = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=1024,
    messages=conversation_history
)

print("Claude's first response:")
print(response1.content[0].text)
print("\n" + "="*60 + "\n")

# Add Claude's response to history
conversation_history.append({
    "role": "assistant", 
    "content": response1.content[0].text
})

# Follow-up question with context
conversation_history.append({
    "role": "user", 
    "content": "What specific Python libraries would you recommend for data validation?"
})

response2 = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=1024,
    messages=conversation_history
)

print("Claude's follow-up response:")
print(response2.content[0].text)