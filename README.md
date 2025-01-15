# ESG_indicator_dashboard
## 📝 Introduction 
Through this analysis project our goal is to apply ESG (Environmental, Social, and Governance) criteria to countries around the world and create visualizations that track how these nations have evolved over time. ESG is a framework used by investors to assess where their money is going and how it can be used to make a positive impact. Given the growing concerns around global warming and the lasting effects of the COVID-19 pandemic, ESG topics have never been more relevant. This project explores the importance of ESG, not only for investors but for global well-being as a whole.

#### Business Task
To Create an Interactive Dashboard for ESG Data by Country.

    - Visualize and compare ESG indicators across different countries.
    - Allow users to filter by specific ESG categories (Environment, Social, Governance).
    - Enable users to view detailed descriptions of each Series Code.

### Prepare
#### 🔗 Quick Links
**Data Source:** [World Bank](https://databank.worldbank.org/source/environment-social-and-governance?preview=on) <br>

#### Considerations
* I have selected 9 indicators, which are classified into Environment,  Social and Governance as following:-
    - **Environment :** CO2 emissions (metric tons per capita)[**EN.ATM.CO2E.PC**], Electricity production from coal sources (% of total)[**EG.ELC.COAL.ZS**], and Renewable energy consumption (% of total final energy consumption)[**EG.FEC.RNEW.ZS**].
    - **Social      :** Literacy rate, adult total (% of people ages 15 and above)[**SE.ADT.LITR.ZS**], Fertility rate, total (births per woman)[**SP.DYN.TFRT.IN**] and Life expectancy at birth[**SP.DYN.LEOO.IN**].
    - **Governance  :** Control of Corruption: Estimate[**CC.EST**], Political Stability[**PV.EST**] and Absence of Violence/Terrorism: Estimate and Strength of legal rights index (0=weak to 12=strong)[**IC.LGL.CRED.XQ**].
* I have selected 26 countries based on :-
    - **BRICS countries :** Brazil, Russia, India, China, South Africa, Iran, Egypt, Ethiopia, Indonesia, Mexico, and the United Arab Emirates.
    - **High Income Leaders :** USA, Australia, Germany, Canada and Sweden.
    - **Fragile States :** Afghanistan, Sudan, Somalia, Central African Republic and Haiti.
    - **Small Island State :** Barbados, Fiji, Maldives, Seychelles and Tuvalu.
* I have selected data from 1990 to 2020.

**Tools:** <br>
- Data Wrangling : Excel and Python.
- [Data Preparation](https://github.com/sangeetbanik/ESG_indicator_dashboard/blob/main/Data_Preparation.sql) - Excel, Python and SQL.
- Data visualization - [Tableau](https://public.tableau.com/app/profile/sangeet.banik/viz/ESG_Indicator/Dashboard1)

  ### 3. Process
The original dataset has 16,013 rows and 67 columns. To get it ready for analysis, a few steps were taken to clean and prepare the data.

| **No.**|  **Variable**       |  **Description**                                          |
|--------|------------------   | ----------------------------------------------------------|
| 1      | Country Name        | Represents the country name                               |
| 2      | Country Code        | Represents the country (e.g.,"IND" for India).            |
| 3      | Series Code         | Represents different ESG indicators (e.g., CO2 emissions).|
| 4      | Description         | A brief explanation of each Series Code.                  |
| 5      | 1960                | Measurement of indicators on 1960                         |
| 6      | 1961                | Measurement of indicators on 1961                         |
| 7      | 1962                | Measurement of indicators on 1962                         |
..........
| 65      |  2019                | Measurement of indicators on 2019                       |
| 66      |  2020                | Measurement of indicators on 2020                       |
| 67      |  2050                | Measurement of indicators on 2050                       |

#### Data Wrangling
##### Data cleaning
My initial step was to check the dataset using Excel to determine the **data type** and to  uncover any **missing values, outliers, inconsistencies, and errors** within the tables. 
- **Missing values** : The values of indicator measurements were missing for some years. This was resolved by using **df.fillna(0,inplace= True)**, so that all the null values are replaced with 0.

##### Data Preparation
- Using BigQuery, I filtered the dataset as per country, indicator and year requirements.
- Using Excel, I concatenated the indicator measurement values for each years into a single cell [i.e. yr_1990_to_2020], separated by commas.
- Using Python, i exploded the yr_1990_to_2020 column, to get the year wise measurement values for each indicators in a long format.

### Visualisation
![Screenshot 2024-11-29 153041](https://github.com/user-attachments/assets/fd37e864-9bca-4a25-ba93-223531c32bb8)



View [ESG_Indicator Dashboard](https://public.tableau.com/app/profile/sangeet.banik/viz/ESG_Indicator/Dashboard1).









  
