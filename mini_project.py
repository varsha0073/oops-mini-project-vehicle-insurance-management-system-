class Insurance:

    CompanyName = 'SafeDrive'
    HeadOffice = 'Chennai'
    RegistrationNo = 'IRDA-99871'

    def __init__(self, name, policy_no, pin, sum_assured):
        self.name = name
        self.__policy_no = policy_no
        self.__pin = pin
        self.__sum_assured = sum_assured
        self.__premium = 0
        self.__last_transaction = "NO TRANSACTION YET DONE"

    # Private methods

    def __authenticate(self):
        policy_no = int(input('Enter Policy-no Here: '))
        pin = int(input('Enter Pin-no Here: '))
        return self.__policy_no == policy_no and self.__pin == pin

    def __generate_receipt(self, type, amount):
        return f'''
==================================================
              INSURANCE TRANSACTION RECEIPT
==================================================
Company           : {self.CompanyName}
Head Office       : {self.HeadOffice}
Registration No   : {self.RegistrationNo}
Vehicle Category  : {self.VehicleCategory}
Policy Holder     : {self.name}
Transaction Type  : {type}
Policy Number     : {self.__policy_no}
Transaction Amount: {amount}
Sum Assured       : {self.__sum_assured}
Current Premium   : {self.__premium}
=================================================='''

    def __calculate_base_premium(self):
        # Generic fallback rate; overridden by each child class
        return self.__sum_assured * 0.03

    # Public methods

    def buy_policy(self):
        premium = self.__calculate_base_premium()
        self.__premium = premium
        self.__last_transaction = self.__generate_receipt('BUY POLICY', premium)
        print(f'Policy Purchased Successfully. Initial Premium: {premium}')

    def pay_premium(self):
        if self.__authenticate():
            amount = int(input('Enter Premium amount to pay: '))
            if amount > 0:
                self.__premium += amount
                self.__last_transaction = self.__generate_receipt('PAY PREMIUM', amount)
                print('Premium Paid Successfully')
            else:
                print('Invalid amount')
        else:
            print('Authenticate Failed')

    def claim_policy(self):
        if self.__authenticate():
            amount = int(input('Enter claim amount: '))
            if amount > 0 and amount <= self.__sum_assured:
                self.__sum_assured -= amount
                self.__last_transaction = self.__generate_receipt('CLAIM', amount)
                print('Claim Processed Successfully')
            else:
                print('Invalid claim or exceeds sum assured')
        else:
            print('Authentication Failed')

    def show_policy_details(self):
        if self.__authenticate():
            print('==================================================')
            print(f'Company           : {self.CompanyName}')
            print(f'Vehicle Category  : {self.VehicleCategory}')
            print(f'Name              : {self.name}')
            print(f'Policy-no         : {self.__policy_no}')
            print(f'Sum Assured       : {self.__sum_assured}')
            print('==================================================')
        else:
            print('Authentication failed')

    def show_premium(self):
        if self.__authenticate():
            print(f'Current Premium: {self.__premium}')
        else:
            print('Authentication Failed')

    def list_last_transaction(self):
        if self.__authenticate():
            print(self.__last_transaction)
        else:
            print('Authentication Failed')


class CarInsurance(Insurance):

    VehicleCategory = 'Four Wheeler - Car'

    def __init__(self, name, policy_no, pin, sum_assured, car_number):
        super().__init__(name, policy_no, pin, sum_assured)
        self.__car_number = car_number

    def _Insurance__calculate_base_premium(self):
        # Cars are costlier to insure
        return self._Insurance__sum_assured * 0.05


class BikeInsurance(Insurance):

    VehicleCategory = 'Two Wheeler - Bike'

    def __init__(self, name, policy_no, pin, sum_assured, bike_number):
        super().__init__(name, policy_no, pin, sum_assured)
        self.__bike_number = bike_number

    def _Insurance__calculate_base_premium(self):
        # Bikes are cheaper to insure
        return self._Insurance__sum_assured * 0.02


# --------------------- Driver code ---------------------

car1 = CarInsurance('Bablu', 630514, 2255, 500000, 'TN01AB1234')
bike1 = BikeInsurance('Ramu', 720811, 1122, 100000, 'TN82CD5678')

while True:
    print('''
==================================================
             WELCOME TO SAFEDRIVE INSURANCE
==================================================
1. Buy-Policy
2. Pay-Premium
3. Claim-policy
4. Show-policy-details
5. Show-premium
6. List-last-transaction
7. Exit
==================================================''')

    choice = int(input('Enter your choice: '))

    if choice in range(1, 7):
        vehicle_choice = input('Select vehicle - Car or Bike: ').strip().lower()

        obj = car1 if vehicle_choice == 'car' else bike1 if vehicle_choice == 'bike' else None

        if obj is None:
            print('Please type "Car" or "Bike"')
            continue

        if choice == 1:
            obj.buy_policy()
        elif choice == 2:
            obj.pay_premium()
        elif choice == 3:
            obj.claim_policy()
        elif choice == 4:
            obj.show_policy_details()
        elif choice == 5:
            obj.show_premium()
        elif choice == 6:
            obj.list_last_transaction()

    elif choice == 7:
        print('''
==================================================
               THANK YOU, DRIVE SAFE!
==================================================''')
        break

    else:
        print('Arree yaaar pls enter valid choice number')
