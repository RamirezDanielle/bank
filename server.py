from flask import Flask, request, render_template, redirect, session
app = Flask(__name__)

app.secret_key = "hack the planet"

class BankAccount:
    def __init__(self, int_rate=0.02, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_account_info(self, user_name):
        return f"{user_name}'s Account - Balance: ${self.balance:.2f}"

    def yield_interest(self):
        self.balance += self.balance * self.int_rate

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.user_account= BankAccount(int_rate=0.02, balance = 0)

    def make_deposit(self, amount):
        self.user_account.deposit(amount)

    def account_info(self):
        self.user_account.display_account_info(self.name)

    def make_withdrawal(self, amount):
        self.user_account.withdraw(amount)

    def yield_interest(self):
        self.user_account.yield_interest()

    def account(self):
        self.account.deposit(100)
        print(self.account.balance)


@app.route('/')
def index():
    user1 = User("Bruce Wayne", "brucewayne@roadrunner.com")
    user1.make_deposit(500)
    user1.make_withdrawal(200)
    user1.yield_interest()
    user1_account_info = user1.account_info()
    # if request.method == 'POST':
    #     if 'deposit' in request.form:
    #         deposit_amount = float(request.form['deposit'])
    #         user1.make_deposit(deposit_amount)
    #         user1_account_info = user1.account_info()
    #     elif 'withdraw' in request.form:
    #         withdraw_amount = float(request.form['withdraw'])
    #         user1.make_withdrawal(withdraw_amount)
    #         user1_account_info = user1.account_info()
    return render_template('index.html', account_info=user1_account_info)

@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    return render_template('deposit.html')

@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    return render_template('withdraw.html')

@app.route('/process_deposit', methods=['POST'])
def process_deposit():
    user1 = User("Bruce Wayne", "brucewayne@roadrunner.com")
    deposit_amount = float(request.form['deposit'])
    user1.make_deposit(deposit_amount)
    return redirect('index.html')

@app.route('/process_withdrawal', methods=['POST'])
def process_withdrawal():
    user1 = User("Bruce Wayne", "brucewayne@roadrunner.com")
    withdraw_amount = float(request.form['withdraw'])
    user1.make_withdrawal(withdraw_amount)
    return redirect('index.html')

if __name__=='__main__':
    app.run(debug=True)