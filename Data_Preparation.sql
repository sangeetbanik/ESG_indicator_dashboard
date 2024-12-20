-- Selecting the necessary Countries and Indicators for the Dashboard
SELECT *
from prime-cosmos-432406-m6.ESG.main_data
where (series_code = 'EN.ATM.CO2E.PC' 
OR 
series_code =  'EG.ELC.COAL.ZS' 
OR series_code = 'EG.FEC.RNEW.ZS'
OR series_code = 'SP.DYN.LE00.IN'
OR series_code = 'SP.DYN.TFRT.IN'
OR series_code = 'SE.ADT.LITR.ZS' 
OR series_code = 'CC.EST' 
OR  series_code = 'PV.EST' 
OR series_code = 'IC.LGL.CRED.XQ')
and 
(country_code = 'USA' 
or country_code = 'AUS' 
OR country_code = 'DEU'
OR country_code = 'SWE'
OR country_code = 'CAN' 
OR country_code = 'BRA' 
OR country_code = 'IND' 
OR country_code = 'CHN' 
OR country_code = 'MEX'
OR country_code = 'ZAF'
OR country_code = 'IDN'
OR country_code = 'AFG'
OR country_code = 'HTI'
OR country_code = 'CAF'
OR country_code = 'SOM'
OR country_code = 'SDN'
OR country_code = 'MDV'
OR country_code = 'SYC'
OR country_code = 'FJI'
OR country_code = 'BRB' 
OR country_code = 'TUV'
OR country_code = 'RUS'
OR country_code = 'IRN'
OR country_code = 'EGY'
OR country_code = 'ETH'
OR country_code = 'ARE')
ORDER BY country_name
