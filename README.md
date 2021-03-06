# Final Project Proposals & Reports

## Code for final projects

https://github.com/carissableker/Reddit_Analysis




## Output format

The project will explore one or more of the themes covered in the course that students find particularly compelling. The group needs to submit a project proposal (1.5-2 pages IEEE format) approximately 1.5 months before the end of term. The proposal should provide

   1. a brief motivation of the project,
   1. detailed discussion of the data that will be obtained or used in the project,
   1. a time-line of milestones, and
   1. expected outcome.

At the end of the semester each project will be presented in class: see schedule.

Project report (approximately 4 pages IEEE format) will be due on the last day of classes. 
The format will be similar to the proposal but with emphasis on the results:

   1. a brief motivation of the project,
   1. a detailed discussion of the context and data
   1. a description of the quantitative method used to analyze data
   1. a description of the results
   1. related work, limitations, issues encountered
   1. future work, and conclusions


# Final project teasers

## GroupMe and Discord APIs: Please contact Kevin Ye
Using the GroupMe and Discord APIs, pick two chats within a larger group and evaluate how usage differs. Which application do people prefer/use more? Do they post different kind of content? Do people use the applications at different times?

## Reddit social interactions analysis. Please contact Carissa Bleker & Ashley Cliff

We plan to scrape reddit posts and comments and analysis user interactions with each other and posts. 
Perhaps we can identify elements which generate a lot of activity in the form of upvotes and downvotes. 
We also plan to identify themes and how they might evolve over time. 

Tools:

* [Reddit API](https://github.com/reddit/reddit/wiki/API)
* [The Python Reddit API Wrapper](https://praw.readthedocs.io/en/latest/)

Issues: 
* subreddits to scrape
* time limit to scrape

## Media Vs. Social media correlation pattern discovery. Please contact Gerald Jones

I want to use text analysis to attempt to look for correlations and possible perceivable patterns in relation to the prominent Ideas and 
themes expressed in Main Stream and Independent news sources and what the prominent themes and Ideas trending across social media across 
a predefined time frame (say a few months).I would like to see if the ideas/thems follow social media or vice versa, as well as look for 
differences in major stories that can be noticed through time, and maybe see how well the different news sources stay neutral or who ends
up closer to the truth overall.

## Bitcoin Money Laundering. Please contact Chris Shurtleff
Bitcoin is a pseudo-anonymous cryptocurrency, known for making millionaires of random internet geeks and its association with online drug trafficking. The most interesting feature (for our purposes) of bitcoin is the blockchain: a completely public ledger that records every transaction ever performed, and is updated in real time as new transactions occur. The blockchain represents a public treasure trove of data, ripe for interested data scientist to play with. There are many sites and programs that perform various levels of analysis on the blockchain. My interest, with this project, will be part of an attempt to de-anonymize certain transactions by finding a measure that can determine how related two transactions are.

Bitcoin transactions can be modeled as unidirectional, sparse graphs. This has been done many times before. The goal for this project would be to model bitcoin transactions as a graph, and identify an easy method or tool to measure how related two transactions are. This measure or technique could be useful in identifying money laundering operations, where criminals seek to obscure the 'dirty' source of money to create 'clean' cash for legal uses. A stretch goal for this project would be to create a web scraper designed to look for and identify valid bitcoin addresses online, and associate those with posted identities.

## Gymnastic outcomes. Please contact Kirsten Dawes

I will be investigating Gymnastic outcomes. Using gymnastic competition score to determine base hierarchical structure of top gymnast. Then some correlation and analysis on this heirarctical structure based on gyms rank, age, age based on level, years in each level. Is there a way to predict early on if a gymnast is more likely to get injury or take injury time off , if so what age and what is its relation to score? As well as we can as a few more questions.

Data source: Competition gymnastic site: example usa gymnastics Articles and Website information about known top level gymnasts Video to text data: A Lot of gymnastic competition is stream, and include some information about injuries and breaks from gymnastics. As well as technical aspects that we later could use to help certain injuries.
Social Media Image Analysis
Goal


## Quantify professionalism, interests, and activities based on individual's images on social media. Contact Paine Leffler
Reasoning

   - Tedious to look through a large amount of images.
   - Can be subjective.
   - Could help fit individuals on teams based on similar interests.
   - Could help individuals analyze their public web presence.

Tools & Data sources

   - Google's Cloud Vision API https://cloud.google.com/vision/
   - LinkedIn API
   - Instagram API
   - Facebook API
   - Twitter API

Stretch goal

   - Compare individuals' images to get a compatibility score / visualization.

## Analyze data from libraries.io using TDA: Please contact Jacob Miller at jmill225@vols.utk.edu

Question: Using topological data analysis software, can one determine a way of classifying similar structures of open source software?

What: Topological data analytics is a new field of data analytics which attempts to understand the underlying space that data comes from. It can capitalize from data sources in the form of point clouds or networks to form simplicial complexes. This form of data analytics has been popular in the study of brainwave data. Specifically there is research where the analysis is used on hypocampal brainwave data of lab mice to determine where the mouse is located within an arena.

How: Possibly relying on the network structure of open source dependencies, we could create simplicial complexes using something like the "nearest-neighbor" filtration. With this new encoding of the data, we can use available software to find the zigzag persistant homology of the system.

- An introduction to TDA by one of its founders:

[![IMAGE ALT TEXT](http://img.youtube.com/vi/XfWibrh6stw/0.jpg)](http://www.youtube.com/watch?v=XfWibrh6stw "Introduction to Topological Data Analysis")


Further ideas are encouraged. 

## Startup Analytics Idea: Contact Luke Mills

Every year there are myriad new startups launched. These span numerous industries, with a greater number failing than suceeding.

This project will analyze startup data such as industry, location, and other parameters to see if there is any correlation between these factors and success.
    
The crunchbase API will be used to obtain necessary data.

## Retrieve and fix missing/incorrect metadata on Music or Video Media Files: Contact Axel Hranov

-Provide a file with missing/incorrect metadata
-Have user provide optional additional search suggestions
-Crawl public metadata databases and search for song/movie/show/etc. and udpdate metadata if found
-Possibly maintain seperate database for files that do not exist in other DBs.

### Lightweight Tool for Retrieval of Optimal Settings/Modification of PC games (Pulled from PCGamingWiki)

-Small program that can be run that asks for a game name (or detects what game is being run through Steam API)
-Search PCGamingWiki.com for the game, and collects the standardized and nonstandardized information
-Organize and display information in single screen format
-Provide hyperlinks to the folders containing the save files/ini files/etc. (No need to manually go through file explorer)

### DeepDream Video Converter (DeepDream Batch Handler)

-Input a video/gif/WEBM file
-User can choose several different parameters to determine DeepDream algorithm
-Interperet individual frames and feed each one into DeepDream
-Replace the frame with the new frame generated
-Output new file to desired filename
-Result is trippy, crazy version of input video.
-Example of Video Ran through Deep Dream

### JanusVR Web Crawler

-JanusVR is a platform that allows visual representations of web pages -Each web page is an enviroment and allows any sort of user-generated content to be displayed -Users can explore the webspaces, and travel through portal (link) to other sites. -Develop Crawler to map out the JanusWeb and allow users to choose an insertion point

## How do political donations affect policy decisions?  Contact Denizhan Pak

Opensecrets.org provides a list of donations made to US politicians and the policies they have sponsored, co-sponsored or signed. I want to do a text analysis comparing the donating groups by field of interest to policies that relate to the regulation of that field, to see if there is a relationship between the policy and the donations.


## Correlation between Pitchfork review scores and Pitchfork Metadata (Contact J.T. Liso at gliso@vols.utk.edu)
 - Scrape data from Pitchfork (https://github.com/nolanbconaway/pitchfork-data.git)
 - Discover if certain artists are unproportionally rated low or high scores
 - Find correlation between certain scores and words within a review
 - Discover if certain reviewers tend to review high or low scores (or use certain words)
 - Is there a certain time of the week/year that gets high or low scores?
 - Perhaps compare Pitchfork reviews to social media mentions, sales, or stream frequencies

## Search for code clones
   https://www.itwire.com/security/79504-researchers-find-marcus-hutchins-code-that-was-used-in-malware.html
   https://github.com/MalwareTech/BasicHook/blob/master/BasicHook/hook.cpp#L77
   
## Help software heritage by writing a new lister for your favorite forge
   https://www.softwareheritage.org/2017/03/24/list-the-content-of-your-favorite-forge-in-just-a-few-steps/


## Help identify critical open source infrastructure by analyzing data from libraries.io 
There are three problems:

- Identify critical infrastructure: the free and open source
  software contributed as a public good that underpins much of
  today's technology 


- Identify unseen infrastructure: open source libraries that are
  heavily depended upon by the community but don't receive much
  recognition or attention. 

- Identify ecosystem Bus factor: the number of key developers who
  would need to be incapacitated to make a project unable to
  proceed. 

- Distribution of developers over developed/developing countries https://motherboard.vice.com/en_us/article/neekm8/coders-in-wealthy-and-developing-countries-lean-on-different-programming-languages

- What are the companies behind the various open source projects?http://www.zdnet.com/article/open-source-professionals-are-more-in-demand-than-ever/

- Can we find systematic differences in the online discussions: https://medium.com/@amuse/how-the-nsa-caught-satoshi-nakamoto-868affcef595

- 

- Data: Libraries.io-open-data-1.0.1.zip
   - projects: > 2M
   - dependencies
   - statistics


## Forensic database of images

In this project, you will learn to apply machine learning techniques
to images. OpenCV is the recommended tool and Python is the
recommended programming language. You may also use other machine
learning models, such as deep learning if you can get high
performance. The project has two milestone objectives – image
classification and object detection. 

- Problem 1 – Image Classification

You will be given a dataset - “body” which contains annotated
sub-images of body parts, including ear, eye, hair, head, left foot,
and mouth. These labeled sub-images will serve as the ground
truth. The problem is as follows, can you provide a machine learning
algorithm to automatically label new sub-images? Here are a few tips
using OpenCV. 
For each image, you will be able to extract keypoints representing
high-level features. Read through ORB (Oriented FAST and Rotated
BRIEF) and Feature Matching to get some ideas. Then you need to try
out classifying the sub-images based on the detected keypoints. Note
that each image may have a different number of keypoints and
different keypoints may represent different features. Binary
classification, for instance, left foot vs. eye AND left foot
vs. others, are desired. Ten-fold cross-validation could be used to
measure and improve the model performance. Finally, you need to
write up the algorithm, chosen parameters, and classification
performance (i.e., mean and std of accuracy). 

- Problem 2 – Object Detection

In the Problem 1, you are given the annotated sub-images. The harder
problem would be, how can you detect the body parts from the full
images, which may contain multiple body parts? Note that when you
detect left foot, only some of the full images contain this body
part. Same with the other body parts. 

This problem contains two image datasets. One is exactly the one
used in Problem 1, another is the dataset of the full images -
“images”. Moreover, the two datasets are connected via the file
“tags.csv”. In the CSV file, the column “ID” contains the
sub-images’ names, the column “tag” gives the tag of each sub-image,
and the column “Image” tells which full image the sub-image is
from. 
There are several ideas to solve this problem. One idea is that you
can split the full image into several (i.e., 3 * 4) sub-images and
classify the sub-images based on the model you train when solving
Problem 1.  Another idea is that the full image should contain left
foot if it contains sufficiently many similar keypoints from the
annotated left foot sub-images.

## What is the population of developers, what is the distribution of skills?
  - http://coderwall.com/{username}.json
  - Type in google search: "scraping linkedin python"
  - https://www.scrapehero.com/tutorial-scraping-linkedin-for-public-company-data/
  - https://www.fullcontact.com/developer/docs/ (limits to 100 names per month)
  - https://github.com/blackducksoftware/ohloh_api/blob/master/examples/account_sample.py


## Relationship among OSS projects

* When a project A depends on another project B, what factors predict how quickly A's code actually makes use of new methods/classes/etc. of B? Some possible factors include number of shared developers, shared membership in organizations, prior collaboration of devs from A and from B, same country or time zone, past update schedules of A and B.

* Compare across multiple ecosystems to see if there are significant differences in practices like:
    * release frequency; frequency of breaking changes (assuming semver)
    * backporting (Hannah has already done this for npm)
    * dependency freshness (how long until downstream projects update dependency versions)
    * number of automatic updates due to wildcards

A survey of ecosystem values (data at https://doi.org/10.1184/R1/5108716, context at http://breakingapis.org/survey) to see whether ecosystem values have an additional influence and can explain differences among ecosystems.

* Dig into the git repositories and look for release notes or changes to documentation or detect things like deprecating methods. Perhaps apply an automated documentation generation tool to extract the public methods (doxygen works for a number of languages, there are others) and perform a structured diff to see how often public methods are introduced, removed, or signatures are changed.

## ECG data
https://physionet.org/challenge/2017/

The 2017 PhysioNet/CinC Challenge aims to encourage the development
of algorithms to classify, from a single short ECG lead recording
(between 30 s and 60 s in length), whether the recording shows
normal sinus rhythm, atrial fibrillation (AF), an alternative
rhythm, or is too noisy to be classified. 

ECG recordings, collected using the AliveCor device, were generously
donated for this Challenge by AliveCor. The training set contains
8,528 single lead ECG recordings lasting from 9 s to just over 60 s
(see Table 2) and the test set contains 3,658 ECG recordings of
similar lengths. The test set is unavailable to the public and will
remain private for the purpose of scoring for the duration of the
Challenge and for some period afterwards. 

ECG recordings were sampled as 300 Hz and they have been band pass
filtered by the AliveCor device. All data are provided in MATLAB V4
WFDB-compliant format (each including a .mat file containing the ECG
and a .hea file containing the waveform information). More details
of the training set can be seen in Table 2. Figure 1 shows the
examples of the ECG waveforms (lasting for 20 s) for the four
classes in this Challenge. From top to bottom, they are ECG
waveforms of normal rhythm, AF rhythm, other rhythm and noisy
recordings.

