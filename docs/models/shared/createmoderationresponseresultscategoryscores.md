# CreateModerationResponseResultsCategoryScores

A list of the categories along with their scores as predicted by model.


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `harassment`                                         | *Optional[float]*                                    | :heavy_check_mark:                                   | The score for the category 'harassment'.             |
| `harassment_threatening`                             | *Optional[float]*                                    | :heavy_check_mark:                                   | The score for the category 'harassment/threatening'. |
| `hate`                                               | *Optional[float]*                                    | :heavy_check_mark:                                   | The score for the category 'hate'.                   |
| `hate_threatening`                                   | *Optional[float]*                                    | :heavy_check_mark:                                   | The score for the category 'hate/threatening'.       |
| `self_harm`                                          | *Optional[float]*                                    | :heavy_check_mark:                                   | The score for the category 'self-harm'.              |
| `self_harm_instructions`                             | *Optional[float]*                                    | :heavy_check_mark:                                   | The score for the category 'self-harm/instructions'. |
| `self_harm_intent`                                   | *Optional[float]*                                    | :heavy_check_mark:                                   | The score for the category 'self-harm/intent'.       |
| `sexual`                                             | *Optional[float]*                                    | :heavy_check_mark:                                   | The score for the category 'sexual'.                 |
| `sexual_minors`                                      | *Optional[float]*                                    | :heavy_check_mark:                                   | The score for the category 'sexual/minors'.          |
| `violence`                                           | *Optional[float]*                                    | :heavy_check_mark:                                   | The score for the category 'violence'.               |
| `violence_graphic`                                   | *Optional[float]*                                    | :heavy_check_mark:                                   | The score for the category 'violence/graphic'.       |