
"""  Developer Details
Name  : Kamal Kumar Chanchal

"""


#Step 1: Import necessary libraries
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

class Q_OLS:

    def __init__( self , df_data ):
        print("Calling OLS Model")
        self.data = df_data

        self.__Apply_OLS_reg_model()


    def __variables( self ):
        """  independent and dependent variables """
        try:
            X =  self.data['Date']
            y = self.data [ 'Close' ]

            return [X,y]

        except Exception as e:
            print(F"Error Occured : {e}")
            return [-1,-1]

    def __Apply_OLS_reg_model( self ):
        try:

            self.data  [ 'Avg' ] =  (  self.data  [ 'Open' ]  +  self.data  [ 'High' ] + self.data  [ 'Low' ] + self.data  [ 'Close' ]  ) /4

            X =  self.data[['Avg']]  #column_name_for_independent_variable
            y = self.data [ 'Close' ] #column_name_for_dependent_variable



            # var = self.__variables()
            print("Variables : Test & Prepare")
            # print(F" y is {X }")
            # print ( F" X is {y}" )

            model = LinearRegression()



            result = model.fit(X,y)


            """ summary """
            print("Summary of OLS Model is [Y= mX + C]:")
            print ( 'Intercept:' , result.intercept_ )
            print ( 'Slope:' , result.coef_ [ 0 ] )
            print("     -----End----- ")


            self.__View_output(X,  result.predict(X) , y )

        except Exception as e:
            print(F"Error Occured while Applying Model : {e}")

    def __View_output( self , X ,results,y):
        try:
            plt.scatter ( X , y , color = 'blue' , label = 'Actual data' )
            plt.plot ( X , results , color = 'red' , label = 'Regression line' )
            plt.xlabel ( 'Avg Price' )
            plt.ylabel ( 'Close Price' )
            plt.title ( 'OLS Regression Analysis' )
            plt.legend ( )
            plt.show ( )
        except Exception as e:
            print(F"Error Occured while Plotting Summary Of OLS Regression model {e}")
