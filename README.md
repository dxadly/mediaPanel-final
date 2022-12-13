# Team mediaPanel — artistPanel app

Team Members: David Adly

Team Name: mediaPanel

App name: artistPanel


This app provides an interface to an artist to upload their works for their fans to view. The personas that use this app are the artist, user, and donor.

---

[3-5 Minnute Video ](https://www.youtube.com/watch?v=Dqfamu6JcGM "click here for video link")elevator pitch of this product demoing the AppSmith app.


### App Overview:

The purpose of this app to provide an interface that allows an artist to upload links to their works of art.

The links to the art are to be stored on a remote server, the links are stored in the mySQL 8 container.

The links are then accessed in the container by the app smith server. The links are then to be embedded in the app smith server.

The app contains the following views:

* artistView — a view that allows the artist (admin) to send post requests to the server to upload pictures, designs (glb files), or music
* userView —a view that allows the user to view pictures
* musicview — a view that allows the user to listen to music
* donorView — a special page that contains the designs of the artist
* GLB binary files can be viewed on [babylon threejs](https://sandbox.babylonjs.com/)

For use on the 3200 appsmith server.

### POST and GET requests:

The userView, donorView and musicView use GET requests to tell appsmith to fetch the json of the mysql. App smith then takes the json and embeds the pictures, music and glb download links of files hosted on dropbox.

For the admin view the artist can send a POST request to upload remotely hosted music, photos and glbs.

---

### Original boiler plate setup:

This repo contains a boilerplate setup for spinning up 2 docker containers:

1. A MySQL 8 container for obvious reasons
2. A Python Flask container to implement a REST API

## How to setup and start the containers

**Important** - you need Docker Desktop installed

1. Clone this repository.
2. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL.
3. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the `webapp` user.
4. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.
5. Build the images with `docker compose build`
6. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`.

## For setting up a Conda Web-Dev environment:

1. `conda create -n webdev python=3.9`
2. `conda activate webdev`
3. `pip install flask flask-mysql flask-restful cryptography flask-login`
