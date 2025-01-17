from icon_contracts.models.contracts import Contract
from icon_contracts.schemas.contract_processed_pb2 import ContractProcessed


def contract_to_proto(contract_db: Contract, contract_proto: ContractProcessed = None):
    """Convert a SQLModel contract to a protobuf."""
    if contract_proto is None:
        contract_proto = ContractProcessed()

    contract_proto.address = contract_db.address
    contract_proto.name = contract_db.name

    if contract_db.created_timestamp is not None:
        contract_proto.created_timestamp = int(contract_db.created_timestamp)

    if contract_db.status is not None:
        contract_proto.status = contract_db.status

    contract_proto.is_token = contract_db.is_token

    return contract_proto
