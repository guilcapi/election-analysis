# Election Analysis

## Overview of Election Audit
A Colorado Board of Elections employee has given me the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of counties who sent in votes.
3. Calculate the total number of votes each county sent in.
4. Calculate the percentage of votes from the total each county sent in.
5. Call out which county had the largest turnout.
6. Get a complete list of candidates who received votes.
7. Calculate the total number of votes each candidate received.
8. Calculate the percentage of votes each candidate won.
9. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Election-Audit Results
The text file image shown here summarizes the data provided:

![](/Resources/Election_Summary.png)

The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The county results were:
    - Jefferson received 10.5% of the vote and 38,855 number of votes.
    - Denver received 82.8% of the vote and 306,055 number of votes.
    - Arapahoe received 6.7% of the vote and 24,801 number of votes
- The county with the largest number of votes was Denver.
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
    - Diana DeGette who received 73.8% of the vote and 272,892 number of votes.

## Election-Audit Summary
This script was written to run through a list of ballots for candidates running for office. This script could be used for other applications with some modifications for any election that also need total counts of categories, percentage breakdowns, and declaration of a winner. This script could also be modified to include other breakdowns such as how specific groups voted such as in this case, a breakdown of candidate votes for each county. This script could also be rewritten to read from other formats other than .csv files. 
