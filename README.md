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

The only problem with collecting the emails through this method is that the git log might only sees the commits made on the master branch or branches that were merged with master. I'm unsure if this is actually the case, but this could lead to a dataset different from others.

## Deliverable 2

>TODO

## Deliverable 3

>TODO
