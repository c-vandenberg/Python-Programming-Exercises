#!/usr/bin/env python3

from helpers.string_helpers import TransactionLogStringListHelper
from bank_transaction_log_total import BankTransactionLogTotal


def main():
    transaction_log_string_list_helper: TransactionLogStringListHelper = TransactionLogStringListHelper()
    bank_transaction_log_total: BankTransactionLogTotal = BankTransactionLogTotal(transaction_log_string_list_helper)
    print(bank_transaction_log_total.calculate())


if __name__ == '__main__':
    main()
