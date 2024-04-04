# Normal Timezone

## Explanation
Given a list of timestamps, in json format, this python script outputs a normal form list of
timezones that the entity that generated the timestamps could be in, with weighted confidence.  

It can also output a bar graph of most active times.

An example json input of timezones is in `times_example.json`  

## Installing
With pip, run `pip install -r requirements.txt`. Other python package managers may have a similar command.

## Running  
Run using `python normal_timezone.py <input_file.json> [optional_args]`. 
This will print a list of timezones along with weight.  

## Optional Arguments  

| Argument         | Type    | Description                                                                                                 | Example                                        |
|------------------|---------|-------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| `--timezone_utc` | Integer | The timezone the timestamps entered were taken in.                                                          | `--timezone_utc=+5`, `timezone_utc -4`         |
| `--save_plot`    | String  | When this flag is present, a plot will be generated, and saved to the filename given. Supports jpg and png. | `--save_plot="out.png"`, `save_plot "out.jpg"` |
| `--quiet`        |         | Silence text output. For e.g if you only want the output from `--save_plot`                                 | `--quiet`, `-q`                                |
| `--debug`        |         | Enables debug output, like tracebacks and other logs.                                                       | `--debug`                                      |




