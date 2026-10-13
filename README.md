# E-Commerce Test Automation Framework

An automated web testing framework built using Python, Pytest, and Playwright to validate essential e-commerce workflows.

## Tech Stack
- **Language:** Python
- **Test Framework:** Pytest
- **Automation Tool:** Playwright
- **Browser:** Chromium
- **Reporting:** Pytest HTML Reports

## Features
- Login testing with valid and invalid credentials
- Product sorting validation
- Add and remove products from cart
- Checkout form validation
- Complete checkout workflow
- HTML test report generation
- Browser context and page fixtures

## Test Results
- **Total test cases:** 6
- **Passed:** 6
- **Failed:** 0

## Project Structure

```text
ecommerce-test-automation/
├── pages/
│   ├── checkout_page.py
│   ├── login_page.py
│   └── products_page.py
├── tests/
│   ├── test_checkout.py
│   ├── test_login.py
│   └── test_products.py
├── reports/
├── conftest.py
├── pytest.ini
├── test_login.py
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Shubham10012005/ecommerce-test-automation.git
cd ecommerce-test-automation
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install pytest pytest-playwright pytest-html
playwright install chromium
```

## Run Tests

```bash
python -m pytest tests/ --browser chromium -v
```

Generate an HTML report:

```bash
python -m pytest tests/ --browser chromium --html=reports/report.html --self-contained-html
```

## Future Improvements
- GitHub Actions CI/CD integration
- Automated screenshots and traces on test failure
- Additional test scenarios and browser coverage

## Author
Shubham Ingle

GitHub: https://github.com/Shubham10012005