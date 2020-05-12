/* Note: All the outputs screenshots are attached in the Query Output Screenshot folder, named 1,2,3,4,5,6,7,8,9,10,11,12,13,14 and 15 respectively */


/* 1. Display 5 youngest user with their date of birth, dispay the youngest at first */
select fname as 'First Name',lname as 'Last Name', dob as 'Birth Date'
from User
order by dob desc
limit 5;


/* 2. Display the number of Users in each country */
select Country.name as 'Country Name', count(User.country_id) as 'Number Of Users'
from User right join Country on User.country_id = Country.country_id
group by Country.country_id
order by count(User.country_id) desc;


/* 3. Display the song name having maximum number of likes along with the likes count */
select Song.name as 'Song Name',count(*) as 'No. of Likes'
from Song join Likes on Song.song_id=Likes.song_id
group by Likes.song_id
having count(*) =(select max(n) from 
(select song_id,count(*) as n
from Likes
group by song_id) as E);


/* 4. Display all the albums with number of songs in each album and arrange according to Album Name */
select Album.name as 'Album Name',count(*) as 'Number of Songs'
from Song join Album on Song.album_id = Album.album_id
group by Song.album_id
order by Album.name;


/* 5. Display the number of songs in each genre along with its count */
select Genre.name as 'Genre Name',count(Song.genre_id) as 'No. of Songs'
from Genre left join Song on Genre.genre_id=Song.genre_id
group by Genre.genre_id;


/* 6. Display the Albums which has minimum number of songs with its count */
select Album.name as 'Album Name', count(*) as 'No. of Songs'
from Song join Album on Song.album_id=Album.album_id
group by Song.album_id having count(*)=(select min(n) from(
select Album.name as m ,count(*) as n
from Song join Album on Song.album_id = Album.album_id
group by Song.album_id) as K);


/* 7. Display all the Users and Singers who are from Nepal */
select fname as 'First Name',lname as 'Last Name'
from User
where User.country_id='npl'
union
select fname,lname
from Singer
where Singer.country_id='npl';


/* 8. Display Number of Singers by Country */
select name as 'Country', x as 'Number of Singers'
from Country join (select country_id,count(singer_id) as x
from Singer
group by country_id) as e
on Country.country_id= e.country_id;


/* 9. Display all the songs released between 2014-01-01 to 2018-12-30 */
select Song.name as Songs 
from Song
where album_id in (
select album_id as a
from Album
where released_date between '2014-01-01' and '2018-12-30');


/* 10. Display Albums which has more than one song */
select a as 'Albums Name'
from (select Album.name as a ,count(*) as n
from Song join Album on Song.album_id = Album.album_id
group by Song.album_id
having n>1) as c;


/* 11. Display songs whose name ends with vowels and the album which it belongs to, starts with a,b,c,d,e or f */
select Song.name as Songs
from Song 
where album_id in (
select album_id
from Album
where name regexp '^[abcdef]') and 
Song.name regexp '[aeiou]$';


/* 12. Display how would a joint playlist of Sitam and Virat look */
select distinct name as 'Combined Playlist for Sitam and Virat' 
from song 
where song_id in (select song_id
from Playlist
where email_id='sitam@gmail.com'
union
select song_id
from Playlist
where email_id='virat@gmail.com');


/* 13. Display information about each user and it's corresponding number of songs in playlist */
select concat(fname,' ',lname) as Users, count(song_id) as 'Number of Songs in Playlist'
from User left join Playlist on User.email_id = Playlist.email_id
group by User.email_id;


/* 14. Display information about each Singers total number of Songs in the database */
select concat(Singer.fname,' ',Singer.lname) as Singers,count(song_id) as 'Total Songs in the Database'
from Song join Singer on Song.singer_id=Singer.singer_id
group by Song.singer_id;


/* 15. Display songs that neither liked nor kept in playlist by any users */
select name as 'Songs Neither Liked nor kept in Playlist by any User' from Song
where song_id not in 
(select distinct song_id from
(select * from Likes
union
select * from Playlist) as c);
