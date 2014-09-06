import json
from tabulate import tabulate
import requests

class Stocks:
  def __init__(self):
    self.myStocks = []
    self.menu()

  def menu(self):
    input = raw_input("Welcome to your stock application. Type 'view' to view all your current stocks and their current statistics. " +
    "Type edit to add/delete stocks. \n")

    if(input == "view"):
      self.view()
    elif(input == "edit"):
      self.edit()
    else:
      self.menu()

  def view(self):
    if(len(self.myStocks) == 0):
      print("You have no stocks.")
      self.menu()
    else:
      print("Here are all of your current stocks: ")
      table = []
      for symbol in self.myStocks:
        stockData = self.getStockData(symbol)
        row = [symbol, "$" + stockData['price'], "%" + stockData['pChange'], "$" + stockData['aChange']]
        table.append(row)
      print(tabulate(table, headers=["Symbol", "Price", "% Change", "$ Change"]))
    self.menu()

  def edit(self):
    print("Here are all of your stocks: ")
    for symbol in self.myStocks:
      print(symbol + "\n")
    input = raw_input("Type in the symbol of the stock you want to add/delete: \n")
    self.addOrDeleteStock(input)

  def addOrDeleteStock(self, stockSymbol):
    if(stockSymbol in self.myStocks):
      self.myStocks.remove(stockSymbol)
      print(stockSymbol + " has been removed from your arsenal.")
      self.menu()
    else:
      self.myStocks.append(stockSymbol)
      print(stockSymbol + " has been added to your arsenal.")
      print(self.myStocks)
      self.menu()

  def getStockData(self, symbol):
    url = "http://dev.markitondemand.com/Api/v2/Quote/json"
    data = {
      'symbol': symbol
    }
    res = requests.post(url, data)
    json_data = json.loads(res.text)
    stockData = {'price': "%.2f" % json_data['LastPrice'], 'pChange': "%.2f" % json_data['ChangePercent'], 'aChange': "%.2f" % json_data['Change']}
    return(stockData)

s = Stocks()
