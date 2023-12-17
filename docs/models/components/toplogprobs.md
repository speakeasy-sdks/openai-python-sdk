# TopLogprobs


## Fields

| Field                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                               | Required                                                                                                                                                                                                                                                                                                           | Description                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `bytes`                                                                                                                                                                                                                                                                                                            | List[*int*]                                                                                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                                                                                                 | A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token. |
| `logprob`                                                                                                                                                                                                                                                                                                          | *float*                                                                                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                                                                                 | The log probability of this token.                                                                                                                                                                                                                                                                                 |
| `token`                                                                                                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                                                                                 | The token.                                                                                                                                                                                                                                                                                                         |