# TranscriptionSegment


## Fields

| Field                                                                                                                                     | Type                                                                                                                                      | Required                                                                                                                                  | Description                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `avg_logprob`                                                                                                                             | *float*                                                                                                                                   | :heavy_check_mark:                                                                                                                        | Average logprob of the segment. If the value is lower than -1, consider the logprobs failed.                                              |
| `compression_ratio`                                                                                                                       | *float*                                                                                                                                   | :heavy_check_mark:                                                                                                                        | Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed.                                      |
| `end`                                                                                                                                     | *float*                                                                                                                                   | :heavy_check_mark:                                                                                                                        | End time of the segment in seconds.                                                                                                       |
| `id`                                                                                                                                      | *int*                                                                                                                                     | :heavy_check_mark:                                                                                                                        | Unique identifier of the segment.                                                                                                         |
| `no_speech_prob`                                                                                                                          | *float*                                                                                                                                   | :heavy_check_mark:                                                                                                                        | Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent. |
| `seek`                                                                                                                                    | *int*                                                                                                                                     | :heavy_check_mark:                                                                                                                        | Seek offset of the segment.                                                                                                               |
| `start`                                                                                                                                   | *float*                                                                                                                                   | :heavy_check_mark:                                                                                                                        | Start time of the segment in seconds.                                                                                                     |
| `temperature`                                                                                                                             | *float*                                                                                                                                   | :heavy_check_mark:                                                                                                                        | Temperature parameter used for generating the segment.                                                                                    |
| `text`                                                                                                                                    | *str*                                                                                                                                     | :heavy_check_mark:                                                                                                                        | Text content of the segment.                                                                                                              |
| `tokens`                                                                                                                                  | List[*int*]                                                                                                                               | :heavy_check_mark:                                                                                                                        | Array of token IDs for the text content.                                                                                                  |