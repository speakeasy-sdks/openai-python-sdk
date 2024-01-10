"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from gpt import utils
from typing import Optional, Union

class CreateFineTuningJobRequest1(str, Enum):
    AUTO = 'auto'

class CreateFineTuningJobRequestSchemas1(str, Enum):
    AUTO = 'auto'

class CreateFineTuningJobRequestSchemasHyperparameters1(str, Enum):
    AUTO = 'auto'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Hyperparameters:
    r"""The hyperparameters used for the fine-tuning job."""
    batch_size: Optional[Union[CreateFineTuningJobRequest1, int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('batch_size'), 'exclude': lambda f: f is None }})
    r"""Number of examples in each batch. A larger batch size means that model parameters
    are updated less frequently, but with lower variance.
    """
    learning_rate_multiplier: Optional[Union[CreateFineTuningJobRequestSchemas1, float]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('learning_rate_multiplier'), 'exclude': lambda f: f is None }})
    r"""Scaling factor for the learning rate. A smaller learning rate may be useful to avoid
    overfitting.
    """
    n_epochs: Optional[Union[CreateFineTuningJobRequestSchemasHyperparameters1, int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('n_epochs'), 'exclude': lambda f: f is None }})
    r"""The number of epochs to train the model for. An epoch refers to one full cycle
    through the training dataset.
    """
    


class CreateFineTuningJobRequest2(str, Enum):
    BABBAGE_002 = 'babbage-002'
    DAVINCI_002 = 'davinci-002'
    GPT_3_5_TURBO = 'gpt-3.5-turbo'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateFineTuningJobRequest:
    model: Union[str, CreateFineTuningJobRequest2] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model') }})
    r"""The name of the model to fine-tune. You can select one of the
    [supported models](/docs/guides/fine-tuning/what-models-can-be-fine-tuned).
    """
    training_file: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('training_file') }})
    r"""The ID of an uploaded file that contains training data.

    See [upload file](/docs/api-reference/files/upload) for how to upload a file.

    Your dataset must be formatted as a JSONL file. Additionally, you must upload your file with the purpose `fine-tune`.

    See the [fine-tuning guide](/docs/guides/fine-tuning) for more details.
    """
    hyperparameters: Optional[Hyperparameters] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hyperparameters'), 'exclude': lambda f: f is None }})
    r"""The hyperparameters used for the fine-tuning job."""
    suffix: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('suffix') }})
    r"""A string of up to 18 characters that will be added to your fine-tuned model name.

    For example, a `suffix` of \"custom-model-name\" would produce a model name like `ft:gpt-3.5-turbo:openai:custom-model-name:7p4lURel`.
    """
    validation_file: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validation_file') }})
    r"""The ID of an uploaded file that contains validation data.

    If you provide this file, the data is used to generate validation
    metrics periodically during fine-tuning. These metrics can be viewed in
    the fine-tuning results file.
    The same data should not be present in both train and validation files.

    Your dataset must be formatted as a JSONL file. You must upload your file with the purpose `fine-tune`.

    See the [fine-tuning guide](/docs/guides/fine-tuning) for more details.
    """
    

