# Selenium-Python-Framework

## Managing virtual enviroment (venv)

**Create virtual environment**

```bash
python3 -m venv .venv
```

**Activate virtual environment**

```bash
source .venv/bin/activate
```

**Install dependencies**

```bash
pip install -r requirements.txt
```

**Write dependencies used**

```bash
pip freeze > requirements.txt
```

## Running tests

**Running all test cases**

```bash
    pytest
```

**Showing standard outputs**

```bash
    pytest -s
```

**Running a specific test**

```bash
    pytest -k {name of test case}
```

**Run tests in parallel**

```bash
    pytest -n {number of browsers to use}
```

**Generate HTML report**

```bash
    pytest --html=report.html --self-contained-html
```

**Generate XML report**

```bash
    pytest --junitxml="junitxml_report.xml"
```

**Generate report and run programs in parallel**

```bash
    pytest --junitxml="./e2e/reports/result.xml" -n auto
```

## Libraries used

- [pytest](https://pypi.org/project/pytest/)
- [selenium](https://pypi.org/project/selenium/)
- [webdriver-manager](https://pypi.org/project/webdriver-manager/)
- [pytest-xdist](https://pypi.org/project/pytest-xdist/)
- [autopep8](https://pypi.org/project/autopep8/)
- [pytest-html](https://pypi.org/project/pytest-html/)
