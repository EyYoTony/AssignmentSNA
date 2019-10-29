# AssignmentSNA

## Deliverable 1

You can find the results of the email extraction in the `finalData.txt` file in the `Deliverable 1` folder

I played around with the github api and the git log command for getting the committer's emails. I ended up going with the `git log` command as you could easily specify to only return the commiters email and the command could easily be used in a .sh script.

### How to recreate the data
Start by cloning the repo as a new folder in the same directory as the `getCommitters.sh` file

`git clone https://github.com/eclipse/che/tree/master`

Then compile and run the shell script to get a file called `emails.txt`

`chmod u+x getCommitters.sh`

`getCommitters.sh`

Then we will format this data with the `removeDuplicates.py` and `createPairs.py` scripts

The script `removeDuplicates.py` takes the txt file `emails.txt` and outputs the file `nodupe.txt`

The script `createPairs.py` takes the txt file `nodupe.txt` and outputs the file `finalData.txt`

I ran these scripts through the PyCharm IDE

The only problem with collecting the emails through this method is that the git log might only see the commits made on the master branch or branches that were merged with master. I'm unsure if this is actually the case, but this could lead to a dataset different from others.

## Deliverable 2

I was able to create a graph with the data collected in deliverable 1, which can be seen here:

[<img src="https://i.imgur.com/q7XRNdn.png">](https://i.imgur.com/)

As you can see there is a limit in the query, this is because there were too many edges and vertices to be able to view them all without the webapp breaking.

Also these edges are meant to be undirected, but Neo4j only has directed edges. So I had to go back to Deliverable 1 and create a new `finalData.txt` which each edge has a reversed edge to simulate an undirected graph.

### How to recreate the database/graph

First you will need a local Neoj4 database running on your machine to be able to run the python script `py2neoGraph.py`

This script takes the pairs from the txt file `finalData.txt` and adds all the nodes and pairs to the database

All the rest can be done in the local database webapp with queries.

## Deliverable 3

For this section I decided to use the library 'networkx' as it had built in functions to find the closeness, betweenness, and degree centrality.

I was unable to get the visualisation of the graph working, but since I only needed the values of the the different centrality this was not a problem.

I got on output like this in the form of a `centrality.csv` file:
>mario.loriedo@gmail.com,1.2,0.005058314202344416,0.7142857142857143

>fbenoit@redhat.com,1.6,0.036381762373363165,0.8333333333333334

>noreply@github.com,1.9764705882352942,0.14573172411318136,0.9883720930232558

>rhopp@redhat.com,0.3764705882352941,0.00045001986580088413,0.5483870967741935

>monaka@monami-ya.jp,0.611764705882353,0.003958784561676397,0.5902777777777778

>amisevsk@redhat.com,0.9647058823529412,0.003370520282115119,0.6589147286821705

### How to recreate the centrality.csv file

just run the `findCentrality.py` file within the same folder as the `finalData.txt` file from Deliverable 1
