# Four Russians Algorithm

From: https://github.com/vklyukin/four_russians 

**Setup**
1. The Four Russians algorithm in https://github.com/angrynarwhal/string_algorithms/02-module/code/four_russians has a subdirectory for `four_russians` under the first `four_russians` directory. The double nesting is to keep the four_russians example and python3 cache files out of the main code directory. An attemp at tidyness in the context of the course. 
2. If you clone from the source, everything is in Python presently, but I am optimistic the developer will accept my pull request to update it to Python3. In that case, you do not need to worry about the double nesting. 
```
python3 -m venv ~/.fourrussians
source ~/.fourrussians/bin/activate
pip install wheel
/Users/gogginsS/.fourrussians/bin/python3.9 -m pip install --upgrade pip
pip install -r requirements.txt
```

**Running Tests**
First, make sure you are in the root directory for four_russians, which is *actually* `four_russians/four_russians` and have activated your virtual environment as noted above. `source ~/.fourrussians/bin/activate`. 

```
python -m pytest tests/test_four_russians.py
python -m pytest tests/test_bool_matrix.py
```

These should pass. 

**Running Four Russians**
1. There are test files in the examples subdirectory.
2. `/Users/gogginsS/github/angrynarwhal/stringer/02-module/code/four_russians` experimental
2. `x`


## Table of contents
* [Description](#description)
* [Setup](#setup)
* [Usage](#usage)

## Description
This project contains the implementation of **Four Russians Algorithm** for multiplication of boolean matrices.
The pseudocode is given below:
![pseudocode](https://louridas.github.io/rwa/assignments/four-russians/four_russians_algorithm.png)

The code wraps boolean matrices into the `BoolMatrix` abstraction, which can manipulate with raw 2d-lists. In particular, it supports logical-OR between matrices and rows, extracting blocks (row-wise and column-wise) from matrix, assigning and reading by index.

The Four Russians Algorithm itself is divided into 2 parts: decomposition into blocks (lines 2-4 and 19-20) and blocks multiplication (lines 5-18).

Block multiplication is done as follows:
1. Create matrix with all possible disjunctions (RS) from row-wise block matrix (B_i)
2. Create an empty block multiplication matrix (C_i)
3. Convert each row from column-wise block matrix (A_i) into the decimal number
4. Assign the row from RS by this decimal index to the corresponing row of C_i

In the block decomposition module we create row-wise and column-wise blocks and iteratively multiply them. After each block multiplication we apply logical-OR between result matrix in block multiplication result matrix.


Time complexity: <img src="https://render.githubusercontent.com/render/math?math=O(\frac{n^3}{log(n)})">

Explanation of the algorithm: [Real World Algorithms](https://louridas.github.io/rwa/assignments/four-russians/)  
The details of the algorithm: [Springer](https://link.springer.com/content/pdf/10.1007%2F978-0-387-88757-9_9.pdf).

## Setup
The algorithm is implemented using `python 3.8.5`.  
Tested using `pytest`.  
Console interface is provided by `click`.

> :warning: Numpy is used only for testing. All matrices manipulation is done using custom wrapper `BoolMatrix`


To set up the environment run:
```
pip install -r requirements.txt
```

## Usage

### Run

To run the algorithm you should create a `json`-file with `left` and `right` matrices' data as following:
```json
{
    "left": [[true, false], [false, true]],
    "right": [[true, true], [false, false]]
}
```

#### Simple
The following command will log into the console the result of computation:
```
python3 main.py <matrices' data json-file>
```

#### Save the output
To save the output in json file run:
```
python3 main.py <matrices' data json-file> --result_write_path <output json-file>
```

### Test
To run the tests make sure that `pytest` is installed.
Simply run the following command to test the whole `four_russians` library, including both `BoolMatrix` and algorithm implementation:
```
pytest
```

Numpy is used for the reference computation.
