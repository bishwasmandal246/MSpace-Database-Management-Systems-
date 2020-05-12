# Original work of Bishwas Mandal.

import mysql.connector
import time
import sys
import re

def email_check(email_id):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if (re.search(regex, email_id)):
        return email_id
    else:
        return '0'


mydb = mysql.connector.connect(host="localhost", user="root", passwd="localhost", database="MSpace")
mycursor = mydb.cursor()


def main_page():
    print(" "*90,"Welcome to  MSpace")
    print(" "*83,"----------------------------------------")
    print()
    try:
        main_input=int(input("Are you? \n1.Admin \n2.User: "))
        if main_input==1:
            return admin()
        elif main_input==2:
            return home()
        else:
            time.sleep(0.3)
            print("\033[91m\033[1mWrong Input. Please run your program again \nApplication Closing...\033[0m")
            sys.exit(0)
    except ValueError:
        print("Incorrect Input type, Please Try again")
        return main_page()



def admin():
    print("Welcome to the ADMINISTRATOR Section of MSpace")
    print("------------------------------------------------")
    print()
    email_id = input("Email ID: ")
    password = input('Password: ')
    check = ("select * from Admin where email_id=%s and password=%s")
    mycursor.execute(check, (email_id, password,))
    result = mycursor.fetchall()
    if len(result) == 0:
        print("Sorry you're not the admin. Redirecting to main page... ")
        time.sleep(0.6)
        return main_page()
    else:
        print("\033[91m\033[1mHello Mr. Administrator, It's great seeing you!\033[0m")
        query0=("select revenue from Admin where email_id=%s")
        mycursor.execute(query0,(email_id,))
        var0=mycursor.fetchall()
        print()
        print("\033[91m\033[1m==========================\033[0m")
        print("| Total Revenue:  $",var0[0][0])
        print("\033[91m\033[1m==========================\033[0m")
        print()
        print("\033[4mA brief report is presented below:\033[0m")
        mycursor.execute("select count(*) from User")
        var1=mycursor.fetchall()
        print("Total Number of MSpace's Registered Users: ",var1[0][0])
        mycursor.execute("select count(*) from Singer")
        var2=mycursor.fetchall()
        print("Total Number of Singers whose songs are in MSpace: ",var2[0][0])
        mycursor.execute("select count(*) from Album")
        var3 = mycursor.fetchall()
        print("Total Number of Albums whose songs are in MSpace: ",var3[0][0])
        mycursor.execute("select count(*) from Genre")
        var4 = mycursor.fetchall()
        print("Number of Genres present in MSpace: ",var4[0][0])
        mycursor.execute("select count(*) from Song")
        var5 = mycursor.fetchall()
        print("Total Number of Songs in MSpace: ",var5[0][0])
        print()
        print("\033[4m5 youngest user of MSpace with their Date of Birth\033[0m")
        mycursor.execute("select fname,lname,dob from User order by dob desc limit 5")
        var6=mycursor.fetchall()
        for i in range(len(var6)):
            print(var6[i][0],var6[i][1],"was born in",var6[i][2])
        print()
        mycursor.execute("select Country.name, count(User.country_id) from User right join Country on User.country_id = Country.country_id group by Country.country_id order by count(User.country_id) desc")
        var7=mycursor.fetchall()
        print("\033[4mNumber of Users by Country\033[0m")
        for i in range(len(var7)):
            print(var7[i][0],":",var7[i][1])
        print()
        print("\033[4mSongs most Liked by Users along with their counts\033[0m")
        mycursor.execute("select Song.name,count(*) from Song join Likes on Song.song_id=Likes.song_id group by Likes.song_id having count(*) =(select max(n) from (select song_id,count(*) as n from Likes group by song_id) as E)")
        var8=mycursor.fetchall()
        for i in range(len(var8)):
            print(var8[i][0],"is liked by",var8[i][1],"users")
        print()
        print("\033[4mAlbums with their song count \033[0m")
        mycursor.execute("select Album.name ,count(*) from Song join Album on Song.album_id = Album.album_id group by Song.album_id order by Album.name")
        var9=mycursor.fetchall()
        for i in range(len(var9)):
            print("Album",var9[i][0],"has",var9[i][1],"songs")
        print()
        print("\033[4m Number of songs in each genre along with its count\033[0m")
        mycursor.execute("select Genre.name,count(Song.genre_id) from Genre left join Song on Genre.genre_id=Song.genre_id group by Genre.genre_id")
        var10=mycursor.fetchall()
        for i in range(len(var10)):
            print("Genre",var10[i][0],"has",var10[i][1],"songs")
        print()
        print("\033[4mAlbums which has minimum number of songs with its count\033[0m")
        mycursor.execute("select Album.name, count(*) from Song join Album on Song.album_id=Album.album_id group by Song.album_id having count(*)=(select min(n) from(select Album.name as m ,count(*) as n from Song join Album on Song.album_id = Album.album_id group by Song.album_id) as K)")
        var11=mycursor.fetchall()
        for i in range(len(var11)):
            print("Album:",var11[i][0],"Count:",var11[i][1])
        print()
        print("\033[4mNumber of Singers by Country \033[0m")
        mycursor.execute("select name, x from Country join (select country_id,count(singer_id) as x from Singer group by country_id) as e on Country.country_id= e.country_id")
        var12=mycursor.fetchall()
        for i in range(len(var12)):
            print(var12[i][0],"has",var12[i][1],"singers")
        print()
        print("\033[4mAlbums which has more than one songs\033[0m")
        mycursor.execute("select a from (select Album.name as a ,count(*) as n from Song join Album on Song.album_id = Album.album_id group by Song.album_id having n>1) as c")
        var13=mycursor.fetchall()
        for i in range(len(var13)):
            print(var13[i][0])
        print()
        print("\033[4mUsername and it's corresponding number of songs in playlist \033[0m")
        mycursor.execute("select fname,lname, count(song_id) from User left join Playlist on User.email_id = Playlist.email_id group by User.email_id")
        var14=mycursor.fetchall()
        for i in range(len(var14)):
            print(var14[i][0],var14[i][1],"has",var14[i][2],"songs in his/her Playlist")
        print()
        print("\033[4mEach Singers total number of Songs in MSpace\033[0m")
        mycursor.execute("select Singer.fname,Singer.lname,count(song_id) from Song join Singer on Song.singer_id=Singer.singer_id group by Song.singer_id")
        var15=mycursor.fetchall()
        for i in range(len(var15)):
            print(var15[i][0],var15[i][1],"'s total number of songs:",var15[i][2])
        print()
        print("\033[4mSongs that neither liked nor kept in playlist by any users\033[0m")
        mycursor.execute("select name from Song where song_id not in (select distinct song_id from (select * from Likes union select * from Playlist) as c)")
        var16=mycursor.fetchall()
        for i in range(len(var16)):
            print(var16[i][0])
        print()
        print("\033[4mDisplay all the songs whose name ends with a vowel and the album which it belongs to, its name starts with any letter from a to f\033[0m")
        mycursor.execute("select Song.name from Song where album_id in (select album_id from Album where name regexp '^[abcdef]') and Song.name regexp '[aeiou]$'")
        var17=mycursor.fetchall()
        for i in range(len(var17)):
            print(var17[i][0])
        print()
        print("What else would you like to do?")
        print("1. Display all the Users name and Singers who are from a particular country")
        print("2. Display all the songs released between some particular Date")
        print("3. Display how joint playlist of two Users look")
        print("4. Log Out")
        while True:
            try:
                inp_f=int(input("Please enter your choice: "))
                if (inp_f==1):
                    new_1=input("Enter Country Name: ")
                    query_1=("select concat(fname,' ',lname) from User where User.country_id in (select country_id from Country where name=%s) union select concat(fname,' ',lname) from Singer where Singer.country_id in (select country_id from Country where name=%s)")
                    mycursor.execute(query_1,(new_1,new_1,))
                    print()
                    var18=mycursor.fetchall()
                    if len(var18)==0:
                        print("Sorry No Users Found")
                    else:
                        print("The name of all the Users and Singers are given below: ")
                        for i in range(len(var18)):
                            print(i+1,'.',var18[i][0])
                    print()
                elif(inp_f==2):
                    date1=input("Please enter Start Date: ")
                    date2=input("Please enter End Date: ")
                    query_2=("select Song.name from Song where album_id in ( select album_id as a from Album where released_date between %s and %s)")
                    mycursor.execute(query_2,(date1,date2,))
                    var19=mycursor.fetchall()
                    if len(var19)==0:
                        print("No Songs found between the duration of Time you entered")
                    else:
                        for i in range(len(var19)):
                            print(i+1,'.',var19[i][0])
                    print()
                elif(inp_f==3):
                    user1=input("Enter User1 email: ")
                    user2=input("Enter User2 email: ")
                    query_3=("select distinct name from song where song_id in (select song_id from Playlist where email_id=%s union select song_id from Playlist where email_id=%s)")
                    mycursor.execute(query_3,(user1,user2,))
                    var20=mycursor.fetchall()
                    if len(var20)==0:
                        print("No one has a single song in their playlist. Therefore their joint playlist is also empty.")
                    else:
                        print("Here's the list of songs in their joint list: ")
                        for i in range(len(var20)):
                            print(var20[i][0])
                        print()
                elif(inp_f==4):
                    print("\033[91m\033[1mMr. Admin Signing OUT...\033[0m")
                    time.sleep(0.5)
                    print("Logged Out Succesfully!")
                    sys.exit(0)
                else:
                    print("Invalid Input.")
            except ValueError:
                print("Invalid Value type, Please input integers.")


def home():
    print("Welcome to the User Section of MSpace")
    print("---------------------------------------")
    print()
    print("\033[4mSign In/ Sign Up\033[0m")
    try:
        home1=int(input("For Sign In enter 1 \nFor Sign Up enter 2. \nIf you want to exit the application enter 3: "))
        if home1==1:
            return signin()
        elif home1==2:
            return signup()
        elif home1==3:
            print("\033[91m\033[1mGood Bye...\033[0m")
            sys.exit(0)
        else:
            print("Sorry Inavlid Character")
            invalid1=input("Please enter y to start over or any letter to close the application: ")
            if invalid1.lower()=='y':
                return home()
            else:
                print("\033[91m\033[1mGood Bye...\033[0m")
                sys.exit(0)
    except ValueError:
        print("Invalid Value type, Please input integers.")



def signin():
    try:
        print()
        print("-----------")
        print("| Sign In |")
        print("-----------")
        email_id = input("Email ID: ")
        password = input('Password: ')
        check=("select * from User where email_id=%s and password=%s")
        mycursor.execute(check,(email_id,password,))
        result=mycursor.fetchall()
        if len(result)==0:
            inp1=input("Your email id and password doesn't match or your account doesn't exist. If you want to re-enter credentials enter y else use another letter to go to Home Page: ")
            if inp1=='y':
                return signin()
            else:
                return home()
        else:
            print("Logging in...")
            time.sleep(0.5)
            print()
            print("Welcome back",end=" ")
            return dashboard(email_id)
    except ValueError:
        print("Invalid Input type. Please check your Input Type")
        return signin()


def email_execute():
    email_id = input("Email ID: ")
    temp=email_check(email_id)
    if temp=='0':
        print("Invalid Email ID")
        return email_execute()
    else:
        check=("select * from User where email_id=%s ")
        mycursor.execute(check,(temp,))
        result=mycursor.fetchall()
        if len(result)==0:
            return str(temp)
        else:
            print("\033[91m\033[1mThis Email ID is already in Use. Please Use Different Email ID\033[0m")
            return email_execute()


def email_update(email_id):
    email = input("Enter new Email ID: ")
    temp=email_check(email)
    if temp=='0':
        print("Invalid Email ID")
        return email_update(email_id)
    else:
        check=("select * from User where email_id=%s ")
        mycursor.execute(check,(temp,))
        result=mycursor.fetchall()
        if len(result)==0:
            try:
                query=("update User set email_id=%s where email_id=%s")
                mycursor.execute(query,(temp,email_id,))
                mydb.commit()
                print("Email ID changed")
                print("\033[91m\033[1mYou are logging out...\033[0m")
                time.sleep(0.8)
                print("\033[91m\033[1mGood Bye!\033[0m")
                return home()
            except mysql.connector.Error as error:
                print("Failed to update record to database rollback: {}".format(error))
                print("Please Enter Details again")
                mydb.rollback()
                return email_update(email_id)
        else:
            print("This Email ID is already in Use. Please Use Different Email ID")
            return email_update(email_id)


def country_execute():
    try:
        mycursor.execute("select * from Country order by country_id")
        country1 = mycursor.fetchall()
        print("\033[4mCountries List\033[0m")
        for i in range(len(country1)):
            print(i+1,'.',country1[i][1])
        country = int(input("Country (Enter integer as per above Countries List) : "))
        if (country>len(country1) or country<1):
            print("Invalid Country. Please Select Integer as per the Countries list")
            return country_execute()
        else:
            country_id=str(country1[country-1][0])
            return country_id
    except ValueError:
        print("Invalid Input type. Please check your Input Type")
        return country_execute()


def signup():
    try:
        print()
        print("--------------------------------------------")
        print("| Please Fill the details below to Sign Up |")
        print("--------------------------------------------")
        email_id = email_execute()
        password = input("Password: ")
        fname = input("First Name: ")
        lname = input("Last Name: ")
        dob = input("Date of Birth: ")
        sex = input("Sex: ")
        phone = input("Phone Number: ")
        country_id = country_execute()
        insert_statement=("insert into User(email_id,password,fname,lname,dob,sex,phone,country_id,funds,plan_name) values(%s,%s,%s,%s,%s,%s,%s,%s,default,default)")
        mycursor.execute(insert_statement,(email_id,password,fname,lname,dob,sex,phone,country_id,))
        mydb.commit()
        print("Congratulations You're a new user of MSpace now. Redirecting to your dashboard...")
        time.sleep(0.8)
        print()
        return dashboard(email_id)
    except mysql.connector.Error as error:
        print("Failed to update record to database rollback: {}".format(error))
        mydb.rollback()
        return signup()


def playlist(email_id):
    print("\033[4mMY PLAYIST\033[0m")
    playlist1 = ("select name from Song where song_id in (select song_id from Playlist where email_id=%s)")
    mycursor.execute(playlist1,(email_id,))
    p1=mycursor.fetchall()
    if len(p1)>0:
        for i in range(len(p1)):
            print(p1[i][0])
        print()
    else:
        print("No Songs in the list.")
        print()


def likes(email_id):
    print("\033[4mMy Liked Songs\033[0m")
    like1 = ("select name from Song where song_id in (select song_id from Likes where email_id=%s)")
    mycursor.execute(like1, (email_id,))
    l1 = mycursor.fetchall()
    if len(l1)>0:
        for i in range(len(l1)):
            print(l1[i][0])
    else:
        print("No Songs in the list.")
        print()


def add_funds(email_id):
    present_fund=("select funds from User where email_id=%s")
    mycursor.execute(present_fund,(email_id,))
    temp=mycursor.fetchall()
    cash=int(temp[0][0])
    try:
        add_cash=int(input("Enter the amount you want to add in your account ($): "))
    except ValueError:
        print("Enter valid Input")
        return add_funds(email_id)
    new_cash=cash+add_cash
    try:
        new_fund=("update User set funds=%s where email_id=%s")
        mycursor.execute(new_fund,(new_cash,email_id,))
        mydb.commit()
        print("$",add_cash,"has been added to your account. You new available balance is $",new_cash)
    except mysql.connector.Error as error:
        print("Failed to update record to database rollback: {}".format(error))
        print("Please Start Over Again")
        mydb.rollback()
        return add_funds(email_id)


def remove_funds(email_id):
    present_fund=("select funds from User where email_id=%s")
    mycursor.execute(present_fund,(email_id,))
    temp=mycursor.fetchall()
    cash=int(temp[0][0])
    print("Available Funds: $",cash)
    try:
        minus_cash=int(input("Enter the amount you want to remove from your account ($): "))
    except ValueError:
        print("Invalid input. Start again...")
        return remove_funds(email_id)
    if minus_cash>cash:
        print("\033[91m\033[1mYou don't have the mentioned amount in your Account. Please enter amount that is less or equal to accounts balance.\033[0m")
        return remove_funds(email_id)
    else:
        new_cash=cash-minus_cash
        new_fund=("update User set funds=%s where email_id=%s")
        try:
            mycursor.execute(new_fund,(new_cash,email_id,))
            mydb.commit()
            print("$",minus_cash,"has been withdrawn from your account. You new available balance is $",new_cash)
        except mysql.connector.Error as error:
            print("Failed to update record to database rollback: {}".format(error))
            print("Please Start Over again")
            mydb.rollback()
            return remove_funds(email_id)


def monthly_subscription(email_id):
    view=("select * from Monthly_Plan order by cost")
    mycursor.execute(view)
    virtual_table=mycursor.fetchall()
    print("--------------------------------------------------------------")
    print("| Plan Name    | Maximum Songs Allowed in Playlist  |  Cost ($)")
    print("--------------------------------------------------------------")
    for i in range(len(virtual_table)):
        print("|",virtual_table[i][0]," "*(18-len(str(virtual_table[i][0]))),virtual_table[i][1]," "*(34-len(str(virtual_table[i][1]))),virtual_table[i][2])
    print("--------------------------------------------------------------")
    print()
    new_plan=input("Enter the Plan name you want to upgrade to: ")
    retr1=("select * from Monthly_Plan where plan_name=%s")
    mycursor.execute(retr1,(new_plan,))
    var1=mycursor.fetchall()
    if len(var1)==0:
        print("Invalid Plan Name. Try Again")
        return monthly_subscription(email_id)
    else:
        checker1=("select * from User where email_id=%s")
        mycursor.execute(checker1,(email_id,))
        result1=mycursor.fetchall()
        present_plan=str(result1[0][9])
        retr2=("select * from Monthly_Plan where plan_name=%s")
        mycursor.execute(retr2,(present_plan,))
        var2=mycursor.fetchall()
        if(var1[0][2]>var2[0][2]):
            print("Warning: You won't be able to cancel this or change your subscription to lower cost then what you currently are!!!")
            confirmation=input("Are you sure you want to (y/n or any letter): ")
            if confirmation.lower()=='y':
                amount_check=result1[0][8]+var2[0][2]-var1[0][2]
                if(amount_check>=0):
                    print("Subscription Change Success. You are now a '",new_plan.upper(),"' member")
                    update1=("update User set funds=%s , plan_name=%s where email_id=%s")
                    try:
                        mycursor.execute(update1,(amount_check,new_plan,email_id,))
                        mydb.commit()
                    except mysql.connector.Error as error:
                        print("Failed to update record to database rollback: {}".format(error))
                        print("Start Over again")
                        mydb.rollback()
                        return monthly_subscription(email_id)
                    mycursor.execute("select revenue from Admin")
                    update2=mycursor.fetchall()
                    new_revenue=int(update2[0][0])+var1[0][2]-var2[0][2]
                    admin_query=("update Admin set revenue=%s where email_id=%s")
                    admin_email='bishwas@gmail.com'
                    try:
                        mycursor.execute(admin_query,(new_revenue,admin_email,))
                        mydb.commit()
                    except mysql.connector.Error as error:
                        print("Failed to update record to database rollback: {}".format(error))
                        print("Start Over again")
                        mydb.rollback()
                        return monthly_subscription(email_id)
                else:
                    print("You are short of funds. Please Add funds in order to upgrade")
                    return dashboard(email_id)
            else:
                return dashboard(email_id)
        else:
            print("Sorry you can only upgrade your plan. ")
            return dashboard(email_id)


def profile(email_id):
    query=("select * from User where email_id=%s")
    mycursor.execute(query,(email_id,))
    upd=mycursor.fetchall()
    query1=("select name from Country where country_id=%s")
    mycursor.execute(query1,(upd[0][7],))
    nationality=mycursor.fetchall()
    print()
    print(" Profile Details")
    print("-----------------")
    print("Name: ",upd[0][2],upd[0][3])
    print("Registered Email: ", upd[0][0])
    print("Date of Birth: ", upd[0][4])
    print("Sex: ", upd[0][5])
    print("Phone: ", upd[0][6])
    print("Nationality: ",nationality[0][0])
    print("Account Balance: ",upd[0][8])
    print("Subscription Type: ",upd[0][9])


def search():
    try:
        what_search=int(input("What do you want to search? 1. Songs   OR   2. Users --> " ))
    except ValueError:
        print("Invalid Input Type. Please try again")
        return search()
    if what_search==1:
        try:
            song_search=int(input("Search Songs by: 1. Albums  2. Singers   3. Song Name   4. Genre -->"))
        except ValueError:
            print("Wrong Input Type. Please Start Over")
            return search()
        if song_search==1:
            search_=input("Search Song whose Album starts with: ")
            search1="^"+search_
            query=("select Song.name from Song where album_id in (select album_id from Album where name regexp %s)")
            mycursor.execute(query,(search1,))
            songs=mycursor.fetchall()
            print("\033[4mSearch Results: \033[0m")
            if(len(songs)==0):
                print("No Songs Found")
            else:
                for i in range(len(songs)):
                    print(i+1,'. ',songs[i][0])
            wish=input("Do you wish to search more? (y/n): ")
            if wish=='y':
                search()
            else:
                print()
        elif song_search==2:
            search_=input("Search Song whose Singer's name starts with: ")
            search1="^"+search_
            query=("select Song.name from Song where singer_id in (select singer_id from Singer where fname regexp %s or lname regexp %s)")
            mycursor.execute(query,(search1,search1,))
            songs=mycursor.fetchall()
            print("\033[4mSearch Results: \033[0m")
            if (len(songs) == 0):
                print("No Songs Found")
            else:
                for i in range(len(songs)):
                    print(i+1,'. ',songs[i][0])
            wish = input("Do you wish to search more? (y/n): ")
            if wish=='y':
                return search()
            else:
                print()
        elif song_search==3:
            search_=input("Search Songs which has its name starting with: ")
            search1="^"+search_
            query=("select Song.name from Song where name regexp %s")
            mycursor.execute(query,(search1,))
            songs=mycursor.fetchall()
            print("\033[4mSearch Results: \033[0m")
            if (len(songs) == 0):
                print("No Songs Found")
            else:
                for i in range(len(songs)):
                    print(i+1,'. ',songs[i][0])
            wish = input("Do you wish to search more? (y/n): ")
            if wish=='y':
                return search()
            else:
                print()
        elif song_search == 4:
            mycursor.execute("select name,description from Genre")
            genre_info=mycursor.fetchall()
            for i in range(len(genre_info)):
                print(genre_info[i][0])
                print("-"*(len(genre_info[i][0])+2))
                print(genre_info[i][1])
            print()
            search_ = input("Search Song whose Genre starts with: ")
            search1 = "^" + search_
            query = ("select Song.name from Song where genre_id in (select genre_id from Genre where name regexp %s)")
            mycursor.execute(query, (search1,))
            songs = mycursor.fetchall()
            print("\033[4mSearch Results: \033[0m")
            if (len(songs) == 0):
                print("No Songs Found")
            else:
                for i in range(len(songs)):
                    print(i + 1, '. ', songs[i][0])
            wish = input("Do you wish to search more? (y/n): ")
            if wish == 'y':
                return search()
            else:
                print()
        else:
            print("Invalid Input! Start Over")
            return search()
    elif what_search==2:
        user_search=input("Enter the first coming letters of the first or last name of the users that you want to search --> ")
        search1="^"+user_search
        query=("select fname,lname from User where fname regexp %s or lname regexp %s")
        mycursor.execute(query,(search1,search1,))
        users=mycursor.fetchall()
        print("\033[4mSearch Results: \033[0m")
        if len(users)==0:
            print("No Users Found")
        else:
            for i in range(len(users)):
                print(i + 1, '. ', users[i][0],users[i][1])
        wish = input("Do you wish to search more? (y/n): ")
        if wish=='y':
            return search()
        else:
            print()
    else:
        print("Invalid Input")


def update_playlist(email_id):
    option=int(input("1. Add Songs to Playlist  |  2. Delete Songs from Playlist   | Please Enter your Selection:  "))
    if option==1:
        print("\033[4mSongs List\033[0m")
        print()
        mycursor.execute("select Song.song_id,Song.name,Album.name,Genre.name,Singer.fname,Singer.lname from Song join Album on Song.album_id=Album.album_id join Singer on Song.singer_id=Singer.singer_id join Genre on Song.genre_id=Genre.genre_id")
        song_description=mycursor.fetchall()
        for i in range(len(song_description)):
            print(i+1,".Song:'",song_description[i][1],"'from the Album:",song_description[i][2],"of Genre:",song_description[i][3],"by Singer:",song_description[i][4],song_description[i][5])
        edit1=int(input("Select the song that you want to add to your playlist: "))
        temp_song_id=str(song_description[edit1-1][0])
        temp=("select * from Playlist where email_id=%s and song_id=%s")
        mycursor.execute(temp,(email_id,temp_song_id,))
        temp_fetch=mycursor.fetchall()
        song_count_check=("select song_id from Playlist where email_id=%s")
        mycursor.execute(song_count_check,(email_id,))
        count_var=mycursor.fetchall()
        query=("select max_song_allowed from User join Monthly_Plan on User.plan_name=Monthly_Plan.plan_name where email_id=%s")
        mycursor.execute(query,(email_id,))
        limit=mycursor.fetchall()
        if len(temp_fetch)==0:
            if(len(count_var)<int(limit[0][0])):
                try:
                    add_song="insert into Playlist (email_id,song_id) values (%s,%s)"
                    mycursor.execute(add_song,(email_id,temp_song_id,))
                    mydb.commit()
                    print("Playlist Updated. Thank you")
                    return playlist(email_id)
                except mysql.connector.Error as error:
                    print("Failed to update record to database rollback: {}".format(error))
                    print("Start Over again")
                    mydb.rollback()
                    return update_playlist(email_id)
            else:
                print("Sorry Your current monthly plan doesn't allow you to keep more songs in your Playlist. Please delete some songs or upgrade your plan.")
        else:
            else1=input("The song you selected is already in your playlist. Enter y to proceed to update playlist page or another letter to return to your dashboard: ")
            if else1=='y':
                return update_playlist(email_id)
            else:
                return dashboard(email_id)
    elif option==2:
        print("\033[4mYOUR PLAYIST\033[0m")
        playlist1 = ("select name,song_id from Song where song_id in (select song_id from Playlist where email_id=%s)")
        mycursor.execute(playlist1, (email_id,))
        p1 = mycursor.fetchall()
        for i in range(len(p1)):
            print(i+1,'. ',p1[i][0])
        print()
        del_song=int(input("Enter the song that you want to delete from the playlist: "))
        if del_song<=0 or del_song>len(p1):
            print("Sorry the song you chose is not in your playlist")
        else:
            songid=str(p1[del_song-1][1])
            query=("delete from Playlist where song_id=%s and email_id=%s")
            try:
                mycursor.execute(query,(songid,email_id,))
                mydb.commit()
                print("Playlist Updated. Thank you")
                return playlist(email_id)
            except mysql.connector.Error as error:
                print("Failed to update record to database rollback: {}".format(error))
                print("Start Over again")
                mydb.rollback()
                return update_playlist(email_id)
    else:
        print("Invalid Selection")
        print()



def like_dislike(email_id):
    try:
        option=int(input("1. Like a song  |  2. Dislike a song   | Please Enter your Selection:  "))
    except ValueError:
        print("Invalid Input type")
        return like_dislike(email_id)
    if option==1:
        print("\033[4mSongs List\033[0m")
        print()
        mycursor.execute("select Song.song_id,Song.name,Album.name,Genre.name,Singer.fname,Singer.lname from Song join Album on Song.album_id=Album.album_id join Singer on Song.singer_id=Singer.singer_id join Genre on Song.genre_id=Genre.genre_id")
        song_description=mycursor.fetchall()
        for i in range(len(song_description)):
            print(i+1,". Song '",song_description[i][1],"' from the Album ",song_description[i][2],"of Genre ",song_description[i][3]," by Singer ",song_description[i][4],song_description[i][5])
        edit1=int(input("Select the song that you want to like: "))
        temp_song_id=str(song_description[edit1-1][0])
        temp=("select * from Likes where email_id=%s and song_id=%s")
        mycursor.execute(temp,(email_id,temp_song_id,))
        temp_fetch=mycursor.fetchall()
        if len(temp_fetch)==0:
            add_song=("insert into Likes (email_id,song_id) values (%s,%s)")
            try:
                mycursor.execute(add_song,(email_id,temp_song_id,))
                mydb.commit()
                print("You've liked the song. Thank you")
                return likes(email_id)
            except mysql.connector.Error as error:
                print("Failed to update record to database rollback: {}".format(error))
                print("Start Over again")
                mydb.rollback()
                return like_dislike(email_id)
        else:
            else1=input("The song you selected is already liked by you. If you want to return to Like OR Dislike Page Enter y otherwise enter any other letter: ")
            if else1=='y':
                return like_dislike(email_id)
            else:
                return dashboard(email_id)
    elif option==2:
        print("\033[4mYOUR LIKED SONGS\033[0m")
        likes1 = ("select name,song_id from Song where song_id in (select song_id from Likes where email_id=%s)")
        mycursor.execute(likes1, (email_id,))
        p1 = mycursor.fetchall()
        for i in range(len(p1)):
            print(i+1,'. ',p1[i][0])
        print()
        try:
            del_song=int(input("Enter the song that you want to dislike: "))
        except ValueError:
            print("Invalid Input type. Start Over")
            return like_dislike(email_id)
        if del_song<=0 or del_song>len(p1):
            print("Sorry the song you chose is not in liked by you. In order to dislike a song it first should be liked by you.")
        else:
            songid=str(p1[del_song-1][1])
            query=("delete from Likes where song_id=%s and email_id=%s")
            try:
                mycursor.execute(query,(songid,email_id,))
                mydb.commit()
                print("Your choice of Song was Disliked. Thank you")
                return likes(email_id)
            except mysql.connector.Error as error:
                print("Failed to update record to database rollback: {}".format(error))
                print("Start Over again")
                mydb.rollback()
                return like_dislike(email_id)
    else:
        print("Invalid Selection")
        print()



def update_profile(email_id):
    print("Update: 1. First Name   2. Last Name   3. Date of Birth   4. Sex     5. Phone Number    6.Email    7. Password")
    print("Except the above options you aren't allowed to change other details. Others are Fixed and can never be changed")
    try:
        inp1=int(input("Update: "))
    except ValueError:
        print("Wrong Input Type. Start Over again")
        return update_profile(email_id)
    try:
        if inp1==1:
            fname=input("Enter your new first Name: ")
            query=("update User set fname=%s where email_id=%s")
            mycursor.execute(query,(fname,email_id,))
            mydb.commit()
            print("First Name changed. Redirecting...")
            print()
        elif inp1==2:
            lname=input("Enter your new Last Name: ")
            query=("update User set lname=%s where email_id=%s")
            mycursor.execute(query,(lname,email_id,))
            mydb.commit()
            print("Last Name changed. Redirecting...")
            print()
        elif inp1==3:
            dob=input("Enter your new Date of Birth: ")
            query=("update User set dob=%s where email_id=%s")
            mycursor.execute(query,(dob,email_id,))
            mydb.commit()
            print("Date of Birth changed. Redirecting...")
            print()
        elif inp1==4:
            sex=input("Update/ Change your sex: ")
            query=("update User set sex=%s where email_id=%s")
            mycursor.execute(query,(sex,email_id,))
            mydb.commit()
            print("Sex changed. Redirecting...")
            print()
        elif inp1==5:
            phone=input("Enter your new Phone Number: ")
            query=("update User set phone=%s where email_id=%s")
            mycursor.execute(query,(phone,email_id,))
            mydb.commit()
            print("Phone Number changed. Redirecting...")
            print()
        elif inp1==6:
            print("You'll have to login again after you change your email!")
            return email_update(email_id)
        elif inp1==7:
            old_password=input("Enter your Old password: ")
            verify_old=("select password from User where email_id=%s")
            mycursor.execute(verify_old,(email_id,))
            old1=mycursor.fetchall()
            if old_password==old1[0][0]:
                new_password=input("Enter your new password: ")
                query=("update User set password=%s where email_id=%s")
                mycursor.execute(query,(new_password,email_id,))
                mydb.commit()
                print("Password Change Success. Redirecting... ")
                print()
            else:
                print("\033[91m\033[1mYour Password is incorrect. Redirecting to your dashboard...\033[0m")
                print()
        else:
            print("Invalid Input")
    except mysql.connector.Error as error:
        print("Failed to update record to database rollback: {}".format(error))
        print("Start Over again")
        mydb.rollback()
        return update_profile(email_id)


def delete_account(email_id):
    confirmation=input("\033[91m\033[1mAre you sure you want to continue? (y/n): \033[0m")
    if confirmation=='y':
        query=("delete from User where email_id=%s")
        try:
            mycursor.execute(query,(email_id,))
            mydb.commit()
            print("Your account is deleted")
            return home()
        except mysql.connector.Error as error:
            print("Failed to update record to database rollback: {}".format(error))
            print("Start Over again")
            mydb.rollback()
            return delete_account(email_id)
    else:
        return dashboard(email_id)


def show_dashboard(email_id):
    statement1 = ("select * from User where email_id=%s")
    mycursor.execute(statement1, (email_id,))
    result1 = mycursor.fetchall()
    print("You are Logged in as ", result1[0][2].upper(), " !")
    print("YOUR DASHBOARD")
    print('-------------------------------------------------------------')
    print('| Funds Available    |   Subscription Type or Monthly Plan   ')
    print('............................................................')
    print("|      $", result1[0][8], " " * (10 - len(str(result1[0][8]))), "|      ", result1[0][9])
    print('-------------------------------------------------------------')
    print()

def dashboard(email_id):
    statement1=("select * from User where email_id=%s")
    mycursor.execute(statement1,(email_id,))
    result1=mycursor.fetchall()
    print(" You are Logged in as ",result1[0][2].upper()," !")
    print("YOUR DASHBOARD")
    print('-------------------------------------------------------------')
    print('| Funds Available    |   Subscription Type or Monthly Plan   ')
    print('............................................................')
    print("|      $",result1[0][8]," "*(10-len(str(result1[0][8]))),"|      ",result1[0][9])
    print('-------------------------------------------------------------')
    print()
    print("What would you like to do?: ")
    print("1. View my Playlist")
    print("2. View my Liked Songs")
    print("3. Add Funds")
    print("4. Remove Funds")
    print("5. Change your Subscription Type or Monthly Plan")
    print("6. Search")
    print("7. Update Playlist")
    print("8. Like or Dislike Song")
    print("9. Show Funds Available and Subscription Type")
    print("10. View my Profile Details")
    print("11. Update Profile Details")
    print("12. Logout")
    print("13. Delete Account")
    while True:
        try:
            action=int(input("Enter your choice: "))
            if action==1:
                playlist(email_id)
            elif action==2:
                likes(email_id)
            elif action==3:
                add_funds(email_id)
            elif action==4:
                remove_funds(email_id)
            elif action==5:
                monthly_subscription(email_id)
            elif action==6:
                search()
            elif action==7:
                update_playlist(email_id)
            elif action==8:
                like_dislike(email_id)
            elif action==9:
                show_dashboard(email_id)
            elif action==10:
                profile(email_id)
            elif action==11:
                update_profile(email_id)
            elif action==12:
                print("\033[91m\033[1mYou are logging out...\033[0m")
                time.sleep(0.8)
                print("\033[91m\033[1mGood Bye!\033[0m")
                home()
            elif action==13:
                delete_account(email_id)
            else:
                print("Invalid Action")
        except ValueError:
            print("Invalid Input type. Start Over")
            return dashboard(email_id)


def main():
    main_page()

main()
