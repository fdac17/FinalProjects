# Final project teasers

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


