"""11. Payment System (Runtime Polymorphism)
An online store supports multiple payment methods: CreditCard, UPI, and
NetBanking. Create a base class Payment with a method process_payment() and
override it in each payment type."""
from abc import ABC, abstractmethod


# Base Class
class Payment(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass


# Subclass 1: Credit Card
class CreditCard(Payment):

    def __init__(self, card_number, card_holder):
        self.card_number = card_number
        self.card_holder = card_holder

    def process_payment(self, amount):
        print(
            f"Processing Credit Card payment of ₹{amount} for"
            f" {self.card_holder} (Card ending in {self.card_number[-4:]})."
        )


# Subclass 2: UPI
class UPI(Payment):

    def __init__(self, upi_id):
        self.upi_id = upi_id

    def process_payment(self, amount):
        print(f"Processing UPI payment of ₹{amount} via {self.upi_id}.")


# Subclass 3: NetBanking
class NetBanking(Payment):

    def __init__(self, bank_name, account_number):
        self.bank_name = bank_name
        self.account_number = account_number

    def process_payment(self, amount):
        print(
            f"Processing NetBanking payment of ₹{amount} through"
            f" {self.bank_name} (A/C ending in {self.account_number[-4:]})."
        )


# Checkout function demonstrating runtime polymorphism
def checkout(payment_method: Payment, amount: float):
    payment_method.process_payment(amount)


# --- Execution ---
if __name__ == "__main__":
    cc = CreditCard("4532015112830366", "Aarav Sharma")
    upi = UPI("aarav@okicici")
    net_banking = NetBanking("State Bank of India", "987654321012")

    # The exact method called is determined at runtime based on the object type
    checkout(cc, 2500.00)
    checkout(upi, 450.50)
    checkout(net_banking, 12000.00)
