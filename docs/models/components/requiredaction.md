# RequiredAction

Details on the action required to continue the run. Will be `null` if no action is required.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `submit_tool_outputs`                                                        | [components.SubmitToolOutputs](../../models/components/submittooloutputs.md) | :heavy_check_mark:                                                           | Details on the tool outputs needed for this run to continue.                 |
| `type`                                                                       | [components.RunObjectType](../../models/components/runobjecttype.md)         | :heavy_check_mark:                                                           | For now, this is always `submit_tool_outputs`.                               |