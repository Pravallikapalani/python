class CarShowroom:
    def __init__(self):
        # Dictionary to store company-wise models and their prices
        self.car_models = {
            'mercedes': {'gvegan': 5000000, 'amg': 8000000},
            'toyota': {'innova': 1500000, 'fortuner': 3000000},
            'mahindra': {'scorpio': 1200000, 'thar': 1000000}
        }
        # Default values for CGST, SGST, and Insurance
        self.cgst = 0.1  # 10%
        self.sgst = 0.1  # 10%
        self.insurance = 50000  # INR 50,000

    def company(self, company_name):
        # Check if the company name is valid
        if company_name.lower() in self.car_models:
            self.selected_company = company_name.lower()
            print(f"Company selected: {company_name.capitalize()}")
        else:
            print("Invalid company name.")

    def model(self):
        # Check if a company has been selected
        if hasattr(self, 'selected_company'):
            models = self.car_models[self.selected_company]
            print("Available models:")
            for model in models.keys():
                print(model.capitalize())
            selected_model = input("Enter the model you want to select: ").lower()
            if selected_model in models:
                self.selected_model = selected_model
                print(f"Selected model: {selected_model.capitalize()}")
            else:
                print("Invalid model.")
        else:
            print("Please select a company first.")

    def price(self):
        # Check if both company and model are selected
        if hasattr(self, 'selected_company') and hasattr(self, 'selected_model'):
            showroom_price = self.car_models[self.selected_company][self.selected_model]
            total_price = showroom_price + (showroom_price * self.cgst) + (showroom_price * self.sgst) + self.insurance
            print(f"On-road price for {self.selected_model.capitalize()} from {self.selected_company.capitalize()}: INR {total_price:.2f}")
        else:
            print("Please select a company and model first.")


# Example usage
showroom = CarShowroom()
showroom.company('toyota')
showroom.model()
showroom.price()
