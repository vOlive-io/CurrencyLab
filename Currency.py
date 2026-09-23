class CurrencyConverter:
    def __init__(self, ex):
        self.exchange_rates = ex

    def convert(self, amount, from_currency, to_currency): 
        return round(amount/self.exchange_rates[from_currency] * self.exchange_rates[to_currency], 2)
        
    def add_rate(self, currency, rate): 
        self.exchange_rates[currency] = rate
