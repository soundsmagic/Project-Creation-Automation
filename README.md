# Project-Creation-Automation
Python script for automating the set-up process of a new Python project.

My first Python project! I made this with the goal of learning more about Python, CLI commands and arguments, GIT, and environment variables. And I did! I also made this public with the goal of helping others starting out with these topics.

You need to create two environment variables for this script: "GITHUB_TOKEN" where you store a GitHub access token to use to access your account throught the GitHub API, and "MY_EMAIL" containing the email address you want to use as contact in the Code of Conduct.

You also need node installed to be able to run the "npx" command to fetch the MIT license. If I find time, I'll continue to search for a cleaner solution to this step, but feel free to comment if you have suggestions!

When starting this script, just provide it with one CLI argument: the project name (in quotation marks if you wish it to contain spaces).

As you can see, this script creates the main project folder at "C:\dev\Python Projects". Change this to suit your preferences if they differ from this!

When researching the topic of project creation automation, I found lots of useful information from the following places:
https://realpython.com/python-application-layouts/
https://philna.sh/blog/2019/01/10/how-to-start-a-node-js-project/
https://towardsdatascience.com/all-the-things-you-can-do-with-github-api-and-python-f01790fca131
Lots of Python videos on YouTube by Corey Schafer
David Mahlers YouTube videos on GIT
(stackoverflow...of course)


Future plans for taking this project to the next level include building different project creation processes for different programming languages and adding a CLI argument for choosing language, and functionality for expanding the file and folder structure of an existing project if it outgrows this initial, barebones file structure (see the link to realpython.com for suggestions how to expand the folder structure when a project grows).
