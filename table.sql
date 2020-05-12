/* The entire database is encoded in utf8 character set and the collation is utf8_general_ci */
/* As I've been using MySQL workbench we don't need to specify that after every table, we can set the entire database while initialising the database */
/* Relational Schema of this database and it's table has been given in 'RelationSchema.png' */

create table if not exists MSpace.Country(
country_id varchar(3) not null,
name varchar(100) not null,
primary key (country_id),
unique (name)
) ENGINE=INNODB; /* This table has one primary key and one unique column */


create table if not exists MSpace.Genre(
genre_id varchar(5) not null,
name varchar(50) not null,
description varchar(10000) not null,
primary key(genre_id),
unique(name)
) ENGINE=INNODB; /* This table has one primary key and one unique column */


create table if not exists MSpace.Monthly_Plan(
plan_name varchar(20)  not null,
max_song_allowed int  not null,
cost int not null,
primary key(plan_name),
unique (max_song_allowed),
unique (cost)
) ENGINE=INNODB; /* This table has one primary key and two unique columns */


create table if not exists MSpace.User(
email_id varchar(60) not null,
password varchar(60) not null,
fname varchar(45) not null,
lname varchar(45) not null,
dob DATE not null,
sex varchar(15) not null,
phone varchar(15) not null,
country_id varchar(3) not null,
funds int default 0,
plan_name varchar(20) default 'Basic',
primary key (email_id),
foreign key(country_id) references MSpace.Country(country_id)
ON DELETE CASCADE
ON UPDATE CASCADE,
foreign key(plan_name) references MSpace.Monthly_Plan(plan_name)
ON DELETE CASCADE
ON UPDATE CASCADE
) ENGINE=INNODB; /* There is no additional keys except for the primary key and two foreign keys */


create table if not exists MSpace.Admin(
email_id varchar(60) not null,
password varchar(60) not null,
revenue int,
foreign key(email_id) references MSpace.User(email_id)
ON DELETE CASCADE
ON UPDATE CASCADE,
primary key(email_id)
)ENGINE=INNODB;


create table if not exists MSpace.Singer(
singer_id varchar(5) not null,
fname varchar(45) not null,
lname varchar(45) not null,
dob DATE not null,
country_id varchar(3) not null,
primary key(singer_id),
foreign key(country_id) REFERENCES MSpace.Country(country_id)
ON DELETE CASCADE
ON UPDATE CASCADE
) ENGINE=INNODB; /* There is no additional keys except for the primary key and a foreign key */


create table if not exists MSpace.Album(
album_id varchar(5)  not null,
name varchar(150)  not null,
released_date DATE not null,
primary key(album_id),
unique (name)
) ENGINE=INNODB; /* This table has one primary key and one unique column */

create table if not exists MSpace.ASG(
album_id varchar(5) not null,
singer_id varchar(5) not null,
genre_id varchar(5) not null,
foreign key(album_id) references MSpace.Album(album_id)
ON DELETE CASCADE
ON UPDATE CASCADE,
foreign key(singer_id) references MSpace.Singer(singer_id)
ON DELETE CASCADE
ON UPDATE CASCADE,
foreign key(genre_id) references MSpace.Genre(genre_id)
ON DELETE CASCADE
ON UPDATE CASCADE,
primary key(album_id,singer_id,genre_id)
) ENGINE= INNODB; /* This table ensures that one song cannot be in multiple Albums, or sung by multiple singers or in multiple genres */


create table if not exists MSpace.Song(
song_id varchar(5) not null,
name varchar(150) not null,
album_id varchar(5) not null,
singer_id varchar(5) not null,
genre_id varchar(5) not null,
foreign key (album_id,singer_id,genre_id) references MSpace.ASG(album_id,singer_id,genre_id)
ON DELETE CASCADE
ON UPDATE CASCADE,
primary key(song_id)
) ENGINE=INNODB; /* There is no additional keys except for the primary key and three foreign keys */

create table if not exists MSpace.Likes(
email_id varchar(60) not null,
song_id varchar(5) not null,
foreign key(email_id) references MSpace.User(email_id)
ON DELETE CASCADE
ON UPDATE CASCADE,
foreign key(song_id) references MSpace.Song(song_id)
ON DELETE CASCADE
ON UPDATE CASCADE,
primary key(email_id,song_id)
) ENGINE= INNODB; /* There is no additional keys except for the primary key and two foreign keys */

create table if not exists MSpace.Playlist(
email_id varchar(60) not null,
song_id varchar(5) not null,
foreign key(email_id) references MSpace.User(email_id)
ON DELETE CASCADE
ON UPDATE CASCADE,
foreign key(song_id) references MSpace.Song(song_id)
ON DELETE CASCADE
ON UPDATE CASCADE,
primary key(email_id,song_id)
) ENGINE= INNODB; /* There is no additional keys except for the primary key and two foreign keys */
