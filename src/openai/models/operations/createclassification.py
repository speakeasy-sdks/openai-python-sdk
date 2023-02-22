import dataclasses
from ..shared import createclassificationrequest as shared_createclassificationrequest
from ..shared import createclassificationresponse as shared_createclassificationresponse
from typing import Optional


@dataclasses.dataclass
class CreateClassificationRequest:
    request: shared_createclassificationrequest.CreateClassificationRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateClassificationResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_classification_response: Optional[shared_createclassificationresponse.CreateClassificationResponse] = dataclasses.field(default=None)
    