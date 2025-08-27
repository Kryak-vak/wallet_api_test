class InsufficientBalanceError(Exception):
    def __init__(self, wallet_id):
        super().__init__(f"Insufficient balance in wallet with id {wallet_id}")
        self.wallet_id = wallet_id
