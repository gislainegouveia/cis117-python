
# CIS-117 Lab3
# This program reads a CSV file containing country information
# and creates separate CSV files for each region.
# Student Name: Gislaine Pires  
# Group #: Individual - Gislaine Pires
# Collaboration: I completed this assignment individually.


import csv


def main():

    try:
        # Open the original CSV file
        with open("country_full.csv", "r", newline="", encoding="utf-8-sig") as input_file:

            reader = csv.DictReader(input_file)

            # Dictionary to store countries by region
            regions = {}

            # Read each country from the CSV file
            for row in reader:

                country = row["name"]
                region = row["region"]

                # Skip countries without a region
                if not region:
                    continue

                # Add country to its region
                if region not in regions:
                    regions[region] = []

                regions[region].append([country, region])

        # Create one file for each region
        for region, countries in regions.items():

            filename = region + ".CSV"

            try:
                with open(filename, "w", newline="", encoding="utf-8") as output_file:

                    writer = csv.writer(output_file)

                    # Write column headings
                    writer.writerow(["Country", "Region"])

                    # Write country information
                    writer.writerows(countries)

                print(filename + " created successfully!")

            except PermissionError:
                print("Permission denied when creating " + filename)

            except IOError as error:
                print("Error writing file:", error)

    except FileNotFoundError:
        print("Error: country_full.csv was not found.")

    except PermissionError:
        print("Error: You do not have permission to read the file.")

    except IOError as error:
        print("An error occurred while reading the file:", error)

    except KeyError as error:
        print("A required column was not found:", error)

    except csv.Error as error:
        print("CSV file error:", error)


if __name__ == "__main__":
    main()
