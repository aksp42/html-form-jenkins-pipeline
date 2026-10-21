# Automated HTML Form Testing using Jenkins Pipeline

## Project Objective

To build a simple HTML form and automatically test its structure with a Python script, then prepare a Jenkins Declarative Pipeline that runs those tests whenever the project is built from a GitHub repository. This is a beginner-level DevOps practical on Continuous Integration (CI).

## Technologies Used

- **HTML5 and CSS3**: the form and its styling
- **Python 3** (standard library only, `html.parser`): automated tests
- **Jenkins** (Declarative Pipeline): build automation
- **Git and GitHub**: source code hosting

## Project Structure

```
html-form-jenkins/
├── index.html      # The HTML form (Name, Email, Contact Number, Submit)
├── test_form.py    # Automated test script
├── Jenkinsfile     # Jenkins Declarative Pipeline
└── README.md       # This file
```

## File Descriptions

| File | Description |
|------|-------------|
| `index.html` | A registration form with required Name, Email and Contact Number fields and a Submit button. CSS is included inside the file. Validation uses HTML attributes (`required`, `type="email"`, `type="tel"`, `pattern`). No backend or database is needed. |
| `test_form.py` | Reads `index.html`, parses it with `html.parser` and runs 6 tests. Prints PASS or FAIL for each test. Exits with code `0` if all pass, otherwise `1`. |
| `Jenkinsfile` | Declarative Pipeline with two stages: **Checkout** and **Run HTML Form Tests**. It contains no passwords or tokens. |
| `README.md` | Project documentation. |

## Open the Form Locally

1. Open the `html-form-jenkins` folder.
2. Double-click `index.html` (it opens in your default browser).
3. Try submitting with empty or invalid fields to see the browser validation, then fill in valid values and click **Submit**.

## Run the Tests Locally

Requirement: Python 3 installed (check with `python --version`).

Open Command Prompt inside the project folder and run:

```
python test_form.py
```

Expected output when everything is correct:

```
[PASS] HTML file exists - Found index.html
[PASS] Page contains a form element - Page contains a <form> element
...
OVERALL: PASS
```

To see a failing test, temporarily change `type="email"` to `type="text"` in `index.html` and run the tests again. You should see `[FAIL]` for the email test. Check the exit code with `echo %ERRORLEVEL%` (it will be `1`). Change it back afterwards.

## How Jenkins Runs the Pipeline

This describes the setup you will do. It has not been done yet.

1. Push the project to a GitHub repository.
2. In Jenkins, create a new **Pipeline** job.
3. Under *Pipeline*, choose **Pipeline script from SCM**, set SCM to **Git**, enter your repository URL, choose the branch (for example `main`) and keep the Script Path as `Jenkinsfile`. If the repository is private, pick a credential from the Jenkins credentials dropdown (never type tokens into the Jenkinsfile).
4. Click **Build Now**.
5. Jenkins then:
   - **Checkout stage**: downloads the code from GitHub (`checkout scm`).
   - **Run HTML Form Tests stage**: runs `python test_form.py` (`python3` on Linux).
   - If the script exits with `0`, the build is **SUCCESS**. If any test fails, the script exits with `1` and the build is **FAILED**.
6. Open the build's **Console Output** to read the stage names and the PASS/FAIL lines.

Note: Python 3 must be installed on the machine running Jenkins and available in its PATH.
