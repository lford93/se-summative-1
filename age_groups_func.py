# import numpy to be able to use np.array
import numpy as np
import pandas as pd
import re

# create the function in this chunk
def age_groups(ages):
    """
    Create age bands from age

    This function creates age bands based on the input of ages and the breaks. 
    The output is a list of corresponding age bands for the inputs.

    Parameters
    ----------
    ages : int
        A list of integers or a single integer used as age to be converted to a corresponding age band.
    breaks : int
        A list of integers to be used to create the breaks for the age bands.

    Returns
    -------
    str
        The corresponding age bands of the inputted ages.

    Examples
    --------
    >>> 
    """
    # these are the default age breaks
    breaks = np.linspace(start=0, stop=90, num=10)
    
    # use pandas to cut the ages by the breaks
    age_groups = pd.cut(x=ages, bins=breaks, right=False)

    # get the categories created by cut
    age_bands = age_groups.categories.astype("str")
    
    # loop through and extract the first number (age) from each category
    x1 = []
    for i in age_bands:
        x = re.sub("^\[([0-9]{1,2}).*", "\\1", str(i))
        x = int(x)
        x1.append(x)

    # loop through and extract the second number - 1 (age) from each category
    x2 = []
    for i in age_bands:
        x = re.sub("^\[[0-9]{1,2}\.0, ([0-9]{1,2}).*", "\\1", str(i))
        x = int(x) - 1
        x2.append(x)
        
    # loop through and put the first age and second ages back together
    age_bands = []
    for i in range(len(x1)):
        age_bands.append(str(x1[i]) + "-" + str(x2[i]))

    # rename the original categories with the new categories
    age_groups = age_groups.rename_categories(age_bands)
    age_groups = age_groups.astype("str")
    
    # return the age bands as required by the function
    return(age_groups)