# Election Analysis

## Overview of Election Audit

In this analysis, we are working with two Colorado Board of Elections employees, Tom and his manager, Seth, in
an effort to conduct an audit of the election results for their precinct. Historically, this process has been
completed in Excel, however Seth hopes that the process can be automated. In light of this, we will be using 
Python, to write a code that will read the provided election data and provide the needed election statistics
and data points required.

### Purpose

The purpose of this project will be to create a Python code that will automate the election audit process. A
successful implementation of this code can then be used to conduct audits of other election precints and 
other local and state races.

## Election Audit Results

Using the Python code created, we can confirm that:

- 369,711 total votes were cast in this congressional election.

- by county, the election results are as follows;

![This is an image](https://github.com/jstawarz/jstawarz/election-analysis/blob/main/Resources/County_Votes.png)

- with 306, 055 votes, Denver county had the largest number of votes.

- by candidate, the election results are as follows;

![This is an image](https://github.com/jstawarz/election-analysis/blob/main/Resources/Candidate%20_votes.png)

- overall, Diana DeGette won the election.

![This is an image](https://github.com/jstawarz/election-analysis/blob/main/Resources/Winner.png)


## Election Audit Summary

In summary, the Python code created confirmed the election results with the dataset provided. In the future
this code can be recycled, built upon, and modified to automate the election audit process to quickly verify
election results. 

One example would be that With a few small modifications, the code can be updated to be used in local elections.
In this instance, by changing the county variables to wards, say if used in a city-wide election, and updating
the row references to match the data, we could track the votes cast in each city district. 

A second example could be to exapnd the data show by the code. If we were interested in confirming the results
of say, a congressional race and a senatorial race, we could update the varibales to reflect congressional
candidates and senate candidates, as well as congressional and senate vote countes then following the template
already created in the code, create a new for loop to read the senate results as well as the congressional results. 


