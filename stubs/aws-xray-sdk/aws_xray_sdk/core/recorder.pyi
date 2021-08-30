import time
from logging import Logger
from typing import Any, Callable, Iterable

from aws_xray_sdk import global_sdk_config as global_sdk_config
from aws_xray_sdk.version import VERSION as VERSION

from .context import Context as Context
from .daemon_config import DaemonConfig as DaemonConfig
from .emitters.udp_emitter import UDPEmitter as UDPEmitter
from .exceptions.exceptions import (
    SegmentNameMissingException as SegmentNameMissingException,
    SegmentNotFoundException as SegmentNotFoundException,
)
from .lambda_launcher import check_in_lambda as check_in_lambda
from .models.default_dynamic_naming import DefaultDynamicNaming as DefaultDynamicNaming
from .models.dummy_entities import DummySegment as DummySegment, DummySubsegment as DummySubsegment
from .models.segment import Segment as Segment, SegmentContextManager as SegmentContextManager
from .models.subsegment import Subsegment as Subsegment, SubsegmentContextManager as SubsegmentContextManager
from .plugins.utils import get_plugin_modules as get_plugin_modules
from .sampling.local.sampler import LocalSampler as LocalSampler
from .sampling.sampler import DefaultSampler as DefaultSampler
from .streaming.default_streaming import DefaultStreaming as DefaultStreaming
from .utils import stacktrace as stacktrace
from .utils.compat import string_types as string_types

log: Logger
TRACING_NAME_KEY: str
DAEMON_ADDR_KEY: str
CONTEXT_MISSING_KEY: str
XRAY_META: Any
SERVICE_INFO: Any

class AWSXRayRecorder:
    def __init__(self) -> None: ...
    def configure(
        self,
        sampling: bool | None = ...,
        plugins: Iterable[str] | None = ...,
        context_missing: str | None = ...,
        sampling_rules: dict[str, Any] | str | None = ...,
        daemon_address: str | None = ...,
        service: str | None = ...,
        context: Context | None = ...,
        emitter: UDPEmitter | None = ...,
        streaming: DefaultStreaming | None = ...,
        dynamic_naming: DefaultDynamicNaming | None = ...,
        streaming_threshold: int | None = ...,
        max_trace_back: int | None = ...,
        sampler: LocalSampler | DefaultSampler | None = ...,
        stream_sql: bool | None = ...,
    ) -> None: ...
    def in_segment(self, name: str | None = ..., **segment_kwargs): ...
    def in_subsegment(self, name: str | None = ..., **subsegment_kwargs): ...
    def begin_segment(
        self, name: str | None = ..., traceid: str | None = ..., parent_id: str | None = ..., sampling: bool | None = ...
    ): ...
    def end_segment(self, end_time: time.struct_time | None = ...) -> None: ...
    def current_segment(self): ...
    def begin_subsegment(self, name: str, namespace: str = ...): ...
    def current_subsegment(self): ...
    def end_subsegment(self, end_time: time.struct_time | None = ...) -> None: ...
    def put_annotation(self, key: str, value: Any) -> None: ...
    def put_metadata(self, key: str, value: Any, namespace: str = ...) -> None: ...
    def is_sampled(self): ...
    def get_trace_entity(self): ...
    def set_trace_entity(self, trace_entity: Context) -> None: ...
    def clear_trace_entities(self) -> None: ...
    def stream_subsegments(self) -> None: ...
    def capture(self, name: str | None = ...): ...
    def record_subsegment(
        self,
        wrapped: Callable[..., Any],
        instance: Any,
        args: list[Any],
        kwargs: dict[str, Any],
        name: str,
        namespace: str,
        meta_processor: Callable[..., Any],
    ): ...
    @property
    def enabled(self): ...
    @enabled.setter
    def enabled(self, value: bool) -> None: ...
    @property
    def sampling(self): ...
    @sampling.setter
    def sampling(self, value: bool) -> None: ...
    @property
    def sampler(self): ...
    @sampler.setter
    def sampler(self, value: LocalSampler | DefaultSampler) -> None: ...
    @property
    def service(self): ...
    @service.setter
    def service(self, value: str) -> None: ...
    @property
    def dynamic_naming(self): ...
    @dynamic_naming.setter
    def dynamic_naming(self, value) -> None: ...
    @property
    def context(self): ...
    @context.setter
    def context(self, cxt: Context) -> None: ...
    @property
    def emitter(self): ...
    @emitter.setter
    def emitter(self, value: UDPEmitter) -> None: ...
    @property
    def streaming(self): ...
    @streaming.setter
    def streaming(self, value: DefaultStreaming) -> None: ...
    @property
    def streaming_threshold(self): ...
    @streaming_threshold.setter
    def streaming_threshold(self, value: int) -> None: ...
    @property
    def max_trace_back(self): ...
    @max_trace_back.setter
    def max_trace_back(self, value: int) -> None: ...
    @property
    def stream_sql(self): ...
    @stream_sql.setter
    def stream_sql(self, value: bool) -> None: ...