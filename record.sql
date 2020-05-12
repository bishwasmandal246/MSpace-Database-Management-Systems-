/* Populate the table Country */
insert into MSpace.Country (country_id, name) values
('usa','United States of America'),
('spn','Spain'),
('col','Colombia'),
('itl','Italy'),
('ind','India'),
('npl','Nepal'),
('rmn','Romania'),
('chn','China'),
('frn','France'),
('aus','Australia'),
('mxc','Mexico'),
('prt','Portugal'),
('rsa','South Africa'),
('rus','Russia'),
('jpn','Japan');
/* There are a total of 15 different countries i.e. Number of rows= 15 */
/* For ease only 15 countries were kept */


/* Populate the table Genre */
insert into MSpace.Genre (genre_id, name, description) values
('edm', 'Electronic Dance Music (EDM)','Generally referred as EDM, this form of music is produced by DJs who add dozens of tones to a piece to create unique music. You can hear them in clubs or even live, depending upon your accessibility for the same. In the early twenties, electronic dance music was known in the form of Jamaican dub music, the electronic music of Kraftwerk, the disco music of Giorgio Moroder, the Yellow Magic Orchestra and many more.'),
('jzz', 'Jazz','Identified with swing and blue notes, Jazz has its roots both in the West African and European culture. It is said that Jazz is “One of America’s original art forms” and boasts a unique combination of creativity, coactions and interactivity. Originating in the late 19th to early 20th century, Jazz has also played an important role in introducing the world to a number of women performers like Ella Fitzgerald, Betty Carter, Abbey Lincoln and Ethel Waters.'),
('rm', 'Rock Music','Originated as “Rock & Roll” in the United States, Rock music has been rocking the world since the 1950s. It is a form of music that started actually around string instruments, but now uses other modern instruments too making it a little difficult to give it an accurate definition. Its loud and strong beats make it popular among the youths. Some of the rock stars who have popularized the culture include Little Richard, Bill Haley and Chuck Berry while rock bands like Pink Floyd, The Doors, Metallica, Nirvana and Megadeth are the modern bands who have taken the culture by storm.'),
('dbs', 'Dubstep','The use of instruments attracting music lovers for its bass and rhythm, this falls in the electronic music genre. People consider it to be a darker form of music, but since its birth in the late 1990s, this genre has successfully made its place in the industry.'),
('rnb', 'Rhythm  and Blues','Vocalists like Rihanna, Mariah Carey, Beyoncé, Usher and the legendary Michael Jackson have all made it huge in the music industry with their love for this form of music. Originated in the 1940s, this African-American music is a combination of hip hop, funk, dance, pop and soul focusing on themes like relationships, sex and freedom.'),
('cm', 'Country Music','Another popular genre of American music which originated in the 1920s, Country music has its roots from American folk and western music. It is formed using simple forms of instruments ranging from electric and steel guitars to drums and mandolin or mouth organ. Some very popular country music singers include Shania Twain, Johnny Cash Taylor Swift and Kenny Rogers.'),
('pm', 'Pop Music','“Pop” is a term derived from “Popular” and thus Pop Music is known to be a genre of popular music. With its roots in the rock & roll style, this form can include any form of music ranging from urban and dance to rock, country and Latin. Instruments highly used are electric guitars, synthesizer drums as well as bass and one can listen to this form of music by listening to songs by Britney Spears, Madonna, Beyonce Lady Gaga and of course the “King of Pop”, Michael Jackson.'),
('ele','Electro','A perfect blend of hip hop and electronic music, electro or electro-funk uses drum machine, vocoder and talkbox helping it to distinguish itself from another similar form of music, Disco. Notable artists who have been into this form of music include Arthur Baker, Freeez, Man Parrish and Midnight Star.'),
('tch','Techno','You may have listened to a number of techno music while clubbing, but it is Detroit techno that is considered to be the foundation of this form of music. Unlike the days of its emergence, the use of technology today has greatly enhanced the quality of techno style music and popularizing it among people day by day.'),
('ide','Indie Rock','Falling in the genre of alternative rock music, Indie Rock originated in the 1980s and has gradually changed the music industry. After a decade, it also gave birth to a couple of sun-genres in related styles such as math rock, emo, noise pop, post rock and lo-fi.');
/* There are a total of 10 different genres i.e. Number of rows= 10 */
/* Description is copied from source: https://medium.com/giglue/top-10-genres-of-music-industry-7f19cdb177cb */


/* Populate the table Monthy_Plan */
insert into MSpace.Monthly_Plan (plan_name, max_song_allowed, cost) values
('Basic',1,0),
('Silver',3,5),
('Gold',7,7),
('Diamond',10,9),
('Platinum',15,10);
/* There are a total of 5 different plans i.e. Number of rows = 5 */


/* Populate the table User */
insert into MSpace.User ( email_id, password, fname, lname, dob, sex, phone, country_id,funds,plan_name) values
('bibidh@gmail.com','bibidh123','Bibidh','Mainali','1995-04-13','Male','9841414101','rsa',default,'Gold'),
('chandan@gmail.com','chandan123','Chandan','Shah','1996-09-06','Male','9841414102','npl',default,'Gold'),
('aakankshya@gmail.com','aakankshya123','Aakankshya','Shrestha','1997-07-30','Female','9841414103','col',default,'Gold'),
('sitam@gmail.com','sitam123','Sitam','Gautam','1996-04-20','Female','9841414104','chn',default,'Gold'),
('alex@gmail.com','alex123','Alex','Hans','1987-08-28','Male','9841414105','usa',default,'Gold'),
('felix@gmail.com','felix123','Felix','Trans','2002-12-02','Female','9841414106','rus',default,'Gold'),
('steve@gmail.com','steve123','Steve','Smith','1986-11-03','Male','9841414107','aus',default,'Gold'),
('abd@gmail.com','abd123','ABD','Villiers','1990-01-01','Male','9841414108','rsa',default,'Gold'),
('virat@gmail.com','virat123','Virat', 'Kohli','1988-08-18','Male','9841414109','ind',default,'Gold'),
('vishal@gmail.com','vishal123','Vishal','Mandal','1995-03-10','Male','9841414110','npl',default,'Gold'),
('bishwas@gmail.com','bishwas123','Bishwas','Mandal','1997-11-11','Male','9812345670','npl',default,'Gold');
/* In my complete project I wish to take the input from the user itself when they create account and no information of other accounts can be seen by other users. But as of now just created a random set of values with my friends name for fulfilling the requirements of this assignment */
/* There are a total of 11 users, i.e. Number of rows = 11 */

/* Populate the admin table */
insert into MSpace.Admin(email_id,password,revenue) values ('bishwas@gmail.com','bishwas123',0);
/* There is only one admin i.e. Number of rows = 1

/* Populate the table Singer */
insert into MSpace.Singer (singer_id, fname, lname, dob, country_id) values
('ts1','Taylor','Swift','1989-12-13','usa'),
('ak1','Akon','Thiam','1973-04-16','usa'),
('mj1','Michael','Jackson','1958-08-29','usa'),
('jz1','Jane','Zhang','1984-10-11','chn'),
('yb1','Yama','Buddha','1987-05-30','npl'),
('gk1','Girish','Khatiwada','1979-09-30','npl'),
('ei1','Enrique','Iglesias','1975-05-08','spn'),
('hs1','Yo Yo Honey','Singh','1983-03-15','ind'),
('si1','Shakira','Isabel','1977-02-02','col'),
('nk1','Neha','Kakkar','1988-06-06','ind');
/* All the singers information are correct as per internet sources */
/* There are a total of 10 Singers from 6 countries, i.e. Number of rows = 10 */
/* If possible I would add more singers for my final project */


/* Populate the table Album */
insert into MSpace.Album (album_id, name, released_date) values
('th1','Thriller','1982-11-30'),
('dn1','Dangerous','1991-11-26'),
('lv1','Lovers','2019-08-23'),
('rp1','Reputation','2017-11-10'),
('fr1','Freedom','2008-12-01'),
('bj1','Believe in Jane','2010-02-02'),
('ek1','Ekadesh','2012-07-06'),
('pr1','Prasanga','2017-02-11'),
('lh1','Lok Hop','2017-12-25'),
('is1','Insomniac','2007-06-11'),
('sl1','Sex and Love','2014-03-14'),
('iv1','International Villager','2011-11-11'),
('dk1','Desi Kalakar','2014-08-26'),
('ed1','El Dorado','2017-05-26'),
('fv1','Fever','2016-07-15'),
('sd1','Student of the year 2','2018-12-24');
/* All the mentioned singer's 1 or 2 albums are kept in the Album Table */
/* Total number of Albums is 16 i.e. Number of rows = 16 */


/*Populate the table ASG */
insert into MSpace.ASG (album_id, singer_id, genre_id) values
('th1','mj1','pm'),
('dn1','mj1','tch'),
('lv1','ts1','edm'),
('lv1','ts1','ide'),
('rp1','ts1','jzz'),
('rp1','ts1','cm'),
('fr1','ak1','rnb'),
('bj1','jz1','cm'),
('bj1','jz1','dbs'),
('ek1','yb1','ele'),
('ek1','yb1','tch'),
('pr1','yb1','ele'),
('lh1','gk1','ide'),
('is1','ei1','pm'),
('sl1','ei1','cm'),
('iv1','hs1','tch'),
('dk1','hs1','cm'),
('ed1','si1','ide'),
('fv1','nk1','jzz'),
('sd1','nk1','rnb'),
('sd1','nk1','pm');
/* This table records distinct combinations of Album ID, Singer ID and Genre ID. Number of rows = 21 */


/* Populate the table Song */
insert into MSpace.Song (song_id, name, album_id, singer_id, genre_id) values
('s1','Beat it','th1','mj1','pm'),
('s2','Thriller','th1','mj1','pm'),
('s3','Human Nature','th1','mj1','pm'),
('s4','In the closet','dn1','mj1','tch'),
('s5','Who is it','dn1','mj1','tch'),
('s6','Soon you will get better','lv1','ts1','edm'),
('s7','Me!','lv1','ts1','ide'),
('s8','Don''t blame me','rp1','ts1','jzz'),
('s9','Ready for it','rp1','ts1','cm'),
('s10','Right now (Na Na Na)','fr1','ak1','rnb'),
('s11','Beautiful','fr1','ak1','rnb'),
('s12','I believe','bj1','jz1','cm'),
('s13','Can''t do it','bj1','jz1','dbs'),
('s14','Sathi','ek1','yb1','ele'),
('s15','Ek Prasanga','ek1','yb1','ele'),
('s16','Aama','ek1','yb1','tch'),
('s17','Aaudai chu ma','pr1','yb1','ele'),
('s18','Bol bham bole','lh1','gk1','ide'),
('s19','Tonight I''m loving you','is1','ei1','pm'),
('s20','Bailando (Spanish Version)','sl1','ei1','cm'),
('s21','Brown Rang','iv1','hs1','tch'),
('s22','Gabru','iv1','hs1','tch'),
('s23','Yaar tera superstar Desi kalakar','dk1','hs1','cm'),
('s24','Nada','ed1','si1','ide'),
('s25','Chantaje','ed1','si1','ide'),
('s26','Coco Cola','fv1','nk1','jzz'),
('s27','The Jawaani Song','sd1','nk1','rnb'),
('s28','The Hookup Song','sd1','nk1','rnb'),
('s29','Miley ho tum humse','sd1','nk1','pm');
/* All the mentioned album's one, two or three songs are kept inside the table */
/* Number of rows = 29 */


/* Populate the table Likes */
insert into MSpace.Likes (email_id, song_id) values
('bibidh@gmail.com','s12'),
('bibidh@gmail.com','s19'),
('bibidh@gmail.com','s2'),
('bibidh@gmail.com','s7'),
('bibidh@gmail.com','s1'),
('bibidh@gmail.com','s9'),
('bibidh@gmail.com','s22'),
('bibidh@gmail.com','s17'),
('chandan@gmail.com','s3'),
('chandan@gmail.com','s13'),
('chandan@gmail.com','s23'),
('chandan@gmail.com','s11'),
('aakankshya@gmail.com','s1'),
('aakankshya@gmail.com','s11'),
('aakankshya@gmail.com','s13'),
('aakankshya@gmail.com','s14'),
('aakankshya@gmail.com','s15'),
('aakankshya@gmail.com','s10'),
('alex@gmail.com','s25'),
('alex@gmail.com','s27'),
('alex@gmail.com','s29'),
('alex@gmail.com','s5'),
('felix@gmail.com','s3'),
('felix@gmail.com','s13'),
('felix@gmail.com','s23'),
('felix@gmail.com','s19'),
('felix@gmail.com','s17'),
('felix@gmail.com','s4'),
('felix@gmail.com','s24'),
('steve@gmail.com','s8'),
('steve@gmail.com','s28'),
('abd@gmail.com','s6'),
('abd@gmail.com','s26'),
('abd@gmail.com','s16'),
('abd@gmail.com','s5'),
('virat@gmail.com','s5'),
('virat@gmail.com','s15'),
('virat@gmail.com','s25'),
('virat@gmail.com','s11'),
('virat@gmail.com','s1'),
('virat@gmail.com','s2'),
('virat@gmail.com','s22'),
('virat@gmail.com','s3'),
('virat@gmail.com','s4'),
('virat@gmail.com','s6'),
('virat@gmail.com','s27'),
('virat@gmail.com','s29'),
('vishal@gmail.com','s2'),
('vishal@gmail.com','s6');
/* Number of rows= 49 */
/* This table keeps the records of all the songs liked by a particular user */


/* Populate the table Playlist */
insert into MSpace.Playlist (email_id, song_id) values
('bibidh@gmail.com','s19'),
('bibidh@gmail.com','s2'),
('chandan@gmail.com','s9'),
('chandan@gmail.com','s3'),
('chandan@gmail.com','s13'),
('sitam@gmail.com','s11'),
('sitam@gmail.com','s17'),
('sitam@gmail.com','s21'),
('sitam@gmail.com','s18'),
('virat@gmail.com','s3'),
('virat@gmail.com','s4'),
('virat@gmail.com','s6'),
('virat@gmail.com','s5'),
('virat@gmail.com','s27'),
('virat@gmail.com','s29'),
('sitam@gmail.com','s12'),
('alex@gmail.com','s25'),
('alex@gmail.com','s27'),
('alex@gmail.com','s29'),
('felix@gmail.com','s19'),
('felix@gmail.com','s17'),
('felix@gmail.com','s4'),
('felix@gmail.com','s24'),
('felix@gmail.com','s14'),
('steve@gmail.com','s18'),
('abd@gmail.com','s6'),
('abd@gmail.com','s16'),
('vishal@gmail.com','s6'),
('vishal@gmail.com','s2');
/* Number of rows = 29 */
/* This table keeps the record of songs in a user's playlist */


