<img src="assets/logo.png" alt="talentwunder" width="500" align="middle"/>

## Data Analyst - _Assignment_

Thank you for showing interest in Talentwunder and for wanting to be part of 
Talentwunder's Data Team.

This assignment is a chance for you to showcase your technical skills, your 
creativity as well as your business sense. We hope it will form a good base for 
further discussions in the interview process.

### Rules
#### How much time do I have?
We value your time and so should you. Please post your solutions in **7 days** from 
receiving the task.
#### How much time should I spent on the tasks?
The assignment should not take longer then **6 hours total**. However, Time is 
somtimes hard to find. If you had less time at hand, please tell us. We try to 
account for it when assessing your solutions.
#### How should I post my solutions?
The easiest would be to fork this repository and commit your solutions to your 
fork. Please detail instructions on how to execute your solutions. If you use 
_jupyter_ notebooks or similar, document your thought process in respective 
markdown fields. If you develop your own reusable python code in python 
scripts, we consider it a plus.
#### Need any more clarification?
If you still have some questions regarding the assignment, please reply to the 
email we send the assignment in, or contact us directly: 
**career@talentwunder.com**


---
# 1.  Programming Language Statistics
The marketing team of Talentwunder wants to write a blog post on one of our
supported networks '_GitHub_'. They want to educate our users on the types of 
candidates present at _GitHub_. To this end, they would like to show 
statistics on the programming languages that are used by the _GitHub_ users. 

### 1.1 Data 
For the purpose of this coding challenge, we have sampled a small portion of 
our _GitHub_ profiles, which are stored in a JSONL. To obtain this file, please
extract `data/github_profiles_samples.zip`. The resulting 
`github_profiles_samples.jsonl` contains one JSON object per line, which 
corresponds to one _GitHub_ profile each. The profiels have the following
structure:

    _id: unique identify used by the database
    repos: [
        # A list of objects, with structure:
        name: name of the github repo
        stars: number of stars given to this repository
        forks: number of repositories forking from this repository
        commitCount: number of commits pushed for this repository
        contributors: Number of programmers contributing to the code in addition to the creator/author of the repository
        isFork: indicates if this repo is a fork of another
        languages: [
            # A list of objects, with structure:
            name: name of the programming language
            percentage: GitHubs estimate of how much code was written in the corresponding language
        ]
        lastUpdated: Object holding the date when the repository was last updated
    ]
    activity: 
        visitFreqLast90Days: Statistic reported by GitHub how often the user has logged in in the last 90 days.
        numContributionsLast365Days: Statistic reported by GitHub how much commits have been pushed in the last year.

### 1.2 Tasks
1. Parse the programming languages per profile from the provided file `github_profiles_samples.jsonl`
2. Compute and visualize statistics on the programming languages, that you would deem useful for our marketing team. E.g.:
   - most frequent programming languages
   - mean number of profiles/candidates per language
   - most frequent combination of programming languages
   - programming language pair correlations
   - ... make your own decision! You do not need chose any statistic suggested here.
3. **Bonus**: Can you think of a method to group _GitHub_ profiles by their programming languages? For example to distinguish frontend/web developers from backend developers, data scientist, and so on. _No implementation required!_
____
# 2. Proficiency Measure

Talentwunder is gathering the data of millions of potential candidates 
from all over the web. At the same time, we try to make it easy for our users 
to interpret the massive amount of data that we end up with. For example, we 
would like to help our customers in assessing the proficiency level of a 
candidate at a programming language based on his _GitHub_ profile.

### 2.1 Data

See data description (1.1) of the first task "_Programming Language Statistics_"

### 2.2 Tasks
1. Come up with a measure/statistic that approximates the proficiency of a candidate in a specific programming langauge. Proficiency to our users could mean anything from years using the programming language to simply count how much code has been written. Keep in mind your time constraint and settle for some reasonable approach. **Bonus**: If you have a more intricate approach, feel free to outline that. (_No implementation required_)
2. Implement a function that consumes a _GitHub_ profile and returns your proficiency measure per language
3. **Bonus**: Wrap the function in a python script that can be called from command line.

----
# 3. _GitHub_ Brainstorming

Based on your own knowledge and what you have done so far: **Can you think of 
other ways you can use the provided data?** Pick one idea that you have, 
preferably from the following domains:
- Data visualizations and story telling for marketing
- Profile enrichment, helping users understand and assess the candidate behind the _GitHub_ profile
- Insights about our data for the purpose of business intelligence or job-market insights