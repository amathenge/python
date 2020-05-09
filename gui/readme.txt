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

--------------------------------------------------------
if you've run <git commit -m "comment"> and you want to see what's waiting to be committed.

You can do this. First run

git show | head -1

This will give you something that looks like this:

	commit 5977301d0896e58f59054732dbd310650d9b2acf (HEAD -> master)
	
Now run 

git diff-tree --no-commit-id --name-only -r 5977301d08

Notice that the string after "-r" are the first 10 characters of the long string in the first
command.

You should now get a list.

I got the following:

--------------------------------------------------------
andrew@MATHENGE MINGW64 ~/Documents/src/python (master)
$ git diff-tree --no-commit-id --name-only -r 5977301d08
url-shortener/app.py
url-shortener/static/user_files/housedovercourt-house.png
url-shortener/static/user_files/yyyoda-sketch.png
url-shortener/templates/home.html
url-shortener/templates/page_not_found.html
url-shortener/templates/your_url.html
url-shortener/urls.json
--------------------------------------------------------

