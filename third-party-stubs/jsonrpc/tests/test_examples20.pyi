# Stubs for jsonrpc.tests.test_examples20 (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import unittest2 as unittest
from ..jsonrpc2 import JSONRPC20BatchRequest, JSONRPC20Request
from ..manager import JSONRPCResponseManager
from typing import Any

def isjsonequal(json1: Any, json2: Any): ...

class TestJSONRPCExamples(unittest.TestCase):
    dispatcher: Any = ...
    def setUp(self): ...
    def test_rpc_call_with_positional_parameters(self) -> None: ...
    def test_rpc_call_with_named_parameters(self): ...
    def test_notification(self) -> None: ...
    def test_rpc_call_of_non_existent_method(self) -> None: ...
    def test_rpc_call_with_invalid_json(self) -> None: ...
    def test_rpc_call_with_invalid_request_object(self) -> None: ...
    def test_rpc_call_batch_invalid_json(self) -> None: ...
    def test_rpc_call_with_an_empty_array(self) -> None: ...
    def test_rpc_call_with_rpc_call_with_an_invalid_batch_but_not_empty(self) -> None: ...
    def test_rpc_call_with_invalid_batch(self) -> None: ...
    def test_rpc_call_batch(self) -> None: ...
    def test_rpc_call_batch_all_notifications(self) -> None: ...
    def test_rpc_call_response_request(self) -> None: ...
    def test_rpc_call_response_request_batch(self) -> None: ...