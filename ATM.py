class Account:
  def __init__(self,bal,accNo):
    self.balanace = bal
    self.accountNumber = accNo
  def debit (self,debitmount):
     self.balanace = self.balanace-debitmount
     print(self.balanace)
  def credite(self,creditamount):
    self.balanace = self.balanace + creditamount
    print(self.balanace)
c1= Account(5000,123)
c1.debit(200)
