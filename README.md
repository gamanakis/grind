# Project Title

This program converts exported table data from FlowJo to a format 
suitable for use with SPICE (niaid.github.io/spice)

### Prerequisites

What software is require for the program to run:
* python3
* pandas library
* numpy library

The above python libraries along with python3 are installed by default on MacOSX.

### Installing

To install the program, clone its repository to a folder by running:

```
git clone github.com/gamanakis/muller
```

Otherwise, you can also grab the muller.py file along with LICENSE.txt and README.md
from this repository and put them altogether in a folder.

## Running

Select your markers in FlowJo and run them through Combination Gates.
This should create all possible combinations for these markers.
Export them in a table like the following:

| Subject    | Marker-1   | Marker-2   | Marker-1/Marker-2   | neg   | Virus      |
| :--------- |:-----------|:-----------|:--------------------|:------|:-----------|
| A          | 1          | 5          | 11                  | 0.1   | HBV        |
| B          | 2          | 6          | 12                  | 0.2   | HBV        |
| C          | 3          | 7          | 13                  | 0.3   | HBV        |

Save the file in csv format, name it Book1.csv, this is important.
Copy it to the directory where the program has been downloaded.

Run: 
./muller.py

It will display the columns it detected in Book1.csv:
Subject
Marker-1
Marker-2
Marker-1/Marker-2
neg

Then, it will ask:
* for the column(s) that will be preserved in the new table,
here "Subject Virus" (these are usually the subjects and any columns to be used
as overlays
* for the delimiter between the markers, here the "/" was used
* for the column where none of the markers is expressed, 
in our example this is the "neg" column.

The program will produce a file "Book2.csv" with the following format:

| Subject    | Virus      | Marker-1   | Marker-2   | Value   |
| :--------- |:-----------|:-----------|:-----------|:--------|
| A          | HBV        | -          | -          | 0.1     |
| A          | HBV        | +          | -          | 1       |
| A          | HBV        | -          | +          | 5       |
| A          | HBV        | +          | +          | 11      |
| B          | HBV        | -          | -          | 0.2     |
| B          | HBV        | +          | -          | 2       |
| B          | HBV        | -          | +          | 6       |
| B          | HBV        | +          | +          | 12      |
| C          | HBV        | -          | -          | 0.3     |
| C          | HBV        | +          | -          | 3       |
| C          | HBV        | -          | +          | 7       |
| C          | HBV        | +          | +          | 13      |

This file can be imported into SPICE directly for further analysis.

## License

This project is licensed under the GPLv3 License - see the [LICENSE.txt](LICENSE.txt) file for details

