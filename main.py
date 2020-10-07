import datetime as dt
# REVIEW: json is not used, delete it
import json
# REVIEW: no 2 empty lines before class (PEP8)
class Record:
    # REVIEW: no Docsring of the class
    def __init__(self, amount, comment, date=''):
        # REVIEW: no spaces before and after operator
        self.amount=amount
        # REVIEW: length line more than 79 characters,
        # divide it or move text to next line
        self.date = dt.datetime.now().date() if not date else dt.datetime.strptime(date, '%d.%m.%Y').date()
        # REVIEW: no spaces before and after operator
        self.comment=comment
# REVIEW: no 2 empty lines before class (PEP8)
class Calculator:
    # REVIEW: no Docsring of the class
    def __init__(self, limit):
        self.limit = limit
        # REVIEW: no spaces before and after operator
        self.records=[]
    # REVIEW: no free space between blocks
    def add_record(self, record):
        # REVIEW: no Docsring of the method
        self.records.append(record)
    # REVIEW: no free space between functions
    def get_today_stats(self):
        # REVIEW: no Docsring of the method
        # REVIEW: no spaces before and after operator
        today_stats=0
        # REVIEW: incorrect variable declaration, don't use capital letters
        for Record in self.records:
            if Record.date == dt.datetime.now().date():
                # REVIEW: no spaces before and after operator
                today_stats = today_stats+Record.amount
        return today_stats
    # REVIEW: no free space between functions
    def get_week_stats(self):
        # REVIEW: no Docsring of the method
        # REVIEW: no spaces before and after operator
        week_stats=0
        today = dt.datetime.now().date()
        for record in self.records:
            # REVIEW: length line more than 79 characters, move te text 
            # to next line
            # REVIEW: wrong code formatting, extra spaces
            if (today -  record.date).days <7 and (today -  record.date).days >=0:
                # REVIEW: no space after operator
                week_stats +=record.amount
        return week_stats
# REVIEW: no 2 empty lines before class (PEP8)
class CaloriesCalculator(Calculator):
    # REVIEW: no Docsring of the class
    # REVIEW: comment is bad-formatted, no dot at the end
    # REVIEW: the comment should be on a separate line above the variable
    def get_calories_remained(self): # Получает остаток калорий на сегодня
        # REVIEW: no Docsring of the method
        # REVIEW: no spaces before and after operator
        # REVIEW: incorrect variable declaration, the variable name must be 
        # meaningful, not a single letter
        x=self.limit-self.get_today_stats()
        if x > 0:
            # REVIEW: length line more than 79 characters
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {x} кКал'
        else:
            return 'Хватит есть!'
# REVIEW: no 2 empty lines before class (PEP8)
class CashCalculator(Calculator):
    # REVIEW: no Docsring of the class
    # REVIEW: no spaces before and after operator
    # REVIEW: comment should be in line above, not inline
    # REVIEW: constant variables should be declared right after the imports
    USD_RATE=float(60) #Курс доллар США.
    # REVIEW: no spaces before and after operator
    EURO_RATE=float(70) #Курс Евро.
    # REVIEW: no free space between blocks
    # REVIEW: length line more than 79 characters, move to next line
    # REVIEW: do not pass constants to the function explicitly
    # REVIEW: incorrect names of the variables, do not use capital letters
    def get_today_cash_remained(self, currency, USD_RATE=USD_RATE, EURO_RATE=EURO_RATE):
        # REVIEW: no Docsring of the method
        # REVIEW: no spaces before and after operator
        currency_type=currency
        cash_remained = self.limit - self.get_today_stats()
        # REVIEW: no spaces before and after operator
        if currency=='usd':
            cash_remained /= USD_RATE
            # REVIEW: no space after operator
            currency_type ='USD'
            # REVIEW: no spaces before and after operator
        elif currency_type=='eur':
            cash_remained /= EURO_RATE
            # REVIEW: no space after operator
            currency_type ='Euro'
            # REVIEW: no spaces before and after operator
            # REVIEW: type rubles is the last variant, use else instead of elif
        elif currency_type=='rub':
            # REVIEW: not consistent code, use /=
            # operator == is logical operator, use = or /=, here is /=
            # REVIEW: divide by 1 is not needed, delete this line
            cash_remained == 1.00
            # REVIEW: no spaces before and after operator
            currency_type ='руб'
        # REVIEW: no free space between separate logical blocks
        if cash_remained > 0:
            # REVIEW: length line more than 79 characters
            # REVIEW: f'' string used incorrectly, no function calls should
            # be inside of it
            return f'На сегодня осталось {round(cash_remained, 2)} {currency_type}'
        elif cash_remained == 0:
            return 'Денег нет, держись'
        elif cash_remained < 0:
            # REVIEW: length line more than 79 characters
            # REVIEW: f'' string used incorrectly, no function calls should
            # be inside of it
            return 'Денег нет, держись: твой долг - {0:.2f} {1}'.format(-cash_remained, currency_type)

    # REVIEW: method not used, delete it
    def get_week_stats(self):
        # REVIEW: no Docsring of the method
        super().get_week_stats()
# REVIEW: no construction if __name__ == ‘__main__’
# REVIEW: no 1 empty line after whole code