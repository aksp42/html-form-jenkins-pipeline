"""
test_form.py - Automated tests for index.html

Uses only the Python standard library (html.parser), so no packages need
to be installed. Prints PASS/FAIL for every test and exits with:
    0  -> all tests passed
    1  -> at least one test failed (Jenkins marks the build as failed)

Usage:
    python test_form.py              (tests index.html next to this script)
    python test_form.py other.html   (tests a different file)
"""

import os
import sys
from html.parser import HTMLParser

# Default: index.html in the same folder as this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = sys.argv[1] if len(sys.argv) > 1 else os.path.join(SCRIPT_DIR, "index.html")


class FormParser(HTMLParser):
    """Collects <form>, <input> and <button> tags found in the HTML."""

    def __init__(self):
        super().__init__()
        self.forms = []
        self.inputs = []
        self.buttons = []

    def handle_starttag(self, tag, attrs):
        # attrs is a list of (name, value) pairs; convert to a dictionary.
        # Attribute names are already lower-case. A bare attribute such as
        # "required" has the value None, so check with "in", not by value.
        attributes = dict(attrs)
        if tag == "form":
            self.forms.append(attributes)
        elif tag == "input":
            self.inputs.append(attributes)
        elif tag == "button":
            self.buttons.append(attributes)


def parse_html(path):
    """Read and parse the HTML file. Returns an empty parser if the file is missing."""
    parser = FormParser()
    if os.path.isfile(path):
        with open(path, "r", encoding="utf-8") as f:
            parser.feed(f.read())
    return parser


def find_input(parser, input_id):
    """Return the attributes of the <input> with the given id, or None."""
    for attributes in parser.inputs:
        if attributes.get("id") == input_id:
            return attributes
    return None


# ----------------------------------------------------------------------
# Tests: each returns (passed: bool, message: str)
# ----------------------------------------------------------------------

def test_html_file_exists(parser):
    if os.path.isfile(HTML_FILE):
        return True, "Found " + os.path.basename(HTML_FILE)
    return False, "File not found: " + HTML_FILE


def test_form_exists(parser):
    if len(parser.forms) >= 1:
        return True, "Page contains a <form> element"
    return False, "No <form> element found"


def test_name_input(parser):
    field = find_input(parser, "name")
    if field is None:
        return False, 'No <input> with id="name" found'
    if field.get("type", "text").lower() != "text":
        return False, 'Name input should have type="text"'
    if "required" not in field:
        return False, "Name input should be required"
    return True, 'Name input found (type="text", required)'


def test_email_input(parser):
    field = find_input(parser, "email")
    if field is None:
        return False, 'No <input> with id="email" found'
    if field.get("type", "").lower() != "email":
        return False, 'Email input should have type="email"'
    if "required" not in field:
        return False, "Email input should be required"
    return True, 'Email input found (type="email", required)'


def test_contact_input(parser):
    field = find_input(parser, "contact")
    if field is None:
        return False, 'No <input> with id="contact" found'
    if field.get("type", "").lower() != "tel":
        return False, 'Contact input should have type="tel"'
    if "required" not in field:
        return False, "Contact input should be required"
    return True, 'Contact Number input found (type="tel", required)'


def test_submit_button(parser):
    # A <button> without a type attribute also submits, so treat it as submit.
    for button in parser.buttons:
        if button.get("type", "submit").lower() == "submit":
            return True, "Submit button found (<button type=\"submit\">)"
    for field in parser.inputs:
        if field.get("type", "").lower() == "submit":
            return True, "Submit button found (<input type=\"submit\">)"
    return False, "No submit button found"


TESTS = [
    ("HTML file exists", test_html_file_exists),
    ("Page contains a form element", test_form_exists),
    ("Name input exists", test_name_input),
    ("Email input exists with type=email", test_email_input),
    ("Contact Number input exists with type=tel", test_contact_input),
    ("Submit button exists", test_submit_button),
]


def main():
    print("=" * 60)
    print("Running HTML form tests on: " + HTML_FILE)
    print("=" * 60)

    parser = parse_html(HTML_FILE)
    failed = 0

    for title, test_function in TESTS:
        passed, message = test_function(parser)
        status = "PASS" if passed else "FAIL"
        print("[{}] {} - {}".format(status, title, message))
        if not passed:
            failed += 1

    print("-" * 60)
    total = len(TESTS)
    print("Result: {} passed, {} failed, {} total".format(total - failed, failed, total))

    if failed:
        print("OVERALL: FAIL")
        return 1
    print("OVERALL: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
