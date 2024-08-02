from typing import (
    Any,
    Callable,
    ContextManager,
    Iterator,
    List,
    Literal,
    NamedTuple,
    Optional,
    overload,
    Sequence,
    Tuple,
    TypeVar,
    Union,
)

@overload
def _cudnn_ctc_loss(log_probs: Tensor, targets: Tensor, input_lengths: Tensor, target_lengths: Tensor, blank: _int, deterministic: _bool, zero_infinity: _bool) -> Tuple[Tensor, Tensor]: ...