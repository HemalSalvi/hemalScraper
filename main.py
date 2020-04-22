import scraper
scraper.createListCSV("https://www.utdallas.edu/coronavirus/", "covid", 1, "UTDCoronaUpdates.csv")
scraper.createTableCSV("https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/previouscases.html", "Total Cases", 1, "USTable.csv")
scraper.createTableCSV("https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/cases-in-us.html", "15,831", 1, "USDemographics.csv")