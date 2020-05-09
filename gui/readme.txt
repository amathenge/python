Notes for git commands here:

1. initialise git in a folder
git init

2. check on git
git status

3. add files to git - there are many ways to do this
git add filename
git add directory/*
git add file*.ext
git add directory/filename
git add directory/file*.ext

4. stage files = make them ready to update git
git commit -m "my super long comment explaining this update"

5. update github with the files
git push

--------------------------------------------------------
Next, how to get a file from git and update a local copy.

if there's a file in the remote repository that you want to bring back, you type in the
following command:

git fetch -s origin/master path/to/file

example, I have the following file structure

src -+- python -+- file1
     |          |
	 +- java    +- file2
	 |
	 +- mysql
	 
assume that I've deleted "file2" and GIT is tracking from "src"

So, from "src" I can run the following command:

git fetch -s origin/master python/file1

This will bring back file1 from github.com
