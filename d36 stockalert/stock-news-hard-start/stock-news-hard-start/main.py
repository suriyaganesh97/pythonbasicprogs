import requests
from datetime import datetime,timedelta
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_API_KEY = "B2ACEYZ0L9L10W8R"
NEWS_API_KEY="eaaf681786bc4654b880a285b9604d3a"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_PARAMETERS ={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":ALPHA_API_KEY
}

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday.
# Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.

# response  = requests.get(url=STOCK_ENDPOINT,params=STOCK_PARAMETERS)
# response.raise_for_status()
# yesterday_close_price = float(response.json()["Time Series (Daily)"]["2021-10-22"]["4. close"])
# db_yesterday_close_price = float(response.json()["Time Series (Daily)"]["2021-10-21"]["4. close"])
# #above values are hardcoded
# if abs(yesterday_close_price - db_yesterday_close_price)>20:
#     print("get news")
# print(0.05*(yesterday_close_price))
yesterday = datetime.now() - timedelta(2)
yesterday_date = datetime.strftime(yesterday, '%Y-%m-%d')
db_yesterday = datetime.now() - timedelta(2)
db_yesterday_date = datetime.strftime(yesterday, '%Y-%m-%d')
## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

