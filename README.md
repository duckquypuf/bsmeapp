# Step 1: Clone the repo (do this once per project)
$ git clone https://github.com/duckquypuf/bsmeapp.git
$ cd bsmeapp                    # Go into the folder

# Before you start working, pull the latest
$ git pull origin main

# Or if you're on a feature branch, pull that branch
$ git pull origin my-feature

# Step 2: Create your feature branch
$ git checkout -b my-feature      # Creates branch and switches to it

# Step 3: Make edits in your code editor (not terminal)
# [You edit files.js in VS Code or your editor]

# Step 4: Commit your work
$ git add .                       # Stage all changes
$ git commit -m "add login form"  # Save locally

# Step 5: Push to GitHub
$ git push origin my-feature      # Upload your branch

# Step 6: Checkout to main
$ git checkout main

# Step 7: Delete a branch (locally) once you have merged it
$ git branch -d my-feature

# To force delete of branch if not merged off computer
$ git branch -D my-feature

# Step 8: Delete a branch (off github) once you have merged it
$ git push origin --delete my-feature

# Step 9: Pull latest
git pull origin main