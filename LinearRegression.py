import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


#sample OHLC data
class QuantML:

    def __init__(self):
        print("****** My First ML model(On Stocks Data) *******")
        self.__prepare_data()

    def __prepare_data( self ):
        try:

            dates = pd.date_range ( start = '1/1/2024' , end = '4/10/2024' )
            open_prices = np.random.randint ( 100 , 200 , size = len ( dates ) )
            high_prices = open_prices + np.random.randint ( 5 , 20 , size = len ( dates ) )
            low_prices = open_prices - np.random.randint ( 5 , 20 , size = len ( dates ) )
            close_prices = np.random.randint ( 100 , 200 , size = len ( dates ) )

            # Creating DataFrame
            self.__df_hlc_data = pd.DataFrame ( {
                'Date' : dates ,
                'Open' : open_prices ,
                'High' : high_prices ,
                'Low' : low_prices ,
                'Close' : close_prices
            }
            )
            self.__df_hlc_data.set_index("Date")
            print(self.__df_hlc_data.describe())
        except Exception as e:
            print("Error Ocurred in Prepration of Data : {e}")


    def Engine( self ):
        # self.__NewColoumns()
        self.__calculateMean()

        self.__start()


    def __calculateMean( self ):
        try:

            self.__df_hlc_data [ 'OHLC_mean' ] = self.__df_hlc_data [ [ 'Open' , 'High' , 'Low' , 'Close' ] ].mean ( axis = 1 )

            # print(self.__df_hlc_data)

        except Exception as e:
            print(F"Error(s) Occured while performing Mean of OHLC price {e}")


    def __start( self ):
        try:
            X = np.arange ( len(self.__df_hlc_data) ).reshape(-1,1)
            y = self.__df_hlc_data["OHLC_mean"]
            # print(X)
            print("Applying Linear Regression Model into my Stocks Data")
            model = LinearRegression()

            model.fit(X,y)

            y_predict = model.predict(X)

            self.__ViewOutput(X,y,y_predict)

        except Exception as e:
            print(F" Exception Ocuured as {e} ")


    def __getresult( self ):
        try:
            pass
        except Exception as e:
            print(F"Error Occured while preparing result {e}")

    def __ViewOutput( self  , X,y,y_predict):
        try:
            plt.figure ( figsize = (10 , 6) )
            plt.scatter ( X , y , color = 'blue' , label = 'Actual OHLC Mean' )
            plt.plot ( X , y_predict , color = 'red' , linewidth = 2 , label = 'Linear Regression' )
            plt.title ( 'Linear Regression on OHLC Data' )
            plt.xlabel ( 'Days' )
            plt.ylabel ( 'OHLC Mean' )
            plt.legend ( )
            plt.grid ( True )
            plt.show ( )

        except Exception as e:
            print(F"Error Occured while display datapoint : {e}")