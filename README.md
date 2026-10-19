# GitHub Workflow Guide

A step-by-step guide for collaborating with your team using Git and GitHub.

---

## Step 1: Clone the Repository

Clone the repo once per project. This downloads everything from GitHub to your machine.

```bash
git clone https://github.com/duckquypuf/bsmeapp.git
cd bsmeapp
```

---

## Step 2: Pull the Latest

Before you start working, grab the latest code from `main` branch.

```bash
git pull origin main
```

---

## Step 3: Create Your Feature Branch

Create a new branch with a descriptive name. You'll work on this branch, not on `main`.

```bash
git checkout -b my-feature
```

Replace `my-feature` with something like `add-login-form` or `fix-navbar`.

---

## Step 4: Make Your Changes

Edit your files in VS Code (or your editor). Make changes, test locally, and repeat.

*(This happens outside the terminal)*

---

## Step 5: Commit Your Work

Stage and commit your changes regularly. Good commits = good history.

```bash
git add .
git commit -m "add login form"
```

Write clear commit messages. Use present tense: "add feature" not "added feature".

---

## Step 6: Push to GitHub

Upload your branch to GitHub so your team can see it.

```bash
git push origin my-feature
```

---

## Step 7: Create a Pull Request

Go to GitHub.com and create a Pull Request (PR). Describe what you changed. Your team will review it.

Once approved, merge it on GitHub.

---

## Step 8: Switch Back to Main

After merging on GitHub, switch back to your `main` branch locally.

```bash
git checkout main
```

---

## Step 9: Pull Latest Changes

Pull the merged code into your local `main`.

```bash
git pull origin main
```

---

## Step 10: Delete Your Branch (Locally)

Clean up by deleting the feature branch from your machine.

```bash
git branch -d my-feature
```

**Force delete** (if not merged):
```bash
git branch -D my-feature
```

---

## Step 11: Delete Your Branch (Remote)

Delete the branch from GitHub.

```bash
git push origin --delete my-feature
```

You can also click the "Delete branch" button on GitHub after merging.

---

## Quick Reference

| Command | What it does |
|---------|-------------|
| `git clone <url>` | Download repo for first time |
| `git pull origin main` | Get latest from GitHub |
| `git checkout -b my-feature` | Create and switch to new branch |
| `git add .` | Stage all changes |
| `git commit -m "message"` | Save changes locally |
| `git push origin my-feature` | Upload branch to GitHub |
| `git checkout main` | Switch to main branch |
| `git branch -d my-feature` | Delete local branch |
| `git push origin --delete my-feature` | Delete remote branch |

---

## Tips

- **Always pull before starting work** to avoid conflicts
- **Commit often** with clear messages
- **Use descriptive branch names**: `add-login`, `fix-bug-navbar`, `update-docs`
- **One feature per branch** (don't mix unrelated changes)
- **Delete branches after merging** to keep the repo clean

---

## Getting Help

If something goes wrong:
- `git status` — see what branch you're on and what files changed
- `git log` — see commit history
- `git diff` — see exactly what changed in your files