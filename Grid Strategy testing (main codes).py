from datetime import datetime
from xlrd import xldate_as_tuple
import numpy as np
import matplotlib.pyplot as plt
from xlwt import Workbook
wb=Workbook()
sheet1=wb.add_sheet('Sheet 1')
import  xdrlib ,sys
import xlrd
#workbook = xlrd.open_workbook('C:\\Users\\Administrator\\Desktop\\Y4\\FYP\\BTC USD\\2014-2016 BTC USD.xlsx')
workbook = xlrd.open_workbook('C:\\Users\\Administrator\\Desktop\\Y4\\FYP\\结果\\backtesting_random_100.xls')
worksheets = workbook.sheet_names()
#print('worksheets is %s' %worksheets)
table = workbook.sheets()[0]
#change the value of i if you want to change the tested time period, refering to excel
i = 1
date = table.cell(i,8).value
#date = datetime(*xldate_as_tuple(i, 0))

initialprice = table.cell(i,1).value
total = 1000000
bitcoin = 500000/initialprice
cash = 500000
sellingnet = 0.05
buyingnet = 0.05
position = 0.5
#initial position
cell_overwrite_ok=True

#change the value of i if you want to change the tested time period, refering to excel
for i in range (0,100):

        date = table.cell(i,8).value

        # High price in a day
        #price = table.cell(i,5+(-1)^i).value
        #price
        price = table.cell(i,1).value
        #balance
        balance = cash + bitcoin * price

        #profit
        profit = balance - total
        s_return = (profit/total)  
        b_return = ((price - initialprice)/initialprice)
        #bitcoinvalue
        bitcoinvalue = bitcoin*price
        
        #tendaysaverage=(price + table.cell(i-1,1).value + table.cell(i-2,1).value + table.cell(i-3,1).value + table.cell(i-4,1).value + table.cell(i-5,1).value + table.cell(i-6,1).value+ table.cell(i-7,1).value+ table.cell(i-8,1).value+ table.cell(i-9,1).value )/10 

        #short
        if price > initialprice :
                
                if price >= (1+1*sellingnet)*initialprice and position > 0.45:
                        tradebalance=(cash+bitcoin*(1+1*sellingnet)*initialprice)
                        if bitcoin - (0.45*tradebalance)/((1+1*sellingnet)*initialprice) >=0:
                                
                                cash = cash + (bitcoin - (0.45*tradebalance)/((1+1*sellingnet)*initialprice))* (1+1*sellingnet)*initialprice*0.997
                                bitcoin = (0.45*tradebalance)/((1+1*sellingnet)*initialprice)
                                position = 0.45
                                print('You have changed your position to 45% in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)
                        else:
                                print('No enough bitcoin to sale to change the position to be 40% when the price is',price,'in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)

                if price >= (1+2*sellingnet)*initialprice and position > 0.4:
                        tradebalance=(cash+bitcoin*(1+2*sellingnet)*initialprice)
                        if bitcoin - (0.4*tradebalance)/((1+2*sellingnet)*initialprice) >=0:
                                
                                cash = cash + (bitcoin - (0.4*tradebalance)/((1+2*sellingnet)*initialprice))* (1+2*sellingnet)*initialprice*0.997
                                bitcoin = (0.4*tradebalance)/((1+2*sellingnet)*initialprice)
                                position = 0.4
                                print('You have changed your position to 40% in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)
                        else:
                                print('No enough bitcoin to sale to change the position to be 30% when the price is',price,'in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)

                if price >= (1+3*sellingnet)*initialprice and position > 0.35:
                        tradebalance=(cash+bitcoin*(1+3*sellingnet)*initialprice)
                        if bitcoin - (0.35*tradebalance)/((1+3*sellingnet)*initialprice) >=0:
                                
                                cash = cash + (bitcoin - (0.35*tradebalance)/((1+3*sellingnet)*initialprice))* (1+3*sellingnet)*initialprice*0.997
                                bitcoin = (0.35*tradebalance)/((1+3*sellingnet)*initialprice)
                                position = 0.35
                                print('You have changed your position to 35% in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)
                        else:
                                print('No enough bitcoin to sale to change the position to be 20% when the price is',price,'in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)



                if price >= (1+4*sellingnet)*initialprice and position > 0.3:
                        tradebalance=(cash+bitcoin*(1+4*sellingnet)*initialprice)
                        if bitcoin - (0.3*tradebalance)/((1+4*sellingnet)*initialprice) >=0:
                                
                                cash = cash + (bitcoin - (0.3*tradebalance)/((1+4*sellingnet)*initialprice))* (1+4*sellingnet)*initialprice*0.997
                                bitcoin = (0.3*tradebalance)/((1+4*sellingnet)*initialprice)
                                position = 0.3
                                print('You have changed your position to 30% in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)
                        else:
                                print('No enough bitcoin to sale to change the position to be 10% when the price is',price,'in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)  


                if price >= (1+5*sellingnet)*initialprice and position > 0.25:
                        tradebalance=(cash+bitcoin*(1+5*sellingnet)*initialprice)
                        if bitcoin - (0.3*tradebalance)/((1+5*sellingnet)*initialprice) >=0:
                                
                                cash = cash + (bitcoin - (0.25*tradebalance)/((1+5*sellingnet)*initialprice))* (1+5*sellingnet)*initialprice*0.997
                                bitcoin = (0.25*tradebalance)/((1+5*sellingnet)*initialprice)
                                position = 0.25
                                print('You have changed your position to 25% in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)
                        else:
                                print('No enough bitcoin to sale to change the position to be 0% when the price is',price,'in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)

                
                if price >= (1+6*sellingnet)*initialprice and position > 0.2:
                        tradebalance=(cash+bitcoin*(1+6*sellingnet)*initialprice)
                        if bitcoin - (0.2*tradebalance)/((1+6*sellingnet)*initialprice) >=0: 
                                
                                cash = cash + (bitcoin - (0.2*tradebalance)/((1+6*sellingnet)*initialprice))* (1+6*sellingnet)*initialprice*0.997
                                bitcoin = (0.2*tradebalance)/((1+6*sellingnet)*initialprice)
                                position = 0.2
                                print('You have changed your position to 20% in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)
                        else:
                                print('No enough bitcoin to sale to change the position to be 40% when the price is',price,'in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)

                if price >= (1+7*sellingnet)*initialprice and position > 0.15:
                        tradebalance=(cash+bitcoin*(1+7*sellingnet)*initialprice)
                        if bitcoin - (0.15*tradebalance)/((1+7*sellingnet)*initialprice) >=0:
                                
                                cash = cash + (bitcoin - (0.15*tradebalance)/((1+7*sellingnet)*initialprice))* (1+7*sellingnet)*initialprice*0.997
                                bitcoin = (0.15*tradebalance)/((1+7*sellingnet)*initialprice)
                                position = 0.15
                                print('You have changed your position to 15% in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)
                        else:
                                print('No enough bitcoin to sale to change the position to be 30% when the price is',price,'in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)

                if price >= (1+8*sellingnet)*initialprice and position > 0.10:
                        tradebalance=(cash+bitcoin*(1+8*sellingnet)*initialprice)
                        if bitcoin - (0.1*tradebalance)/((1+8*sellingnet)*initialprice) >=0:
                                
                                cash = cash + (bitcoin - (0.1*tradebalance)/((1+8*sellingnet)*initialprice))* (1+8*sellingnet)*initialprice*0.997
                                bitcoin = (0.1*tradebalance)/((1+8*sellingnet)*initialprice)
                                position = 0.1
                                print('You have changed your position to 10% in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)
                        else:
                                print('No enough bitcoin to sale to change the position to be 20% when the price is',price,'in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)



                if price >= (1+9*sellingnet)*initialprice and position > 0.05:
                        tradebalance=(cash+bitcoin*(1+9*sellingnet)*initialprice)
                        if bitcoin - (0.05*tradebalance)/((1+9*sellingnet)*initialprice) >=0:
                                
                                cash = cash + (bitcoin - (0.05*tradebalance)/((1+9*sellingnet)*initialprice))* (1+9*sellingnet)*initialprice*0.997
                                bitcoin = (0.05*tradebalance)/((1+9*sellingnet)*initialprice)
                                position = 0.05
                                print('You have changed your position to 5% in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)
                        else:
                                print('No enough bitcoin to sale to change the position to be 10% when the price is',price,'in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)  


                if price >= (1+10*sellingnet)*initialprice and position > 0:
                        tradebalance=(cash+bitcoin*(1+10*sellingnet)*initialprice)
                        if bitcoin >=0:
                                
                                cash = cash + (bitcoin - (0*tradebalance)/((1+10*sellingnet)*initialprice))* (1+10*sellingnet)*initialprice*0.997
                                bitcoin = (0*tradebalance)/((1+10*sellingnet)*initialprice)
                                position = 0
                                print('You have changed your position to 0% in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)
                        else:
                                print('No enough bitcoin to sale to change the position to be 0% when the price is',price,'in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)


        if price == initialprice and position < 0.5:
                        
                        tradebalance = (cash + bitcoin*(1-0*buyingnet)*initialprice)
                        if cash - ((tradebalance*0.5)/((1-0*buyingnet)*initialprice)-bitcoin)*(1-0*buyingnet)*initialprice >=0: 
                                
                                cash = cash - ((tradebalance*0.5)/((1-0*buyingnet)*initialprice)-bitcoin)*(1-0*buyingnet)*initialprice*1.003
                                bitcoin = (tradebalance*0.5)/((1-0*buyingnet)*initialprice)
                                position = 0.5
                                print('You have changed your position to 50% in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)
                        else:
                                print('No enough cash to buy to change the position to be 50% when the price is',price,'in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)
                        

        if price == initialprice and position > 0.5:
                        
                        tradebalance=(cash+bitcoin*(1+0*sellingnet)*initialprice)
                        if bitcoin - (0.5*tradebalance)/((1+0*sellingnet)*initialprice) >=0:
                                
                                cash = cash + (bitcoin - (0.5*tradebalance)/((1+0*sellingnet)*initialprice))* (1+0*sellingnet)*initialprice*0.997
                                bitcoin = (0.5*tradebalance)/((1+0*sellingnet)*initialprice)
                                position = 0.5
                                print('You have changed your position to 50% in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)
                        else:
                                print('No enough bitcoin to sale to change the position to be 50% when the price is',price,'in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)  


         #long      
        if price < initialprice:
                

                        if price <= (1-1*buyingnet)*initialprice and position < 0.55:
                                tradebalance = (cash + bitcoin*(1-1*buyingnet)*initialprice)
                                if cash - ((tradebalance*0.55)/((1-1*buyingnet)*initialprice)-bitcoin)*(1-1*buyingnet)*initialprice >=0:
                                        
                                        cash = cash - ((tradebalance*0.55)/((1-1*buyingnet)*initialprice)-bitcoin)*(1-1*buyingnet)*initialprice*1.003
                                        bitcoin = (tradebalance*0.55)/((1-1*buyingnet)*initialprice)
                                        position = 0.55
                                        print('You have changed your position to 55% in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)
                                else:
                                        print('No enough cash to buy to change the position to be 55% when the price is',price,'in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)

                                        
                        if price <= (1-2*buyingnet)*initialprice and position < 0.6:
                                tradebalance = (cash + bitcoin*(1-2*buyingnet)*initialprice)
                                if cash - ((tradebalance*0.6)/((1-2*buyingnet)*initialprice)-bitcoin)*(1-2*buyingnet)*initialprice >=0: 
                                        
                                        cash = cash - ((tradebalance*0.6)/((1-2*buyingnet)*initialprice)-bitcoin)*(1-2*buyingnet)*initialprice*1.003
                                        bitcoin = (tradebalance*0.6)/((1-2*buyingnet)*initialprice)
                                        position = 0.6
                                        print('You have changed your position to 60% in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)
                                else:
                                        print('No enough cash to buy to change the position to be 60% when the price is',price,'in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)

                                        
                        if price <= (1-3*buyingnet)*initialprice and position < 0.65:
                                tradebalance = (cash + bitcoin*(1-3*buyingnet)*initialprice)
                                if cash - ((tradebalance*0.65)/((1-3*buyingnet)*initialprice)-bitcoin)*(1-3*buyingnet)*initialprice >=0: 
                                        
                                        cash = cash - ((tradebalance*0.65)/((1-3*buyingnet)*initialprice)-bitcoin)*(1-3*buyingnet)*initialprice*1.003
                                        bitcoin = (tradebalance*0.65)/((1-3*buyingnet)*initialprice)
                                        position = 0.65
                                        print('You have changed your position to 65% in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)
                                else:
                                        print('No enough cash to buy to change the position to be 65% when the price is',price,'in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)

                                        
                        if price <= (1-4*buyingnet)*initialprice and position < 0.7:
                                tradebalance = (cash + bitcoin*(1-4*buyingnet)*initialprice)
                                if cash - ((tradebalance*0.7)/((1-4*buyingnet)*initialprice)-bitcoin)*(1-4*buyingnet)*initialprice >=0: 
                                        
                                        cash = cash - ((tradebalance*0.7)/((1-4*buyingnet)*initialprice)-bitcoin)*(1-4*buyingnet)*initialprice*1.003
                                        bitcoin = (tradebalance*0.7)/((1-4*buyingnet)*initialprice)
                                        position = 0.7
                                        print('You have changed your position to 70% in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)
                                else:
                                        print('No enough cash to buy to change the position to be 70% when the price is',price,'in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)

                                        
                        if price <= (1-5*buyingnet)*initialprice and position < 0.75:
                                tradebalance = (cash + bitcoin*(1-5*buyingnet)*initialprice)
                                if cash - ((tradebalance*0.75)/((1-5*buyingnet)*initialprice)-bitcoin)*(1-5*buyingnet)*initialprice >=0: 
                                        
                                        cash = cash - ((tradebalance*0.75)/((1-5*buyingnet)*initialprice)-bitcoin)*(1-5*buyingnet)*initialprice*1.003
                                        bitcoin = (tradebalance*0.75)/((1-5*buyingnet)*initialprice)
                                        position = 0.75
                                        print('You have changed your position to 75% in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)
                                else:
                                        print('No enough cash to buy to change the position to be 75% when the price is',price,'in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)

                        if price <= (1-6*buyingnet)*initialprice and position < 0.8:
                                tradebalance = (cash + bitcoin*(1-6*buyingnet)*initialprice)
                                if cash - ((tradebalance*0.8)/((1-6*buyingnet)*initialprice)-bitcoin)*(1-6*buyingnet)*initialprice >=0: 
                                        
                                        cash = cash - ((tradebalance*0.8)/((1-6*buyingnet)*initialprice)-bitcoin)*(1-6*buyingnet)*initialprice*1.003
                                        bitcoin = (tradebalance*0.8)/((1-6*buyingnet)*initialprice)
                                        position = 0.8
                                        print('You have changed your position to 80% in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)
                                else:
                                        print('No enough cash to buy to change the position to be 80% when the price is',price,'in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)

                                        
                        if price <= (1-7*buyingnet)*initialprice and position < 0.85:
                                tradebalance = (cash + bitcoin*(1-7*buyingnet)*initialprice)
                                if cash - ((tradebalance*0.85)/((1-7*buyingnet)*initialprice)-bitcoin)*(1-7*buyingnet)*initialprice >=0: 
                                        
                                        cash = cash - ((tradebalance*0.85)/((1-7*buyingnet)*initialprice)-bitcoin)*(1-7*buyingnet)*initialprice*1.003
                                        bitcoin = (tradebalance*0.85)/((1-7*buyingnet)*initialprice)
                                        position = 0.85
                                        print('You have changed your position to 85% in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)
                                else:
                                        print('No enough cash to buy to change the position to be 85% when the price is',price,'in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)

                                        
                        if price <= (1-8*buyingnet)*initialprice and position < 0.9:
                                tradebalance = (cash + bitcoin*(1-8*buyingnet)*initialprice)
                                if cash - ((tradebalance*0.9)/((1-8*buyingnet)*initialprice)-bitcoin)*(1-8*buyingnet)*initialprice >=0: 
                                        
                                        cash = cash - ((tradebalance*0.9)/((1-8*buyingnet)*initialprice)-bitcoin)*(1-8*buyingnet)*initialprice*1.003
                                        bitcoin = (tradebalance*0.9)/((1-8*buyingnet)*initialprice)
                                        position = 0.9
                                        print('You have changed your position to 90% in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)
                                else:
                                        print('No enough cash to buy to change the position to be 90% when the price is',price,'in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)

                                        
                        if price <= (1-9*buyingnet)*initialprice and position < 0.95:
                                tradebalance = (cash + bitcoin*(1-9*buyingnet)*initialprice)
                                if cash - ((tradebalance*0.95)/((1-9*buyingnet)*initialprice)-bitcoin)*(1-9*buyingnet)*initialprice >=0: 
                                        
                                        cash = cash - ((tradebalance*0.95)/((1-9*buyingnet)*initialprice)-bitcoin)*(1-9*buyingnet)*initialprice*1.003
                                        bitcoin = (tradebalance*0.95)/((1-9*buyingnet)*initialprice)
                                        position = 0.95
                                        print('You have changed your position to 95% in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)
                                else:
                                        print('No enough cash to buy to change the position to be 95% when the price is',price,'in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)

                                        
                        if price <= (1-10*buyingnet)*initialprice and position < 1:
                                tradebalance = (cash + bitcoin*(1-10*buyingnet)*initialprice)
                                if cash - ((tradebalance*1)/((1-10*buyingnet)*initialprice)-bitcoin)*(1-10*buyingnet)*initialprice >=0: 
                                        
                                        cash = cash - ((tradebalance*1)/((1-10*buyingnet)*initialprice)-bitcoin)*(1-10*buyingnet)*initialprice*1.003
                                        bitcoin = (tradebalance*1)/((1-10*buyingnet)*initialprice)
                                        position = 1
                                        print('You have changed your position to 100% in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)
                                else:
                                        print('No enough cash to buy to change the position to be 100% when the price is',price,'in',date,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin, your position is',position)

                        
        else:
                        print('You didnt change your position in',date,'your position is',position,'your balance is',balance,'you have',cash,'in cash',bitcoin,'in bitcoin')

        sheet1.write(i,0,round(profit,2))
        #sheet1.write(i,1,round(price,2))
        x = date
        y1,y2 = s_return,b_return


        i=i+1
                             

else:
        print('testing finished')
        print('cash =', cash)
        print('bitcoin =', bitcoin)
        print('balance=',balance)
        print('profit=',profit)
        wb.save('testing_random_100_result.xls')

