# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import LinearRegression as P
import OrdinaryLeastSquares
# import Ml2 as t

import getHistoricalData as feed


# def myproject():
#     model = P.QuantML ()
#     model.Engine()


def project_2():
    print(" Model 2 ")
    """ Get Stocks Data -- Reliance """
    _t = feed.FinancialData()
    df_stocks_data =_t.get_historical_data()


    m2 = OrdinaryLeastSquares.Q_OLS(df_stocks_data)



    print(F"number of Record Found is  : {len(df_stocks_data)}")







# # Press the green button in the gutter to run the script.
if __name__ == '__main__':

    """ Linear Regression to On Mean Price """
    # myproject()

    """ model 2 :  """
    project_2()



