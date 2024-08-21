def create_greeting(first_name, last_name):
    # Generate the personalized greeting message
    greeting_message = f"Hello, {first_name} {last_name}! Welcome!"
    
    return greeting_message

# Example usage
first_name = "John"
last_name = "Doe"

greeting = create_greeting(first_name, last_name)
print(greeting)
