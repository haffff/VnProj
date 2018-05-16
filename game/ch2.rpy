# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.
label start2:
    scene bedr
    "{cps=*0.2}Kto z rana wstaje,  temu Pan Bóg daje.{/cps}"
    "Coś takiego."
    "Ale ja chce spać. Nie rano wstawać."
    "W towarzystwie tych pozytywnych myśli wyciągnąłem się z łóżka. Może przynajmniej dzisiaj się nie spóźnię."
    "..."
    
    scene shiochis with Dissolve(3.0)
    
    menu:
        "TODO: implementacja systemu punktów"
        
        "*rozszerzony komentarz dla bardziej przyjaznych wyborów*":
            "Na stacji jednak coś mnie uderzyło."
            "Ten widok wszystkich innych licealistów,  którzy teraz dla mnie,  jednego z nich,  wyróżniali się."
            "Różne mundurki,  damskie,  męskie,  obok garniturów i garsonek wybijały się żywymi twarzami gimnazjalistów i licealistów."
            "To było miłe uczucie."
            
        "*krótsza wersja*":
            "Tym razem na stacje przyszedłem z wyprzedzeniem."
            "Bądź co bądź,  ale pierwszej lekcji tak sobie nie mogę ominąć."
            "Obok mnie na stacji zauważyłem wiele innych mundurków,  damskich,  męskich. Do nich twarze,  jedne znudzone,  niewyspane,  jak moja,  inne rozbawione,  rozmawiające."
            
    scene trainin
    "W pociągu tłok. Chociaż,  to normalne. Był normalny tłok,  taki,  że każdy ocierał się o kogoś innego,  a nie taki,  że wszyscy byli w siebie wtuleni jak jedna masa."
    "Licealiści,  Licealiski,  wszyscy inni uczniowie,  biznesmeni,  sekretarki.. wszyscy ściśnięci."
    "Mei ban fa,  każdy musi jakoś dojechać,  a to ‘jak’ to już mniejsza."
    show hikaridefdeft with dissolve
    "..."
    "Kątem oka zauważam Hikari. Jest gdzieś 5 metrów ode mnie,  w słuchawkach,  wpatrzona w okno. Cóż,  teoretycznie mógłbym się do niej przecisnąć,  ale.."
    
    menu w11:
        "w11/TODO: 02de versions"
        "Podejdź":
            $ w11 = 1
            "Ale czemu nie? Strzelając ‘przepraszam’ jak z karabinu przeciskam się przez ludzi."
            "Pociąg jedzie spokojnym,  jednostajnym tempem,  więc nie jest nawet tak źle."
            "Hikari mnie wreszcie zauważa,  wyjmuje słuchawki z uszu i uśmiecha się."
            hide hikaridefdeft
            show hikaridefdef at c1 with dissolve
            h "Hej Taro! Właśnie myślałam,  że gdzieś tutaj będziesz wsiadał. Jak tam się wstawało?"
            g "Ha-ha,  no wybornie,  już jak otworzyłem oczy to już się paliłem,  by spędzić kolejną lekcje z Alberto."
            h "Tak,  lekcje pana Alberto są specyficzne,  ale co,  nie cieszyłeś się,  że zobaczysz swoich kolegów i koleżanki z klasy?"
            h "Z resztą,  to jeszcze nie kolegów i koleżanki,  bo prawie nikogo nie znasz."
            h "Oj,  przepraszam. Nie było to zbyt złośliwe?"
            g "Nie,  nie przejmuj się. Kogo powinienem poznać?"
            h "No,  um,  wszystkich?"
            g "Oj wiem,  wiem. Ale kogo pierwszego?"
            h "Proszę cię,  gdzie ma być zabawa w poznawaniu ludzi,  jeśli ci o nich wszystko powiem."
            g "Masz rację. Jeszczę ominą mnie jakieś nieporozumienia, prawda."
            h "...które będziesz później wspominać,  chichrając się jak głupi."
            g "Albo przez które nie będę mógł się do tej osoby odezwać przez trzy lata. Jedno z dwóch."
            h "Nie ma takich rzeczy wśród naszej klasy."
            "Jej pewność mnie trochę przeraża."
            "..."
            scene stationent
            "Dotarliśmy na naszą stację."
            g "Gdzieś powinniśmy znaleźć Anie,  Hanie i Jausza,  co nie?"
            h "Jesteśmy trochę wcześniej,  ale pewnie tak."
            scene black
            "..."
        
        "Zignoruj":
            $ w11 = 2
            "Ale nie będę się przeciskał przez pół pociągu."
            "Jak się obrócę to pewnie nawet mnie nie zauważy,  nie będzie tej dziwnej atmosfery."
            scene black
            "..."
            
    scene bcgklasafull        
    "Przynajmniej się nie spóźniłem."
    "Dobrze,  bo nasza nauczycielka japońskiego okazała się szmatą."
    "Ziu,  punkciki za brak krawata,  ziu,  przpina się do tego,  jak to my ‘nie umiemy się wypowiadać poprawnie,"
    "za jej czasów to było inaczej,  ta dzisiejsza młodzież’."
    "Ale kto jest w ostatniej ławce,  ten jest w ostatniej ławce."
    scene hall
    "Ah,  tak. Była już długa przerwa."
    "Jakoś mi się nie uśmiechało siedzenie przez pół godziny w telefonie,  jakkolwiek mój harmonogram snu byłby temu wdzięczny,  gdybym nie znajdywał miliona rzeczy do zrobienia tuż przed snem."
    "A teraz zorientowałem się,  że cała klasa stoi pusta."
    "Oprócz mnie,  to jest. Westchnąłem na moje umiejętności społeczne,  a raczej ich brak i udałem się na poszukiwanie czegoś do zjedzenia."
    "Po cichu też miałem nadzieję,  że znajdę kogoś by z nim to zjeść,  ale pytany zaprzeczyłbym."
    "..."
    "Po chwili wylądowałam przed szkolnym sklepikiem,  który to przeżywał istny szturm ze strony uczniów."
    show loli at rc4
    "Trudno było to nawet nazwać kolejką. Nic dziwnego,  prawdę mówiąc. Co zwróciło moją uwagę,  to była dziewczyna,  bezskutecznie próbująca dostać się do lady."
    "Nie pasowała do tego tłumu,  była za niska,  zbyt krucho wyglądała i nawet jak ktoś ewidentnie przed nią wepchał,  tylko spuściła głowę i znowu podeszła,  teraz z innego kąta,  jakby to miało cokolwiek zmienić."
    
    menu w12:
        
        "w12"
        "Pomóż dziewczynie":
            $ w12 = 1
            "To było naprawdę zbyt bolesny widok."
            "Poczułem,  że trzeba coś z tym zrobić,  jednak jakoś tak bardziej subtelnie."
            "Jakkolwiek upośledzony społecznie mogłem być,  pomysł zrobienia sceny przed całą kolejką nie wydawał się dobry."
            "..."
            show loli at c1
            "Stanąłem za dziewczyną;  z bliska zauważyłem jak niska jest,  dosięgając mi ledwo do podbródka."
            show loli at l2 
            show bully at r2 with dissolve
            "Jak się spodziewałem,  ktoś znowu próbował się wepchnąć przed nią."
            "Na to czekałem."
            hide bully
            show bully1
            g "Ej,  ty,  kolejka jest."
            "Zebrałem każdy kawałek dresa w sobie na tą wypowiedź."
            "..."
            "Co gorsze,  nie uzyskałem reakcji."
            "Nie."
            "On to usłyszał,  napięła mu się ręka."
            "Moja dłoń na jego ramię,  mój dresowy zmysł podpowiadał"
            hide bully1
            show bully2
            hide loli with dissolve
            g "Kolejka zaczyna się na końcu a nie w środku."
            "Wreszcie się obrócił."
            "Nie jestem pewien,  czy pierwszak,  czy może z drugiej klasy. Zmierzył mnie wzrokiem,  ale w końcu odszedł."
            hide bully2 with dissolve
            "Zrobiło się luźno."
            "Za luźno."
            "Dziewczyna przede mną gdzieś zniknęła."
            "Musiałem też ją wystraszyć. Na tyle z mojej subtelności. Rozejrzałem się."
            "Mała postać właśnie zniknęła za schodami."
            "Teraz chyba wypada ją przeprosić,  co nie?"
            scene black
            "..."
            scene stairs
            "Znalazłem ją siedzącą na schodach w dziwnie cichej części szkoły."
            "Wciąż nie miałem sposobności przypatrzeć się jej twarzy,  ale jej figury nie mógłbym pomylić."
            show loli at lc4
            g "Err… Przepraszam,  że tak wyszło,  nie chciałem cię przestraszyć."
            "Jeśli jeszcze miałem jakieś wątpliwości,  to teraz naprawdę czuję się niezręcznie."
            Character("Dziewczyna") "Oh,  nie,  to nic takiego,  proszę się nie przejmować. Tam było trochę.. zbyt duszno dla mnie."
            g "Ah…"
            "..."
            "Chyba powinienem"
            g "To może.. powiedz mi,  co chciałaś. Przyniosę ci."
            Character("Dziewczyna") "Nie,  nie,  naprawdę,  nie jestem taka głodna czy coś,  pójdę później,  nie musisz."
            g "Daj spokój, wszyscy mi z klasy uciekli i nie mam z kim zjeść. To co chcesz?"
            "Może jak to obrócę w żart będzie łatwiej… nie?"
            Character("Dziewczyna") "..."
            Character("Dziewczyna") "..."
            Character("Dziewczyna") "Chleb melonowy"
            "..."
            scene black
            "..."
            scene stairs with dissolve
            show loliwithbread at lc4
            g "Wciąż nie zapytałem cię o imię."
            Character("Dziewczyna") "Jestem Asia."
            "..."
            "Tutaj się kończy mój plan charyzmatycznego przystojniaka."
            "..."
            g "A z której jesteś klasy?"
            aaa "Um, jestem z drugiej c"
            "To jest trochę niekomfortowe."
            " Może jednak jedzenie w samotności to nie jest zły pomysł..."
            aaa "Wiesz..."
            g "Tak? Co jest?"
            aaa "Nie robisz tego z litości,  co nie?"
            "Nie tego się spodziewałem."
            menu:
                "w12a"
                "Nie,  nie robię tego z litości":
                    $ w12a = 1
                    g "Nie,  to nie tak. Chciałem ci po prostu pomóc."
                    g "Każdy ma swoja slabsze strony,  jestem pewny,  że ty też w czymś mogłabyś mnie poratować."
                    "…"
                    g "No cóż,  a..."
                    aaa "Wybacz,  muszę iść do klasy."
                    hide loliwithbread
                    "Zerwała się,  idąc nienaturalnie sztywnym krokiem."
                    "..."
                    "Nie tego się spodziewałem raz jeszcze."
                    "..."
                    "Nie oddała mi za chleb melonowy."
                    
                "Tak, to z litości":
                    $ w12a = 2
                    "Musiałem to przyznać."
                    g "Jak mam być z tobą szczery… to tak."
                    g "Kiedy tak dawałaś się wypychać z tej kolejki… żal mi się cię zrobiło."
                    "..."
                    "Nic nie potrafiłem wyczytać z jej twarzy."
                    aaa "Wybacz,  muszę pójść do klasy. Cześć."
                    "Nawet ja potrafiłem załapać taką oczywistą sugestie."
                    "..."
                    "Wychodzi na to, że dzisiaj jem sam."
                    "..."
                    "Nie oddała mi za chleb melonowy."
                    
        "Zignoruj ją":
            $ w12 = 2
            "Czułem się trochę źle ze sobą,  ale uśmiechnąłem się na komiczność sytuacji,  jak bezradna jest ta dziewczynka"
            hide loli
            "…"
            "Jak i tak nie miałem nic w szkole do zrobienia,  to przynajmniej mogę się przejść na dwór do jakiegoś sklepu."
            "Jeśli mnie nie wyśmieją za paradowanie w mundurze,  to jest."
            "..."
            "Taki sobie skrót wymyśliłem,  że nie wiem,  gdzie wylądowałem. Wrodzony zmysł orientacji."
            "Tyle wiem,  że jestem na parterze,  przy drzwiach na dwór,  chociaż nie wyglądają jakby były do użytku dla uczniów."
            "..."
            scene tree
            "Przeszedłem przez nie i tak."
            "Znalazłem się na tyłach szkoły,  w pewnej odległości od boiska."
            "Pode mną rosła krótko przycięta trawa,  a pod murem całkiem potężne drzewa."
            "Coś innego jednak zwróciło moją uwagę: dym,  który wyłaniał się zza jednego z dalszych drzew. Ale coś z tym dymem było nie tak."
            "Faktycznie,  to nie był dym palących się drzew. To był dym papierosowy."
            show edgybp at c1
            Character("Dziewczyna z papierosem") "Czego chcesz?"
            g "Ah,  nie,  tylko trochę zabłądziłem w tej szkole."
            "Jej spojrzenie mnie lekko przeraża."
            Character("Dziewczyna z papierosem") "Ty… jesteś tym typem z ostatniej ławki pod oknem… co nie?"
            g "Tak.. Siedzę tam."
            Character("Dziewczyna z papierosem")"Jak masz na imię?"
            g "Taro"
            Character("Dziewczyna z papierosem") "Słuchaj,  Taro. Bardzo miło było cię poznać,  ale tutaj nikogo nie spotkałeś,  prawda?"
            "I tak nie miałem w tym żadnego interesu."
            g "Nikogo. Gdzie dojdę do jakiegoś sklepu?"
            Character("Dziewczyna z papierosem") "I bardzo dobrze."
            Character("Dziewczyna z papierosem") "Jak pójdziesz wzdłuż tego muru powinieneś znaleźć małą furtkę. Później na lewo."
            hide edgyb with dissolve
            scene black with dissolve
            "Odszedłem z lekkim kiwnięciem głowy."
            "..."
            scene tree
            "Jak wracałem już jej nie było."
            pause 1.3
            
    scene black
    Character("Nauczycielka")"...i dlatego geny dzielimy na..."
    scene bcgklasafull with Dissolve(3.0)
    "Nie było to ani trochę interesujące. Ani przydatne."
    "Ale całkiem łatwo z tego ułożyć pytania,  więc pewnie będzie na sprawdzianie. "
    "Tak działa ta kobieta,  przyczepi się do wszystkiego,  co może."
    "..."
    "{cps=*1.1}A co jeśli ten system jest kontrolowany przez jakieś tajemnicze figury z wysokich sfer,{nw}{/cps}"
    "{cps=*1.3}które stopniowo ogłupiają całe społeczeństwo dla swoich nikczemnych interesów{nw}{/cps}"
    "{cps=*1.5}i przestawiają wszystkich uczniów na robotyczny tok myślenia by byli dobrymi pracownikami w firmach{nw}{/cps}"
    "{cps=*1.7}a nie jakimiś darmozjadami artystami i to wszystko zachodzi tak bardzo powoli,{nw}{/cps}"
    "{cps=*2}że nikt tego nigdy nie zauważył tylko ja jestem pierwszy i będę musiał coś z tym zrobić bo inaczej…{nw}{/cps}"
    "...Chyba czas się przejść"
    g "Proszę pani,  mogę do toalety?"
    scene hall
    "Puściła mnie,  ale z takim wzrokiem,  jakby mówiłą do jakiegoś menela."
    "Udało się,  to się udało."
    "Nawet jak Hikari mi poradziła,  to nie za bardzo miałem okazję do poznania ludzi."
    "Wciąż jest ta dziwna atmosfera obserwacji wśród nas."
    "A mi nie za bardzo podoba się pomysł bycia tym super-przyjaznym kolegą,  który zagada do wszystkich i najlepiej jeszcze jakby socjalizował całą klasę."
    scene gaypanic
    "Nawet ją trochę podziwiam,  za to jaką to łatwością jej to przychodzi."
    "Od niej bije… taka naturalność i szczerość intencji."
    "Chyba każdy,  mniej lub bardziej ma taką chęć posiadania przyjaciół w szkole,  i to nie tylko do spisywania prac domowych czy ściągania."
    "Po prostu,  żeby to nie było miejsce,  gdzie młody człowiek idzie uczyć się nudnych rzeczy bo tak uważa państwo,  a bardziej do jakiejś społeczności,  mikrokultury..."
    "Czekaj."
    "Coś jest nie tak."
    scene gaypanic2
    pause 3
    
    nie "Eeej, co tam robisz?"
    g "Załatwiam swój interes,  nie widać?"
    "I jeszcze nie skończyłem,  a ten co?"
    nie "A nie,  pozwól,  że się przyjrzę~"
    scene gaypanic3
    pause 2
    g "Ej,  ej typie,  wyluzuj,  dobra?"
    nie "Typie~ hehe"
    scene toile
    show gay at c1
    g "Dobra,  masz jakiś interes do mnie,  czy nie?"
    nie "Tak,  zostałeś wezwany do dyrektorki ze względu na palenie papierosów na terenie szkoły."
    g "C-co?"
    nie "…"
    "..."
    "{cps=*0.6}A-ale to przecież nie ja,  to była ona. Tylko tamtędy przechodziłem. Wpakowała mnie?{nw}{/cps}"
    pause 1.0
    nie "Hahaha,  powinieneś siebie zobaczyć haha"
    nie "Ah,  nie tak sobie tylko śmieszkuje a byłeś taki sam pogrążony w myślach,  że tak mnie naszła ochota."
    nie "Wybacz,  to było silniejsze ode mnie."
    "Czy on sobie jaja robi?"
    "…"
    "Tak,  on sobie robi jaja."
    "Ugh."
    g "Dobrze, dobrze,  bardzo śmieszne,  wiem."
    g "Nie masz lekcji,  że się tak wydurniasz?"
    hide gay with ease
    "Chyba już wolę być na tej biologii. Wyminąłem go w stronę wyjścia."
    nie "To było zdecydowanie ciekawsze niż jakaś tam lekcja."
    scene hall
    "Wyszedł z łazienki za mną."
    g "Nie mów,  że wyszedłeś z lekcji tylko po to,  żeby się przejść."
    "Obróciłem się."
    "..."
    "Jedyne co zauważyłem to zamykające się drzwi toalety."
    scene black
    "Damskiej."
    
         
jump ch2e