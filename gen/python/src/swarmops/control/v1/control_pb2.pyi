import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from swarmops.drone.v1 import drone_pb2 as _drone_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommandStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMMAND_STATUS_UNSPECIFIED: _ClassVar[CommandStatus]
    COMMAND_STATUS_QUEUED: _ClassVar[CommandStatus]
    COMMAND_STATUS_SENT: _ClassVar[CommandStatus]
    COMMAND_STATUS_ACKED: _ClassVar[CommandStatus]
    COMMAND_STATUS_COMPLETED: _ClassVar[CommandStatus]
    COMMAND_STATUS_REJECTED: _ClassVar[CommandStatus]
    COMMAND_STATUS_FAILED: _ClassVar[CommandStatus]
    COMMAND_STATUS_TIMED_OUT: _ClassVar[CommandStatus]
COMMAND_STATUS_UNSPECIFIED: CommandStatus
COMMAND_STATUS_QUEUED: CommandStatus
COMMAND_STATUS_SENT: CommandStatus
COMMAND_STATUS_ACKED: CommandStatus
COMMAND_STATUS_COMPLETED: CommandStatus
COMMAND_STATUS_REJECTED: CommandStatus
COMMAND_STATUS_FAILED: CommandStatus
COMMAND_STATUS_TIMED_OUT: CommandStatus

class DroneSummary(_message.Message):
    __slots__ = ("latest", "stale")
    LATEST_FIELD_NUMBER: _ClassVar[int]
    STALE_FIELD_NUMBER: _ClassVar[int]
    latest: _drone_pb2.Telemetry
    stale: bool
    def __init__(self, latest: _Optional[_Union[_drone_pb2.Telemetry, _Mapping]] = ..., stale: bool = ...) -> None: ...

class ListDronesRequest(_message.Message):
    __slots__ = ("fleet_id",)
    FLEET_ID_FIELD_NUMBER: _ClassVar[int]
    fleet_id: str
    def __init__(self, fleet_id: _Optional[str] = ...) -> None: ...

class ListDronesResponse(_message.Message):
    __slots__ = ("drones",)
    DRONES_FIELD_NUMBER: _ClassVar[int]
    drones: _containers.RepeatedCompositeFieldContainer[DroneSummary]
    def __init__(self, drones: _Optional[_Iterable[_Union[DroneSummary, _Mapping]]] = ...) -> None: ...

class GetDroneRequest(_message.Message):
    __slots__ = ("drone_id",)
    DRONE_ID_FIELD_NUMBER: _ClassVar[int]
    drone_id: str
    def __init__(self, drone_id: _Optional[str] = ...) -> None: ...

class GetDroneResponse(_message.Message):
    __slots__ = ("drone",)
    DRONE_FIELD_NUMBER: _ClassVar[int]
    drone: DroneSummary
    def __init__(self, drone: _Optional[_Union[DroneSummary, _Mapping]] = ...) -> None: ...

class CommandRecord(_message.Message):
    __slots__ = ("command_id", "drone_id", "status", "reason", "created_at", "updated_at")
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    DRONE_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    command_id: str
    drone_id: str
    status: CommandStatus
    reason: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, command_id: _Optional[str] = ..., drone_id: _Optional[str] = ..., status: _Optional[_Union[CommandStatus, str]] = ..., reason: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SendCommandRequest(_message.Message):
    __slots__ = ("drone_id", "command", "idempotency_key")
    DRONE_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    drone_id: str
    command: _drone_pb2.Command
    idempotency_key: str
    def __init__(self, drone_id: _Optional[str] = ..., command: _Optional[_Union[_drone_pb2.Command, _Mapping]] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class SendCommandResponse(_message.Message):
    __slots__ = ("command",)
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    command: CommandRecord
    def __init__(self, command: _Optional[_Union[CommandRecord, _Mapping]] = ...) -> None: ...

class GetCommandRequest(_message.Message):
    __slots__ = ("command_id",)
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    command_id: str
    def __init__(self, command_id: _Optional[str] = ...) -> None: ...

class GetCommandResponse(_message.Message):
    __slots__ = ("command",)
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    command: CommandRecord
    def __init__(self, command: _Optional[_Union[CommandRecord, _Mapping]] = ...) -> None: ...
