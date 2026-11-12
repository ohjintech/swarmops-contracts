import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from swarmops.drone.v1 import drone_pb2 as _drone_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Viewport(_message.Message):
    __slots__ = ("min_lat", "min_lon", "max_lat", "max_lon")
    MIN_LAT_FIELD_NUMBER: _ClassVar[int]
    MIN_LON_FIELD_NUMBER: _ClassVar[int]
    MAX_LAT_FIELD_NUMBER: _ClassVar[int]
    MAX_LON_FIELD_NUMBER: _ClassVar[int]
    min_lat: float
    min_lon: float
    max_lat: float
    max_lon: float
    def __init__(self, min_lat: _Optional[float] = ..., min_lon: _Optional[float] = ..., max_lat: _Optional[float] = ..., max_lon: _Optional[float] = ...) -> None: ...

class ClientFrame(_message.Message):
    __slots__ = ("viewport",)
    VIEWPORT_FIELD_NUMBER: _ClassVar[int]
    viewport: Viewport
    def __init__(self, viewport: _Optional[_Union[Viewport, _Mapping]] = ...) -> None: ...

class FleetSnapshot(_message.Message):
    __slots__ = ("ts", "drones", "total_drones")
    TS_FIELD_NUMBER: _ClassVar[int]
    DRONES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DRONES_FIELD_NUMBER: _ClassVar[int]
    ts: _timestamp_pb2.Timestamp
    drones: _containers.RepeatedCompositeFieldContainer[_drone_pb2.Telemetry]
    total_drones: int
    def __init__(self, ts: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., drones: _Optional[_Iterable[_Union[_drone_pb2.Telemetry, _Mapping]]] = ..., total_drones: _Optional[int] = ...) -> None: ...

class ServerFrame(_message.Message):
    __slots__ = ("snapshot", "ack", "event")
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    ACK_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    snapshot: FleetSnapshot
    ack: _drone_pb2.CommandAck
    event: _drone_pb2.DroneEvent
    def __init__(self, snapshot: _Optional[_Union[FleetSnapshot, _Mapping]] = ..., ack: _Optional[_Union[_drone_pb2.CommandAck, _Mapping]] = ..., event: _Optional[_Union[_drone_pb2.DroneEvent, _Mapping]] = ...) -> None: ...
