# Python Project: Daily Weather City Comparison Using Matplotlib
This project compares two cities and their daily high and low temperatures by extracting each city's weather data from CSV files.

# Dependencies
## Matplotlib:
```
$ python -m pip install pip
$ python -m pip install -U matplotlib
```

# Notes:
* It is best to download each city data of the same year for a better graph display.
* The website used to download the CSV files utilizes an "Add to Cart" feature but downloading data is entirely free.


# Instructions:
* Copy and paste the code from "compare_weather_csv.py" into your development environment.

The CSV files are retrieved from https://www.ncdc.noaa.gov/cdo-web/search.
## How to download files:
In the dropdown menus, select the following:

__Select Weather Observation Type/Dataset__: Daily Summaries
__Select Date Range__: _This should be a year's worth of data (Example: 2020-01-01 to 2020-12-31). This should match for both cities._
__Search for__: Cities
__Enter a Search Term__: _City you want data for_

* In the results, click on "View Full Details" for the desired city.
* Select "Station List" in the left panel.
* Sort the table so that "Coverage" shows 100% first.
    * Note that "Coverage" percentage signifies completeness of data so selecting a station with 100% (or as close to) is ideal.
* From here, find a station that has a "Start" and "End" that includes your date range.
    * (Using the date range above, a station with "Start" = 1992-02-12 and "End" = 2024-10-29 would include your desired date range.)
* Click on "Add to Cart".
* In the top right highlighted in orange, hover over your cart and select "View All Items".
* The "Select the Output Format" should be: Custom GHCN-Daily CSV.
* Date Range should automatically be the date range you inputted initially.
* Click "Continue".
* On the Custom Options page, ensure "Station Name" is checked.
    * In the "Select data types for custom output", check "Air Temperature".
* Click "Continue".
* On the Review Order page, enter your email address and click "Submit Order".
* You will receive an email containing the requested CSV file.
* Download the file and move it to the same directory of where you copied and pasted the "compare_weather_csv.py" file.
* Repeat the above steps for the second city you want to compare the first city with.
* Run the code from "compare_weather_csv.py".
* When prompted, enter the file names.
    * To get the file names, right-click the file in your development environment and click on either "Copy Path" or "Copy Relative Path" for each file.


