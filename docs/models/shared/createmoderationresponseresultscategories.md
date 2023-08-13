# CreateModerationResponseResultsCategories

A list of the categories, and whether they are flagged or not.


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `hate`                                                 | *bool*                                                 | :heavy_check_mark:                                     | Whether the content was flagged as 'hate'.             |
| `hate_threatening`                                     | *bool*                                                 | :heavy_check_mark:                                     | Whether the content was flagged as 'hate/threatening'. |
| `self_harm`                                            | *bool*                                                 | :heavy_check_mark:                                     | Whether the content was flagged as 'self-harm'.        |
| `sexual`                                               | *bool*                                                 | :heavy_check_mark:                                     | Whether the content was flagged as 'sexual'.           |
| `sexual_minors`                                        | *bool*                                                 | :heavy_check_mark:                                     | Whether the content was flagged as 'sexual/minors'.    |
| `violence`                                             | *bool*                                                 | :heavy_check_mark:                                     | Whether the content was flagged as 'violence'.         |
| `violence_graphic`                                     | *bool*                                                 | :heavy_check_mark:                                     | Whether the content was flagged as 'violence/graphic'. |