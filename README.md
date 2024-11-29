# ESG_indicator_dashboard
## 📝 Introduction 
Through this analysis project our goal is to apply ESG (Environmental, Social, and Governance) criteria to countries around the world and create visualizations that track how these nations have evolved over time. ESG is a framework used by investors to assess where their money is going and how it can be used to make a positive impact. Given the growing concerns around global warming and the lasting effects of the COVID-19 pandemic, ESG topics have never been more relevant. This project explores the importance of ESG, not only for investors but for global well-being as a whole.

#### Business Task
To Create an Interactive Dashboard for ESG Data by Country.

### Prepare
#### 🔗 Quick Links
**Data Source:** [World Bank](https://databank.worldbank.org/source/environment-social-and-governance?preview=on) <br>

#### Considerations
* I have selected 9 indicators, which are classified into Environment,  Social and Governance as following:-
    - **Environment :** CO2 emissions (metric tons per capita), Electricity production from coal sources (% of total), and Renewable energy consumption (% of total final energy consumption).
    - **Social      :** Literacy rate, adult total (% of people ages 15 and above), Fertility rate, total (births per woman) and Fertility rate, total (births per woman).
    - **Governance  :** Control of Corruption: Estimate, Political Stability and Absence of Violence/Terrorism: Estimate and Strength of legal rights index (0=weak to 12=strong).
* I have selected 26 countries based on :-
    - **BRICS countries :** Brazil, Russia, India, China, South Africa, Iran, Egypt, Ethiopia, Indonesia, Mexico, and the United Arab Emirates.
    - **High Income Leaders :** USA, Australia, Germany, Canada and Sweden.
    - **Fragile States :** Afghanistan, Sudan, Somalia, Central African Republic and Haiti.
    - **Small Island State :** Barbados, Fiji, Maldives, Seychelles and Tuvalu.

**Tools:** <br>
- Data Wrangling : Excel and Python.
- [Data Preprocessing](https://github.com/sangeetbanik/ESG_indicator_dashboard/blob/main/Data_Preprocessing.sql) - Excel, Python and SQL.
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
I used BigQuery to filter the dataset as per requiremment.








  
