# AdNabu QA Assignment

## Objective
Automate product search and add to cart functionality using Selenium.

## Tools Used
- Python
- Selenium
- WebDriver Manager

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Run script:
   python test_script.py

## Scenario Covered
- Search for a product
- Add product to cart (handles sold-out cases)

## Notes
- Explicit waits used (no sleep)
- Handles dynamic UI and unavailable products

## Known Limitation

All products in the test store were found to be out of stock during execution.

Due to this, the "Add to Cart" functionality could not be fully validated.

The script is designed to:
- Attempt multiple products
- Handle out-of-stock scenarios gracefully
- Log appropriate messages in the test report
