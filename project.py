class CRM:
    def __init__(self):
        self.customers = {}
        self.next_customer_id = 1  # Start customer IDs from 1
    
    def add_customer(self, name, email, phone, address):
        customer_id = self.next_customer_id
        new_customer = Customer(customer_id, name, email, phone, address)
        self.customers[customer_id] = new_customer
        self.next_customer_id += 1
        print(f"Customer {name} added successfully!")
    
    def update_customer(self, customer_id, name=None, email=None, phone=None, address=None):
        if customer_id in self.customers:
            customer = self.customers[customer_id]
            if name:
                customer.name = name
            if email:
                customer.email = email
            if phone:
                customer.phone = phone
            if address:
                customer.address = address
            print(f"Customer {customer_id} updated successfully!")
        else:
            print("Customer not found!")
    
    def delete_customer(self, customer_id):
        if customer_id in self.customers:
            del self.customers[customer_id]
            print(f"Customer {customer_id} deleted successfully!")
        else:
            print("Customer not found!")
    
    def view_customer(self, customer_id):
        if customer_id in self.customers:
            print(self.customers[customer_id])
        else:
            print("Customer not found!")
    
    def list_all_customers(self):
        if self.customers:
            for customer in self.customers.values():
                print(customer)
        else:
            print("No customers found.")
