from dataclasses import dataclass
from typing import Any, Dict

HexStr = str
STARTING_BALANCE = 1000

@dataclass
class PublicAccountInfo:
    public_key: HexStr
    balance: float

    def to_jsonable(self):
        return asdict(self)



@dataclass
class Account:
    key_pair: KeyPair
    balance: float

    @property
    def public_key(self) -> HexStr:
        return self.key_pair.public

    @classmethod
    def new(cls):
        return Account(key_pair=KeyPair.new(), balance=STARTING_BALANCE)

    def sign(self, data: str) -> HexStr:
        return bls_pop.Sign(SK=self.key_pair.private, message=data.encode()).hex()

    def to_jsonable(self) -> Dict:
        return dict(address=self.address, balance=self.balance)

    def public_info(self) -> PublicAccountInfo:
        return PublicAccountInfo(self.public_key, self.balance)

