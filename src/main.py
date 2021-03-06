import csv
import random
import string
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
    print(user_obj)
    all_users.append(user_obj)

# Done with user creation

# TODO: COMPILE URLS, TITLES, CATEGORIES
URLS = ["github.com", "stackoverflow.com", "monday.com", "slack.com", "cyberforumleaks.com", "facebook.com", "coinbase.com", "fiver.com"]
CATS = ["code", "code", "pm", "pm", "breach", "social", "crypto", "hire"]
TITL = ["GitHub", "StackOverflow", "Monday", "Slack", "CyberforumLeaks", "Facebook", "crypto", "Fiver"]

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
        print(browse_data)

        # After a user has a browse history, they will have a random number of browses based on %
        while random.randint(0, 1) == 0:
            browse_data = browse_generator(browse_id, each_user['id'])
            browse_id += 1
            all_users_browse.append(browse_data)
            print(browse_data)

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
    return incident_obj

all_users_incidents = []
incident_id = 1
for each_user in all_users:
    random_number = random.randint(1, 100)

    # 5% of users will have an incident history
    if random_number <= 5:
        incident_data = incident_generator(incident_id, each_user['id'])
        incident_id += 1
        all_users_incidents.append(incident_data)
        print(incident_data)

        # 10% of users will have more than 1 incident
        while random.randint(1, 100) <= 10:
            incident_data = incident_generator(incident_id, each_user['id'])
            incident_id += 1
            all_users_incidents.append(incident_data)
            print(incident_data)

# Done with incident history
FILES = ['employees.xml', 'salaries.csv', 'password.txt', 'config.yaml', 'main.py', 'index.html', 'style.css', 'script.js', 'projectdeadlines.xml', 'confidential.docx', 'secret.docx', 'hidden.xml']
FILE_CATS = ['hr', 'hr', 'secret', 'code', 'code', 'code', 'code', 'code', 'pm', 'secret', 'secret', 'secret']
all_files_honeypot = []
hid = 1

def file_generator(fid, uid):
    global FILES
    global FILE_CATS
    global hid
    global all_files_honeypot

    file_obj = {}
    file_obj['id'] = fid
    file_obj['uid'] = uid

    m = random.randint(1, 3)
    d = random.randint(1, 28)
    h = random.randint(0, 23)
    mi = random.randint(0, 50)

    file_obj['start_date'] = "2022-{}-{} {}:{}:{}".format(m, d, h, mi, 0)
    # Ensure that the end date is after the start date
    file_obj['end_date'] = "2022-{}-{} {}:{}:{}".format(m, d, h, random.randint(51, 59), random.randint(0, 59))
    file_obj['action_type'] = "read"

    random_index = random.randint(0, len(FILES) - 1)

    prefix = random.choice(string.ascii_letters) + random.choice(string.digits)

    file_obj['file_path'] = prefix + FILES[random_index]
    file_obj['category'] = FILE_CATS[random_index]

    if file_obj['category'] == 'secret':
        honeypot_obj = {}
        honeypot_obj['id'] = hid
        hid += 1
        honeypot_obj['fid'] = fid
        honeypot_obj['severity'] = "HIGH"
        all_files_honeypot.append(honeypot_obj)
        print(honeypot_obj)
    
    return file_obj



all_user_files = []
file_id = 1
for each_user in all_users:
    random_number = random.randint(1, 100)

    # 50% of users will have a file
    if random_number <= 50:
        file_data = file_generator(file_id, each_user['id'])
        file_id += 1
        all_user_files.append(file_data)
        print(file_data)

        # 65% of users will have more than 1 file
        while random.randint(1, 100) <= 65:
            file_data = file_generator(file_id, each_user['id'])
            file_id += 1
            all_user_files.append(file_data)
            print(file_data)


def external_generator(eid, uid):
    device_names = ["UltraSSD 1TB", "Flashdrive", "iPhone X", "iPhone 13 Pro Max", "SD Card", "CD"]
    external_obj = {}
    external_obj['id'] = eid
    external_obj['uid'] = uid
    external_obj['date'] = "2022-{}-{} {}:{}:{}".format(random.randint(1, 3), random.randint(1, 28), random.randint(0, 23), random.randint(0, 59), random.randint(0, 59))
    external_obj['devicename'] = device_names[random.randint(0, len(device_names) - 1)]
    return external_obj

all_users_external = []
external_id = 1
for each_user in all_users:
    random_number = random.randint(1, 100)

    # 10% of users will have an external device
    if random_number <= 10:
        external_data = external_generator(external_id, each_user['id'])
        external_id += 1
        all_users_external.append(external_data)
        print(external_data)

        # 10% of users will have more than 1 external device
        while random.randint(1, 100) <= 10:
            external_data = external_generator(external_id, each_user['id'])
            external_id += 1
            all_users_external.append(external_data)
            print(external_data)


APPS = ['Excel', 'Word', 'Atom', 'VS Code', 'Jira', 'Adobe Photoshop', 'Adobe Illustrator', 'Node.js', 'Git', 'Wireshark', 'Metasploit', 'Slack']
APPS_CATS = ['hr', 'hr', 'code', 'code', 'pm', 'design', 'design', 'code', 'code', 'cyber', 'cyber', 'pm']

def application_generator(aid, uid):
    app_obj = {}
    app_obj['id'] = aid
    app_obj['uid'] = uid
    m = random.randint(1, 3)
    d = random.randint(1, 28)
    h = random.randint(0, 23)
    mi = random.randint(0, 35)

    app_obj['start_date'] = "2022-{}-{} {}:{}:{}".format(m, d, h, mi, 0)
    # Ensure that the end date is after the start date
    app_obj['end_date'] = "2022-{}-{} {}:{}:{}".format(m, d, h, random.randint(37, 59), random.randint(0, 59))

    random_index = random.randint(0, len(APPS) - 1)
    app_obj['app_name'] = APPS[random_index]
    app_obj['category'] = APPS_CATS[random_index]
    return app_obj

all_user_apps = []
app_id = 1
for each_user in all_users:
    random_number = random.randint(1, 100)

    # 10% of users will have an application
    if random_number <= 80:
        app_data = application_generator(app_id, each_user['id'])
        app_id += 1
        all_user_apps.append(app_data)
        print(app_data)

        # 10% of users will have more than 1 application
        while random.randint(1, 100) <= 65:
            app_data = application_generator(app_id, each_user['id'])
            app_id += 1
            all_user_apps.append(app_data)
            print(app_data)

def email_generator(eid, uid, username):
    messages = ["Lorem Ipsum is a bad example of messages", "Nate is the best", "We are big fans of Dr. Henrich and Oscar", "Click here to win the jackpot! https://win.com", "Your email was hacked! Click here to recover it: https://evil.com"]
    providers = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@aol.com", "@ussf.mil", "@ussf.mil", "@ussf.mil"]
    words = []
    for each_message in messages:
        words += each_message.split()
    
    random_words = random.sample(words, random.randint(5,8))
    
    email_obj = {}
    email_obj['id'] = eid
    email_obj['uid'] = uid
    email_obj['date'] = "2022-{}-{} {}:{}:{}".format(random.randint(1, 3), random.randint(1, 28), random.randint(0, 23), random.randint(0, 59), random.randint(0, 59))
    email_obj['message'] = ' '.join(random_words)
    email_obj['sender'] = username + "@ussf.mil"
    email_obj['recipient'] = random.choice(names) + random.choice(providers)
    # random float with 2 decimals between -1.0 to 1.0
    email_obj['sentiment'] = round(random.uniform(-1.0, 1.0), 2)
    email_obj['attachment'] = "false"

    # random number between 0 and 100
    # if <= 5, then email has attachment
    if random.randint(0, 100) <= 5:
        email_obj['attachment'] = "true"

    return email_obj

all_user_emails = []
email_id = 1
for each_user in all_users:
    random_number = random.randint(1, 100)

    # 100% of users will have an email
    if random_number <= 100:
        email_data = email_generator(email_id, each_user['id'], each_user['name'])
        email_id += 1
        all_user_emails.append(email_data)
        print(email_data)

        # 60% of users will have more than 1 email
        while random.randint(1, 100) <= 60:
            email_data = email_generator(email_id, each_user['id'], each_user['name'])
            email_id += 1
            all_user_emails.append(email_data)
            print(email_data)

# Takes a list of dictionaries
# and write a csv file for it.
# Each row in the csv file is one dictionary from the list.
# The keys of the dictionary are the column names.
def write_csv(list_of_dictionaries, filename):
    with open(filename, 'w') as csvfile:
        fieldnames = list_of_dictionaries[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for each_dict in list_of_dictionaries:
            writer.writerow(each_dict)

write_csv(all_users, 'users.csv')
write_csv(all_users_external, 'users_external.csv')
write_csv(all_user_apps, 'users_apps.csv')
write_csv(all_user_emails, 'users_emails.csv')
write_csv(all_user_files, 'users_files.csv')
write_csv(all_users_browse, 'users_browser.csv')
write_csv(all_users_incidents, 'users_incidents.csv')
write_csv(all_files_honeypot, 'files_honeypot.csv')