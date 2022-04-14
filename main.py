import random
# Run Data Collection

roles = ["Cable and Antenna Systems", "Client Systems", "Computer Systems Programming", "Cyber Systems Operations",
        "Intelligence Analyst", "Intelligence Officer", "Developmental Engineer", "Fusion Analyst", "Software Engineer",
        "Radio Frequency Transmission Systems", "Cybersecurity Developer", "Security Engineer", "Cyber Warfare Operations Officer"]

max_threat_scores = [40, 30, 60, 70, 60, 100, 70, 35, 60, 40, 80, 80, 80, 100]

names = ["Aaden", "Oscar", "Aarav", "Aaron", "Aayan", "Abbie", "Abdul", "Abner", "Abram", "Adams", "Addie", "Adlai", "Adolf", "Adron", "Aedan", "Agnes", "Ahmad", "Ahmed", "Ahmir", "Aidan", "Aiden", "Aidyn", "Akeem", "Akira", "Albin", "Alcee", "Alden", "Aleck", "Alfie", "Alger", "Algie", "Algot", "Alice", "Allan", "Allen", "Allie", "Allyn", "Almer", "Almon", "Almus", "Alois", "Aloys", "Alpha", "Alton", "Alvah", "Alvan", "Alver", "Alvia", "Alvie", "Alvin", "Alvis", "Alwin", "Amado", "Amare", "Amari", "Amasa", "Ameer", "Amias", "Ammon", "Ancel", "Ancil", "Andon", "Andra", "Andre", "Angel", "Angus", "Annie", "Ansel", "Anson", "Anton", "Anwar", "Arbie", "Arden", "Arian", "Ariel", "Aries", "Arjun", "Arlan", "Arlen", "Arley", "Arlie", "Arlin", "Arlis", "Arlyn", "Arman", "Armin", "Arnav", "Arnie", "Arron", "Artie", "Artis", "Arvel", "Arvid", "Arvil", "Arvin", "Aryan", "Ashby", "Asher", "Atlas", "Aubra", "Audie", "Autry", "Avery", "Axton", "Ayaan", "Aydan", "Ayden", "Aydin", "Aziel", "Baker", "Banks", "Baron", "Barry", "Basil", "Benji", "Benny", "Berry", "Beryl", "Betty", "Bilal", "Billy", "Bjorn", "Blain", "Blair", "Blake", "Blane", "Blaze", "Bliss", "Bobby", "Boden", "Bodhi", "Bodie", "Boone", "Boris", "Bowen", "Bowie", "Boyce", "Brady", "Brain", "Brant", "Brent", "Brett", "Brian", "Briar", "Brice", "Brien", "Brion", "Britt", "Brock", "Brody", "Brook", "Brown", "Bruce", "Bruno", "Bryan", "Bryce", "Bryon", "Buddy", "Buell", "Buren", "Burke", "Burns", "Butch", "Bynum", "Byron", "Caden", "Cairo", "Caleb", "Calum", "Carey", "Carlo", "Carol", "Casen", "Casey", "Cason", "Cecil", "Cesar", "Chace", "Chadd", "Chaim", "Champ", "Chase", "Chevy", "Chris", "Chuck", "Clabe", "Clair", "Clara", "Clare", "Clark", "Claud", "Claus", "Clell", "Cleon", "Cleve", "Clide", "Cliff", "Clint", "Clive", "Cloyd", "Clyde", "Codey", "Codie", "Cohen", "Colby", "Coley", "Colie", "Colin", "Colon", "Conor", "Corey", "Corry", "Cosmo", "Craig", "Creed", "Cyril", "Cyrus", "Daisy", "Damon", "Danny", "Dante", "Darby", "Darcy", "Daren", "Darin", "Dario", "Daron", "Darry", "Daryl", "Daryn", "Davey", "David", "Davie", "Davin", "Davis", "Davon", "Dayne", "Deane", "Debra", "Deion", "Dejon", "Della", "Delos", "Denis", "Denny", "Derek", "Deric", "Derik", "Deron", "Deryl", "Devan", "Deven", "Devin", "Devon", "Devyn", "Dewey", "Dhruv", "Diane", "Diego", "Dijon", "Dilan", "Dixie", "Dixon", "Dolph", "Donal", "Donat", "Donna", "Donny", "Donta", "Donte", "Doris", "Doyle", "Drake", "Drury", "Duane", "Duard", "Dusty", "Dwain", "Dwane", "Dylan", "Dylon", "Earle", "Early", "Eason", "Ebbie", "Ebert", "Eddie", "Edgar", "Edith", "Edmon", "Edsel", "Edson", "Edwin", "Effie", "Efrem", "Efren", "Einar", "Elden", "Elder", "Eldon", "Elgie", "Elgin", "Elian", "Elias", "Elick", "Eliel", "Eliga", "Elige", "Elihu", "Eliot", "Eliza", "Ellen", "Ellie", "Ellis", "Elmer", "Elroy", "Elsie", "Elton", "Elvie", "Elvin", "Elvis", "Elwin", "Elwyn", "Elzie", "Emery", "Emett", "Emile", "Emmet", "Emmit", "Emory", "Ennis", "Enoch", "Erich", "Erick", "Ernie", "Ernst", "Errol", "Ervin", "Erwin", "Esker", "Esley", "Essex", "Essie", "Estel", "Ester", "Estes", "Eston", "Ethan", "Ethel", "Ethen", "Evans", "Evert", "Ewald", "Ewart", "Ewell", "Ewing", "Ezell", "Faron", "Felix", "Fidel", "Finis", "Fleet", "Flint", "Flora", "Floyd", "Flynn", "Fount", "Frank", "Franz", "Fredy", "Fritz", "Gaige", "Galen", "Garey", "Garry", "Garth", "Gauge", "Gaven", "Gavin", "Gavyn", "Gayle", "Geary", "Genie", "Geoff", "Gerry", "Giles", "Glenn", "Glynn", "Gorge", "Grace", "Grady", "Grant", "Green", "Gregg", "Grove", "Guido", "Haden", "Hakim", "Hamza", "Handy", "Hardy", "Harry", "Harve", "Harvy", "Hasan", "Haven", "Hayes", "Hazel", "Hazen", "Heath", "Heber", "Helen", "Hence", "Henri", "Henry", "Hideo", "Hiram", "Holly", "Homer", "Hosea", "Hosie", "Hyman", "Hymen", "Hyrum", "Idris", "Illya", "Imran", "Irene", "Irven", "Irvin", "Irwin", "Isaac", "Isaak", "Isham", "Isiah", "Issac", "Ivory", "Jabez", "Jacky", "Jacob", "Jaden", "Jadon", "Jadyn", "Jahir", "Jaime", "Jairo", "Jakob", "Jalen", "Jalon", "Jamal", "Jamar", "Jamel", "James", "Jamey", "Jamie", "Jamil", "Jamin", "Jamir", "Janet", "Jarad", "Jared", "Jaren", "Jaret", "Jarod", "Jaron", "Jasen", "Jason", "Javen", "Javon", "Jaxen", "Jaxon", "Jayce", "Jayme", "Jayse", "Jemal", "Jerad", "Jered", "Jerel", "Jerod", "Jerry", "Jesse", "Jessy", "Jesus", "Jevon", "Jewel", "Jiles", "Jimmy", "Jodie", "Johan", "Johny", "Jonah", "Jonas", "Jones", "Jordi", "Jordy", "Jorge", "Josef", "Josue", "Jovan", "Joyce", "Judah", "Judge", "Juelz", "Jules", "Julia", "Julio", "Juwan", "Kabir", "Kaden", "Kadin", "Kadyn", "Kairo", "Kaleb", "Kalel", "Kalen", "Kanye", "Karen", "Karim", "Kasen", "Kasey", "Kason", "Kavon", "Kazuo", "Keanu", "Kegan", "Keion", "Keith", "Kelan", "Kelby", "Kelly", "Kenan", "Kenji", "Kenny", "Kenya", "Kenzo", "Kerry", "Kevan", "Keven", "Kevin", "Kevon", "Keyon", "Khari", "Khiry", "Kiaan", "Kiara", "Kieth", "Kiley", "Kinte", "Kirby", "Knute", "Kohen", "Kolby", "Korey", "Kraig", "Krish", "Kunta", "Kwame", "Kylan", "Kylen", "Kyler", "Kyree", "Kyrie", "Kyron", "Kyson", "Lacey", "Lamar", "Lance", "Lanny", "Laron", "Larry", "Larue", "Laura", "Lavar", "Lavon", "Layne", "Leigh", "Lemon", "Lenny", "Lenon", "Leona", "Leroy", "Levar", "Levie", "Levin", "Levon", "Lewis", "Lexie", "Linda", "Lindy", "Linus", "Linzy", "Lisle", "Lloyd", "Logan", "Loney", "Lonie", "Lonny", "Lonzo", "Loran", "Loren", "Lorin", "Lorne", "Louie", "Louis", "Lovie", "Loyal", "Lucas", "Lucca", "Lucio", "Lucky", "Luigi", "Lukas", "Lyman", "Lyric", "Mabel", "Maceo", "Major", "Makai", "Makhi", "Malik", "Mamie", "Manly", "Marco", "Maria", "Marie", "Mario", "Marlo", "Marsh", "Marty", "Masao", "Masen", "Mason", "Mateo", "Maude", "Maury", "Maxie", "Maxim", "Mearl", "Mekhi", "Merle", "Metro", "Meyer", "Micah", "Micky", "Mikal", "Mikel", "Milan", "Milas", "Miles", "Mills", "Miner", "Minor", "Mitch", "Monte", "Monty", "Moody", "Moses", "Moshe", "Murry", "Mykel", "Myles", "Myron", "Najee", "Nakia", "Namon", "Nancy", "Nasir", "Neely", "Nello", "Nevin", "Nicky", "Nigel", "Nikko", "Niles", "Nixon", "Noble", "Nolan", "Nolen", "North", "Oddie", "Odell", "Offie", "Ogden", "Oland", "Olive", "Ollie", "Omari", "Oneal", "Orion", "Orley", "Orlin", "Orren", "Orrie", "Orrin", "Orris", "Orson", "Orval", "Orvel", "Orvil", "Orvin", "Orvis", "Oscar", "Ossie", "Othel", "Ottie", "Ottis", "Ovila", "Owens", "Ozell", "Ozzie", "Pablo", "Paris", "Patsy", "Paulo", "Pearl", "Pedro", "Percy", "Perry", "Peter", "Philo", "Pleas", "Posey", "Pratt", "Press", "Price", "Pryor", "Quinn", "Quint", "Rahul", "Ralph", "Ramon", "Rance", "Randy", "Raoul", "Raven", "Rayan", "Reece", "Reese", "Regan", "Regis", "Reign", "Reino", "Reyes", "Rhett", "Rhoda", "Riaan", "Ricci", "Ricki", "Ricky", "Ridge", "Riley", "Rishi", "River", "Robby", "Robin", "Rocco", "Rocky", "Roddy", "Roger", "Rohan", "Rolla", "Rollo", "Roman", "Romeo", "Romie", "Ronal", "Ronan", "Ronin", "Ronny", "Rosco", "Rowan", "Rowen", "Royal", "Royce", "Ruben", "Rubin", "Rufus", "Rusty", "Ryder", "Ryker", "Rylan", "Rylee", "Rylen", "Ryley", "Saint", "Salem", "Samie", "Samir", "Sammy", "Sandy", "Santo", "Sarah", "Savon", "Scott", "Semaj", "Seven", "Shade", "Shane", "Shaun", "Shawn", "Shoji", "Silas", "Simon", "Slade", "Smith", "Solon", "Sonny", "Soren", "Stacy", "Steve", "Stone", "Storm", "Susan", "Susie", "Sylas", "Tadeo", "Talan", "Talen", "Talon", "Tammy", "Tandy", "Tarik", "Tariq", "Tatum", "Tavon", "Teddy", "Tegan", "Telly", "Terry", "Tevin", "Timmy", "Titan", "Titus", "Tobie", "Tobin", "Toivo", "Tomas", "Tomie", "Tommy", "Toney", "Torey", "Torin", "Torry", "Trace", "Tracy", "Trent", "Tripp", "Tyler", "Tylor", "Tyree", "Tyrek", "Tyrel", "Tyrik", "Tyrin", "Tyriq", "Tyron", "Tyrus", "Tyson", "Urban", "Uriah", "Uriel", "Vance", "Verle", "Verna", "Verne", "Vidal", "Vince", "Viola", "Virge", "Waino", "Waldo", "Wally", "Wayde", "Wayne", "Wells", "Wiley", "Willy", "Woody", "Worth", "Wyatt", "Wylie", "Wyman", "Yahir", "Yahya", "Yancy", "Yosef", "Young", "Yurem", "Yusuf", "Zahir", "Zaire", "Zakai", "Zayne", "Zenas"]

all_users = []

id = 1
for each_name in names:
    user_obj = {}
    user_obj['name'] = each_name
    user_obj['id'] = id
    # user's role will be a random index from array roles
    role_index = random.randint(0, len(roles) - 1)
    user_obj['role'] = roles[role_index]
    individual_threat_score = random.randint(max_threat_scores[role_index]-20, max_threat_scores[role_index])
    user_obj['threatscore'] = individual_threat_score
    id += 1
    all_users.append(user_obj)

# Done with user creation

# TODO: COMPILE URLS, TITLES, CATEGORIES
URLS = []
CATS = []
TITL = []

def browse_generator(bid, uid):
    global URLS
    global CATS
    global TITL
    browse_obj = {}
    random_index = random.randint(0, len(URLS) - 1)
    browse_obj['url'] = URLS[random_index]
    browse_obj['title'] = TITL[random_index]
    browse_obj['category'] = CATS[random_index]
    browse_obj['date'] = "2022-{}-{} {}:{}:{}".format(random.randint(1, 3), random.randint(1, 28), random.randint(0, 23), random.randint(0, 59), random.randint(0, 59))
    browse_obj['id'] = bid
    browse_obj['uid'] = uid
    return browse_obj


all_users_browse = []
browse_id = 1
for each_user in all_users:
    random_number = random.randint(1, 100)

    # 75% of users will have a browse history
    if random_number <= 75:
        browse_data = browse_generator(browse_id, each_user['id'])
        browse_id += 1
        all_users_browse.append(browse_data)

        # After a user has a browse history, they will have a random number of browses based on %
        while random.randint(0, 1) == 0:
            browse_data = browse_generator(browse_id, each_user['id'])
            browse_id += 1
            all_users_browse.append(browse_data)

# Done with browse history

def incident_generator(iid, uid):
    sev = ["LOW", "MEDIUM", "HIGH"]
    incident_obj = {}
    incident_obj['id'] = iid
    incident_obj['uid'] = uid
    incident_obj['date'] = "2022-{}-{} {}:{}:{}".format(random.randint(1, 3), random.randint(1, 28), random.randint(0, 23), random.randint(0, 59), random.randint(0, 59))
    incident_obj['description'] = "Incident {} description".format(iid)
    incident_obj['severity'] = sev[random.randint(0, 2)]
    incident_obj['reportedby'] = names[random.randint(0, len(names) - 1)]

all_users_incidents = []
incident_id = 1
for each_user in all_users:
    random_number = random.randint(1, 100)

    # 5% of users will have an incident history
    if random_number <= 5:
        incident_data = incident_generator(incident_id, each_user['id'])
        incident_id += 1
        all_users_incidents.append(incident_data)

        # 10% of users will have more than 1 incident
        while random.randint(1, 100) <= 10:
            incident_data = incident_generator(incident_id, each_user['id'])
            incident_id += 1
            all_users_incidents.append(incident_data)

# Done with incident history