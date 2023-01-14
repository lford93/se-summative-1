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

The project will involve creating a Python function that takes input integers and an integer sequence to generate corresponding age bands. The initial design of the product will be outlined in this README file. The project management and planning will be conducted using GitHub Project Boards, where issues will be raised and treated as sprints in an Agile-like methodology. The function will be tested using the doctest library.

The final product will be documented with README documentation and will be evaluated in a dedicated "Evaluation" section of the README.

## Prerequisites and using the MVP

In order to run the script to convert an age to an age band there are several files and programmes required.

1. Install a Jupyter notebook, use deepnote or use another programme or facility that allows the use of Python and Juypter notebook files.
2. Ensure the necessary libraries are installed onto your system or the cloud system being used. To install the libraries required use the `pip install` command from a terminal.

```
pip install numpy
pip install pandas
pip install regex
```

3. Download the (age_groups_func.py)[https://github.com/lford93/se-summative-1/blob/main/age_groups_func.py] file and (create_age_groups.ipynb)[https://github.com/lford93/se-summative-1/blob/main/create_age_groups.ipynb] file and save to the same folder.
4. The create_age_groups.ipynb can be opened and ages entered onto line 5.

```python
Python
# please enter ages to be coverted to an age band separated by commas
# example:
    # ages = 30, 46, 78
# output will be shown in the fourth code block
ages = 
```

5. The output will be shown in the fourth code block and can be expected to be seen as below.

```python
# print the output
print(output)
     
['10-19']
```

6. Alternatively, those with Python knowledge can download the (age_groups_func.py)[https://github.com/lford93/se-summative-1/blob/main/age_groups_func.py] script and import the function to be used as seen fit.

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
The minimal viable product (MVP) will not allow the separate input for breaks and will instead just allow the user to input ages. The breaks used in the  will be 10 year age groups.

### Design testing

The function will be built iteratively. Using [doctest](https://docs.python.org/3/library/doctest.html), the function will continously be tested after each iteration. This will ensure that the function outputs are what should be expected. It will also help make sure the final product will deliver what has been outlined.

## Project management

This project will be managed managed using Agile principles. Agile project management is an iterative and flexible approach to managing the development of a product or service. It is based on the Agile Manifesto, a set of guiding values and principles for software development that emphasises the importance of collaboration, flexibility, and customer satisfaction. (Agile Alliance, 2022)

In Agile project management, development is broken down into smaller chunks of work called sprints. At the end of each sprint, the team reviews and demonstrates the work completed during the sprint to the customer. (Agile Alliance, 2022)

For this project GitHub issues will be used as so called sprints. The issues will be raised as small pieces of work for edits to the product and relevant documentation through the project. Another method borrowed from Agile for this project is the Kanban board. GitHub's project area allows for the creation of a Kanban board, this is where the issues's progress will be tracked.

![projectboard](https://user-images.githubusercontent.com/120586818/212328979-73f18518-4d4c-4c5a-b57b-92162b55a6c3.png)

The screenshot above shows the Kanban board being used for this project. Issues raised will fall into the "Todo" category until they are picked up and work beings on them. This is when the so called sprint will start for this piece of work. The changes and additions required for the issue/ task will be carried out. During this period the task will sit in the "In Progress" column. Once the changes have been made, a pull request can be created. During this period the task will move to the "Review" section. The task will be reviewed and if it satisfies the requirements can be moved to completed and the related pull request merged. This task is then finished. If the changes are unsatisfactory, comments can be raised on the pull request and the issue can be moved back to "In Progress" to be started again.

### Why use Agile

The Agile methodology has been used due to the flexibility and focus on sprints the methodology provides. This project needs to be able to change according to needs arising and changing. Using issues as sprints gives the ability to focus on building the project in small blocks iteratively. This allows for finer control, especially when working with scripts where bugs can very easily occur. By breaking the processes down into smaller manageable chunks, there is less risk of bugs occuring and when they do occur, they can be more easily dealt with.

## Building the product

The scripts for the product have been created using Python on [deepnote](https://deepnote.com/). Deepnote is a web-based platform that allows users to collaborate and built scripts. It combines a Jupyter Notebook with a collaborative code editor using a cloud-based platform to make it easier for teams to work together.

The repository can be connected to deepnote to enable the adding of commits and push them to the repository via a terminal screen using git commands.

![deepnote_integrations](https://user-images.githubusercontent.com/120586818/212341356-c61392ae-5b03-4989-ae33-a8daa745e71d.png)

Using the integrations panel allows for the connection to a GitHub repository.

![deepnote_terminal](https://user-images.githubusercontent.com/120586818/212341874-25e91680-1bb8-457a-b9c9-e86ed5170dae.png)

Files can be created in deepnote and then be added and pushed to the repository. Any additional changes are tracked and can be added then commited and finally pushed to the repository. The files created in deepnote will be managed in this way.

The function was enhanced and now takes an input and turns it into an ageband. These changes were made using deepnote. They were then pushed as a new branch to the GitHub repository.

![func_enhancement](https://user-images.githubusercontent.com/120586818/212382781-3a3f730f-6a48-4aae-acc3-ca3fc4f352db.png)

By using this method, the new branch is visible on GitHub. The branch can then be merged to the main branch via a standard pull request. This helps ensure the main branch is not changed without any considerations.

![new_pull_request](https://user-images.githubusercontent.com/120586818/212384021-5e788c5e-7bff-4cb8-a49f-ea4204844de6.png)


## Testing the Product

As stated earlier, [doctest](https://docs.python.org/3/library/doctest.html) will be used to test the function. Each iteration will be tested to ensure the function is performing as expected. Initially, a script has been created to import the function and then test. The script is named [testing.ipynb](https://github.com/lford93/se-summative-1/blob/main/testing.ipynb). 

```python
from age_groups_func import age_groups

import doctest

def testing():
    """
    >>> age_groups(1, 1)
    2
    """

doctest.testmod(verbose=True)
```

## Testing MVP

The MVP is a basic version of the designed function. The function has been designed to allow the input of an age or several ages. These ages should then be converted to their corresponding age band based on 10-year age bands. The function is now ready for some extensive testing.

![doctest1](https://user-images.githubusercontent.com/120586818/212416407-020efa43-87b6-4abb-85cc-a0a5101ea81a.png)

It looks like the function has failed at the very first hurdle. The error received is:

```python
ValueError: Input array must be 1 dimensional
```

The problem seems to be related to the input. The input needs to be converted to an array before anything else in the function. This will be raised as an issue to be dealt with in a new commit and pull request.

Bug was fixed in pull request https://github.com/lford93/se-summative-1/pull/30 and issue was closed.

Further testings was conducted after the bug fix. The function needs to be tested with several inputs to check the correct outpot is given. Using the code below, the function was more extensively tested.

```python
Python
def testing():
    """
    >>> print(age_groups(1))
    ['0-9']
    """

def testing1():
    """
    >>> print(age_groups(10))
    ['10-19']

    """

def testing2():
    """
    >>> print(age_groups(55))
    ['50-59']

    """

def testing3():
    """
    >>> print(age_groups([1, 10, 55]))
    ['0-9' '10-19' '50-59']

    """

def testing4():
    """
    >>> print(age_groups([5, 15, 25, 35, 45, 55, 65, 75, 85]))
    ['0-9' '10-19' '20-29' '30-39' '40-49' '50-59' '60-69' '70-79' '80-89']

    """
```

These tests were carried out using the [testing.ipynb](https://github.com/lford93/se-summative-1/blob/main/testing.ipynb) script.

![doctest2](https://user-images.githubusercontent.com/120586818/212474818-ef8c3df1-e712-4a44-9657-e6c64e022d28.png)

As shown in the screenshot, the tests were ran through doctest. All the tests were attempted and succesfully passed. The detail of each test can be seen in the screenshot above.

With this testing complete, I am happy for the MVP to be released and shown to the business. It could also be deployed, but there is currently no error handling within the function itself. There is also no checks for unexpected inputs from users. This is something would be an extra enhancement for to be completed before the full release of the product.

## MVP implementation

The MVP can be used via a jupyter notebook script named [create_age_groups.ipynb](https://github.com/lford93/se-summative-1/blob/main/create_age_groups.ipynb). This script is very simple and allows the user to input some ages into an object. This object is then ran through the age_groups function and the output is printed into the script.

![create_age_groups_screenshot](https://user-images.githubusercontent.com/120586818/212476089-1f451b3a-0b9d-4f7f-943d-868d2dcfcc81.png)

An issue with this implementation is that it does require the user to have some Python knowledge or technical savviness. The user needs to enter integers into the object being created. This could very easily become an issue if they type in the wrong place or accidentally delete something. 

## Evaluation

The main purpose of this GitHub repository and project is was creating a Python function that takes input ages as integers and converts them into corresponding age bands. The project management and planning was conducted using GitHub Project Boards, with issues being raised and treated as sprints in an Agile-like methodology. The function has been tested using the doctest library. The development of the MVP has been be documented with README documentation. The product design is a Python function that can be used by users in various platforms such as Jupyter Notebook, Deepnote, or other software that allow the use of .ipynb files.

The MVP is a basic version of the initial product design. This is so that something can be produced and shown to the business as early as possible. The function has been created and correctly allows the input of ages and creates an output of the corresponding age band. I am satisfied that this is a good quality MVP, however, many issues could occur with the product in its current state. Further extensive testing needs to be carried out on the function. Particularly focusing around the input a user makes. Currently, the function has not been tested on the input of different data types. This could cause the function to break.

Further development needs to be made before full release of the function and product. The function should take into consideration of human error when typing in the input for the function to use. It needs to ensure the user types in integer values and should utilise error handling to inform the user of when a mistake has been made. Eventually, the function could be used in a graphical user interface. This will allow users with no knowledge of Python to simply input ages to be converted into age bands and display a pretty output for them to use.
