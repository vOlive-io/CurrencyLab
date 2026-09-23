# Currency Lab
This is a lab assignment from Ms Ormes' software engineering class, for more information look [here](https://gormes-epic.github.io/#Software-Engineering/Currency-Translator-Lab)

## Class working
This class is a simple currency translator, based in USD

|Instance Variables & Methods | Description |
|----|--------|
| Self.exchangerates | a dictionary contains every exchange rate, based in USD given to the translator |
| .convert(amount, from_currency, to_currency) | converts from one currency to the other currency. from_currency should be in the currency you are translating from |
| .add_rate(currency, rate) | adds a new exchange rate, currency is a string, rate is a float |



## Automated Testing
Every time I commit to the repository GitHub actions runs tests for me, you can replicate this by creating a .github/workflows/run-tests.yml file with the same code as mine
