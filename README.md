# Election_Analysis
## Overview of Election Audit
The purpose of this project was to analyse the data that contained the votes in a specific precint for the colorado board of election. In this analysis we will doa breakdown of the most important information wich is:
- Total votes in the precint.
- The different counties and their total votes and porcentages.
- The largest county.
- The different candidates with theur resoectives total votes and percentages.
- The winner of the election.

### Resources
- **Data Source:** election_results.csv
- **Software:** Python 3.10.0, Visual Studio Code, 1.63.2

## Election-Audit Results
After developing the analysis int eh election data we came to the following results:

- There were a total of 369,711 casted in the congressional election.

- The total votes for each county are:
  - Jefferson had a total of 38,855 votes wich represents a 10.5% of the votes.
  - Denver had a total of 306,055 votes wich is 82.8% of the total votes.
  - Arapahoe had 24,801 votes wich represents the 6.7% of the total votes.
 
- The county with the largest number of votes was Denver.

- There were three candidates in the election which are:
  - Charles Casper Stockham who had 23.0% wich are 85,213 votes.
  - Diana DeGette who had 73.8% wich are 272,892 votes.
  - Rymon Anthiny Doane who had 3.1% wich are 11,606 votes.
 
- The winner of the election is Diana DeeGette with a 73.8% of the total votes wich are 272,892.

<img width="384" alt="Screen Shot 2022-01-09 at 10 11 09 PM" src="https://user-images.githubusercontent.com/95391094/148714314-27d21ba2-d804-4cc5-b78a-f5c0b9ac1167.png">

## Election-Audit Summary
This script is pretty general so it can be reused to get the results of any other election. For example, it can be used for any state election or presidential election or any other kind. Some of the ways it my be edited to be more eficient are:

- Asking the user for an imput: Since in some cases some of the votes are colllected electronically we can prompt the user for the state or cunty where they are from and wich candidate would they like to vote for and save it to a dictionary.
- Comparing the total amount of votes of each year: We can compare how the total votes through the years to evaluate how the voters have been increassing or decreassing and how it may be stimulated in each county.
