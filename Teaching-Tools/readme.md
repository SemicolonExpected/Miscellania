## crossreferenceFormToRoster.py

Cross references students' unique id numbers to unique ids submitted onto csv files generated from forms. 
Run using:

    crossreferenceFormToRoster.py <rosterfile> <formfilename> [colnumber] -maxteamsize [int]

`colnumber` corresponds to which column the ids are in 
`-maxteamsize` denotes what the max amount of people in a team would be. It's default value is 1 (which assumes everyone submits their form individually) The purpose of this was to decrease run time in case of large forms which is why the default is a low number. If you instead prefer it to check each form row regardless just set the default to some arbitrarily high number.

I wonder if joining all the rows of the form file together and then checking if each id is a substring of the big form is a better way of solving. Can someone try that and benchmark, or if someone has knowledge of how the membership function `in` works in python can explain if it is better and why, that would be great.