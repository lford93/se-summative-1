#  Software Engineering Summative Assignment 1: Report

## Introduction

This project is for the submission of summative assignment 1 of the Software Engineering course. To compelete this assignment the brief has detailed that the project needs to meet the following:

1. Propose a new product for your employer or a small-scale side project for your organisation. It may be:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- a simple web app, e.g., a currency converter (written in HTML, CSS and JavaScript)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- a data product, e.g., a Jupyter notebook with some data visualisations that collects data from a web API or an online SQL database

2. Design your product using Figma or an alternative.
3. Outline how you planned your project using modern planning techniques (e.g., agile with sprints). Reflect on your planning using a project Project Management Tool (we strongly recommend GitHub Projects, a free alternative to Jira).
4. Capture the requirements for your project as issues or tickets shown via your chosen Project Management Tool
5. Summarise how you built the minimal viable product or a prototype step by step in a written report.
6. Use Test Driven Development to produce an initial codebase for your product.
7. Use GitHub or an alternative to add features to your prototype or MVP gradually.
8. Document your MVP with README documentation.
9. Document and use a ticketing system according to the documentation. Conventionally one ticket is one feature corresponding to one branch and one pull request.
10. Evaluate your design in a dedicated “Evaluation” section of your README

The project will involve creating a Python function that takes input integers and an integer sequence to generate corresponding age bands. The initial design of the product will be outlined in this README file. The project management and planning will be conducted using GitHub Project Boards, where issues will be raised and treated as sprints in an Agile-like methodology. The function will be tested using the pytest library.

The final product will be documented with README documentation and will be evaluated in a dedicated "Evaluation" section of the README.

## Product design

The product for this project is a Python function that can be used by users in various platforms such as Jupyter Notebook, Deepnote, or even in base Python. The function enables users to input integers and a custom age break, and it returns the corresponding age bands for the inputted integers.

### Initial design

The function will have two inputs.

```python
Python
def age.groups(age, breaks)
```

The `age` parameter is where the ages will be specified. These will need to be integer values and the fucntion will need to have checks in place to ensure an integer has been inputted for the function to run.

The second argument will contain the age breaks. It will allow the input of integers that will then be transformed to a sequence in order to split the age input into the desired breaks.

The output will show the corresponding age bands for the inputted integers. For example, if the input is age 15 and the specified age bands are 0-9, 10-19, etc then the input of 15 should return 10-19.

```python
Python
ages = 15
breaks = [0,10,20,30,40] 

print(age.groups(ages, breaks))
```

```python
Output
"10-19"
```
### Design testing

The function will be built iteratively. Using [pytest](https://docs.pytest.org/en/7.2.x/), the function will continously be tested after each iteration. This will ensure that the function outputs are what should be expected. It will also help make sure the final product will deliver what has been outlined.
