
import LinearRegression as P
import OrdinaryLeastSquares


import getHistoricalData as feed


def project_2():
    print(" Model 2 ")
    """ Get Stocks Data -- Reliance """
    _t = feed.FinancialData()
    df_stocks_data =_t.get_historical_data()
    print(F"number of Record Found is  : {len(df_stocks_data)}")
    m2 = OrdinaryLeastSquares.Q_OLS(df_stocks_data)



if __name__ == '__main__':

    """ Linear Regression to On Mean Price """
    """ model 2 : get best fit Line (Reliance Stocks)  """
    project_2()



