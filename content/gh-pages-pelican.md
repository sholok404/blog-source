Title: Hosting Your Pelican Website in Github Pages
Date: 2017-11-06 3:17
Category: Git
Tags: github, github pages, pelican, python, web hosting, git

Hosting Pelican websites can be pretty complicated; there is not a lot
of documentation about it. This is why I am writing this article. Also, I am assuming
you already have built a website using Pelican. Also make sure to delete the output
directory before proceeding.

To get started, create two repositories. One of them should be named `<username>.github.io`.
Name the other one whatever you want. Then add the first repo as the origin of the
root of your project. Use this: `git remote add origin <url-of-repo>`. Replace the part
in '<>'s with your repository's url. Then, add your `<username>.github.io` repository
as a submodule in the output directory. For this, use `git submodule add <url-of-repo> output`.
Then, build your website using `pelican -s pelicanconf.py`.

After that, first add, commit and push all the files to its repository. Then navigate
to the output directory and do the same. You should have your website up and running in
a few minutes.
