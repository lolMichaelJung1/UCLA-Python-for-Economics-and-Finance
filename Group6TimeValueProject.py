class TimeValue:
  rate=0
  capital=0
  month=0
  def __init__(investment,rate,capital,month):
    investment.rate = rate
    investment.capital = capital
    investment.month = month
  def futureValue(investment):
    FV= 0
    print("Interest rate: ", rate)
    print("Initial deposit amount: ", capital)
    print("The total months that you invest: ", month)
    FV = float(capital)*(1+float(rate))**float(month)
    print("Future value of your investment:{:.2f}", format(FV))