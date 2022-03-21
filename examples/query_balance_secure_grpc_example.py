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

"""REST example of query balance."""

from re import A
from cosmpy.clients.cosmwasm_client import CosmWasmClient
from cosmpy.protos.cosmos.bank.v1beta1 import query_pb2_grpc 
from cosmpy.protos.cosmos.bank.v1beta1 import query_pb2
import certifi
import grpc

ADDRESS = "fetch1mrf5yyjnnlpy0egvpk2pvjdk9667j2gtu8kpfy"
DENOM = "atestfet"

# read in certificates
with open(certifi.where(), 'rb') as f:
    trusted_certs = f.read()

# create credentials
credentials = grpc.ssl_channel_credentials(root_certificates=trusted_certs)

# create secure channel using ssl credentials
channel = grpc.secure_channel('{}:{}'.format("grpc-capricorn.fetch.ai", 443), credentials)

response = CosmWasmClient(channel).get_balance(address=ADDRESS, denom=DENOM)
print(response)
