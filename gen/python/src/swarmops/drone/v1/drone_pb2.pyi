import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FlightState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FLIGHT_STATE_UNSPECIFIED: _ClassVar[FlightState]
    FLIGHT_STATE_LANDED: _ClassVar[FlightState]
    FLIGHT_STATE_TAKING_OFF: _ClassVar[FlightState]
    FLIGHT_STATE_HOLDING: _ClassVar[FlightState]
    FLIGHT_STATE_EN_ROUTE: _ClassVar[FlightState]
    FLIGHT_STATE_RETURNING: _ClassVar[FlightState]
    FLIGHT_STATE_LANDING: _ClassVar[FlightState]
    FLIGHT_STATE_FAULT: _ClassVar[FlightState]

class AckStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACK_STATUS_UNSPECIFIED: _ClassVar[AckStatus]
    ACK_STATUS_ACCEPTED: _ClassVar[AckStatus]
    ACK_STATUS_REJECTED: _ClassVar[AckStatus]
    ACK_STATUS_COMPLETED: _ClassVar[AckStatus]
    ACK_STATUS_FAILED: _ClassVar[AckStatus]

class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEVERITY_UNSPECIFIED: _ClassVar[Severity]
    SEVERITY_INFO: _ClassVar[Severity]
    SEVERITY_WARNING: _ClassVar[Severity]
    SEVERITY_CRITICAL: _ClassVar[Severity]
FLIGHT_STATE_UNSPECIFIED: FlightState
FLIGHT_STATE_LANDED: FlightState
FLIGHT_STATE_TAKING_OFF: FlightState
FLIGHT_STATE_HOLDING: FlightState
FLIGHT_STATE_EN_ROUTE: FlightState
FLIGHT_STATE_RETURNING: FlightState
FLIGHT_STATE_LANDING: FlightState
FLIGHT_STATE_FAULT: FlightState
ACK_STATUS_UNSPECIFIED: AckStatus
ACK_STATUS_ACCEPTED: AckStatus
ACK_STATUS_REJECTED: AckStatus
ACK_STATUS_COMPLETED: AckStatus
ACK_STATUS_FAILED: AckStatus
SEVERITY_UNSPECIFIED: Severity
SEVERITY_INFO: Severity
SEVERITY_WARNING: Severity
SEVERITY_CRITICAL: Severity

class Position(_message.Message):
    __slots__ = ("lat", "lon", "alt_m")
    LAT_FIELD_NUMBER: _ClassVar[int]
    LON_FIELD_NUMBER: _ClassVar[int]
    ALT_M_FIELD_NUMBER: _ClassVar[int]
    lat: float
    lon: float
    alt_m: float
    def __init__(self, lat: _Optional[float] = ..., lon: _Optional[float] = ..., alt_m: _Optional[float] = ...) -> None: ...

class Telemetry(_message.Message):
    __slots__ = ("drone_id", "fleet_id", "ts", "seq", "position", "home", "heading_deg", "ground_speed_mps", "climb_rate_mps", "battery_pct", "state", "link_quality", "active_command_id")
    DRONE_ID_FIELD_NUMBER: _ClassVar[int]
    FLEET_ID_FIELD_NUMBER: _ClassVar[int]
    TS_FIELD_NUMBER: _ClassVar[int]
    SEQ_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    HOME_FIELD_NUMBER: _ClassVar[int]
    HEADING_DEG_FIELD_NUMBER: _ClassVar[int]
    GROUND_SPEED_MPS_FIELD_NUMBER: _ClassVar[int]
    CLIMB_RATE_MPS_FIELD_NUMBER: _ClassVar[int]
    BATTERY_PCT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    LINK_QUALITY_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    drone_id: str
    fleet_id: str
    ts: _timestamp_pb2.Timestamp
    seq: int
    position: Position
    home: Position
    heading_deg: float
    ground_speed_mps: float
    climb_rate_mps: float
    battery_pct: float
    state: FlightState
    link_quality: float
    active_command_id: str
    def __init__(self, drone_id: _Optional[str] = ..., fleet_id: _Optional[str] = ..., ts: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., seq: _Optional[int] = ..., position: _Optional[_Union[Position, _Mapping]] = ..., home: _Optional[_Union[Position, _Mapping]] = ..., heading_deg: _Optional[float] = ..., ground_speed_mps: _Optional[float] = ..., climb_rate_mps: _Optional[float] = ..., battery_pct: _Optional[float] = ..., state: _Optional[_Union[FlightState, str]] = ..., link_quality: _Optional[float] = ..., active_command_id: _Optional[str] = ...) -> None: ...

class Takeoff(_message.Message):
    __slots__ = ("alt_m",)
    ALT_M_FIELD_NUMBER: _ClassVar[int]
    alt_m: float
    def __init__(self, alt_m: _Optional[float] = ...) -> None: ...

class GoTo(_message.Message):
    __slots__ = ("target", "speed_mps")
    TARGET_FIELD_NUMBER: _ClassVar[int]
    SPEED_MPS_FIELD_NUMBER: _ClassVar[int]
    target: Position
    speed_mps: float
    def __init__(self, target: _Optional[_Union[Position, _Mapping]] = ..., speed_mps: _Optional[float] = ...) -> None: ...

class FollowRoute(_message.Message):
    __slots__ = ("waypoints", "speed_mps")
    WAYPOINTS_FIELD_NUMBER: _ClassVar[int]
    SPEED_MPS_FIELD_NUMBER: _ClassVar[int]
    waypoints: _containers.RepeatedCompositeFieldContainer[Position]
    speed_mps: float
    def __init__(self, waypoints: _Optional[_Iterable[_Union[Position, _Mapping]]] = ..., speed_mps: _Optional[float] = ...) -> None: ...

class Hold(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReturnToLaunch(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Land(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Command(_message.Message):
    __slots__ = ("command_id", "drone_id", "issued_at", "expires_at", "takeoff", "go_to", "follow_route", "hold", "return_to_launch", "land")
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    DRONE_ID_FIELD_NUMBER: _ClassVar[int]
    ISSUED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    TAKEOFF_FIELD_NUMBER: _ClassVar[int]
    GO_TO_FIELD_NUMBER: _ClassVar[int]
    FOLLOW_ROUTE_FIELD_NUMBER: _ClassVar[int]
    HOLD_FIELD_NUMBER: _ClassVar[int]
    RETURN_TO_LAUNCH_FIELD_NUMBER: _ClassVar[int]
    LAND_FIELD_NUMBER: _ClassVar[int]
    command_id: str
    drone_id: str
    issued_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    takeoff: Takeoff
    go_to: GoTo
    follow_route: FollowRoute
    hold: Hold
    return_to_launch: ReturnToLaunch
    land: Land
    def __init__(self, command_id: _Optional[str] = ..., drone_id: _Optional[str] = ..., issued_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., takeoff: _Optional[_Union[Takeoff, _Mapping]] = ..., go_to: _Optional[_Union[GoTo, _Mapping]] = ..., follow_route: _Optional[_Union[FollowRoute, _Mapping]] = ..., hold: _Optional[_Union[Hold, _Mapping]] = ..., return_to_launch: _Optional[_Union[ReturnToLaunch, _Mapping]] = ..., land: _Optional[_Union[Land, _Mapping]] = ...) -> None: ...

class CommandAck(_message.Message):
    __slots__ = ("command_id", "drone_id", "ts", "status", "reason")
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    DRONE_ID_FIELD_NUMBER: _ClassVar[int]
    TS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    command_id: str
    drone_id: str
    ts: _timestamp_pb2.Timestamp
    status: AckStatus
    reason: str
    def __init__(self, command_id: _Optional[str] = ..., drone_id: _Optional[str] = ..., ts: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[_Union[AckStatus, str]] = ..., reason: _Optional[str] = ...) -> None: ...

class DroneEvent(_message.Message):
    __slots__ = ("drone_id", "ts", "severity", "code", "message")
    DRONE_ID_FIELD_NUMBER: _ClassVar[int]
    TS_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    drone_id: str
    ts: _timestamp_pb2.Timestamp
    severity: Severity
    code: str
    message: str
    def __init__(self, drone_id: _Optional[str] = ..., ts: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., severity: _Optional[_Union[Severity, str]] = ..., code: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...
