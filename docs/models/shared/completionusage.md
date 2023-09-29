# CompletionUsage

Usage statistics for the completion request.


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `completion_tokens`                                               | *Optional[int]*                                                   | :heavy_check_mark:                                                | Number of tokens in the generated completion.                     |
| `prompt_tokens`                                                   | *Optional[int]*                                                   | :heavy_check_mark:                                                | Number of tokens in the prompt.                                   |
| `total_tokens`                                                    | *Optional[int]*                                                   | :heavy_check_mark:                                                | Total number of tokens used in the request (prompt + completion). |