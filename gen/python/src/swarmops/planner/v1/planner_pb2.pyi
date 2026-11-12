from swarmops.drone.v1 import drone_pb2 as _drone_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DroneStart(_message.Message):
    __slots__ = ("drone_id", "position")
    DRONE_ID_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    drone_id: str
    position: _drone_pb2.Position
    def __init__(self, drone_id: _Optional[str] = ..., position: _Optional[_Union[_drone_pb2.Position, _Mapping]] = ...) -> None: ...

class PlanSurveyRequest(_message.Message):
    __slots__ = ("polygon", "drones", "line_spacing_m", "altitude_m")
    POLYGON_FIELD_NUMBER: _ClassVar[int]
    DRONES_FIELD_NUMBER: _ClassVar[int]
    LINE_SPACING_M_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_M_FIELD_NUMBER: _ClassVar[int]
    polygon: _containers.RepeatedCompositeFieldContainer[_drone_pb2.Position]
    drones: _containers.RepeatedCompositeFieldContainer[DroneStart]
    line_spacing_m: float
    altitude_m: float
    def __init__(self, polygon: _Optional[_Iterable[_Union[_drone_pb2.Position, _Mapping]]] = ..., drones: _Optional[_Iterable[_Union[DroneStart, _Mapping]]] = ..., line_spacing_m: _Optional[float] = ..., altitude_m: _Optional[float] = ...) -> None: ...

class DroneRoute(_message.Message):
    __slots__ = ("drone_id", "waypoints", "length_m")
    DRONE_ID_FIELD_NUMBER: _ClassVar[int]
    WAYPOINTS_FIELD_NUMBER: _ClassVar[int]
    LENGTH_M_FIELD_NUMBER: _ClassVar[int]
    drone_id: str
    waypoints: _containers.RepeatedCompositeFieldContainer[_drone_pb2.Position]
    length_m: float
    def __init__(self, drone_id: _Optional[str] = ..., waypoints: _Optional[_Iterable[_Union[_drone_pb2.Position, _Mapping]]] = ..., length_m: _Optional[float] = ...) -> None: ...

class PlanSurveyResponse(_message.Message):
    __slots__ = ("routes",)
    ROUTES_FIELD_NUMBER: _ClassVar[int]
    routes: _containers.RepeatedCompositeFieldContainer[DroneRoute]
    def __init__(self, routes: _Optional[_Iterable[_Union[DroneRoute, _Mapping]]] = ...) -> None: ...
