#!/usr/bin/env python3

from helpers.string_helpers import TransactionLogStringListHelper
import re


class BankTransactionLogTotal:
    def __init__(self, transaction_log_string_list_helper: TransactionLogStringListHelper):
        self.transaction_log_string_list_helper = transaction_log_string_list_helper

    def _get_user_transaction_log(self) -> list[str]:
        user_input: str = input(
            "Please enter your bank transaction log in format 'D XXX' for deposits and 'W XXX' for withdrawals: "
        )

        return self.transaction_log_string_list_helper.get_validated_transaction_log_string_list(user_input)

    def calculate(self) -> str:
        user_transaction_log: list[str] = self._get_user_transaction_log()
        bank_balance: float = 0

        for transaction in user_transaction_log:
            transaction_amount = float(re.sub(r'\D', '', transaction))
            if 'D' in transaction:
                bank_balance += transaction_amount
            elif 'W' in transaction:
                bank_balance -= transaction_amount

        return format(bank_balance, '.2f')
