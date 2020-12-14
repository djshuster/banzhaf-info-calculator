# What Is It?
<img src="Images/vote-pic.png" alt="silhouette of voting" width="40%" height="40%" align="right" style="float:right; padding-left:20px"/>
The Banzhaf power index of a given voter is a metric of the voter's power in a weighted voting system, where some quota must be reached to pass a motion. For instance, in a parliamentary democracy, different parties may form voting blocs, towards approving a prime minister nominee by strict majority. For more information on the Banzhaf index, check out Chapter 8 of _The Mathematics of Voting and Elections: a Hands-On Approach_, American Mathematical Society, 2018, by Jonathan K. Hodge and Richard E. Klima, or you can just read the [Wikipedia article](https://en.wikipedia.org/wiki/Banzhaf_power_index).

By examining a party's Banzhaf index and comparing it to the number of votes given to those parties in their election into parliament, we can measure how much power a given individual voter is effectively getting by voting for a party.

# How Do I Use It?
You will want to run banzhaf_info.py. This program takes in data from electionData.csv and outputs the "Ratio of Banzhaf Index to Fraction of Vote" for each party in results.csv.
The current use focuses on the Israeli Parliamentary ("Knesset") election from March 2020 with respect to the approval of a prime minister nominee, which requires 61/120 votes.

To use this program for a different election, follow these 3 steps:

(1) Change the electionsData.csv file to reflect the information from the new election. Note that only columns A, C, and D are necessary.

(2) The default quota is 61. To use a different quota, enter the new quota as a whole number in the command line when running the program. For example "py banzhaf_info.py 90" will set the quota to 90.

(3) After running the program, in results.csv, change the column A header to the appropriate political bodies' title.

# Data Sources
Data for the specific example election is taken from https://knesset.gov.il/description/eng/eng_mimshal_res23.htm.

Other years for the Knesset can be found at https://main.knesset.gov.il/EN/mk/Pages/Elections.aspx.

# Contact Me
Did you encounter a bug in my application? Do you want to request a new feature? Have a funny meme for me? Feel free to email me at djs.shuster@gmail.com.

# Acknowledgements
My gratitude to Professor Tanya Leise for teaching me much about the mathematics behind voting systems and sparking my interest in the topic!
