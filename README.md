Analyze NPMS data
=================



Mini-Project3 - Step 1
----------------------

Please use the data stored in your mongodb table to model/predict number of downloads using 
other attributes in the data.

1. First extract data from the table using, for example, the supplied extract.py script.

2. Then read it into R and do the analysis of univariate and multivariate distributions.

3. Formulate various hypotheses on what could drive the number of downloads and construct
   measures that would represent them.

4. Finally prepare a presentation that explains or predicts the number of downloads using remaining 
   variables.



Mini-Project3 - Step 2: Challenge
----------------------


1. Think of alternative hypotheses that rely on data that is not extracted by extract.py script.
Could it be that properties of a maintainer (e.g., being successful with other projects)
might drive the downloads? Could it be that certain type of applications based on the text 
analysis of reade file may also affect the number of downloads?

2. Write scripts top extract and compute needed measures from MongoDB (perhaps utilizing information
in collections collected by others). The full collection of packages is in database NPMS_packages
collection npms_all.

3. Fit suitable models and present results.

