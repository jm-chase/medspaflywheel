#!/usr/bin/env python3
"""
Generate location-specific landing pages from template
"""

# Location data for all Southeast cities
LOCATIONS = {
    'FL': {
        'name': 'Florida',
        'cities': [
            {
                'name': 'Miami', 'slug': 'miami-fl',
                'neighborhoods': ['Brickell', 'Coral Gables', 'Coconut Grove', 'South Beach', 'Wynwood'],
                'nearby_cities': ['Fort Lauderdale', 'Hollywood', 'Coral Springs', 'Pembroke Pines', 'Hialeah'],
                'suburbs': ['Kendall', 'Doral', 'Aventura', 'Pinecrest', 'Key Biscayne'],
                'population': '6.1M', 'median_income': '$57,000', 'target_age': '42',
                'lat': '25.7617', 'lon': '-80.1918'
            },
            {
                'name': 'Orlando', 'slug': 'orlando-fl',
                'neighborhoods': ['Downtown', 'Winter Park', 'College Park', 'Baldwin Park', 'Thornton Park'],
                'nearby_cities': ['Kissimmee', 'Sanford', 'Altamonte Springs', 'Winter Park', 'Oviedo'],
                'suburbs': ['Lake Nona', 'Dr. Phillips', 'Windermere', 'Celebration', 'Winter Garden'],
                'population': '2.7M', 'median_income': '$55,000', 'target_age': '38',
                'lat': '28.5383', 'lon': '-81.3792'
            },
            {
                'name': 'Tampa', 'slug': 'tampa-fl',
                'neighborhoods': ['Hyde Park', 'South Tampa', 'Westshore', 'Channelside', 'Seminole Heights'],
                'nearby_cities': ['St. Petersburg', 'Clearwater', 'Brandon', 'Largo', 'Palm Harbor'],
                'suburbs': ['Carrollwood', 'Town N Country', 'Lutz', 'Riverview', 'Wesley Chapel'],
                'population': '3.2M', 'median_income': '$56,000', 'target_age': '40',
                'lat': '27.9506', 'lon': '-82.4572'
            },
            {
                'name': 'Jacksonville', 'slug': 'jacksonville-fl',
                'neighborhoods': ['Riverside', 'San Marco', 'Avondale', 'Mandarin', 'Southside'],
                'nearby_cities': ['St. Augustine', 'Orange Park', 'Fernandina Beach', 'Ponte Vedra', 'Jacksonville Beach'],
                'suburbs': ['Nocatee', 'Fruit Cove', 'Fleming Island', 'Neptune Beach', 'Atlantic Beach'],
                'population': '1.6M', 'median_income': '$56,500', 'target_age': '39',
                'lat': '30.3322', 'lon': '-81.6557'
            },
            {
                'name': 'Fort Lauderdale', 'slug': 'fort-lauderdale-fl',
                'neighborhoods': ['Las Olas', 'Victoria Park', 'Lauderdale-by-the-Sea', 'Rio Vista', 'Harbor Beach'],
                'nearby_cities': ['Miami', 'Boca Raton', 'Pompano Beach', 'Hollywood', 'Deerfield Beach'],
                'suburbs': ['Plantation', 'Weston', 'Coral Springs', 'Davie', 'Parkland'],
                'population': '6.1M', 'median_income': '$61,000', 'target_age': '43',
                'lat': '26.1224', 'lon': '-80.1373'
            },
            {
                'name': 'Naples', 'slug': 'naples-fl',
                'neighborhoods': ['Old Naples', 'Park Shore', 'Aqualane Shores', 'Port Royal', 'Coquina Sands'],
                'nearby_cities': ['Marco Island', 'Bonita Springs', 'Estero', 'Cape Coral', 'Fort Myers'],
                'suburbs': ['North Naples', 'Pelican Bay', 'Lely Resort', 'Golden Gate', 'Vineyards'],
                'population': '384K', 'median_income': '$78,000', 'target_age': '48',
                'lat': '26.1420', 'lon': '-81.7948'
            },
            {
                'name': 'Sarasota', 'slug': 'sarasota-fl',
                'neighborhoods': ['Downtown', 'St. Armands', 'Lido Key', 'Siesta Key', 'Longboat Key'],
                'nearby_cities': ['Bradenton', 'Venice', 'North Port', 'Englewood', 'Lakewood Ranch'],
                'suburbs': ['Palmer Ranch', 'Gulf Gate', 'Southgate', 'Fruitville', 'Bee Ridge'],
                'population': '836K', 'median_income': '$62,000', 'target_age': '47',
                'lat': '27.3364', 'lon': '-82.5307'
            },
            {
                'name': 'West Palm Beach', 'slug': 'west-palm-beach-fl',
                'neighborhoods': ['CityPlace', 'Northwood', 'Flamingo Park', 'South Olive', 'El Cid'],
                'nearby_cities': ['Palm Beach', 'Boca Raton', 'Delray Beach', 'Jupiter', 'Wellington'],
                'suburbs': ['Palm Beach Gardens', 'Royal Palm Beach', 'Lake Worth', 'Boynton Beach', 'Greenacres'],
                'population': '1.5M', 'median_income': '$62,000', 'target_age': '44',
                'lat': '26.7153', 'lon': '-80.0534'
            },
            {
                'name': 'Boca Raton', 'slug': 'boca-raton-fl',
                'neighborhoods': ['Mizner Park', 'Royal Palm', 'Boca West', 'Broken Sound', 'Spanish River'],
                'nearby_cities': ['Delray Beach', 'Deerfield Beach', 'Highland Beach', 'Boynton Beach', 'Coconut Creek'],
                'suburbs': ['West Boca', 'East Boca', 'Palmetto Park', 'Sandalfoot Cove', 'Glades'],
                'population': '98K', 'median_income': '$87,000', 'target_age': '46',
                'lat': '26.3683', 'lon': '-80.1289'
            },
            {
                'name': 'Clearwater', 'slug': 'clearwater-fl',
                'neighborhoods': ['Downtown', 'Clearwater Beach', 'Island Estates', 'Countryside', 'East Lake'],
                'nearby_cities': ['Tampa', 'St. Petersburg', 'Dunedin', 'Palm Harbor', 'Largo'],
                'suburbs': ['Safety Harbor', 'Belleair', 'Tarpon Springs', 'Oldsmar', 'Seminole'],
                'population': '117K', 'median_income': '$52,000', 'target_age': '41',
                'lat': '27.9659', 'lon': '-82.8001'
            }
        ]
    },
    'GA': {
        'name': 'Georgia',
        'cities': [
            {
                'name': 'Atlanta', 'slug': 'atlanta-ga',
                'neighborhoods': ['Buckhead', 'Midtown', 'Virginia-Highland', 'Inman Park', 'Old Fourth Ward'],
                'nearby_cities': ['Sandy Springs', 'Alpharetta', 'Marietta', 'Roswell', 'Johns Creek'],
                'suburbs': ['Dunwoody', 'Brookhaven', 'Decatur', 'Smyrna', 'Peachtree City'],
                'population': '6.1M', 'median_income': '$68,000', 'target_age': '37',
                'lat': '33.7490', 'lon': '-84.3880'
            },
            {
                'name': 'Savannah', 'slug': 'savannah-ga',
                'neighborhoods': ['Historic District', 'Ardsley Park', 'Midtown', 'Starland', 'Victorian District'],
                'nearby_cities': ['Pooler', 'Richmond Hill', 'Hinesville', 'Tybee Island', 'Port Wentworth'],
                'suburbs': ['Southbridge', 'Georgetown', 'Windsor Forest', 'Skidaway Island', 'Isle of Hope'],
                'population': '404K', 'median_income': '$54,000', 'target_age': '39',
                'lat': '32.0809', 'lon': '-81.0912'
            },
            {
                'name': 'Augusta', 'slug': 'augusta-ga',
                'neighborhoods': ['Downtown', 'Summerville', 'National Hills', 'West Augusta', 'Forest Hills'],
                'nearby_cities': ['Evans', 'Martinez', 'Grovetown', 'North Augusta', 'Hephzibah'],
                'suburbs': ['Columbia County', 'Fort Gordon', 'Harlem', 'Thomson', 'Waynesboro'],
                'population': '611K', 'median_income': '$47,000', 'target_age': '40',
                'lat': '33.4735', 'lon': '-82.0105'
            },
            {
                'name': 'Columbus', 'slug': 'columbus-ga',
                'neighborhoods': ['Midtown', 'Uptown', 'Downtown', 'North Columbus', 'South Columbus'],
                'nearby_cities': ['Phenix City', 'Fort Benning', 'LaGrange', 'Auburn', 'Opelika'],
                'suburbs': ['Midland', 'Harris County', 'Pine Mountain', 'Hamilton', 'Fortson'],
                'population': '328K', 'median_income': '$48,000', 'target_age': '38',
                'lat': '32.4609', 'lon': '-84.9877'
            },
            {
                'name': 'Sandy Springs', 'slug': 'sandy-springs-ga',
                'neighborhoods': ['Riverside', 'North River', 'High Point', 'Dunwoody Club', 'Spalding Drive'],
                'nearby_cities': ['Atlanta', 'Roswell', 'Dunwoody', 'Alpharetta', 'Marietta'],
                'suburbs': ['Perimeter Center', 'Abernathy', 'Brandon', 'Hammond', 'Riverside'],
                'population': '108K', 'median_income': '$82,000', 'target_age': '42',
                'lat': '33.9304', 'lon': '-84.3733'
            },
            {
                'name': 'Alpharetta', 'slug': 'alpharetta-ga',
                'neighborhoods': ['Downtown', 'Windward', 'Crabapple', 'Haynes Bridge', 'Milton'],
                'nearby_cities': ['Roswell', 'Johns Creek', 'Milton', 'Cumming', 'Duluth'],
                'suburbs': ['Forsyth County', 'Cherokee County', 'Fulton County', 'Gwinnett County', 'North Fulton'],
                'population': '65K', 'median_income': '$101,000', 'target_age': '40',
                'lat': '34.0754', 'lon': '-84.2941'
            },
            {
                'name': 'Athens', 'slug': 'athens-ga',
                'neighborhoods': ['Downtown', 'Five Points', 'Normaltown', 'Boulevard', 'Cobbham'],
                'nearby_cities': ['Watkinsville', 'Bogart', 'Jefferson', 'Winder', 'Commerce'],
                'suburbs': ['Oconee County', 'Winterville', 'Statham', 'Monroe', 'Lawrenceville'],
                'population': '210K', 'median_income': '$42,000', 'target_age': '32',
                'lat': '33.9519', 'lon': '-83.3576'
            }
        ]
    },
    'NC': {
        'name': 'North Carolina',
        'cities': [
            {
                'name': 'Charlotte', 'slug': 'charlotte-nc',
                'neighborhoods': ['Uptown', 'South End', 'Dilworth', 'Myers Park', 'NoDa'],
                'nearby_cities': ['Gastonia', 'Concord', 'Rock Hill', 'Huntersville', 'Matthews'],
                'suburbs': ['Ballantyne', 'SouthPark', 'University City', 'Plaza Midwood', 'Fort Mill'],
                'population': '2.7M', 'median_income': '$64,000', 'target_age': '36',
                'lat': '35.2271', 'lon': '-80.8431'
            },
            {
                'name': 'Raleigh', 'slug': 'raleigh-nc',
                'neighborhoods': ['Downtown', 'North Hills', 'Brier Creek', 'Midtown', 'Glenwood South'],
                'nearby_cities': ['Durham', 'Cary', 'Apex', 'Wake Forest', 'Holly Springs'],
                'suburbs': ['Morrisville', 'Garner', 'Knightdale', 'Clayton', 'Fuquay-Varina'],
                'population': '2.1M', 'median_income': '$68,000', 'target_age': '35',
                'lat': '35.7796', 'lon': '-78.6382'
            },
            {
                'name': 'Greensboro', 'slug': 'greensboro-nc',
                'neighborhoods': ['Downtown', 'Fisher Park', 'Irving Park', 'Westerwood', 'Adams Farm'],
                'nearby_cities': ['High Point', 'Winston-Salem', 'Burlington', 'Asheboro', 'Lexington'],
                'suburbs': ['Summerfield', 'Oak Ridge', 'Jamestown', 'Whitsett', 'Pleasant Garden'],
                'population': '774K', 'median_income': '$52,000', 'target_age': '38',
                'lat': '36.0726', 'lon': '-79.7920'
            },
            {
                'name': 'Durham', 'slug': 'durham-nc',
                'neighborhoods': ['Downtown', 'Brightleaf', 'Trinity Park', 'Duke Park', 'Hope Valley'],
                'nearby_cities': ['Raleigh', 'Chapel Hill', 'Cary', 'Hillsborough', 'Morrisville'],
                'suburbs': ['Research Triangle Park', 'Southpoint', 'North Durham', 'South Durham', 'East Durham'],
                'population': '644K', 'median_income': '$60,000', 'target_age': '34',
                'lat': '35.9940', 'lon': '-78.8986'
            },
            {
                'name': 'Winston-Salem', 'slug': 'winston-salem-nc',
                'neighborhoods': ['Downtown', 'Ardmore', 'West End', 'Reynolda', 'Buena Vista'],
                'nearby_cities': ['Greensboro', 'High Point', 'Kernersville', 'Clemmons', 'Lexington'],
                'suburbs': ['Lewisville', 'Tobaccoville', 'Rural Hall', 'Walkertown', 'Pfafftown'],
                'population': '695K', 'median_income': '$50,000', 'target_age': '39',
                'lat': '36.0999', 'lon': '-80.2442'
            },
            {
                'name': 'Asheville', 'slug': 'asheville-nc',
                'neighborhoods': ['Downtown', 'West Asheville', 'North Asheville', 'Biltmore Village', 'River Arts District'],
                'nearby_cities': ['Hendersonville', 'Black Mountain', 'Weaverville', 'Fletcher', 'Arden'],
                'suburbs': ['South Asheville', 'East Asheville', 'Swannanoa', 'Candler', 'Fairview'],
                'population': '462K', 'median_income': '$53,000', 'target_age': '41',
                'lat': '35.5951', 'lon': '-82.5515'
            },
            {
                'name': 'Cary', 'slug': 'cary-nc',
                'neighborhoods': ['Downtown', 'Preston', 'MacGregor', 'Lochmere', 'Amberly'],
                'nearby_cities': ['Raleigh', 'Apex', 'Morrisville', 'Holly Springs', 'Durham'],
                'suburbs': ['Regency', 'Weston', 'Jordan Lake', 'Carpenter', 'Kildaire'],
                'population': '175K', 'median_income': '$100,000', 'target_age': '41',
                'lat': '35.7915', 'lon': '-78.7811'
            },
            {
                'name': 'Chapel Hill', 'slug': 'chapel-hill-nc',
                'neighborhoods': ['Downtown', 'Southern Village', 'Glen Lennox', 'Carrboro', 'Eastgate'],
                'nearby_cities': ['Durham', 'Carrboro', 'Hillsborough', 'Pittsboro', 'Mebane'],
                'suburbs': ['Southern Village', 'Meadowmont', 'Falconbridge', 'Lake Forest', 'Timberlyne'],
                'population': '61K', 'median_income': '$66,000', 'target_age': '30',
                'lat': '35.9132', 'lon': '-79.0558'
            }
        ]
    },
    'SC': {
        'name': 'South Carolina',
        'cities': [
            {
                'name': 'Charleston', 'slug': 'charleston-sc',
                'neighborhoods': ['Downtown', 'West Ashley', 'James Island', 'Mount Pleasant', 'Daniel Island'],
                'nearby_cities': ['North Charleston', 'Mount Pleasant', 'Summerville', 'Goose Creek', 'Hanahan'],
                'suburbs': ['Johns Island', 'Folly Beach', 'Sullivan\'s Island', 'Isle of Palms', 'Kiawah Island'],
                'population': '802K', 'median_income': '$65,000', 'target_age': '39',
                'lat': '32.7765', 'lon': '-79.9311'
            },
            {
                'name': 'Columbia', 'slug': 'columbia-sc',
                'neighborhoods': ['Downtown', 'Shandon', 'Forest Acres', 'Rosewood', 'Five Points'],
                'nearby_cities': ['Irmo', 'Lexington', 'West Columbia', 'Cayce', 'Fort Jackson'],
                'suburbs': ['Northeast Columbia', 'Lake Murray', 'Harbison', 'St. Andrews', 'Dentsville'],
                'population': '838K', 'median_income': '$54,000', 'target_age': '36',
                'lat': '34.0007', 'lon': '-81.0348'
            },
            {
                'name': 'Greenville', 'slug': 'greenville-sc',
                'neighborhoods': ['Downtown', 'North Main', 'Augusta Road', 'Overbrook', 'Paris Mountain'],
                'nearby_cities': ['Spartanburg', 'Greer', 'Simpsonville', 'Mauldin', 'Easley'],
                'suburbs': ['Five Forks', 'Taylors', 'Wade Hampton', 'Berea', 'Travelers Rest'],
                'population': '928K', 'median_income': '$59,000', 'target_age': '38',
                'lat': '34.8526', 'lon': '-82.3940'
            },
            {
                'name': 'Myrtle Beach', 'slug': 'myrtle-beach-sc',
                'neighborhoods': ['Downtown', 'North Myrtle Beach', 'Surfside Beach', 'Garden City', 'Market Common'],
                'nearby_cities': ['Conway', 'Murrells Inlet', 'Pawleys Island', 'Georgetown', 'Little River'],
                'suburbs': ['Carolina Forest', 'Socastee', 'Red Hill', 'Forestbrook', 'Grande Dunes'],
                'population': '481K', 'median_income': '$49,000', 'target_age': '43',
                'lat': '33.6891', 'lon': '-78.8867'
            },
            {
                'name': 'Hilton Head', 'slug': 'hilton-head-sc',
                'neighborhoods': ['Sea Pines', 'Palmetto Dunes', 'Port Royal', 'Shipyard', 'Indigo Run'],
                'nearby_cities': ['Bluffton', 'Beaufort', 'Okatie', 'Hardeeville', 'Savannah'],
                'suburbs': ['Sun City', 'Spanish Wells', 'Moss Creek', 'Wexford', 'Long Cove'],
                'population': '225K', 'median_income': '$72,000', 'target_age': '52',
                'lat': '32.2163', 'lon': '-80.7526'
            }
        ]
    },
    'TN': {
        'name': 'Tennessee',
        'cities': [
            {
                'name': 'Nashville', 'slug': 'nashville-tn',
                'neighborhoods': ['Downtown', 'Gulch', 'Green Hills', '12 South', 'East Nashville'],
                'nearby_cities': ['Franklin', 'Brentwood', 'Murfreesboro', 'Hendersonville', 'Mount Juliet'],
                'suburbs': ['Cool Springs', 'Bellevue', 'Hermitage', 'Donelson', 'Antioch'],
                'population': '2.0M', 'median_income': '$64,000', 'target_age': '35',
                'lat': '36.1627', 'lon': '-86.7816'
            },
            {
                'name': 'Memphis', 'slug': 'memphis-tn',
                'neighborhoods': ['Downtown', 'Midtown', 'East Memphis', 'Germantown', 'Cooper-Young'],
                'nearby_cities': ['Germantown', 'Collierville', 'Bartlett', 'Southaven', 'Olive Branch'],
                'suburbs': ['Cordova', 'Lakeland', 'Arlington', 'Millington', 'Eads'],
                'population': '1.3M', 'median_income': '$49,000', 'target_age': '36',
                'lat': '35.1495', 'lon': '-90.0490'
            },
            {
                'name': 'Knoxville', 'slug': 'knoxville-tn',
                'neighborhoods': ['Downtown', 'Old City', 'Sequoyah Hills', 'Bearden', 'Fountain City'],
                'nearby_cities': ['Farragut', 'Oak Ridge', 'Maryville', 'Sevierville', 'Alcoa'],
                'suburbs': ['West Knoxville', 'Powell', 'Karns', 'Hardin Valley', 'Concord'],
                'population': '879K', 'median_income': '$52,000', 'target_age': '39',
                'lat': '35.9606', 'lon': '-83.9207'
            },
            {
                'name': 'Chattanooga', 'slug': 'chattanooga-tn',
                'neighborhoods': ['Downtown', 'North Shore', 'Southside', 'St. Elmo', 'Lookout Mountain'],
                'nearby_cities': ['Cleveland', 'Red Bank', 'East Ridge', 'Soddy-Daisy', 'Hixson'],
                'suburbs': ['Signal Mountain', 'Ooltewah', 'Harrison', 'Dalton', 'Fort Oglethorpe'],
                'population': '565K', 'median_income': '$53,000', 'target_age': '39',
                'lat': '35.0456', 'lon': '-85.3097'
            },
            {
                'name': 'Franklin', 'slug': 'franklin-tn',
                'neighborhoods': ['Downtown', 'Westhaven', 'Cool Springs', 'Fieldstone Farms', 'Sullivan Farms'],
                'nearby_cities': ['Brentwood', 'Spring Hill', 'Nashville', 'Nolensville', 'Thompson\'s Station'],
                'suburbs': ['Williamson County', 'Grassland', 'Arrington', 'Leipers Fork', 'College Grove'],
                'population': '83K', 'median_income': '$102,000', 'target_age': '42',
                'lat': '35.9251', 'lon': '-86.8689'
            }
        ]
    },
    'AL': {
        'name': 'Alabama',
        'cities': [
            {
                'name': 'Birmingham', 'slug': 'birmingham-al',
                'neighborhoods': ['Downtown', 'Highland Park', 'Forest Park', 'Mountain Brook', 'Homewood'],
                'nearby_cities': ['Hoover', 'Vestavia Hills', 'Homewood', 'Mountain Brook', 'Pelham'],
                'suburbs': ['Trussville', 'Alabaster', 'Chelsea', 'Gardendale', 'Irondale'],
                'population': '1.1M', 'median_income': '$53,000', 'target_age': '38',
                'lat': '33.5186', 'lon': '-86.8104'
            },
            {
                'name': 'Huntsville', 'slug': 'huntsville-al',
                'neighborhoods': ['Downtown', 'Five Points', 'Medical District', 'Twickenham', 'Jones Valley'],
                'nearby_cities': ['Madison', 'Decatur', 'Athens', 'Scottsboro', 'Arab'],
                'suburbs': ['Hampton Cove', 'South Huntsville', 'Research Park', 'Monte Sano', 'Redstone Arsenal'],
                'population': '491K', 'median_income': '$60,000', 'target_age': '37',
                'lat': '34.7304', 'lon': '-86.5861'
            },
            {
                'name': 'Montgomery', 'slug': 'montgomery-al',
                'neighborhoods': ['Downtown', 'Cloverdale', 'Old Alabama Town', 'Garden District', 'Capitol Heights'],
                'nearby_cities': ['Prattville', 'Millbrook', 'Wetumpka', 'Pike Road', 'Tallassee'],
                'suburbs': ['East Montgomery', 'Eastbrook', 'Dalraida', 'Chisholm', 'Taylor Crossing'],
                'population': '373K', 'median_income': '$50,000', 'target_age': '37',
                'lat': '32.3668', 'lon': '-86.3000'
            },
            {
                'name': 'Mobile', 'slug': 'mobile-al',
                'neighborhoods': ['Downtown', 'Midtown', 'Spring Hill', 'West Mobile', 'Oakleigh'],
                'nearby_cities': ['Daphne', 'Fairhope', 'Spanish Fort', 'Foley', 'Gulf Shores'],
                'suburbs': ['Tillman\'s Corner', 'Theodore', 'Semmes', 'Saraland', 'Chickasaw'],
                'population': '430K', 'median_income': '$48,000', 'target_age': '39',
                'lat': '30.6954', 'lon': '-88.0399'
            }
        ]
    },
    'VA': {
        'name': 'Virginia',
        'cities': [
            {
                'name': 'Virginia Beach', 'slug': 'virginia-beach-va',
                'neighborhoods': ['Oceanfront', 'Town Center', 'Hilltop', 'Great Neck', 'Sandbridge'],
                'nearby_cities': ['Norfolk', 'Chesapeake', 'Portsmouth', 'Suffolk', 'Hampton'],
                'suburbs': ['Kempsville', 'Lynnhaven', 'Princess Anne', 'Red Mill', 'Bayside'],
                'population': '1.8M', 'median_income': '$76,000', 'target_age': '37',
                'lat': '36.8529', 'lon': '-75.9780'
            },
            {
                'name': 'Richmond', 'slug': 'richmond-va',
                'neighborhoods': ['Downtown', 'Fan District', 'Carytown', 'Church Hill', 'Scott\'s Addition'],
                'nearby_cities': ['Glen Allen', 'Henrico', 'Midlothian', 'Short Pump', 'Mechanicsville'],
                'suburbs': ['West End', 'Innsbrook', 'Bon Air', 'Lakeside', 'Tuckahoe'],
                'population': '1.3M', 'median_income': '$66,000', 'target_age': '36',
                'lat': '37.5407', 'lon': '-77.4360'
            },
            {
                'name': 'Norfolk', 'slug': 'norfolk-va',
                'neighborhoods': ['Downtown', 'Ghent', 'Ocean View', 'Colonial Place', 'Larchmont'],
                'nearby_cities': ['Virginia Beach', 'Chesapeake', 'Portsmouth', 'Hampton', 'Newport News'],
                'suburbs': ['East Beach', 'Park Place', 'Wards Corner', 'Ballentine', 'Talbot Park'],
                'population': '1.8M', 'median_income': '$52,000', 'target_age': '35',
                'lat': '36.8508', 'lon': '-76.2859'
            },
            {
                'name': 'Chesapeake', 'slug': 'chesapeake-va',
                'neighborhoods': ['Greenbrier', 'Great Bridge', 'Western Branch', 'South Norfolk', 'Deep Creek'],
                'nearby_cities': ['Virginia Beach', 'Norfolk', 'Suffolk', 'Portsmouth', 'Hampton'],
                'suburbs': ['Hickory', 'Grassfield', 'Oak Grove', 'Indian River', 'Fentress'],
                'population': '249K', 'median_income': '$76,000', 'target_age': '38',
                'lat': '36.7682', 'lon': '-76.2875'
            },
            {
                'name': 'Arlington', 'slug': 'arlington-va',
                'neighborhoods': ['Clarendon', 'Ballston', 'Rosslyn', 'Crystal City', 'Pentagon City'],
                'nearby_cities': ['Alexandria', 'Falls Church', 'Fairfax', 'Bethesda', 'Tysons'],
                'suburbs': ['North Arlington', 'South Arlington', 'Columbia Pike', 'Shirlington', 'Cherrydale'],
                'population': '238K', 'median_income': '$120,000', 'target_age': '36',
                'lat': '38.8816', 'lon': '-77.0910'
            }
        ]
    }
}

def generate_location_page(city_data, state_abbrev, state_name):
    """Generate a location page from template"""
    
    # Read template
    with open('/home/user/medspaflywheel/location-template.html', 'r') as f:
        template = f.read()
    
    # Replace placeholders
    content = template
    
    # Basic replacements
    replacements = {
        '[CITY]': city_data['name'],
        '[STATE]': state_name,
        '[STATE_ABBREV]': state_abbrev,
        '[CITY_SLUG]': city_data['slug'],
        '[POPULATION]': city_data['population'],
        '[MEDIAN_INCOME]': city_data['median_income'],
        '[TARGET_AGE]': city_data['target_age'],
        '[LATITUDE]': city_data['lat'],
        '[LONGITUDE]': city_data['lon'],
    }
    
    for placeholder, value in replacements.items():
        content = content.replace(placeholder, value)
    
    # Replace neighborhoods
    for i in range(5):
        placeholder = f'[NEIGHBORHOOD_{i+1}]'
        value = city_data['neighborhoods'][i] if i < len(city_data['neighborhoods']) else f'Neighborhood {i+1}'
        content = content.replace(placeholder, value)
    
    # Replace nearby cities
    for i in range(5):
        placeholder = f'[NEARBY_CITY_{i+1}]'
        value = city_data['nearby_cities'][i] if i < len(city_data['nearby_cities']) else f'City {i+1}'
        content = content.replace(placeholder, value)
    
    # Replace suburbs
    for i in range(5):
        placeholder = f'[SUBURB_{i+1}]'
        value = city_data['suburbs'][i] if i < len(city_data['suburbs']) else f'Suburb {i+1}'
        content = content.replace(placeholder, value)
    
    # Replace generic placeholders with sensible defaults
    content = content.replace('[NEARBY_AREAS]', ', '.join(city_data['nearby_cities'][:3]))
    
    # Client placeholders (use generic examples)
    client_placeholders = {
        '[CLIENT_NAME_1]': f'{city_data["name"]} Aesthetics',
        '[CLIENT_NAME_2]': f'Elite MedSpa - {city_data["name"]}',
        '[CLIENT_NAME_3]': f'Radiance {city_data["name"]}',
        '[CLIENT_SLUG_1]': f'{city_data["slug"]}-aesthetics',
        '[CLIENT_SLUG_2]': f'elite-medspa-{city_data["slug"]}',
        '[CLIENT_SLUG_3]': f'radiance-{city_data["slug"]}',
        '[CHALLENGE_DESCRIPTION_1]': 'Struggling to fill appointment slots consistently',
        '[CHALLENGE_DESCRIPTION_2]': 'Low email open rates and client retention',
        '[CHALLENGE_DESCRIPTION_3]': 'Limited online reviews impacting local search ranking',
        '[RESULT_METRIC_1]': '210%',
        '[RESULT_METRIC_2]': '68%',
        '[RESULT_METRIC_3]': '94',
        '[RESULT_DESCRIPTION_1]': 'Increase in Monthly Bookings',
        '[RESULT_DESCRIPTION_2]': 'Email Conversion Rate',
        '[RESULT_DESCRIPTION_3]': 'New 5-Star Reviews in 90 Days',
        '[CASE_STUDY_SUMMARY_1]': f'Implemented targeted Google Ads campaign focusing on {city_data["name"]} metro area with remarkable results.',
        '[CASE_STUDY_SUMMARY_2]': 'Built automated email nurture sequence that converts consultations into long-term clients.',
        '[CASE_STUDY_SUMMARY_3]': 'Systematic review generation system that captures feedback from satisfied clients.'
    }
    
    for placeholder, value in client_placeholders.items():
        content = content.replace(placeholder, value)
    
    # Write file
    filename = f'/home/user/medspaflywheel/{city_data["slug"]}.html'
    with open(filename, 'w') as f:
        f.write(content)
    
    print(f'Generated: {filename}')
    return filename

def main():
    """Generate all location pages"""
    generated_files = []
    
    for state_abbrev, state_data in LOCATIONS.items():
        state_name = state_data['name']
        print(f'\nGenerating pages for {state_name}...')
        
        for city in state_data['cities']:
            filename = generate_location_page(city, state_abbrev, state_name)
            generated_files.append(filename)
    
    print(f'\n✓ Generated {len(generated_files)} location pages')
    return generated_files

if __name__ == '__main__':
    main()
