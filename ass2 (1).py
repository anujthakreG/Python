from abc import ABC, abstractmethod
import datetime

# Custom Exceptions
class InsufficientFundsError(Exception): pass
class WithdrawalLimitExceededError(Exception): pass
class AccountLockedError(Exception): pass
class MaturityNotReachedError(Exception): pass

# Transaction Class
class Transaction:
    def __init__(self, transaction_id, t_type, amount, description=""):
        self.transaction_id = transaction_id
        self.type = t_type
        self.amount = amount
        self.date = datetime.datetime.now()
        self.description = description

# Customer Class
class Customer:
    def __init__(self, customer_id, name, address, phone):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.phone = phone
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

# Abstract Account Class
class Account(ABC):
    def __init__(self, account_number, balance, customer):
        self.account_number = account_number
        self.balance = balance
        self.customer = customer
        self.transaction_history = []

    @abstractmethod
    def deposit(self, amount): pass

    @abstractmethod
    def withdraw(self, amount): pass

    @abstractmethod
    def calculate_interest(self): pass

    def transfer(self, to_account, amount, inter_branch_fee=10):
        if self.balance < amount + inter_branch_fee:
            raise InsufficientFundsError("Not enough balance for transfer")
        self.balance -= (amount + inter_branch_fee)
        to_account.balance += amount
        self.transaction_history.append(Transaction("TXN1", "TRANSFER", amount, "Transfer to " + to_account.account_number))
        to_account.transaction_history.append(Transaction("TXN2", "TRANSFER", amount, "Transfer from " + self.account_number))

# Savings Account
class SavingsAccount(Account):
    def __init__(self, account_number, balance, customer, interest_rate):
        super().__init__(account_number, balance, customer)
        self.interest_rate = interest_rate
        self.monthly_withdrawals = 0

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(Transaction("TXN", "DEPOSIT", amount))

    def withdraw(self, amount):
        if self.monthly_withdrawals >= 3:
            raise WithdrawalLimitExceededError("Withdrawal limit exceeded")
        if self.balance < amount:
            raise InsufficientFundsError("Insufficient funds")
        self.balance -= amount
        self.monthly_withdrawals += 1
        self.transaction_history.append(Transaction("TXN", "WITHDRAWAL", amount))

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.transaction_history.append(Transaction("TXN", "INTEREST", interest))

# Current Account
class CurrentAccount(Account):
    def __init__(self, account_number, balance, customer, overdraft_limit):
        super().__init__(account_number, balance, customer)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(Transaction("TXN", "DEPOSIT", amount))

    def withdraw(self, amount):
        if self.balance - amount < -self.overdraft_limit:
            raise InsufficientFundsError("Overdraft limit exceeded")
        self.balance -= amount
        self.transaction_history.append(Transaction("TXN", "WITHDRAWAL", amount))

    def calculate_interest(self):
        pass  # No interest

# Fixed Deposit Account
class FixedDepositAccount(Account):
    def __init__(self, account_number, principal, customer, tenure_months, rate):
        super().__init__(account_number, principal, customer)
        self.principal = principal
        self.tenure_months = tenure_months
        self.maturity_date = datetime.date.today() + datetime.timedelta(days=30*tenure_months)
        self.rate = rate

    def deposit(self, amount):
        raise AccountLockedError("Cannot deposit into FD")

    def withdraw(self, amount):
        if datetime.date.today() < self.maturity_date:
            raise MaturityNotReachedError("FD not matured yet")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds")
        self.balance -= amount
        self.transaction_history.append(Transaction("TXN", "WITHDRAWAL", amount))

    def calculate_interest(self):
        # Compound interest
        self.balance = self.principal * ((1 + self.rate) ** self.tenure_months)
        self.transaction_history.append(Transaction("TXN", "INTEREST", self.balance - self.principal))

# Branch Class
class Branch:
    def __init__(self, branch_code, location):
        self.branch_code = branch_code
        self.location = location
        self.accounts = []

# Bank Class
class Bank:
    def __init__(self):
        self.customers = {}
        self.branches = []

    def add_customer(self, customer):
        self.customers[customer.customer_id] = customer

    def add_branch(self, branch):
        self.branches.append(branch)

    def process_monthly_operations(self):
        for cust in self.customers.values():
            for acc in cust.accounts:
                acc.calculate_interest()
                if isinstance(acc, SavingsAccount):
                    acc.monthly_withdrawals = 0



# ERP SYSTEM 


from abc import ABC, abstractmethod
import datetime

# Custom Exceptions
class StockNotAvailableError(Exception): pass
class UnauthorizedAccessError(Exception): pass
class ReorderThresholdBreachedError(Exception): pass
class InvalidOrderError(Exception): pass

# Decorator for auditing
def audit(cls):
    for attr, value in cls.__dict__.items():
        if callable(value):
            def wrapper(func):
                def inner(*args, **kwargs):
                    print(f"[AUDIT] {datetime.datetime.now()} - Calling {func.__name__} with {args[1:]}, {kwargs}")
                    return func(*args, **kwargs)
                return inner
            setattr(cls, attr, wrapper(value))
    return cls

# Abstract ERP Module
class ERPModule(ABC):
    def __init__(self, module_id, name):
        self.module_id = module_id
        self.name = name

    @abstractmethod
    def process_transaction(self, data): pass

    @abstractmethod
    def generate_report(self, criteria): pass

# Entity Classes
class Item:
    def __init__(self, item_code, name, unit_price, stock_qty, reorder_level):
        self.item_code = item_code
        self.name = name
        self.unit_price = unit_price
        self.stock_qty = stock_qty
        self.reorder_level = reorder_level

class Order:
    def __init__(self, order_id, customer_name, items, salesperson_id):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items
        self.total_amount = sum(qty * 100 for qty in items.values())  # simplified
        self.status = "PENDING"
        self.salesperson_id = salesperson_id

class PurchaseOrder:
    def __init__(self, po_id, supplier_name, items, expected_delivery_date):
        self.po_id = po_id
        self.supplier_name = supplier_name
        self.items = items
        self.expected_delivery_date = expected_delivery_date

class Employee:
    def __init__(self, emp_id, name, role, department):
        self.emp_id = emp_id
        self.name = name
        self.role = role
        self.department = department

# Inventory Module
class InventoryModule(ERPModule):
    def __init__(self, module_id, name):
        super().__init__(module_id, name)
        self.items = {}

    def process_transaction(self, data):
        item_code, qty = data
        if self.items[item_code].stock_qty < qty:
            raise StockNotAvailableError("Not enough stock")
        self.items[item_code].stock_qty -= qty

    def generate_report(self, criteria):
        return [item for item in self.items.values() if item.stock_qty < item.reorder_level]

# Sales Module
class SalesModule(ERPModule):
    def __init__(self, module_id, name):
        super().__init__(module_id, name)
        self.orders = []

    def process_transaction(self, data):
        self.orders.append(data)

    def generate_report(self, criteria):
        return [o for o in self.orders if o.status == criteria]

    def pending_orders(self):
        for o in self.orders:
            if o.status == "PENDING":
                yield o

# Procurement Module
class ProcurementModule(ERPModule):
    def __init__(self, module_id, name):
        super().__init__(module_id, name)
        self.purchase_orders = []

    def process_transaction(self, data):
        self.purchase_orders.append(data)

    def generate_report(self, criteria):
        return [po for po in self.purchase_orders if po.expected_delivery_date == criteria]

# HR Module
class HRModule(ERPModule):
    def __init__(self, module_id, name):
        super().__init__(module_id, name)
        self.employees = {}

    def process_transaction(self, data):
        self.employees[data.emp_id] = data

    def generate_report(self, criteria):
        return [e for e in self.employees.values() if e.role == criteria