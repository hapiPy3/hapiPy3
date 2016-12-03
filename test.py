import hapi as h
from pylab import plot
  
if __name__=='__main__':
  h.db_begin(r'c:\temp\data')
  h.fetch('CO2',2,1,2000,2100)
  h.tableList()
  h.describeTable('CO2')
  nu,coef = h.absorptionCoefficient_Lorentz(SourceTables='CO2')

  plot(nu,coef)  