from claude_helper import ask_claude

def debug_code(code_snippet, error_message):
    """Ask Claude to help debug code."""
    prompt = f"""
I'm getting an error in my Python code. Here's the code:
```python
{code_snippet}
```

And here's the error message:
{error_message}

Can you explain what's wrong and suggest a fix?
"""
    return ask_claude(prompt)

def explain_concept(concept):
    """Ask Claude to explain a programming concept."""
    prompt = f"Explain {concept} in the context of Python programming for financial data analysis. Be concise but thorough."
    return ask_claude(prompt)

# Example usage
if __name__ == "__main__":
    # Test the debug function
    buggy_code = """
df = pd.read_csv('data.csv')
result = df['price'] * df['quantity'
print(result)
"""
    error = "SyntaxError: invalid syntax"
    
    print(debug_code(buggy_code, error))
```

**Step 10: Practice and Commit (Day 7)**

Spend the last day experimenting. Try asking Claude to:
- Explain parts of your code
- Suggest improvements to your functions
- Help you understand error messages
- Generate test data or sample code snippets

Commit all your work:
```
git add .
git commit -m "Add Claude API integration with helper functions and examples"
git push