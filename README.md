# MEGA Login Automation

This Python script automates the login process to **MEGA** and ensures that it logs in every 30 minutes. Due to recent changes on MEGA's side, the MEGA SDK only works after logging in to `mega.nz/login`, and the session lasts for just 30 minutes. This script was created to address this issue by automatically logging in again after each session expires.

## Direct Deploy [Heroku]
[![Deploy on Heroku](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new-app?template=https://github.com/Hrishi2861/Mega-Login-Automation)

## Features
- Automatically logs in to **MEGA** using your email and password.
- Handles re-login every 30 minutes to maintain the session.
- Simple and easy to use, with all dependencies included.

## Prerequisites

Before deploying to **Heroku**, make sure you have the following buildpacks installed:

- [Heroku Buildpack for ChromeDriver](https://github.com/heroku/heroku-buildpack-chromedriver.git)
- [Heroku Buildpack for Chrome](https://github.com/heroku/heroku-buildpack-chrome-for-testing.git)
- [Heroku Buildpack for Python](https://github.com/heroku/heroku-buildpack-python)


<b>Fill this Values in [config.env](config.env)</b>
- `MEGA_EMAIL`: Your MEGA Email. `Str`
- `MEGA_PASSWORD`: Your MEGA PASSWORD. `Str/Int`
- `MEGA_API`: Your MEGA API, Get it from [Here](https://graph.org/MEGA-API-04-01). `Str`

## Installation (HEROKU)

### 1. Clone the repository:

```bash
git clone https://github.com/Hrishi2861/mega-login-automation.git
cd mega-login-automation
```

### 2. Login your Heroku and create App:

```bash
heroku login
heroku create your-app-name
```

### 3. Add BuildPacks:

```bash
heroku buildpacks:add https://github.com/heroku/heroku-buildpack-chrome-for-testing.git
heroku buildpacks:add https://github.com/heroku/heroku-buildpack-chromedriver.git
heroku buildpacks:add heroku/python
```

### 4. Commit and Push:

```bash
git add . -f
git commit -m initial
git push heroku master -f
```

### 5. Start the Process:

```bash
heroku ps:scale worker=1
```
###

## Installation (VPS)

### 1. Clone the repository:

```bash
git clone https://github.com/Hrishi2861/mega-login-automation.git
cd mega-login-automation
```

### 2. Create Docker and RUN:

```bash
sudo docker build . -t megalogin
sudo docker run megalogin
```

###       OR

### 2. Using Docker-Compose:

```bash
sudo docker-compose up --build
```
