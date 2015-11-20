HAPI modules
================================

1. FEATURES SUMMARY
-----------------------
Some of the prominent current features of HAPI are:

- Downloading line-by-line data from the HITRANonline site to a local machine.
- Filtering and processing the data in SQL-like fashion.
- Conventional Python structures (lists, tuples, and dictionaries) for representing spectroscopic data.
- Possibility to use a large set of third-party Python libraries to work with the data.
- Python implementation of the HT profile [1-3] which can be used in spectra simulations. This lineshape can also be reduced to a number of conventional line profiles such as Gaussian (Doppler),Lorentzian, Voigt, Rautian, Speed-dependent Voigt and speed-dependent Rautian.
- Python implementation of total internal partition sums (TIPS-2011 [4]) which is used in spectrasimulations as well as scaling some HITRAN [5] parameters.
- High-resolution spectra simulation accounting for pressure, temperature and optical path length.
- The following spectral functions can be calculated:
	- absorption coefficient 
	- absorption spectrum
	- transmittance spectrum 
	- radiance spectrum
- Spectral calculation using a number of instrumental functions to simulate experimental spectra.
- Possibility to extend the user's functionality by adding custom line shapes, partition sums andapparatus functions.

---------------------------------------

2. WORKING WITH DATA 
-------------------------

LOCAL DATABASE STRUCTURE
#####################################

DOWNLOADING AND DESCRIBING DATA
#####################################
	- To start working with HAPI, the user should import all functions from the module “hapi.py”
	- To get additional information on function fetch, call getHelp.
	- To download the data, simply call the function "fetch".
		- See getHelp(fetch_by_ids) to get more information on this.
	- To get a list of tables which are already in the database, use the tableList() function.
	- To learn about the table we just downloaded, let's use a function "describeTable".


FILTERING AND OUTPUTTING DATA
#####################################
Use the simple select(...) call to output the table content. Full information on control parameters can be obtained via the getHelp(select) statement.

FILTERING CONDITIONS
#####################################
The following operations are available in select (case insensitive):

==================== ==========================  ====================================
DESCRIPTION  		 LITERAL 					EXAMPLE
==================== ==========================  ====================================
Range                'RANGE','BETWEEN'           ('BETWEEN','nu',0,1000)
Subset               'IN','SUBSET'               ('IN','local_iso_id',[1,2,3,4])
And                  '&','&&','AND'              ('AND',('<','nu',1000),('>','nu',10))
Or                   '|','||','OR'               ('OR',('>','nu',1000),('<','nu',10))
Not                  '!','NOT'                   ('NOT',('IN','local_iso_id',[1,2,3]))
Less than            '<','LESS','LT'             ('<','nu',1000)
More than            '>','MORE','MT'             ('>','sw',1.0e-20)
Less or equal to     '<=','LESSOREQUAL','LTE'    ('<=','local_iso_id',10)
Greater or equal to  '>=','MOREOREQUAL','MTE'    ('>=','sw',1e-20)
Equal                '=','==','EQ','EQUAL','EQ'  ('<=','local_iso_id',10)
Not equal            '!=','<>','~=','NE','NOTE   ('!=','local_iso_id',1)
Summation            '+','SUM':                  ('+','v1','v2','v3')
Difference           '-','DIFF'                  ('-','nu','elow')
Multiplication       '*','MUL'                   ('*','sw',0.98)
Division             '/','DIV'                   ('/','A',2)
Cast to string       'STR','STRING'              ('STR','some_string')
Cast to Python list  'LIST'                      ('LIST',[1,2,3,4,5])
Match regexp         'MATCH','LIKE'              ('MATCH',(‘STR’,'\w+'),'nu')
Search single match  'SEARCH'                    ('SEARCH',(‘STR’,'\d \d \d'),'quanta')
Search all matches   'FINDALL'                   ('FINDALL',(‘STR’,'\d'),'quanta')
Count within group   'COUNT'                     ('COUNT','local_iso_id')
==================== ==========================  ====================================

ACCESSING COLUMNS IN A TABLE
############################################
For this purpose, there exist two functions:

``getColumn(...)``
``getColumns(...)``

The first one returns just one column at a time. The second one returns a list of columns.

SPECIFYING A LIST OF PARAMETERS
###########################################
The select function has a control parameter "ParameterNames", which makes it possible to specify parameters we want to be selected, and perform some simple arithmetic expressions with them.

SAVING QUERY TO DISK
#############################################
For example, select all lines from H2O and save the result in file 'H2O.txt':

``select('H2O',File='H2O.txt')``

GETTING INFORMATION ON ISOTOPOLOGUES
#############################################
	- Natural abundances
	- Molecular masses
	- Molecule names
	- Isotopologue names
	- ISO_ID

-----------------------------------

3. CALCULATING SPECTRA
-----------------------------
HAPI provides a powerful tool to calculate cross-sections based on line-byline
data contained in HITRAN. This features:

- Python implementation of the HT (Hartmann-Tran [1-3]) profile which is used in spectra simulations. This line shape can also be reduced to a number of conventional line profiles such as Gaussian (Doppler), Lorentzian, Voigt, Rautian, Speed-dependent Voigt and speed-dependent Rautian.
- Python implementation of total internal partition sums (TIPS-2011 [4]) which is used in spectra simulations.
- High-resolution spectra simulation accounting for pressure, temperature, and optical path length. The following spectral functions can be calculated:
	- absorption coefficient
	- absorption spectrum
	- transmittance spectrum
	- radiance spectrum
- Spectra simulation using a number of apparatus functions.
- Possibility to extend the user's functionality by adding custom line shapes, partition sums, and apparatus functions.
- An approach to function code is aimed to be flexible enough, yet hopefully intuitive.

USING LINE PROFILES
#############################
Several line shape (line profile) families are currently available:

- Gaussian (Doppler) profile
- Lorentzian profile
- Voigt profile
- HT profile (Hartmann-Tran)

USING PARTITION SUMS
##############################
To calculate a partition sum for most of the isotopologues in HITRAN, we will use a function partitionSum.
The syntax is as follows: 
partitionSum(M,I,T), where M,I - standard HITRAN molecule-isotopologue notation, T - definition of temperature range.
*use getHelp for detailed info.*

CALCULATING ABSORPTION COEFFICIENTS
##########################################
Currently HAPI can calculate the following spectral function at arbitrary thermodynamic parameters:

1) Absorption coefficient
2) Absorption spectrum
3) Transmittance spectrum
4) Radiance spectrum

All these functions can be calculated with or without accounting of instrument properties (apparatus function, resolution, path length etc...)

To calculate an absorption coefficient, we can use one of the following functions:

- absorptionCoefficient_HT
- absorptionCoefficient_Voigt
- absorptionCoefficient_Lorentz
- absorptionCoefficient_Doppler
Each of these functions calculates cross sections using different line shapes (the names are quite selfexplanatory).
You can get detailed information on using each of these functions by calling getHelp(function_name).

**HAPI provides a flexible control over a calculation procedure. This control can be achieved by using a number of input parameters. See more in hapi_manual.pdf**

CALCULATING ABSORPTION, TRANSMITTANCE, AND RADIANCE SPECTRA
################################################################
In order to be consistent with internal API's units, we need to have an absorption coefficient in cm-1:

``nu,coef = absorptionCoefficient_Lorentz(SourceTables='CO2',HITRAN_units=False)``

To calculate absorption spectrum, use the function absorptionSpectrum():

``nu,absorp = absorptionSpectrum(nu,coef)``

To calculate transmittance spectrum, use function transmittanceSpectrum():

``nu,trans = transmittanceSpectrum(nu,coef)``

To calculate radiance spectrum, use function radianceSpectrum():

``nu,radi = radianceSpectrum(nu,coef)``

The last three commands used a default path length (1 m). To see complete info on all three functions,
look for the section "calculating spectra" in getHelp()

APPLYING INSTRUMENTAL FUNCTIONS
######################################
The following instrumental functions are available:

1) Rectangular (Boxcar) 
2) Triangular 
3) Gaussian
4) Dispersion (Lorentz) 
5) Diffraction 
6) Michelson

`Details are included in hapi_manual.pdf`

ALIASES
#############
To simplify the usage of HAPI, aliases (i.e. shortcuts) are given for the cross section functions:

abscoef_HT 			=> absorptionCoefficient_HT
abscoef_Voigt 		=> absorptionCoefficient_Voigt
abscoef_Lorentz 	=> absorptionCoefficient_Lorentz
abscoef_Doppler 	=> absorptionCoefficient_Doppler
abscoef_Gauss		=> absorptionCoefficient_Doppler

---------------------------------------

PLOTTING WITH MATPLOTLIB
----------------------------
Make plots using the Matplotlib - Python library for plotting.
A step-by-step guide can be found in hapi_manual.pdf

EXAMPLES OF KEY FUNCTIONS
-----------------------------
- Help system
	- getHelp()
- Fetching data
	- fetch(TableName, M, I, numin, numax)
	- fetch_by_ids(TableName, iso_id_list, numin, numax)
- Working with data
	- db_begin(db=None)
	- db_commit()
	- tableList()
	- describeTable(TableName)
	- select(TableName, DestinationTableName='__BUFFER__', ParameterNames=None, Conditions=None, Output=True, File=None)
	- sort(TableName, DestinationTableName=None, ParameterNames=None, Accending=True, Output=False, File=None)
	- group(TableName, DestinationTableName='__BUFFER__', ParameterNames=None, GroupParameterNames=None, Output=True)
	- extractColumns(TableName, SourceParameterName, ParameterFormats, ParameterNames=None, FixCol=False)
	- getColumn(TableName, ParameterName)
	- getColumns(TableName, ParameterNames)
	- dropTable(TableName)
- Calculating spectra
	- PROFILE_HT(sg0, GamD, Gam0, Gam2, Shift0, Shift2, anuVC, eta, sg)
	- PROFILE_VOIGT(sg0, GamD, Gam0, sg)
	- PROFILE_LORENTZ(sg0, Gam0, sg)
	- PROFILE_DOPPLER(sg0, GamD, sg)
	- partitionSum(M, I, T, step=None)
	- absorptionCoefficient_HT()
	- absorptionCoefficient_Voigt()
	- absorptionCoefficient_Lorentz()
	- absorptionCoefficient_Doppler()
	- transmittanceSpectrum()
	- absorptionSpectrum()
	- radianceSpectrum()
- Convolving spectra
	- RECTANGULAR : SLIT_RECTANGULAR
	- TRIANGULAR : SLIT_TRIANGULAR
	- GAUSSIAN : SLIT_GAUSSIAN
	- DIFFRACTION : SLIT_DIFFRACTION
	- MICHELSON : SLIT_MICHELSON
	- DISPERSION/LORENTZ : SLIT_DISPERSION
- Information on isotopologues
	- abundance(M, I)
	- molecularMass(M, I)
	- moleculeName(M)
	- isotopologueName(M, I)
- Miscellaneous
	- getStickXY(TableName)
	- read_xsect(filename)

-----------------------------------------------------------------

TO BE CONTINUED