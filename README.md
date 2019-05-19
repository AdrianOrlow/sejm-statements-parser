# sejm-statements-parser

sejm-statements-parser is a parser of polish MP's statements made with Python. Source of the data is [the Sejm RP website](sejm.gov.pl).

## Installation

Install all the dependencies with pip:

```
pip install -r requirements.txt
```

## Usage

To run the parser, use

```
python saveStatementsToFile.py
```

Data will be saved as an array of strings in the `data.json` file.
You can use this list directly or convert it to plain text via

```
python convertJsonToText.py
```

This data can be used to e.g. create statements generator with deep learning.
I personally wanted to do it with the help of the [textgenrnn](https://github.com/minimaxir/textgenrnn), but my computer turned out to be too weak for this type of operation.

## License

[MIT](https://choosealicense.com/licenses/mit/)
