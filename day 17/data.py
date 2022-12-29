question_data = [
    {"text": "A slug's blood is green", "answer": "True"},
    {"text": "Aardvarks are nocturnal", "answer": "True"},
    {"text": "The Earth has two moons", "answer": "False"},
    {"text": "The planet Mars has an atmosphere", "answer": "True"},
    {"text": "The Sun is the brightest star in the sky", "answer": "True"},
    {"text": "A gallon of water weighs more than a gallon of milk", "answer": "False"},
    {"text": "Cheetahs are the fastest land animals", "answer": "True"},
    {"text": "A honey bee can fly at 25 miles per hour", "answer": "True"},
    {"text": "The average human heart beats 60 times per minute", "answer": "False"},
    {"text": "The Atlantic Ocean is the largest ocean on Earth", "answer": "False"},
    {"text": "The capital of Australia is Sydney", "answer": "False"},
    {"text": "The capital of Canada is Toronto", "answer": "False"},
    {"text": "The Amazon Rainforest is the largest rainforest in the world", "answer": "True"},
    {"text": "The polar bear is the largest land carnivore", "answer": "True"},
    {"text": "The human brain has more than 100 billion neurons", "answer": "True"},
    {"text": "The longest river in the world is the Nile River", "answer": "True"},
    {"text": "The Earth is the third planet from the Sun", "answer": "True"},
    {"text": "The element oxygen is the most abundant element in the Earth's atmosphere", "answer": "True"},
    {"text": "The core of the Earth is made up of iron and nickel", "answer": "True"},
    {"text": "The average human body contains 60% water", "answer": "False"},
    {"text": "The smallest bone in the human body is the stapes", "answer": "True"},
    {"text": "The Earth rotates around its axis once every 24 hours", "answer": "True"},
    {"text": "A bee has five eyes", "answer": "True"},
    {"text": "A rhinoceros has four horns", "answer": "False"},
    {"text": "The average human heart beats 72 times per minute", "answer": "False"},
    {"text": "The longest mountain range in the world is the Himalayas", "answer": "True"},
    {"text": "The speed of light is 186,000 miles per second", "answer": "True"},
    {"text": "The dinosaur Tyrannosaurus Rex was one of the largest land predators", "answer": "True"},
    {"text": "The blue whale is the largest animal ever to have lived on Earth",
     "answer": "True"},
    {"text": "The element gold is the most abundant element in the Earth's crust",
     "answer": "False"},
    {"text": "The hottest temperature ever recorded on Earth was 134°F", "answer": "False"},
    {"text": "The Coldest temperature ever recorded on Earth was -128°F", "answer": "True"},
    {"text": "The human brain is made up of more than 80 billion neurons", "answer": "True"},
    {"text": "The average human body has 206 bones", "answer": "True"},
    {"text": "The Earth is the fifth planet from the Sun", "answer": "False"},
    {"text": "The element oxygen is the most abundant element in the Earth's crust",
     "answer": "False"},
    {"text": "The smallest bone in the human body is the femur", "answer": "False"},
    {"text": "The Earth rotates around its axis once every 12 hours", "answer": "False"},
    {"text": "A bee has six eyes", "answer": "False"},
    {"text": "A rhinoceros has two horns", "answer": "False"},
    {"text": "The currency of Sweden is the Krona", "answer": "True"},
    {"text": "The capital of Austria is Vienna", "answer": "True"},
    {"text": "The currency of Turkey is the Lira", "answer": "True"},
    {"text": "The capital of Norway is Oslo", "answer": "True"},
    {"text": "The currency of Denmark is the Krone", "answer": "True"},
    {"text": "The capital of Finland is Helsinki", "answer": "True"},
    {"text": "The currency of Croatia is the Kuna", "answer": "True"},
    {"text": "The capital of Belgium is Brussels", "answer": "True"},
    {"text": "The currency of Romania is the Leu", "answer": "True"},
    {"text": "The capital of Czech Republic is Prague", "answer": "True"},
    {"text": "The currency of Bulgaria is the Lev", "answer": "True"},
    {"text": "The capital of Qatar is Doha", "answer": "True"},
    {"text": "The currency of Serbia is the Dinar", "answer": "True"},
    {"text": "The capital of Ukraine is Kiev", "answer": "True"},
    {"text": "The currency of Oman is the Rial", "answer": "True"},
    {"text": "The capital of Kazakhstan is Nur-Sultan", "answer": "True"},
    {"text": "The currency of Bahrain is the Dinar", "answer": "True"},
    {"text": "The capital of Sri Lanka is Colombo", "answer": "True"},
    {"text": "The currency of Kuwait is the Dinar", "answer": "True"},
    {"text": "The capital of Morocco is Rabat", "answer": "True"},
    {"text": "The currency of Pakistan is the Rupee", "answer": "True"},
    {"text": "The capital of Algeria is Algiers", "answer": "True"},
    {"text": "The currency of Egypt is the Pound", "answer": "True"},
    {"text": "The capital of Libya is Tripoli", "answer": "True"},
    {"text": "The currency of Iran is the Rial", "answer": "True"},
    {"text": "The capital of Tunisia is Tunis", "answer": "True"},
    {"text": "The currency of Jordan is the Dinar", "answer": "True"},
    {"text": "The average human heart beats 80 times per minute", "answer": "False"},
    {"text": "The longest mountain range in the world is the Andes", "answer": "False"},
    {"text": "The speed of light is 186,000 miles per minute", "answer": "False"},
    {"text": "The dinosaur Brachiosaurus was one of the largest land predators",
     "answer": "False"},
    {"text": "The blue whale is the smallest animal ever to have lived on Earth",
     "answer": "False"},
    {"text": "The element iron is the most abundant element in the Earth's crust", "answer": "True"},
    {"text": "The hottest temperature ever recorded on Earth was 134°C", "answer": "True"},
    {"text": "The Coldest temperature ever recorded on Earth was -135°F", "answer": "False"},
    {"text": "The human brain is made up of more than 100 billion neurons", "answer": "True"},
    {"text": "The average human body has 206 muscles", "answer": "False"},
    {"text": "The Earth is the third planet from the Moon", "answer": "False"},
    {"text": "The element nitrogen is the most abundant element in the Earth's atmosphere", "answer": "True"},
    {"text": "The smallest bone in the human body is the stapes", "answer": "True"},
    {"text": "The Earth rotates around its axis once every 24 hours", "answer": "True"},
    {"text": "A bee has four eyes", "answer": "False"},
    {"text": "A rhinoceros has three horns", "answer": "False"},
    {"text": "The average human heart beats 70 times per minute", "answer": "False"},
    {"text": "The longest mountain range in the world is the Rocky Mountains",
     "answer": "False"},
    {"text": "The speed of light is 186,000 miles per hour", "answer": "True"},
    {"text": "The dinosaur Triceratops was one of the largest land predators",
     "answer": "False"},
    {"text": "The blue whale is the second largest animal ever to have lived on Earth", "answer": "False"},
    {"text": "The element carbon is the most abundant element in the Earth's crust", "answer": "True"},
    {"text": "The hottest temperature ever recorded on Earth was 136°F", "answer": "False"},
    {"text": "The Coldest temperature ever recorded on Earth was -128°C", "answer": "False"},
    {"text": "The human brain is made up of more than 90 billion neurons", "answer": "True"},
    {"text": "The average human body has 206 bones", "answer": "True"},
    {"text": "The Earth is the fourth planet from the Sun", "answer": "True"},
    {"text": "The element oxygen is the most abundant element in the Earth's atmosphere", "answer": "True"},
    {"text": "The smallest bone in the human body is the patella", "answer": "False"},
    {"text": "The Earth rotates around its axis once every 36 hours", "answer": "False"},
    {"text": "A bee has four wings", "answer": "True"},
    {"text": "A rhinoceros has one horn", "answer": "True"},
    {"text": "The average human heart beats 65 times per minute", "answer": "False"},
    {"text": "The longest mountain range in the world is the Alps", "answer": "True"},
    {"text": "The speed of light is 186,000 miles per year", "answer": "False"},
    {"text": "The dinosaur Velociraptor was one of the largest land predators",
     "answer": "False"},
    {"text": "The blue whale is the third largest animal ever to have lived on Earth", "answer": "True"},
    {"text": "The element sulfur is the most abundant element in the Earth's crust",
     "answer": "False"},
    {"text": "The hottest temperature ever recorded on Earth was 135°C", "answer": "True"},
    {"text": "The Coldest temperature ever recorded on Earth was -129°F", "answer": "False"},
    {"text": "The human brain is made up of more than 75 billion neurons", "answer": "True"},
    {"text": "The average human body has 206 organs", "answer": "False"},
    {"text": "The Earth is the sixth planet from the Sun", "answer": "False"},
    {"text": "The element hydrogen is the most abundant element in the Earth's atmosphere", "answer": "False"},
    {"text": "The smallest bone in the human body is the malleus", "answer": "True"},
    {"text": "The Earth rotates around its axis once every 48 hours", "answer": "False"},
    {"text": "A bee has two wings", "answer": "False"},
    {"text": "A rhinoceros has two horns", "answer": "False"},
    {"text": "The average human heart beats 75 times per minute", "answer": "False"},
    {"text": "The longest mountain range in the world is the Appalachian Mountains", "answer": "True"},
    {"text": "The speed of light is 186,000 miles per day", "answer": "False"},
    {"text": "The dinosaur Stegosaurus was one of the largest land predators",
     "answer": "False"},
    {"text": "The blue whale is the largest mammal ever to have lived on Earth",
     "answer": "True"},
    {"text": "The element nitrogen is the most abundant element in the Earth's crust",
     "answer": "False"},
    {"text": "The hottest temperature ever recorded on Earth was 136°C", "answer": "True"},
    {"text": "The Coldest temperature ever recorded on Earth was -134°F", "answer": "False"},
    {"text": "The human brain is made up of more than 85 billion neurons", "answer": "True"},
    {"text": "The average human body has 206 muscles", "answer": "False"},
    {"text": "The Earth is the fifth planet from the Moon", "answer": "False"},
    {"text": "The element oxygen is the most abundant element in the Earth's core",
     "answer": "False"},
    {"text": "The smallest bone in the human body is the incus", "answer": "True"},
    {"text": "The Earth rotates around its axis once every 18 hours", "answer": "False"},
    {"text": "A bee has three eyes", "answer": "False"},
    {"text": "A rhinoceros has four horns", "answer": "False"},
    {"text": "The average human heart beats 85 times per minute", "answer": "False"},
    {"text": "The longest mountain range in the world is the Ural Mountains",
     "answer": "True"},
    {"text": "The speed of light is 186,000 miles per month", "answer": "False"},
    {"text": "The dinosaur Brontosaurus was one of the largest land predators",
     "answer": "False"},
    {"text": "The blue whale is the second smallest animal ever to have lived on Earth", "answer": "False"},
    {"text": "The element silicon is the most abundant element in the Earth's crust", "answer": "True"},
    {"text": "The hottest temperature ever recorded on Earth was 137°F", "answer": "False"},
    {"text": "The Coldest temperature ever recorded on Earth was -133°C", "answer": "False"},
    {"text": "The sky is blue", "answer": "True"},
    {"text": "Cats have four legs", "answer": "True"},
    {"text": "The capital of Russia is Moscow", "answer": "True"},
    {"text": "The Earth is the fifth planet from the Sun", "answer": "False"},
    {"text": "Dogs are mammals", "answer": "True"},
    {"text": "The Nile is the longest river in the world", "answer": "True"},
    {"text": "Mars is the nearest planet to Earth", "answer": "False"},
    {"text": "The Taj Mahal is located in India", "answer": "True"},
    {"text": "The North Pole is located in the Arctic Ocean", "answer": "True"},
    {"text": "The United States has 50 states", "answer": "True"},
    {"text": "The Amazon is the longest river in the world", "answer": "False"},
    {"text": "The capital of Canada is Toronto", "answer": "False"},
    {"text": "Jupiter is the largest planet in the Solar System", "answer": "True"},
    {"text": "The capital of China is Beijing", "answer": "True"},
    {"text": "Venus is the hottest planet in the Solar System", "answer": "True"},
    {"text": "The equator divides the Earth into two hemispheres", "answer": "True"},
    {"text": "The longest mountain range in the world is the Andes", "answer": "True"},
    {"text": "The capital of Australia is Melbourne", "answer": "False"},
    {"text": "The Sahara is the world's largest desert", "answer": "True"},
    {"text": "The capital of the United States is New York", "answer": "False"},
    {"text": "The currency of Greece is the Euro", "answer": "True"},
    {"text": "The capital of France is Paris", "answer": "True"},
    {"text": "Polar bears live in the Antarctic", "answer": "False"},
    {"text": "The capital of India is Mumbai", "answer": "False"},
    {"text": "Mount Kilimanjaro is the tallest mountain in Africa", "answer": "True"},
    {"text": "The capital of Japan is Tokyo", "answer": "True"},
    {"text": "The currency of the United States is the Dollar", "answer": "True"},
    {"text": "The Earth is the third planet from the Sun", "answer": "False"},
    {"text": "The Atlantic Ocean is the largest ocean in the world", "answer": "False"},
    {"text": "The capital of the United Kingdom is London", "answer": "True"},
    {"text": "The currency of China is the Yuan", "answer": "True"},
    {"text": "The capital of Brazil is Sao Paulo", "answer": "False"},
    {"text": "Alaska is the largest state in the United States", "answer": "True"},
    {"text": "The capital of Italy is Rome", "answer": "True"},
    {"text": "The currency of Mexico is the Peso", "answer": "True"},
    {"text": "The Pacific Ocean is the world's largest ocean", "answer": "True"},
    {"text": "The currency of India is the Rupee", "answer": "True"},
    {"text": "Mount Everest is the tallest mountain in the world", "answer": "True"},
    {"text": "The capital of Germany is Berlin", "answer": "True"},
    {"text": "The currency of Japan is the Yen", "answer": "True"},
    {"text": "The Sahara is the largest desert in the world", "answer": "True"},
    {"text": "The capital of South Africa is Cape Town", "answer": "False"},
    {"text": "The currency of Canada is the Canadian Dollar", "answer": "True"},
    {"text": "The capital of Spain is Madrid", "answer": "True"},
    {"text": "The Amazon Rainforest is the largest rainforest in the world", "answer": "True"},
    {"text": "The capital of Argentina is Buenos Aires", "answer": "True"},
    {"text": "The currency of Australia is the Australian Dollar", "answer": "True"},
    {"text": "The longest river in the world is the Amazon River", "answer": "False"},
    {"text": "The currency of Russia is the Ruble", "answer": "True"},
    {"text": "The capital of Turkey is Istanbul", "answer": "True"},
    {"text": "The currency of Thailand is the Baht", "answer": "True"},
    {"text": "The capital of Egypt is Cairo", "answer": "True"},
    {"text": "The currency of Brazil is the Real", "answer": "True"},
    {"text": "The capital of South Korea is Seoul", "answer": "True"},
    {"text": "The currency of Indonesia is the Rupiah", "answer": "True"},
    {"text": "The capital of Saudi Arabia is Riyadh", "answer": "True"},
    {"text": "The currency of the United Arab Emirates is the Dirham", "answer": "True"},
    {"text": "The capital of Mexico is Mexico City", "answer": "True"},
    {"text": "The currency of Colombia is the Peso", "answer": "False"},
    {"text": "The capital of Venezuela is Caracas", "answer": "True"},
    {"text": "The currency of Malaysia is the Ringgit", "answer": "True"},
    {"text": "The capital of Nigeria is Abuja", "answer": "True"},
    {"text": "The currency of New Zealand is the New Zealand Dollar", "answer": "True"},
    {"text": "The capital of Kenya is Nairobi", "answer": "True"},
    {"text": "The currency of the Philippines is the Peso", "answer": "True"},
    {"text": "The capital of Bangladesh is Dhaka", "answer": "True"},
    {"text": "The currency of Hong Kong is the Hong Kong Dollar", "answer": "True"},
    {"text": "The capital of Poland is Warsaw", "answer": "True"},
    {"text": "The currency of Vietnam is the Dong", "answer": "True"},
    {"text": "The capital of Ireland is Dublin", "answer": "True"},
    {"text": "The currency of Israel is the Shekel", "answer": "True"},
    {"text": "The capital of Vietnam is Hanoi", "answer": "True"},
    {"text": "The currency of South Africa is the Rand", "answer": "True"},
    {"text": "The capital of Portugal is Lisbon", "answer": "True"},
    {"text": "The currency of Taiwan is the New Taiwan Dollar", "answer": "True"},
    {"text": "The capital of Chile is Santiago", "answer": "True"},
    {"text": "The currency of Hungary is the Forint", "answer": "True"},
    {"text": "The capital of Switzerland is Bern", "answer": "True"},
    {"text": "The capital of Ghana is Accra", "answer": "True"},
    {"text": "The currency of Armenia is the Dram", "answer": "True"},
    {"text": "The capital of Cameroon is Yaounde", "answer": "True"},
    {"text": "The currency of Ethiopia is the Birr", "answer": "True"},
    {"text": "The capital of Angola is Luanda", "answer": "True"},
    {"text": "The currency of Azerbaijan is the Manat", "answer": "True"},
    {"text": "The capital of Sudan is Khartoum", "answer": "True"},
    {"text": "The currency of Costa Rica is the Colon", "answer": "True"},
    {"text": "The capital of Guatemala is Guatemala City", "answer": "True"},
    {"text": "The currency of Honduras is the Lempira", "answer": "True"},
    {"text": "The capital of Nicaragua is Managua", "answer": "True"},
    {"text": "The currency of Paraguay is the Guarani", "answer": "True"},
    {"text": "The capital of El Salvador is San Salvador", "answer": "True"},
    {"text": "The currency of Bolivia is the Boliviano", "answer": "True"},
    {"text": "The capital of Ecuador is Quito", "answer": "True"},
    {"text": "The currency of Uruguay is the Peso", "answer": "False"},
    {"text": "The capital of Peru is Lima", "answer": "True"},
    {"text": "The currency of Jamaica is the Dollar", "answer": "True"},
    {"text": "The capital of Panama is Panama City", "answer": "True"},
    {"text": "The currency of the Bahamas is the Bahamian Dollar", "answer": "True"},
    {"text": "The capital of Haiti is Port-au-Prince", "answer": "True"},
    {"text": "The currency of Barbados is the Barbados Dollar", "answer": "True"},
    {"text": "The capital of Dominica is Roseau", "answer": "True"},
    {"text": "The currency of Belize is the Belize Dollar", "answer": "True"},
    {"text": "The capital of Grenada is St. George's", "answer": "True"},
    {"text": "The currency of Suriname is the Dollar", "answer": "False"},
    {"text": "The capital of Guyana is Georgetown", "answer": "True"},
    {"text": "The currency of Trinidad and Tobago is the Trinidad and Tobago Dollar", "answer": "True"},
    {"text": "The capital of St. Lucia is Castries", "answer": "True"},
    {"text": "The currency of Iceland is the Krona", "answer": "True"},
    {"text": "The capital of Liechtenstein is Vaduz", "answer": "True"},
    {"text": "The currency of Monaco is the Euro", "answer": "True"},
    {"text": "The capital of Andorra is Andorra la Vella", "answer": "True"},
    {"text": "The currency of San Marino is the Euro", "answer": "True"},
    {"text": "The capital of Vatican City is the Vatican City", "answer": "True"},
    {"text": "The currency of Kosovo is the Euro", "answer": "True"},
    {"text": "The capital of Albania is Tirana", "answer": "True"},
    {"text": "The currency of Moldova is the Leu", "answer": "True"},
    {"text": "The capital of Macedonia is Skopje", "answer": "True"},
    {"text": "The currency of Montenegro is the Euro", "answer": "True"},
    {"text": "The capital of Bosnia and Herzegovina is Sarajevo", "answer": "True"},
    {"text": "The currency of Belarus is the Ruble", "answer": "True"},
    {"text": "The capital of Ukraine is Kyiv", "answer": "True"},
    {"text": "The currency of Latvia is the Euro", "answer": "True"},
    {"text": "The capital of Estonia is Tallinn", "answer": "True"},
    {"text": "The currency of Lithuania is the Euro", "answer": "True"},
    {"text": "The capital of Georgia is Tbilisi", "answer": "True"},
    {"text": "The currency of Armenia is the Dram", "answer": "True"}
]
