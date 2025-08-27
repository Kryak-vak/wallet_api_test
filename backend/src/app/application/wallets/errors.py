class WalletNotFoundError(Exception):
    def __init__(self, wallet_id):
        super().__init__(f"Wallet with id {wallet_id} not found")
        self.wallet_id = wallet_id
