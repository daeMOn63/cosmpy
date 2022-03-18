# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2021 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------
from cosmpy.aerial.client import LedgerClient, NetworkConfig
from cosmpy.aerial.wallet import LocalWallet
from cosmpy.crypto.keypairs import PrivateKey
from cosmpy.protos.cosmos.staking.v1beta1.query_pb2 import QueryValidatorsRequest, QueryDelegationRequest
from cosmpy.protos.cosmos.staking.v1beta1.staking_pb2 import BondStatus
from cosmpy.protos.cosmos.staking.v1beta1.tx_pb2 import MsgDelegate
from cosmpy.protos.cosmos.base.v1beta1.coin_pb2 import Coin
from cosmpy.aerial.tx import Transaction
from cosmpy.aerial.client.utils import prepare_and_broadcast_basic_transaction

def main():
    alice = LocalWallet(PrivateKey("T7w1yHq1QIcQiSqV27YSwk+i1i+Y4JMKhkpawCQIh6s="))

    ledger = LedgerClient(NetworkConfig.latest_stable_testnet())

    # ensure alice have funds
    assert ledger.query_bank_balance(alice.address(), 'atestfet') > 0

    # lookup an active (== not unbonding or jailed) validator
    resp = ledger.staking.Validators(QueryValidatorsRequest())
    assert len(resp.validators) > 0

    target_validator = None
    for validator in resp.validators:
        if validator.status == BondStatus.BOND_STATUS_BONDED and validator.jailed == False:
            target_validator = validator
            break
    
    print(f"validator moniker: \"{target_validator.description.moniker}\" operator address: {target_validator.operator_address}")
    
    # query current delegations
    resp = ledger.staking.Delegation(QueryDelegationRequest(
        delegator_addr=str(alice.address()),
        validator_addr=target_validator.operator_address,
    ))
    print(f"before - {str(alice.address())} delegations to {target_validator.operator_address}: {resp.delegation_response.balance.amount}{resp.delegation_response.balance.denom}")
    
    
    # send delegate transaction
    delegation_coin = Coin(amount="1", denom="atestfet")

    tx = Transaction()
    tx.add_message(
        MsgDelegate(
            delegator_address=str(alice.address()),
            validator_address=target_validator.operator_address,
            amount=delegation_coin,
        )
    )
    tx = prepare_and_broadcast_basic_transaction(ledger, tx, alice)
    print(f"delegated {delegation_coin.amount}{{delegation_coin.denom}}: {tx.tx_hash}")
    print("waiting for tx inclusion in a block...")
    tx.wait_to_complete()

    # query delegation now, must have more than previously
    resp = ledger.staking.Delegation(QueryDelegationRequest(
        delegator_addr=str(alice.address()),
        validator_addr=target_validator.operator_address,
    ))
    print(f"after - {str(alice.address())} delegations to {target_validator.operator_address}: {resp.delegation_response.balance.amount}{resp.delegation_response.balance.denom}")
    

if __name__ == "__main__":
    main()
