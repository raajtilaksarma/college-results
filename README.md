# college-results

Fetch your college result from a pdf. Strictly for Tezpur University students.

## Demo

![usage-gif](https://github.com/raajtilaksarma/college-results/blob/master/college-results.gif)

## Disclaimer

Works for [Tezpur University](http://www.tezu.ernet.in/) result pdfs only.

## Motivation

Results in our college comes in the form of large pdfs where we have to keep scrolling until we find our `gpa(sgpa/cgpa)`.

## Steps to setup

- `pip3 install -r requirements.txt`
- `git clone git@github.com:raajtilaksarma/college-results.git`
- `cd college-results`
- download your respective result pdf file from [website](http://www.tezu.ernet.in/)
- Run `cgpa.py` with required arguments
- You may face [this](https://stackoverflow.com/questions/45912641/unable-to-install-pdftotext-on-python-3-6-missing-poppler) issue while `pdftotext` is being installed. 


## Scripts

### `cgpa.py`

#### Description

This script takes in the result pdf file as input and outputs two files, one containing cgpa of each student by roll no
and another containing department wise average cgpa.

#### Usage

```
python3 cgpa.py --infile Results_finalsem_spring_2019.pdf --roll CSB15007 --cgpa cgpa.csv --deptcgpa dept_cgpa.csv

```

#### Arguments

```
optional arguments:
  -h, --help            show this help message and exit
  -i INFILE, --infile INFILE
                        Input PDF file of result
  -r ROLL, --roll ROLL  Your roll number
  -c CGPA, --cgpa CGPA  Output file name for individual cgpa file
  -d DEPTCGPA, --deptcgpa DEPTCGPA
                        Output file name for department cgpa file
```

