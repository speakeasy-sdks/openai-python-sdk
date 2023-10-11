"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from gpt import utils
from typing import Optional, Union

class CreateFineTuneRequestHyperparametersNEpochs1(str, Enum):
    r"""The number of epochs to train the model for. An epoch refers to one
    full cycle through the training dataset.
    """
    AUTO = 'auto'



@dataclasses.dataclass
class CreateFineTuneRequestHyperparametersNEpochs:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateFineTuneRequestHyperparameters:
    r"""The hyperparameters used for the fine-tuning job."""
    n_epochs: Optional[Union[CreateFineTuneRequestHyperparametersNEpochs1, int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('n_epochs'), 'exclude': lambda f: f is None }})
    r"""The number of epochs to train the model for. An epoch refers to one
    full cycle through the training dataset.
    """
    


class CreateFineTuneRequestModel2(str, Enum):
    r"""The name of the base model to fine-tune. You can select one of \\"ada\\",
    \"babbage\", \"curie\", \"davinci\", or a fine-tuned model created after 2022-04-21 and before 2023-08-22.
    To learn more about these models, see the
    [Models](/docs/models) documentation.
    """
    ADA = 'ada'
    BABBAGE = 'babbage'
    CURIE = 'curie'
    DAVINCI = 'davinci'



@dataclasses.dataclass
class CreateFineTuneRequestModel:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateFineTuneRequest:
    training_file: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('training_file') }})
    r"""The ID of an uploaded file that contains training data.

    See [upload file](/docs/api-reference/files/upload) for how to upload a file.

    Your dataset must be formatted as a JSONL file, where each training
    example is a JSON object with the keys \"prompt\" and \"completion\".
    Additionally, you must upload your file with the purpose `fine-tune`.

    See the [fine-tuning guide](/docs/guides/legacy-fine-tuning/creating-training-data) for more details.
    """
    batch_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('batch_size') }})
    r"""The batch size to use for training. The batch size is the number of
    training examples used to train a single forward and backward pass.

    By default, the batch size will be dynamically configured to be
    ~0.2% of the number of examples in the training set, capped at 256 -
    in general, we've found that larger batch sizes tend to work better
    for larger datasets.
    """
    classification_betas: Optional[list[float]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('classification_betas') }})
    r"""If this is provided, we calculate F-beta scores at the specified
    beta values. The F-beta score is a generalization of F-1 score.
    This is only used for binary classification.

    With a beta of 1 (i.e. the F-1 score), precision and recall are
    given the same weight. A larger beta score puts more weight on
    recall and less on precision. A smaller beta score puts more weight
    on precision and less on recall.
    """
    classification_n_classes: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('classification_n_classes') }})
    r"""The number of classes in a classification task.

    This parameter is required for multiclass classification.
    """
    classification_positive_class: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('classification_positive_class') }})
    r"""The positive class in binary classification.

    This parameter is needed to generate precision, recall, and F1
    metrics when doing binary classification.
    """
    compute_classification_metrics: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compute_classification_metrics') }})
    r"""If set, we calculate classification-specific metrics such as accuracy
    and F-1 score using the validation set at the end of every epoch.
    These metrics can be viewed in the [results file](/docs/guides/legacy-fine-tuning/analyzing-your-fine-tuned-model).

    In order to compute classification metrics, you must provide a
    `validation_file`. Additionally, you must
    specify `classification_n_classes` for multiclass classification or
    `classification_positive_class` for binary classification.
    """
    hyperparameters: Optional[CreateFineTuneRequestHyperparameters] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hyperparameters'), 'exclude': lambda f: f is None }})
    r"""The hyperparameters used for the fine-tuning job."""
    learning_rate_multiplier: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('learning_rate_multiplier') }})
    r"""The learning rate multiplier to use for training.
    The fine-tuning learning rate is the original learning rate used for
    pretraining multiplied by this value.

    By default, the learning rate multiplier is the 0.05, 0.1, or 0.2
    depending on final `batch_size` (larger learning rates tend to
    perform better with larger batch sizes). We recommend experimenting
    with values in the range 0.02 to 0.2 to see what produces the best
    results.
    """
    model: Optional[Union[str, CreateFineTuneRequestModel2]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model') }})
    r"""The name of the base model to fine-tune. You can select one of \\"ada\\",
    \"babbage\", \"curie\", \"davinci\", or a fine-tuned model created after 2022-04-21 and before 2023-08-22.
    To learn more about these models, see the
    [Models](/docs/models) documentation.
    """
    prompt_loss_weight: Optional[float] = dataclasses.field(default=0.01, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prompt_loss_weight') }})
    r"""The weight to use for loss on the prompt tokens. This controls how
    much the model tries to learn to generate the prompt (as compared
    to the completion which always has a weight of 1.0), and can add
    a stabilizing effect to training when completions are short.

    If prompts are extremely long (relative to completions), it may make
    sense to reduce this weight so as to avoid over-prioritizing
    learning the prompt.
    """
    suffix: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('suffix') }})
    r"""A string of up to 40 characters that will be added to your fine-tuned model name.

    For example, a `suffix` of \"custom-model-name\" would produce a model name like `ada:ft-your-org:custom-model-name-2022-02-15-04-21-04`.
    """
    validation_file: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validation_file') }})
    r"""The ID of an uploaded file that contains validation data.

    If you provide this file, the data is used to generate validation
    metrics periodically during fine-tuning. These metrics can be viewed in
    the [fine-tuning results file](/docs/guides/legacy-fine-tuning/analyzing-your-fine-tuned-model).
    Your train and validation data should be mutually exclusive.

    Your dataset must be formatted as a JSONL file, where each validation
    example is a JSON object with the keys \"prompt\" and \"completion\".
    Additionally, you must upload your file with the purpose `fine-tune`.

    See the [fine-tuning guide](/docs/guides/legacy-fine-tuning/creating-training-data) for more details.
    """
    

