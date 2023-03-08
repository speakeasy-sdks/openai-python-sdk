from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from gpt import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateFineTuneRequest:
    training_file: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('training_file') }})
    batch_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('batch_size'), 'exclude': lambda f: f is None }})
    classification_betas: Optional[list[float]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('classification_betas'), 'exclude': lambda f: f is None }})
    classification_n_classes: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('classification_n_classes'), 'exclude': lambda f: f is None }})
    classification_positive_class: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('classification_positive_class'), 'exclude': lambda f: f is None }})
    compute_classification_metrics: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compute_classification_metrics'), 'exclude': lambda f: f is None }})
    learning_rate_multiplier: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('learning_rate_multiplier'), 'exclude': lambda f: f is None }})
    model: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model'), 'exclude': lambda f: f is None }})
    n_epochs: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('n_epochs'), 'exclude': lambda f: f is None }})
    prompt_loss_weight: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prompt_loss_weight'), 'exclude': lambda f: f is None }})
    suffix: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('suffix'), 'exclude': lambda f: f is None }})
    validation_file: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validation_file'), 'exclude': lambda f: f is None }})
    