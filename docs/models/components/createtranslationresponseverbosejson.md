# CreateTranslationResponseVerboseJSON


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `duration`                                                                               | *str*                                                                                    | :heavy_check_mark:                                                                       | The duration of the input audio.                                                         |
| `language`                                                                               | *str*                                                                                    | :heavy_check_mark:                                                                       | The language of the output translation (always `english`).                               |
| `text`                                                                                   | *str*                                                                                    | :heavy_check_mark:                                                                       | The translated text.                                                                     |
| `segments`                                                                               | List[[components.TranscriptionSegment](../../models/components/transcriptionsegment.md)] | :heavy_minus_sign:                                                                       | Segments of the translated text and their corresponding details.                         |