import yfinance as yf

class YahooAPI:
    date ="Date"
    open= "Open"
    high ="High"
    low="Low"
    close ="Close"
    volume ="Volume"
    adjclose= "Adj Close"
    stksplit = "Stock Splits"


class FinancialData:

    def __init__( self ):
        print("Get Historical Data")
        print("Skipping major functions - Validation of Data, etc,etc")

    def get_historical_data( self,ticker = "RELIANCE.NS", starting_Date = '2022-01-01' ,last_date =  '2024-12-31' ):
        try:
            data = yf.download ( tickers =ticker , start = starting_Date , end = last_date )
            return data.reset_index()
        except Exception as e:
            print(F"Error Occured while Downlaoding Data from API : {e}")
            return []

