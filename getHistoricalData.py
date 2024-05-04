import yfinance as yf


class FinancialData:

    def __init__( self ):
        print("Get Historical Data")
        print("Skipping major functions - Validation of Data, etc,etc")

    def get_historical_data( self,ticker = "RELIANCE.NS", starting_Date = '2020-01-01' ,last_date =  '2024-12-31' ):
        try:
            data = yf.download ( tickers =ticker , start = starting_Date , end = last_date )
            return data.reset_index()
        except Exception as e:
            print(F"Error Occured while Downlaoding Data from API : {e}")
            return []

