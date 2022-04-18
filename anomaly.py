import csv
import random
import string

names = ["Aaden", "Oscar", "Aarav", "Amber", "Aaron", "Aayan", "Abbie", "Abdul", "Abner", "Abram", "Adams", "Addie", "Adlai", "Adolf", "Adron", "Aedan", "Agnes", "Ahmad", "Ahmed", "Ahmir", "Aidan", "Aiden", "Aidyn", "Akeem", "Akira", "Albin", "Alcee", "Alden", "Aleck", "Alfie", "Alger", "Algie", "Algot", "Alice", "Allan", "Allen", "Allie", "Allyn", "Almer", "Almon", "Almus", "Alois", "Aloys", "Alpha", "Alton", "Alvah", "Alvan", "Alver", "Alvia", "Alvie", "Alvin", "Alvis", "Alwin", "Amado", "Amare", "Amari", "Amasa", "Ameer", "Amias", "Ammon", "Ancel", "Ancil", "Andon", "Andra", "Andre", "Angel", "Angus", "Annie", "Ansel", "Anson", "Anton", "Anwar", "Arbie", "Arden", "Arian", "Ariel", "Aries", "Arjun", "Arlan", "Arlen", "Arley", "Arlie", "Arlin", "Arlis", "Arlyn", "Arman", "Armin", "Arnav", "Arnie", "Arron", "Artie", "Artis", "Arvel", "Arvid", "Arvil", "Arvin", "Aryan", "Ashby", "Asher", "Atlas", "Aubra", "Audie", "Autry", "Avery", "Axton", "Ayaan", "Aydan", "Ayden", "Aydin", "Aziel", "Baker", "Banks", "Baron", "Barry", "Basil", "Benji", "Benny", "Berry", "Beryl", "Betty", "Bilal", "Billy", "Bjorn", "Blain", "Blair", "Blake", "Blane", "Blaze", "Bliss", "Bobby", "Boden", "Bodhi", "Bodie", "Boone", "Boris", "Bowen", "Bowie", "Boyce", "Brady", "Brain", "Brant", "Brent", "Brett", "Brian", "Briar", "Brice", "Brien", "Brion", "Britt", "Brock", "Brody", "Brook", "Brown", "Bruce", "Bruno", "Bryan", "Bryce", "Bryon", "Buddy", "Buell", "Buren", "Burke", "Burns", "Butch", "Bynum", "Byron", "Caden", "Cairo", "Caleb", "Calum", "Carey", "Carlo", "Carol", "Casen", "Casey", "Cason", "Cecil", "Cesar", "Chace", "Chadd", "Chaim", "Champ", "Chase", "Chevy", "Chris", "Chuck", "Clabe", "Clair", "Clara", "Clare", "Clark", "Claud", "Claus", "Clell", "Cleon", "Cleve", "Clide", "Cliff", "Clint", "Clive", "Cloyd", "Clyde", "Codey", "Codie", "Cohen", "Colby", "Coley", "Colie", "Colin", "Colon", "Conor", "Corey", "Corry", "Cosmo", "Craig", "Creed", "Cyril", "Cyrus", "Daisy", "Damon", "Danny", "Dante", "Darby", "Darcy", "Daren", "Darin", "Dario", "Daron", "Darry", "Daryl", "Daryn", "Davey", "David", "Davie", "Davin", "Davis", "Davon", "Dayne", "Deane", "Debra", "Deion", "Dejon", "Della", "Delos", "Denis", "Denny", "Derek", "Deric", "Derik", "Deron", "Deryl", "Devan", "Deven", "Devin", "Devon", "Devyn", "Dewey", "Dhruv", "Diane", "Diego", "Dijon", "Dilan", "Dixie", "Dixon", "Dolph", "Donal", "Donat", "Donna", "Donny", "Donta", "Donte", "Doris", "Doyle", "Drake", "Drury", "Duane", "Duard", "Dusty", "Dwain", "Dwane", "Dylan", "Dylon", "Earle", "Early", "Eason", "Ebbie", "Ebert", "Eddie", "Edgar", "Edith", "Edmon", "Edsel", "Edson", "Edwin", "Effie", "Efrem", "Efren", "Einar", "Elden", "Elder", "Eldon", "Elgie", "Elgin", "Elian", "Elias", "Elick", "Eliel", "Eliga", "Elige", "Elihu", "Eliot", "Eliza", "Ellen", "Ellie", "Ellis", "Elmer", "Elroy", "Elsie", "Elton", "Elvie", "Elvin", "Elvis", "Elwin", "Elwyn", "Elzie", "Emery", "Emett", "Emile", "Emmet", "Emmit", "Emory", "Ennis", "Enoch", "Erich", "Erick", "Ernie", "Ernst", "Errol", "Ervin", "Erwin", "Esker", "Esley", "Essex", "Essie", "Estel", "Ester", "Estes", "Eston", "Ethan", "Ethel", "Ethen", "Evans", "Evert", "Ewald", "Ewart", "Ewell", "Ewing", "Ezell", "Faron", "Felix", "Fidel", "Finis", "Fleet", "Flint", "Flora", "Floyd", "Flynn", "Fount", "Frank", "Franz", "Fredy", "Fritz", "Gaige", "Galen", "Garey", "Garry", "Garth", "Gauge", "Gaven", "Gavin", "Gavyn", "Gayle", "Geary", "Genie", "Geoff", "Gerry", "Giles", "Glenn", "Glynn", "Gorge", "Grace", "Grady", "Grant", "Green", "Gregg", "Grove", "Guido", "Haden", "Hakim", "Hamza", "Handy", "Hardy", "Harry", "Harve", "Harvy", "Hasan", "Haven", "Hayes", "Hazel", "Hazen", "Heath", "Heber", "Helen", "Hence", "Henri", "Henry", "Hideo", "Hiram", "Holly", "Homer", "Hosea", "Hosie", "Hyman", "Hymen", "Hyrum", "Idris", "Illya", "Imran", "Irene", "Irven", "Irvin", "Irwin", "Isaac", "Isaak", "Isham", "Isiah", "Issac", "Ivory", "Jabez", "Jacky", "Jacob", "Jaden", "Jadon", "Jadyn", "Jahir", "Jaime", "Jairo", "Jakob", "Jalen", "Jalon", "Jamal", "Jamar", "Jamel", "James", "Jamey", "Jamie", "Jamil", "Jamin", "Jamir", "Janet", "Jarad", "Jared", "Jaren", "Jaret", "Jarod", "Jaron", "Jasen", "Jason", "Javen", "Javon", "Jaxen", "Jaxon", "Jayce", "Jayme", "Jayse", "Jemal", "Jerad", "Jered", "Jerel", "Jerod", "Jerry", "Jesse", "Jessy", "Jesus", "Jevon", "Jewel", "Jiles", "Jimmy", "Jodie", "Johan", "Johny", "Jonah", "Jonas", "Jones", "Jordi", "Jordy", "Jorge", "Josef", "Josue", "Jovan", "Joyce", "Judah", "Judge", "Juelz", "Jules", "Julia", "Julio", "Juwan", "Kabir", "Kaden", "Kadin", "Kadyn", "Kairo", "Kaleb", "Kalel", "Kalen", "Kanye", "Karen", "Karim", "Kasen", "Kasey", "Kason", "Kavon", "Kazuo", "Keanu", "Kegan", "Keion", "Keith", "Kelan", "Kelby", "Kelly", "Kenan", "Kenji", "Kenny", "Kenya", "Kenzo", "Kerry", "Kevan", "Keven", "Kevin", "Kevon", "Keyon", "Khari", "Khiry", "Kiaan", "Kiara", "Kieth", "Kiley", "Kinte", "Kirby", "Knute", "Kohen", "Kolby", "Korey", "Kraig", "Krish", "Kunta", "Kwame", "Kylan", "Kylen", "Kyler", "Kyree", "Kyrie", "Kyron", "Kyson", "Lacey", "Lamar", "Lance", "Lanny", "Laron", "Larry", "Larue", "Laura", "Lavar", "Lavon", "Layne", "Leigh", "Lemon", "Lenny", "Lenon", "Leona", "Leroy", "Levar", "Levie", "Levin", "Levon", "Lewis", "Lexie", "Linda", "Lindy", "Linus", "Linzy", "Lisle", "Lloyd", "Logan", "Loney", "Lonie", "Lonny", "Lonzo", "Loran", "Loren", "Lorin", "Lorne", "Louie", "Louis", "Lovie", "Loyal", "Lucas", "Lucca", "Lucio", "Lucky", "Luigi", "Lukas", "Lyman", "Lyric", "Mabel", "Maceo", "Major", "Makai", "Makhi", "Malik", "Mamie", "Manly", "Marco", "Maria", "Marie", "Mario", "Marlo", "Marsh", "Marty", "Masao", "Masen", "Mason", "Mateo", "Maude", "Maury", "Maxie", "Maxim", "Mearl", "Mekhi", "Merle", "Metro", "Meyer", "Micah", "Micky", "Mikal", "Mikel", "Milan", "Milas", "Miles", "Mills", "Miner", "Minor", "Mitch", "Monte", "Monty", "Moody", "Moses", "Moshe", "Murry", "Mykel", "Myles", "Myron", "Najee", "Nakia", "Namon", "Nancy", "Nasir", "Neely", "Nello", "Nevin", "Nicky", "Nigel", "Nikko", "Niles", "Nixon", "Noble", "Nolan", "Nolen", "North", "Oddie", "Odell", "Offie", "Ogden", "Oland", "Olive", "Ollie", "Omari", "Oneal", "Orion", "Orley", "Orlin", "Orren", "Orrie", "Orrin", "Orris", "Orson", "Orval", "Orvel", "Orvil", "Orvin", "Orvis", "Oscar", "Ossie", "Othel", "Ottie", "Ottis", "Ovila", "Owens", "Ozell", "Ozzie", "Pablo", "Paris", "Patsy", "Paulo", "Pearl", "Pedro", "Percy", "Perry", "Peter", "Philo", "Pleas", "Posey", "Pratt", "Press", "Price", "Pryor", "Quinn", "Quint", "Rahul", "Ralph", "Ramon", "Rance", "Randy", "Raoul", "Raven", "Rayan", "Reece", "Reese", "Regan", "Regis", "Reign", "Reino", "Reyes", "Rhett", "Rhoda", "Riaan", "Ricci", "Ricki", "Ricky", "Ridge", "Riley", "Rishi", "River", "Robby", "Robin", "Rocco", "Rocky", "Roddy", "Roger", "Rohan", "Rolla", "Rollo", "Roman", "Romeo", "Romie", "Ronal", "Ronan", "Ronin", "Ronny", "Rosco", "Rowan", "Rowen", "Royal", "Royce", "Ruben", "Rubin", "Rufus", "Rusty", "Ryder", "Ryker", "Rylan", "Rylee", "Rylen", "Ryley", "Saint", "Salem", "Samie", "Samir", "Sammy", "Sandy", "Santo", "Sarah", "Savon", "Scott", "Semaj", "Seven", "Shade", "Shane", "Shaun", "Shawn", "Shoji", "Silas", "Simon", "Slade", "Smith", "Solon", "Sonny", "Soren", "Stacy", "Steve", "Stone", "Storm", "Susan", "Susie", "Sylas", "Tadeo", "Talan", "Talen", "Talon", "Tammy", "Tandy", "Tarik", "Tariq", "Tatum", "Tavon", "Teddy", "Tegan", "Telly", "Terry", "Tevin", "Timmy", "Titan", "Titus", "Tobie", "Tobin", "Toivo", "Tomas", "Tomie", "Tommy", "Toney", "Torey", "Torin", "Torry", "Trace", "Tracy", "Trent", "Tripp", "Tyler", "Tylor", "Tyree", "Tyrek", "Tyrel", "Tyrik", "Tyrin", "Tyriq", "Tyron", "Tyrus", "Tyson", "Urban", "Uriah", "Uriel", "Vance", "Verle", "Verna", "Verne", "Vidal", "Vince", "Viola", "Virge", "Waino", "Waldo", "Wally", "Wayde", "Wayne", "Wells", "Wiley", "Willy", "Woody", "Worth", "Wyatt", "Wylie", "Wyman", "Yahir", "Yahya", "Yancy", "Yosef", "Young", "Yurem", "Yusuf", "Zahir", "Zaire", "Zakai", "Zayne", "Zenas"]
id = 1
roles = ["Software Engineer", "Intelligence Officer", "Project Manager", "Designer", "Security Engineer", "Frequency Transmission Systems"]
roles_percentage = [0.25, 0.15, 0.15, 0.05, 0.25, 0.15]
cats = ["pm", "code", "database", "network", "graphic", "multimedia", "classified", "social", "email", "internal"]

all_users = []
for each_name in names:
    user = {}
    user["name"] = each_name
    user['id'] = id
    id += 1
    if id < len(names) * roles_percentage[0]:

        # Software Engineers
        user["role"] = roles[0]
        # 95% of Software Engineers will be normal
        coin_toss = random.randint(1, 100)
        if coin_toss <= 95:
            # code, database, network, graphic, email, internal
            available_pool = 98
            code = random.randint(40, available_pool-25)
            available_pool -= code

            database = int(available_pool/(random.random()*2.2+2.7))
            available_pool -= database

            network = random.randint(0, available_pool//2)
            available_pool -= network
            graphic = random.randint(0, available_pool//3)
            available_pool -= graphic
            email = random.randint(0, available_pool//2)
            available_pool -= email
            internal = random.randint(0, available_pool)
            available_pool -= internal
            user['code'] = code
            user['database'] = database
            user['network'] = network
            user['graphic'] = graphic
            user['email'] = email
            user['internal'] = internal
            # Distribute the remaining available_pool randomly with the missing cats
            available_pool += 2
            for each_cat in cats:
                if each_cat not in user:
                    user[each_cat] = random.randint(0, available_pool)
                    available_pool -= user[each_cat]
            user['code'] += available_pool
            all_users.append(user)
        # 2 % will be potential anomaly
        elif coin_toss <= 97:
            available_pool = 100
            code = random.randint(25, 45)
            available_pool -= code
            classified = random.randint(0, available_pool//6)
            available_pool -= classified
            database = random.randint(0, available_pool//2)
            available_pool -= database
            internal = random.randint(0, available_pool//2)
            available_pool -= internal
            email = random.randint(0, available_pool//2)
            available_pool -= email
            network = random.randint(0, available_pool//1.5)
            available_pool -= network
            pm = random.randint(0, available_pool//1.5)
            available_pool -= pm
            graphic = random.randint(0, available_pool//2)
            available_pool -= graphic
            social = random.randint(0, available_pool)
            available_pool -= social
            user['code'] = code
            user['classified'] = classified
            user['database'] = database
            user['internal'] = internal
            user['email'] = email
            user['network'] = network
            user['pm'] = pm
            user['graphic'] = graphic
            user['social'] = social
            user['multimedia'] = available_pool
            all_users.append(user)
        else: # super threat
            available_pool = 100
            code = random.randint(5, 25)
            available_pool -= code
            classified = random.randint(25, 50)
            available_pool -= classified
            database = random.randint(0, available_pool//2)
            available_pool -= database
            internal = random.randint(0, available_pool)
            available_pool -= internal
            email = random.randint(0, available_pool//2)
            available_pool -= email
            network = random.randint(0, available_pool//1.5)
            available_pool -= network
            pm = random.randint(0, available_pool//1.5)
            available_pool -= pm
            graphic = random.randint(0, available_pool//2)
            available_pool -= graphic
            social = random.randint(0, available_pool)
            available_pool -= social
            user['code'] = code
            user['classified'] = classified
            user['database'] = database
            user['internal'] = internal
            user['email'] = email
            user['network'] = network
            user['pm'] = pm
            user['graphic'] = graphic
            user['social'] = social
            user['multimedia'] = available_pool
            all_users.append(user)
    elif id < len(names) * roles_percentage[0] + len(names) * roles_percentage[1]:
        # Intelligence Officers
        user["role"] = roles[1]
        # 98% of Intelligence Officers will be normal
        coin_toss = random.randint(1, 100)
        if coin_toss <= 98:
            # cats = ["pm", "code", "database", "network", "graphic", "multimedia", "classified", "social", "email", "internal"]
            available_pool = 100
            classified = random.randint(30, 60)
            available_pool -= classified
            internal = random.randint(0, available_pool//1.5)
            available_pool -= internal
            database = random.randint(0, available_pool//2)
            available_pool -= database
            email = random.randint(0, available_pool//2)
            available_pool -= email
            pm = random.randint(0, available_pool)
            available_pool -= pm
            network = random.randint(0, available_pool//2)
            available_pool -= network
            graphic = random.randint(0, available_pool//2)
            available_pool -= graphic
            social = random.randint(0, available_pool)
            available_pool -= social
            code = random.randint(0, available_pool//2)
            available_pool -= code
            user['classified'] = classified
            user['internal'] = internal
            user['database'] = database
            user['email'] = email
            user['pm'] = pm
            user['network'] = network
            user['graphic'] = graphic
            user['social'] = social
            user['multimedia'] = available_pool
            user['code'] = code
            all_users.append(user)
        else:
            available_pool = 100
            code = random.randint(15, available_pool//2)
            available_pool -= code
            classified = random.randint(20, available_pool//2)
            available_pool -= classified
            network = random.randint(0, available_pool//2)
            available_pool -= network
            graphic = random.randint(0, available_pool//2)
            available_pool -= graphic
            email = random.randint(0, available_pool//2)
            available_pool -= email
            internal = random.randint(0, available_pool//2)
            available_pool -= internal
            pm = random.randint(0, available_pool)
            available_pool -= pm
            database = random.randint(0, available_pool//2)
            available_pool -= database
            social = random.randint(0, available_pool)
            available_pool -= social
            user['code'] = code
            user['classified'] = classified
            user['network'] = network
            user['graphic'] = graphic
            user['email'] = email
            user['internal'] = internal
            user['pm'] = pm
            user['database'] = database
            user['social'] = social
            user['multimedia'] = available_pool
            all_users.append(user)
    elif id < len(names) * roles_percentage[0] + len(names) * roles_percentage[1] + len(names) * roles_percentage[2]:
        # Project Manager
        user["role"] = roles[2]
        # 95% of Project Manager will be normal
        coin_toss = random.randint(1, 100)
        if coin_toss <= 95:
            available_pool = 100
            pm = random.randint(50, 80)
            available_pool -= pm
            email = random.randint(0, available_pool//2)
            available_pool -= email
            classified = random.randint(0, available_pool//5)
            available_pool -= classified
            internal = random.randint(0, available_pool)
            available_pool -= internal
            multimedia = random.randint(0, available_pool//2)
            available_pool -= multimedia
            social = random.randint(0, available_pool)
            available_pool -= social
            graphic = random.randint(0, available_pool//2)
            available_pool -= graphic
            code = random.randint(0, available_pool//2)
            available_pool -= code
            database = random.randint(0, available_pool//2)
            available_pool -= database
            network = random.randint(0, available_pool//2)
            available_pool -= network
            user['pm'] = pm + available_pool
            user['email'] = email
            user['classified'] = classified
            user['internal'] = internal
            user['multimedia'] = multimedia
            user['social'] = social
            user['code'] = code
            user['database'] = database
            user['network'] = network
            user['graphic'] = graphic
            all_users.append(user)
        else:
            available_pool = 100
            pm = random.randint(15, 60)
            available_pool -= pm
            code = random.randint(20, available_pool//1.5)
            available_pool -= code
            classified = random.randint(0, available_pool//5)
            available_pool -= classified
            network = random.randint(0, available_pool//2)
            available_pool -= network
            database = random.randint(0, available_pool//2)
            available_pool -= database
            email = random.randint(0, available_pool//2)
            available_pool -= email
            internal = random.randint(0, available_pool//2)
            available_pool -= internal
            multimedia = random.randint(0, available_pool//2)
            available_pool -= multimedia
            social = random.randint(0, available_pool)
            available_pool -= social
            graphic = random.randint(0, available_pool//2)
            available_pool -= graphic
            user['pm'] = pm
            user['code'] = code + available_pool
            user['classified'] = classified
            user['network'] = network
            user['database'] = database
            user['email'] = email
            user['internal'] = internal
            user['multimedia'] = multimedia
            user['social'] = social
            user['graphic'] = graphic
            all_users.append(user)
    elif id < len(names) * roles_percentage[0] + len(names) * roles_percentage[1] + len(names) * roles_percentage[2] + len(names) * roles_percentage[3]:
        # Designer
        user["role"] = roles[3]
        # 90% of Designer will be normal
        coin_toss = random.randint(1, 100)
        if coin_toss <= 90:
            available_pool = 100
            graphic = random.randint(60, 80)
            available_pool -= graphic
            multimedia = random.randint(available_pool//2, available_pool)
            available_pool -= multimedia
            social = random.randint(available_pool//2, available_pool)
            available_pool -= social
            email = random.randint(0, available_pool//2)
            available_pool -= email
            pm = random.randint(0, available_pool)
            available_pool -= pm
            internal = random.randint(0, available_pool)
            available_pool -= internal
            classified = random.randint(0, min(2, available_pool//5))
            available_pool -= classified
            code = 0
            database = 0
            network = 0
            graphic += available_pool
            user['graphic'] = graphic
            user['multimedia'] = multimedia
            user['social'] = social
            user['email'] = email
            user['pm'] = pm
            user['internal'] = internal
            user['classified'] = classified
            user['code'] = code
            user['database'] = database
            user['network'] = network
            all_users.append(user)
        else:
            available_pool = 100
            graphic = random.randint(15, 60)
            available_pool -= graphic
            multimedia = random.randint(0, available_pool//2)
            available_pool -= multimedia
            code = random.randint(0, available_pool//2)
            available_pool -= code
            internal = random.randint(0, available_pool//2)
            available_pool -= internal
            social = random.randint(0, available_pool//2)
            available_pool -= social
            email = random.randint(0, available_pool//2)
            available_pool -= email
            pm = random.randint(0, available_pool)
            available_pool -= pm
            classified = random.randint(0, available_pool//5)
            available_pool -= classified
            database = random.randint(0, available_pool//2)
            available_pool -= database
            network = random.randint(0, available_pool//2)
            available_pool -= network
            graphic += available_pool
            user['graphic'] = graphic
            user['multimedia'] = multimedia
            user['social'] = social
            user['email'] = email
            user['pm'] = pm
            user['internal'] = internal
            user['classified'] = classified
            user['code'] = code
            user['database'] = database
            user['network'] = network
            all_users.append(user)
    elif id < len(names) * roles_percentage[0] + len(names) * roles_percentage[1] + len(names) * roles_percentage[2] + len(names) * roles_percentage[3] + len(names) * roles_percentage[4]:
        # Security Engineer
        user["role"] = roles[4]
        # 98% of Security Engineer will be normal
        coin_toss = random.randint(1, 100)
        if coin_toss <= 98:
            available_pool = 100
            network = random.randint(60, 80)
            available_pool -= network
            internal = random.randint(available_pool//3, available_pool)
            available_pool -= internal
            database = random.randint(available_pool//2, available_pool)
            available_pool -= database
            classified = random.randint(0, available_pool//5)
            available_pool -= classified
            code = random.randint(0, available_pool//2)
            available_pool -= code
            multimedia = random.randint(0, available_pool//2)
            available_pool -= multimedia
            social = random.randint(0, available_pool)
            available_pool -= social
            graphic = random.randint(0, available_pool//2)
            available_pool -= graphic
            email = random.randint(0, available_pool//2)
            available_pool -= email
            pm = random.randint(0, available_pool)
            available_pool -= pm
            network += available_pool
            user['network'] = network
            user['internal'] = internal
            user['database'] = database
            user['classified'] = classified
            user['code'] = code
            user['multimedia'] = multimedia
            user['social'] = social
            user['graphic'] = graphic
            user['email'] = email
            user['pm'] = pm
            all_users.append(user)
        else:
            available_pool = 100
            network = random.randint(15, 50)
            available_pool -= network
            classified = random.randint(10, available_pool//2)
            available_pool -= classified
            database = random.randint(0, available_pool//1.4)
            available_pool -= database
            code = random.randint(available_pool//3, available_pool)
            available_pool -= code
            multimedia = random.randint(0, available_pool//2)
            available_pool -= multimedia
            social = random.randint(0, available_pool//2)
            available_pool -= social
            graphic = random.randint(0, available_pool//2)
            available_pool -= graphic
            email = random.randint(0, available_pool//2)
            available_pool -= email
            pm = random.randint(0, available_pool)
            available_pool -= pm
            network += available_pool//2
            available_pool -= available_pool//2
            classified += available_pool
            user['network'] = network
            user['classified'] = classified
            user['database'] = database
            user['code'] = code
            user['multimedia'] = multimedia
            user['social'] = social
            user['graphic'] = graphic
            user['email'] = email
            user['pm'] = pm
            all_users.append(user)
    else:
        # Frequency Transmission Systems
        user["role"] = roles[5]
        # all FT Systems will be normal
        available_pool = 100
        network = random.randint(80, available_pool)
        available_pool -= network
        user["network"] = network
        # distribute the rest of the available pool randomly among the other cats
        for cat in cats:
            if cat != "network":
                user[cat] = random.randint(0, available_pool//2)
                available_pool -= user[cat]
        user['network'] += available_pool
        all_users.append(user)

# write the all_users list to a .csv file where the rows are the user data and the columns are the dictionary keys
def write_csv(list_of_dictionaries, filename):
    with open(filename, 'w') as csvfile:
        fieldnames = list_of_dictionaries[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for each_dict in list_of_dictionaries:
            writer.writerow(each_dict)

write_csv(all_users, 'cat_daily.csv')