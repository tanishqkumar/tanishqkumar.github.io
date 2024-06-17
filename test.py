import numpy as np
import matplotlib.pyplot as plt

# GDP per capita data for China and the USA
china_gdp_1992, china_gdp_2022 = 1731.657216, 18187.84112
usa_gdp_1992, usa_gdp_2022 = 40707.29063, 64623.12563

# Number of years from 1992 to 2022
years = 2022 - 1992

# Calculate the annual growth rates
annual_growth_rate_china = ((china_gdp_2022 / china_gdp_1992) ** (1 / years)) - 1
annual_growth_rate_usa = ((usa_gdp_2022 / usa_gdp_1992) ** (1 / years)) - 1
print(annual_growth_rate_china, annual_growth_rate_usa)

# Initialize arrays to store the projected GDP per capita values
years_projection = np.arange(2022, 2101)  # Years from 2022 to 2100
china_gdp_projection = [china_gdp_2022]
usa_gdp_projection = [usa_gdp_2022]

# Calculate the GDP per capita projections for each year
for i in range(1, len(years_projection)):
    china_gdp_projection.append(china_gdp_projection[i - 1] * (1 + annual_growth_rate_china))
    usa_gdp_projection.append(usa_gdp_projection[i - 1] * (1 + annual_growth_rate_usa))

# When will China catch up to the U.S.?
catch_up_year = next((year for year, gdp_china, gdp_usa in zip(years_projection, china_gdp_projection, usa_gdp_projection) if gdp_china >= gdp_usa), None)

# # Create the plot
# plt.figure(figsize=(14, 7))
# plt.plot(years_projection, china_gdp_projection, label='China GDP per Capita', color='red')
# plt.plot(years_projection, usa_gdp_projection, label='USA GDP per Capita', color='blue')
# plt.axvline(x=catch_up_year, color='green', linestyle='--', label=f'Catch Up Year: {catch_up_year}')
# plt.title('Projected GDP per Capita (PPP) from 2022 to 2100')
# plt.xlabel('Year')
# plt.ylabel('GDP per Capita (PPP in constant 2017 international $)')
# plt.yscale('log')  # Logarithmic scale for proportional comparison
# plt.legend()
# plt.grid(True)
# plt.show()

# catch_up_year

# Given data
usa_gdp_2022 = 64623.12563
china_gdp_2022 = 18187.84112
annual_growth_rate_usa = 0.015524780536834593  # U.S. baseline growth rate from 1992 to 2022

# Part (i): Baseline growth rate for China
baseline_growth_rate_china = annual_growth_rate_usa

# Part (ii): Convergence growth rate for China
convergence_factor = 0.02  # China will close 2% of the GDP per capita gap each year
gap_in_gdp_per_capita = usa_gdp_2022 - china_gdp_2022
convergence_growth_rate_china = convergence_factor * gap_in_gdp_per_capita / china_gdp_2022

# Part (iii): Overall growth rate for China between 2022 and 2023
# China's overall growth rate is the sum of its baseline growth rate and the convergence growth rate
overall_growth_rate_china = baseline_growth_rate_china + convergence_growth_rate_china

# Print the calculated rates
print("Baseline Growth Rate for China: ", baseline_growth_rate_china)
print("Convergence Growth Rate for China: ", convergence_growth_rate_china)
print("Overall Growth Rate for China between 2022 and 2023: ", overall_growth_rate_china)

import numpy as np
import matplotlib.pyplot as plt

# Initial GDP per capita values in 2022
china_gdp = china_gdp_2022
usa_gdp = usa_gdp_2022

# Lists to store the projected GDP per capita values for each year
china_gdps = [china_gdp]
usa_gdps = [usa_gdp]

# Years from 2022 to 2100
years = np.arange(2022, 2101)

# Growth rates
usa_growth_rate = annual_growth_rate_usa

# Convergence factor
convergence_factor = 0.02

# Loop through each year to calculate the GDP per capita
for year in years[1:]:
    # Calculate next year's GDP per capita for the USA
    usa_gdp *= (1 + usa_growth_rate)
    usa_gdps.append(usa_gdp)

    # Calculate the convergence boost for China
    convergence_boost = convergence_factor * (usa_gdp - china_gdp)

    # Calculate next year's GDP per capita for China
    china_gdp *= (1 + usa_growth_rate)  # Baseline growth
    china_gdp += convergence_boost  # Convergence boost
    china_gdps.append(china_gdp)

# Find when China reaches 80% of the US's GDP per capita
eighty_percent_years = next((year for year, china_gdp, usa_gdp in zip(years, china_gdps, usa_gdps) if china_gdp >= 0.8 * usa_gdp), None)

# Plot the GDP per capita
plt.figure(figsize=(12, 8))
plt.plot(years, usa_gdps, label='USA GDP per Capita')
plt.plot(years, china_gdps, label='China GDP per Capita')
plt.axhline(y=0.8 * usa_gdps[-1], color='grey', linestyle='--', label='80% of USA GDP per Capita in 2100')
plt.axvline(x=eighty_percent_years, color='orange', linestyle='--', label=f'Year China reaches 80% of USA GDP per Capita: {eighty_percent_years}')
plt.yscale('log')  # Proportional scale (logarithmic)
plt.xlabel('Year')
plt.ylabel('GDP per Capita (log scale)')
plt.title('Projected GDP per Capita (USA vs China) 2022-2100')
plt.legend()
plt.grid(True)
plt.show()

eighty_percent_years
