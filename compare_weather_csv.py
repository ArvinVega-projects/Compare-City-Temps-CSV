# Compare daily highs/low of two cities.
from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

class WeatherData:
    """Represents weather data that we will plot."""
    def __init__(self, path_1, path_2):
        """Initialize attributes of our weather data."""
        self.path_1 = Path(path_1)
        self.path_2 = Path(path_2)
        self.lines_1 = self.path_1.read_text().splitlines()
        self.lines_2 = self.path_2.read_text().splitlines()
        
        self.reader_1 = csv.reader(self.lines_1)
        self.reader_2 = csv.reader(self.lines_2)

        # Assign header row values of each file to a variable.
        self.header_row_1 = next(self.reader_1)
        self.header_row_2 = next(self.reader_2)

        # Create empty lists for each data set we will plot.
        self.dates_1 = []
        self.dates_2 = []

        self.highs_1 = []
        self.highs_2 = []

        self.lows_1 = []
        self.lows_2 = []


    def plot_data(self):
        """
        Extract data from each file,
        append to corresponding list,
        and plot on graph."""
        # Extract the indexes of data we need to compare.
        # Use try-except block for following:
        # File names are found but not the right data in one or both files.
        try:
            dates_index_1 = self.header_row_1.index("DATE")
        except ValueError:
            print("Incorrect data provided in file(s).")
            print("Please double check the data is valid in both files.")
            exit()
        else:
            highs_index_1 = self.header_row_1.index("TMAX")
            lows_index_1 = self.header_row_1.index("TMIN")
            name_index_1 = self.header_row_1.index("NAME")

            dates_index_2 = self.header_row_2.index("DATE")
            highs_index_2 = self.header_row_2.index("TMAX")
            lows_index_2 = self.header_row_2.index("TMIN")
            name_index_2 = self.header_row_2.index("NAME")

        # Read through every row of each file to extract needed data.
        for row in self.reader_1:
            place_name_1 = row[name_index_1]
            date = datetime.strptime(row[dates_index_1], "%Y-%m-%d")
            year_1 = date.year
            # Some TMAX and/or TMIN rows have missing data.
            # Use ValueError exception in these cases.
            try:
                high = int(row[highs_index_1])
                low = int(row[lows_index_1])
            except ValueError:
                print(f"{place_name_1} is missing data for {date}.")
            else:
                # Append each data point to corresponding list.
                self.dates_1.append(date)
                self.highs_1.append(high)
                self.lows_1.append(low)
        
        for row in self.reader_2:
            place_name_2 = row[name_index_2]
            date = datetime.strptime(row[dates_index_2], "%Y-%m-%d")
            year_2 = date.year
            try:
                high = int(row[highs_index_2])
                low = int(row[lows_index_2])
            except ValueError:
                print(f"{place_name_2} is missing data for {date}.")
            else:
                self.dates_2.append(date)
                self.highs_2.append(high)
                self.lows_2.append(low)

        # We need to check that the files aren't dupes.
        # We will compare the entirety of highs_1 to highs_2
        if self.highs_1 == self.highs_2:
            print("Duplicate data found.")
            print("Please ensure that each provided file has different data.")
            exit()
        
        # Plot the extracted data.
        plt.style.use('seaborn-v0_8')
        fig, ax = plt.subplots()

        ax.plot(self.dates_1, self.highs_1, color='red', alpha=0.9)
        ax.plot(self.dates_1, self.lows_1, color='blue', alpha=0.9)
        fill_1 =ax.fill_between(self.dates_1, self.highs_1, self.lows_1,
                        facecolor='purple', alpha=0.9, label=place_name_1)

        ax.plot(self.dates_2, self.highs_2, color='red', alpha=0.3)
        ax.plot(self.dates_2, self.lows_2, color='blue', alpha=0.3)
        fill_2 = ax.fill_between(self.dates_2, self.highs_2, self.lows_2,
                        facecolor='green', alpha=0.3, label=place_name_2)
        
        # Set position of legend.
        ax.legend(handles=[fill_1, fill_2], loc=4)

        # Add title with city names, format date labels.
        # Set title and label sizes.
        title = "Daily Highs and Lows"
        title += f"\n{place_name_1}, {year_1} and {place_name_2}, {year_2}"
        ax.set_title(title, fontsize=16)
        ax.set_xlabel("", fontsize=14)
        fig.autofmt_xdate() # Ensure the dates on x-ais fit graph.
        ax.set_ylabel("Temperature (F)", fontsize=20)
        ax.tick_params(labelsize=20)

        plt.show()

# Create a child class that takes the initialized parent variables.
# this will be used to catch errors for the following block.
class TestFileNames(WeatherData):
    """Represents file names that will be tested."""
    def __init__(self, path_1, path_2):
        """Initialize attributes of our class."""
        super().__init__(path_1, path_2)

# Use try-except block to raise exception if file name(s) not correct.
try:
    first_file = input("Provide the path name of the first CSV file: ")
    second_file = input("Provide the path name of the second CSV file: ")
    TestFileNames(first_file, second_file)
except FileNotFoundError:
    print("File(s) not found. Please confirm the path name(s) are correct.")
else:
    WeatherData(first_file, second_file).plot_data()
