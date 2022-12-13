-- This file is to bootstrap a database for the CS3200 project. 
-- Create a new database.  You can change the name later.  You'll
-- need this name in the FLASK API files  the AppSmith 
-- data source creation.
create database media;
-- Via the Docker Compose file, a special user called webapp will 
-- be created in MySQL. We are going to grant that user 
-- all privilages to the new database we just created. 
-- TODO: If you changed the name of the database above, you need 
-- to change it here too.
use media;
grant all privileges on media.* to 'webapp' @'%';
flush privileges;
-- Movke into the database we just created.
-- TODO: If you changed the name of the database above, you need to
-- change it here too. 
-- Put your DDL 
CREATE TABLE picture (
  name VARCHAR(50) PRIMARY KEY,
  link VARCHAR(500),
  description VARCHAR(100)
);
-- Add sample data. 
INSERT INTO picture (name, link, description)
VALUES (
    'abstract_table',
    'https://www.dropbox.com/s/jkcpj768hqesdl8/original.png?raw=1',
    'Design of abstract table made in Rhino 3D'
  ),
  (
    'shelf',
    
    'https://www.dropbox.com/s/jcyiiuivibsyctd/original.png?raw=1',
    'Design of band made in Rhino 3D and grasshopper using python'
  ),
  (
    'uwu_pendant',
    'https://www.dropbox.com/s/7rsxblxnpz2jdr6/original.png?raw=1',
    'Design of a UWU Japanese Ascii Pendant made in Rhino 3D'
  );
-- force add table music
-- add music data here
CREATE TABLE music (
  musicID varchar(100) PRIMARY KEY,
  musicName VARCHAR(100),
  wavLink VARCHAR(100)
);
INSERT INTO music (musicID, musicName, wavLink)
VALUES (
    '1',
    '',
    'https://www.dropbox.com/s/2755t01si5ymksd/angels.wav?raw=1'
  )
  ,(
    '2',
    'the_tribe',
    'https://www.dropbox.com/s/u9o6bk0cksqxxzk/The%20Tribe%20v2.wav?raw=1'
  ),
  (
    '3',
    'chrome',
    'https://www.dropbox.com/s/bzq5mvsntseokcs/chrome.wav?raw=1'
  );

CREATE TABLE donorDesigns (
  designName VARCHAR(100) PRIMARY KEY,
  designLink VARCHAR(100)
);d
INSERT INTO donorDesigns (designName, designLink)
VALUES (
    'apple watch design',
    'https://www.dropbox.com/s/bomzjkqf2208l93/model.glb?raw=1'
  ),
  (
    'grind_shoe',
    'https://www.dropbox.com/s/yc2h9ayxyfccc5p/model.glb?raw=1'
  ),
  (
    'cd_x',
    'https://www.dropbox.com/s/pwumyunphsqmp7q/model.glb?dl=0'
  );