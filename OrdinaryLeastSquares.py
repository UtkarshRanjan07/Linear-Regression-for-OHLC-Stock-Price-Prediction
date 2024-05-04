
"""  Developer Details
Name  : Kamal Kumar Chanchal

"""


#Step 1: Import necessary libraries
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


class Q_OLS:

    def __init__( self , df_data ):
        print("Processing Linear Regression Model to get the Best fit line [OLS ]")
        self.data = df_data

        self.__Apply_OLS_reg_model()


    def __Apply_OLS_reg_model( self ):
        try:

            #Apply complex calculation on data
            self.data  [ 'Avg' ] =  (  self.data  [ 'Open' ]  +  self.data  [ 'High' ] + self.data  [ 'Low' ] + self.data  [ 'Close' ]  ) /4
            period =  9
            ema_col_name =  F"SMA_{period}"
            self.data[ema_col_name] = self.data['Avg'].rolling(window=period).mean()
            """ remove nan values  record  """
            self.data.dropna( inplace = True)


            #  --- end calculation

            """  feature and targeted data """
            X =  self.data[[ema_col_name]]  #column_name_for_independent_variable
            y = self.data [ 'Avg' ] #column_name_for_dependent_variable

            # var = self.__variables()
            print("Variables : Test & Prepare")

            model = LinearRegression()

            result = model.fit(X,y)

            """ summary """
            print("Summary of OLS Model is [Y= mX + C]:")
            print ( 'Intercept:' , result.intercept_ )
            print ( 'Slope:' , result.coef_ [ 0 ] )
            print("     -----End-----    ")
            self.__View_output(X,  result.predict(X) , y )

        except Exception as e:
            print(F"Error Occured while Applying Model : {e}")

    def __View_output( self , X ,results,y):
        try:
            plt.scatter ( X , y , color = 'blue' , label = 'Actual data' )
            plt.plot ( X , results , color = 'red' , label = 'Regression line' )
            plt.xlabel ( 'Avg Price' )
            plt.ylabel ( 'SMA Values' )
            plt.title ( 'OLS Regression Analysis' )
            plt.legend ( )
            plt.show ( )
        except Exception as e:
            print(F"Error Occured while Plotting Summary Of OLS Regression model {e}")
