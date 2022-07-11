from datetime import datetime
from module import PaymentData
import traceback


def main():
    try:
        payment_info = PaymentData(file_name="cleanup-class-2022.csv")
        __log("Process Start")
        __log(f"CHQ: {payment_info.transaction_types(regex='.*CHQ.*')}")
        __log(f"UPI: {payment_info.transaction_types(regex='.*UPI.*')}")
        __log(f"NEFT: {payment_info.transaction_types(regex='.*NEFT.*')}")
        __log(f"RTGS: {payment_info.transaction_types(regex='.*RTGS.*')}")
        __log(f"CASH: {payment_info.transaction_types(regex='.*CASH DEPOSIT.*')}")
        __log(f"IMPS: {payment_info.transaction_types(regex='.*IMPS.*')}")
        __log(f"Electricity: {payment_info.transaction_types(regex='.*ELECTRICITY.*')}")
        __log(f"Duplicate based on all columns: {payment_info.duplicate_values()}")
        #__log(f"Duplicate based on  credit column: {payment_info.duplicate_values(column='CREDIT')}")
        #__log(f"Duplicate based on  debit column: {payment_info.duplicate_values(column='DEBIT')}")
        #__log(f"Duplicate based on  DESCRIPTION column: {payment_info.duplicate_values(column='DESCRIPTION')}")
        __log(f"top 10 credit transaction: {payment_info.top_10_transaction('CREDIT')}")
        __log(f"top 10 debit transaction: {payment_info.top_10_transaction('DEBIT')}")
        __log(f"top 10 transaction: {payment_info.top_10_transaction_of_all()}")


    except Exception as err:
        traceback.print_exception(type(err), err, err.__traceback__)
        __printabort(f"CRITICAL - {str(err)}")
    finally:
        __log("Process END")


def __log(message):
    utcnow = datetime.utcnow()
    print(f"{utcnow.isoformat()} | {message}")

def __printabort(message):
    __log(message)
    exit(1)

if (__name__ == "__main__"):
    main()