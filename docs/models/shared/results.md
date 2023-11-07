# Results


## Fields

| Field                                                                             | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `categories`                                                                      | [components.Categories](../../models/shared/categories.md)                        | :heavy_check_mark:                                                                | A list of the categories, and whether they are flagged or not.                    |
| `category_scores`                                                                 | [components.CategoryScores](../../models/shared/categoryscores.md)                | :heavy_check_mark:                                                                | A list of the categories along with their scores as predicted by model.           |
| `flagged`                                                                         | *bool*                                                                            | :heavy_check_mark:                                                                | Whether the content violates [OpenAI's usage policies](/policies/usage-policies). |