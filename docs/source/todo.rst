To Do List 
================================

2015-11-22
-----------
1. RESTful API

- http client to download the data from the [HITRANonline]_
- json format to store the different molecules' information
- matplotlib to draw the lines according to different requirements
- and why not provide a tcl/tk interface or PyQt5(Python3) interface

2. The Virtual Atomic and Molecular Data Centre (VAMDC) [VAMDC]_ is working in progress
to provide a XML Schema for the HITRAN Database.

.. [VAMDC] (https://zenodo.org/record/18030?ln=en#.VlGnCKLnlGQ)

2015-11-18
----------------
1. divide the index.rst into different chapters. DO NOT include them in a single file.
And Do Remember to seperate the _build and _source into different directorys.

	e.g.:	Copyright Chapter.
			Forwords Chapter.
			Contact Chapter.(Including the Authors and Contributors)
			Changelog Chapter.(What do you have already done)
			ToDo List Chapter.(TO DO in future)


2. Use the footnotes to emphasize the things that should be taken into considerations.

3. Find a way to highlight the built-in function in the Hapi.py file


4. Some formats are in disorder. e.g.: 

abscoef_HT 			=> absorptionCoefficient_HT
abscoef_Voigt 		=> absorptionCoefficient_Voigt
abscoef_Lorentz 	=> absorptionCoefficient_Lorentz
abscoef_Doppler 	=> absorptionCoefficient_Doppler
abscoef_Gauss		=> absorptionCoefficient_Doppler


5. DO not use the upper characters in the table of contents.
Not all of the Users are native Enligsh Speakers.

6. Add the Mathjax Support, and we need the MathJax to render the Mathmatical forumla.

7. Add the reference papers to the docs. e.g.: 

	- Python implementation of total internal partition sums (TIPS-2011 [4]) which is used in spectrasimulations as well as scaling some HITRAN [5] parameters.

One Should add the reference papers, and the application papers to the docs 

