# Step 1: Clone the repo (do this once per project)
$ git clone https://github.com/duckquypuf/bsmeapp.git
$ cd bsmeapp                    # Go into the folder

# Step 2: Pull the latest from main
$ git pull origin main

# Step 3: Create your feature branch
$ git checkout -b my-feature    # Creates branch and switches to it

# Step 4: Make edits in your code editor (not terminal)
# [You edit files.js in VS Code or your editor]

# Step 5: Commit your work
$ git add .                     # Stage all changes
$ git commit -m "add login form"  # Save locally

# Step 6: Push to GitHub
$ git push origin my-feature    # Upload your branch

# Step 7: Create PR on GitHub, get reviewed, then merge

# Step 8: Switch back to main
$ git checkout main

# Step 9: Pull latest (includes your merged changes)
$ git pull origin main

# Step 10: Delete the branch locally
$ git branch -d my-feature

# (To force delete if not merged)
$ git branch -D my-feature

# Step 11: Delete the branch on GitHub
$ git push origin --delete my-feature