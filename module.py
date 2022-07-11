import pandas as pd


class PaymentData:
    def __init__(self, file_name):
        self.df = pd.read_csv(file_name)

    def transaction_types(self, regex):
        return self.df[self.df.DESCRIPTION.str.match(regex)]                 #classify the transaction on the basis of regex(UPI, NEFT)

    def duplicate_values(self,column=None):
        return self.df[self.df.duplicated(column)]                                 #find out duplicates

    def top_10_transaction(self, type):                                      #find top 10 credit or debit transaction
        return self.df.nlargest(10, [type])

    def top_10_transaction_of_all(self):                                     #find top 10 transaction
        self.df["CRE_DEB"] = self.df[["CREDIT", "DEBIT"]].max(axis=1)
        return self.df.nlargest(10, ['CRE_DEB'])
