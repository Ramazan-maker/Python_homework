class Order:
    def __init__(self, order_id, customer_name, total_amount, status, payment_method, shipping_address):
        self.order_id = order_id
        self.customer_name = customer_name
        self.total_amount = total_amount
        self.status = status
        self.payment_method = payment_method
        self.shipping_address = shipping_address

    def place_order(self):
        print("Order placed.")

    def cancel_order(self):
        print("Order cancelled.")

    def update_status(self, new_status):
        print(f"Order status updated to {new_status}.")

    def calculate_discounted_price(self, discount_percentage):
        discounted_price = self.total_amount * (1 - discount_percentage / 100)
        print(f"Discounted price: {discounted_price}.")


order1 = Order(12345, "John Doe", 1000, "Pending", "Credit Card", "123 Street, City")
order2 = Order(54321, "Jane Smith", 500, "Delivered", "PayPal", "456 Avenue, Town")

order1.place_order()
order1.calculate_discounted_price(10)
order2.update_status("Returned")
order2.cancel_order()