import stripe

stripe.api_key = "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"

customer = stripe.Customer.create(
    email="customer@example.com",
    name="John Doe",
    description="My First Test Customer",
    source="tok_visa" # replace with your token
)

print(customer)
