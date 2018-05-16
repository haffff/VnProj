# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label start:
    scene black
    "To nie tak, że nie chciało mi się iść do szkoły; problem był ze wstawaniem"
    scene bcgmeme with dissolve
    "Nie byłem podekscytowany,  czy coś w tym stylu. Nie chciałem się specjalnie spóźnić,  by wybiec z tostem w ustach,  czy  żeby mieć jakieś dramatyczne wejście."
    "Po prostu nie chciało mi się wstawać rano."
    "Pewnie i bym się nie spóźnił,  gdybym podbiegł na pociąg,  ale nie chciało mi się."
    "Może jednak podświadomie szukałem tego dramatycznego wejścia spóźnionego?"
    "Dopiero w pociągu zorientowałem się,  że chyba jednak powinienem się pośpieszyć."
    "Nie ze względu na lekcje czy nauczycieli,  ale by zająć ostatnią ławkę. Przecież ja w pierwszej nie przeżyje,  a nie ma możliwości,  że inne będą wolne."
    "Wychodząc na stacji zauważam,  że zaczęła się ceremonia. Ojeju,  ominie mnie pół godziny gadania bez treści."
    
    scene bcg2
    
    "Ja idę powoli,  koło mnie przeciska się dziewczyna z mundurkiem mojego nowego liceum."
    "Chyba jeszcze nie zaakceptowała faktu,  że albo kompletnie ominie ceremonie otwarcia,  albo wejdzie cała spocona na ostatnie pare minut."
    "Obserwuje,  jak się skłania ku temu drugiemu i przyśpiesza swój chód do prędkości typowej dla biegu dziewczyn na w-fie. Chwilę później już znika za rogiem."
    "Czy ja potrzebuję dziewczyny? No niby życie licealne i te sprawy,  ale sam nie wiem."
    "Mój nigdy niewypowiedziany plan zakładał dobrą zabawę z kolegami i jakoś tam zdanie szkoły."
    "Nigdy nie byłem jakimś celebrytą klasowym,  ale tych kolegów co miałem,  to miałem i było całkiem przyjemnie."
    "Dziewczyna? Przecież to musi być bardzo dużo zachodu,  a jeszcze znaleźć jakąś normalną,  to nie,  chyba jednak nie."
    "Tuż za wcześniej wspomnianym rogiem,  stoi ta dziewczyna,  a raczej próbuje stać. Opiera się całym ramieniem,  dysząc."
    
    menu:
            
            
            "Zainteresuj się dziewczyną":
                $ w01 = 1
                show sekaiegslide with Dissolve(2.0)
                pause 3.0
                "Nie mogę tak po prostu przejść obok. Sumienie nie dałoby mi spokoju"
                g "Hej, wszystko w porządku?"
                pause 1.0
                "Nie doczekałem się jednak odpowiedzi."
                "Patrzyła tylko na mnie szklistymi oczami. Z bliska zauważyłem, jak blado wygląda."
                g "Usiądź na chwilę, spokojnie."
                show sekaiegunslide
                hide sekaiegslide with Dissolve(0.2)
                "Posłuchała mnie i spoczęła na chwilę przy ścianie."
                "A raczej osunęła się na nią. Dyszała ciężko, wciąż nie mogąc złapać oddechu."
                "Miałem spanikować, kiedy nagle jej oddech nieco się ustabilizował, a ona sama podniosła głowę."
                Character("Dziewczyna") "Już… Wszystko… Dobrze…"
                g "Wcale tak to nie wygląda. Może powinienem wezwać pomoc?"
                Character("Dziewczyna") "Nie, nie… Dziękuję… Już wszystko w porządku. Po prostu… Słabiej się poczułam."
                g "Wygląda na to, że i tak idziemy w to samo miejsce. Jestem Taro."
                "Podałem jej rękę, pomagając wstać."
                hide sekaiegunslide with dissolve
                show sekai at c1 with dissolve
                Character("Dziewczyna") "Sekai. Dzięki za to... Lepiej już chodźmy i tak pewnie się spóźniliśmy."
                g "Moment, nie biegnij tak. Nie chcemy powtórki tej sytuacji."
                sh "Dam sobie radę, ok? Już wszystko gra."
                "Nie miałem ani siły, ani ochoty, żeby się z nią kłócić. Zwłaszcza że ledwo co się poznaliśmy."
                "Postanowiłem dać tym razem za wygraną. Szczególnie że znaleźliśmy się już pod szkołą."
                scene bcg
                show sekai at c1
                sh "Muszę jeszcze na sekundę gdzieś iść."
                sh "Pewnie spotkamy się jeszcze później w szkole. Dzięki za pomoc. Na razie!"
                g "Narka"
                hide sekai with dissolve
                "No i poszła."
                "Teraz wystarczy tylko znaleźć tablicę z ogłoszeniami i rozpiskę klas."
                
            "Zignoruj sytuacje":
                $ w01 = 2
                "No i sobie przesadziła,  pewnie astma czy coś takiego."
                "Zabawnie będzie jak się jeszcze spóźni na lekcje."
                "Mijam ją,  dalej idąc spokojnym krokiem “nic mnie nie obchodzi”."
                "Po drodze wypatruje punkty wokół szkoły,  gdzie można byłoby się udać na dłuższej przerwie,  czy nawet zamiast lekcji."
                "Nie jest to żaden plan,  ale przygotowanym można być. Mały supermarket w odległości jakiś 15-stu minut,  obok niego  DoMac."
                "Na końcu ulicy,  na której są sklepy widzę,  ugh,  stacje policyjną. Mam nadzieje,  że taka odległość od szkoły jest przypadkiem,  choć nie palę."
                "Po prostu,  taka odległość daje mi wrażenie bycia nadmiernie obserwowanym."
                "Bliżej szkoły jest jeszcze jakiś mniejszy sklepik,  nic ciekawego."
                
                scene bcg3
                
                "Mam nadzieję,  że mój wychowawca nie okaże się jakąś babą z problemami do życia i nie będzie mi robił żadnych problemów,  z tym,  że mnie nie ma." 
                "Może jednak nie powinienem testować go tak wcześnie?"
                "Plac szkolny już przede mną i,  oh jaki fart,  akurat uczniowie rozchodzą się do sal." 
                "Bingo. Gdzieś na tablicy powinna być rozpiska."

                
    label afer_menu:
    
    scene bcg
    
    "Jest i rozpiska,  przy niej jakiś chłopak. Jego strój wygląda zdecydowanie zbyt ładnie żeby nie był pierwszakiem."
    "Śledzę wzrokiem tabele sali. Na miejscu mojej sali znajduje się palec,  i to na pewno nie mój."
    
    show cmatekun at c1
    e "Czyli wylądowaliśmy w tej samej męczarni?"
    g "Na to wygląda. Jestem Taro."
    "Wymieniamy uścisk dłoni. To chyba będzie spoko typek. W sam raz do zabijania licealnego czasu."
    e "Ja Glutenian. Miło poznać."
    e "Wiesz co,  typie?  Mam nadzieję,  że w naszej klasie będą jakieś dobre loszki."
    "I jeszcze jest typem,  co prowadzi rozmowę za ciebie. Bogowie,  ale wy łaskawi."
    g "Chcesz się napatrzeć,  czy powyrywać?"
    e "Jasne,  że wyrywać!"
    e "Jesteśmy w liceum,  to jest szczyt naszego życia,  Taro,  korzystaj,  bo jak wyjdziesz stąd prawiczkiem to cie nawet babcia wyśmieje."
    "Może i żartował,  ale jak o tym pomyślę to muszę się z nim zgodzić"
    g "Dobrze już,  jednak się przyłączam do twojej nadziei o dobrych loszkach."
    
    scene bcgklasawideroll with slideleft
    
    "Tak udajemy się do naszej klasy. Glutenian łapie trzecią ławkę pod drzwiami, ja ostatnią pod oknem."
    "Trochę szkoda,  że daleko od niego,  ale przywileje ostatniej ławki są zbyt kuszące."
    "Wygląda na to,  że nauczycielowi się nie śpieszy."
    "Przesuwam wzrokiem po klasie. Różne postacie,  mniej lub bardziej przejęte swoją nową klasą;"
    "niespokojne wzroki,  gładzenie perfekcyjne wyprasowanej spódniczki czy marynarki,  poprawianie włosów,  poprawianie pozycji w krześle."
    "Chociaż, prawdę mówiąc, łapie się na tym samym. Gdzieś po.."
    
    show hikaridefjump with Dissolve(0.15)
   
    h "Hej,  z tobą się jeszcze nie witałam,  jestem Hikari,  a ty?"
    "Uwah! A tutaj znikąd wyskakuje mi dziewczyna.. i to całkiem ładna. Pozbierać słowa,  przynajmniej wysłowić się jak człowiek."
    
    menu:
        
            "0.2a - Dziwna odpowiedź":
                $ w02 = 1
                "Autyzm,  autyzm,  autyzm! Nie chciałem tego powiedzieć...! Nie chcialem,  prawda?"
                h "Ej,  to był mój pomysł,  żeby mówić dziwne rzeczy na pierwszym dniu."
                h " Ale wiesz,  to nie działa. Spędzimy tutaj przecież trzy lata z tymi ludźmi,  chyba nie chcesz zrobić z siebie klauna klasowego,  nie?"
                h "Nie jesteśmy w podstawówce,  chociaż czasami mam takie wrażenie jak patrzę na niektórych. Haha."
                h "Jak z ciebie taki zabawny śmieszek to chyba się dogadamy."
                "Nauczyciel wchodzi do sali"
                h "Pogadamy później."
            
            "0.2b - Przyjazna 1":
                $ w02 = 2
                "Nic nad wymiar autystycznego. Dobrze."
                h "Miło poznać! Jak tutaj wylądowałeś?"
                g "Tak na prawdę to nie wiem,  to nie jest tak,  że ta szkoła jest jakaś specjalna;"
                g "to jest… właśnie takie normalne liceum całkiem blisko domu."
                h "Dokładnie,  takie fajne liceum w którym jednak się czegoś nauczysz,  ale wciąż masz czas na życie społeczne!"
                "Nauczyciel wchodzi do sali"
                h "Pogadamy później"
            
            "0.2c - Przyjazna 2":
                $ w02 = 3
                "To ja chcę tą loszkę,  czy nie?"
                h "Oh,  właśnie miałam cię zapytać o to samo."
                h "Wydaje mi się,  że to jest takie fajne liceum,  gdzie nauczysz się czegoś,  ale wciąż masz czas na życie społeczne…"
                h "cóż,  to drugie właśnie się sprawdza."
                g "Wiem,  co mówisz."
                g "Nie jestem za bardzo pewny,  co chcę zrobić po liceum,  a po tej szkole nie czuje że będę do czegoś uwiązany"
                h "To wolność!"
                "Nauczyciel wchodzi do sali"
                h "Korzystaj z niej póki możesz"

            
            "0.2d - Niezdecydowanie":
                $ w02 = 4
                "Czy to autyzm? Mózg mi się zepsuł?"
                h "Oj,  już nie musisz być taki nieśmiały."
                h "To jest normalne,  żeby zaznajomić się z kolegą z klasy,  prawda?"
                h "Musisz być Taro,  tylko z tobą się nie witałam."
                h "yyy,  to nie tak,  że przestudiowałam całą listę,  czy coś ehehe.."
                h "No,  to pogadamy później!"
                h "...mam nadzieje."
                hide hikaridefjump with dissolve
                "..."
                "..."
                "Ale to było upośledzone."
                "Wchodzi nauczyciel"
        
            "0.2e - Zignorowanie":
                $ w02 = 5
                "Ale,  co ty tak w ogóle robisz?"
                "Tak przed twarz mi wyskakujesz bez powodu? Nawet swojego monologu nie skończyłem. Eh."
                h "Ej no,  aż taka odpychająca nie jestem."
                h "Możesz przynajmniej z siebie wyrzucić jakieś ‘cześć’, czy coś. Powiesz mi przynajmniej jak się nazywasz?"
            
                if w02 == 5: 
                    menu:
                        
                        "Przedstaw się":
                            $ w021 = 1
                            g "Jestem Taro"
                            h "No! Widzisz,  nie było trudno."
                            h "Zamienić dwa słowa z koleżanką w pierwszym dniu to nie jest nic dziwnego? Reszta klasy jakoś nie była taka uparta."
                        
                        "Odmów":
                            "Nie mam najmniejszej ochoty z nią rozmawiać. Nie potrafi zrozumieć,  że nie chce z nią rozmawiać’?"
                            h "Oh. To,  cóż, um, przepraszam,  że przeszkadzam."
                        
                else: 
                    "co to za haxy"
                
    label menu2:
    
    scene bcgklasafull with dissolve

    "Na rozpisce widziałem,  że nasz wychowawca to Gronostaj Alberto,  jednak człowiek,  który wszedł do sali ani trochę nie pasował do tego imienia."
    show alberto at c1 with dissolve
    "Późna czterdziestka,  boki głowy lekko łyse,  ale jego twarz mówiła coś innego,  jakby był żywszy niż się wydawał na pierwszy rzut oka."
    "Jego krok też był jakiś taki młodszy,  jakby przeczyło swojemu właściwemu wiekowi,  i to z sukcesem."
    a "..."
    a "..."
    a "..."
    a "Witaj klaso"
    "Od nas wyszło chórkiem ‘Dzień-do-bry’."
    "..."
    "I tam siedział,  bez słowa,  tylko wpatrzony w klasę,  patrząc po oczach każdemu z osobna."
    "Kątem oka widziałem jak parę osób wymienia się pytającymi spojrzeniami. Po chwili na jego twarz wszedł lekki uśmiech."
    a "Ale jak wy na mnie patrzycie,  jak na jakiegoś ufoludka,  co?"
    "Po klasie przebiegł szmer"
    a "Ale ja naprawdę człowiek,  z krwi i kości. To,  że przyszliście do nowej szkoły,  to już wam myślenia zabrakło?"
    "Wciąż się uśmiechał,  wyraźnie naprawdę go to bawiło."
    Character("Męski głos z przodu sali") "Ależ, panie profesorze,  my byśmy nigdy nie…"
    a "Oj żartuję sobie tylko z was,  ale naprawdę,  siedzicie spięci jakbyście za chwilę mieli wylądować u dyrektorki."
    a "Co wy,  trafiliście do tej szkoły za karę?"
    
    show hikaridefdefside with Dissolve(0.8)
        
    h "Dla niektórych może być to bliskie prawdy,  proszę pana."
    hide hikaridefdefside with dissolve
    a "Wiesz,  ile dłużej uczę w tej szkole,  tym bardziej prawdziwe to jest."
    a "Popatrz sobie na młodzież sprzed 30,  nie,  nawet 10 lat. Ta żądza zdobywania wiedzy."
    a "Teraz to się dziwie,  jak ktokolwiek zada jakieś pytanie. No popatrz na tego,  siedzi,  jakby już zapomniał o świecie poza tą szkołą."
    a "Pewnie myślisz już jakby tą piątkę u tego cepa załapać i się nie napracować."
    hide alberto with Dissolve(0.1)
    show shboy at truecenter with vpunch
    Character("Chłopak") "P-panie profesorze,  ja nigdy bym nie.."
    hide shboy with dissolve   
    show alberto at c1
    a "A ten znowu,  no przecież żartuję sobie. Proszę was, koleżanka jakoś mogła normalnie odpowiedzieć,"
    a "a wy ‘ughhh,  śpieszę się na matematykę,  bo bardzo chcę pouczyć się tych całek'"
    hide alberto with Dissolve(10.0)
    "Tak było przez całą godzinę."
    "Parę uczniów z klasy,  za przykładem Hikari, poczynało wchodzić w rozmowę z nauczycielem,"
    " jednak reszta trzymała się z boku,  jakby wciąż uważając,  co pomyślą inni."
    "Nie było przedstawiania się,  czy jakiś zabaw integracyjnych,  tylko Gronostaj rozmawiał sobie z klasą jakbyśmy byli na pikniku czy coś."
    "Osobliwe. Później rzucił  ‘dobra,  możecie się zwijać’  i wyszedł."
    "Parę osób wystrzeliło z siedzeń do drzwi,  więcej normalnie wstawało z miejsc zagadując do pobliskiego kolegi bądź koleżanki," 
    "a parę siedziało jeszcze chwilę w ławkach,  próbując zrozumieć ,  co się tak właściwie stało,  dlaczego ich wychowawca przez całą godzinę nie zrobił nic wychowawczego"
    
    if w02 <= 3:
        
        "Wreszcie i ja zebrałem się do wyjścia."
        "Alberto jest osobliwy, ale cóż,  przynajmniej jest zabawnie"
        show hikaridef 
        h "Hej hej,  Taro,  idziesz na stacje,  prawda?"
        hide hikaridef
        show hikaridefdef at rc4 with dissolve
        show hania at r4
        show ania at lc4
        show seba at l4
        "Stała tam z dwiema dziewczynami i chłopakiem."
        "Zresztą nic dziwnego,  z jej osobowością połowa klasy pewnie ma już ją za przyjaciela."
        g "Oh,  tak,  idę; zapewne z wami,  prawda?"
        h "Teraz już tak. To Ania,  Hania i Janusz; zgaduję,  że się jeszcze nie poznaliście..?"
        g "Nie,  jeszcze prawie nikogo nie znam z klasy,  prawdę mówiąc. Miło poznać."
        aa "Miło poznać"
        hh "Hej!"
        s "Siema"
        hide hikaridefdef
        hide hania
        hide ania
        hide seba
        scene bcgfullroll with Dissolve(2.0)
        "Znajdujemy swoją drogę do wyjścia przez tłum uczniów."
        pause 1.0
        hide bcgfullroll with Dissolve(1.5)
        scene bcg2sroll
        h "Cóż,  tak się ma,  jak się omija ceremonię i przychodzi na ostatnią chwilę."
        show hikaridefdef at rc4
        show hania at r4 with Dissolve(0.5)
        show ania at lc4 with Dissolve(0.5)
        show seba at l4 with Dissolve(0.5)
        hh "Ale,  uwierz mi,  nic cię nie ominęło."
        g "Tak też myślałem,  po tym jak zaspałem,  już nie chciało mi się biec na pociąg"
        aa "A co na to powiedzą twoi rodzice?"
        g "Jak znam swojego ojca to powie ‘rób co chcesz,  byle by przypału nie było’"
        s "Kurde, też bym chciał,  by mi pisali."
        h "Oj weź,  bo zaraz pomyślę,  że naprawdę trafiłeś do tej szkoły za karę,  jak Pan Gronostaj mówił."
        s "Nie jest aż tak źle,  pierwszego dnia nie dałem się… wdałem się w bójkę,  więc jest ok."
        pause 0.7
        "Na chwilę zapadła cisza. Janusz popatrzył po nas lekko niepewnym wzrokiem. Chyba chciał coś powiedzieć,  ale odezwała się Hania."
        hh "Naprawdę miałeś takie historie w podstawówce?"
        s "A… Tak,  no,  w mojej szkole było to… zwyczajne?"
        hh "Ale my tutaj nawet nie mamy palarni!"
        aa "Miałeś… miejsce przed szkołą,  gdzie wszyscy sobie palili,  tak na legalu?"
        s "Nie przed szkołą,  ale wokół były miejsca,  gdzie się zbierali ludzie,  a nauczyciele przymykali na to oko.."
        g "Przecież to nie takie nadzwyczajne,  no może nie na taką skalę jak u ciebie,  Janusz."
        aa "Ah.."
        hide bcg2sroll with dissolve
        scene stationent
        "Zbliżaliśmy się już do stacji"
        show hikaridefdef at c1 with dissolve
        h "A tak poza tym,  ciebie jeszcze nie pytałam,  jak tam tobie minął pierwszy dzień w nowej szkole?"
        h "Oczywiście poza tym,  że jak przykładny uczeń ominąłeś ceremonię rozpoczęcia haha"
        
        if w01 == 1:
            g "Ah,  to nawet miałem ciekawą drogę do szkoły. Spotkałem dziewczynę z naszym mundurkiem,  gorzej się poczuła. Jak jej się poprawiło poszliśmy razem do szkoły."
            g "Wyglądała,  jakby bardzo jej się nie spodobało,  że się spóźniła,  ale nie wiem."
            h "To ja już myślałam, że tu nasz Taro nie ma żadnych znajomych w nowej, nieznajomej szkole,  a tu co?"
            h "Już po innych klasach ma kontakty."
            show hikaridefdef at l2 with dissolve
            show ania at r2 with dissolve
            aa "Ale z nią… wszystko dobrze,  prawda?"
            g "Tak,  wszystko dobrze, przynajmniej ile mi powiedziała."
            g "I to wcale nie jest tak,  że robiłem jakieś kontakty czy coś,  po prostu pomogłem jej po koleżeńsku; nie miałem wyboru,  żeby ją tam po prostu tam zostawić."
            h "No właśnie, co jakby coś poważnego jej się przydarzyło."
            g "Na szczęście nie było to nic poważnego. Spotkałem jeszcze Glutenian szukając sali. Poznałaś się z nim,  prawda?"
        else:
            g "Nic takiego,  prawdę mówiąc. Spotkałem Glutenian szukając sali,  poznałaś się już z nim,  prawda?"
        
        h "Tak,  prawda,  siedzi w trzeciej ławce pod drzwiami."
        h "Chyba przyuważyłam jak wyszedł z klasy z Justyna zaraz po Panu Alberto. Może znajoma z poprzedniej szkoły?"
        "Przyjeżdża pociąg."
        scene trainin
        "Nie jest aż tak wypełniony; jest dosyć wcześnie jak na kończenie pracy,  więc tylko pierwszaki wracają z ceremonii otwarcia. Nie narzekam."
        show hikaridefdef at c1 with dissolve
        h "Gdzie wysiadacie?"
        h "Zgaduję, że wysiadam ostatnia."
        hide hikaridefdef
        show hikaridefdef at rc4 with dissolve
        show seba at l4 with dissolve
        s "Ja tylko dwie stacje,  wysiadam na Saginomiya"
        show hania at lc4 with dissolve
        hh "Oh,  to naprawdę masz blisko,  mógłbyś z buta chodzić."
        hh "Ja jadę aż do Numabukuro,  to jest z pięć stacji."
        show ania at r4 with dissolve
        aa "Sześć,  też tam wysiadam."
        g "Dwie po waszej,  Shimo-Ochiai."
        h "Więc zgadłam,  trochę szkoda,  że mnie tak wszyscy zostawiacie,  ale co na to poradzić."
        hh "Jak chcesz,  to możesz nas wszystkich odprowadzać po kolei. haha."
        h "Oj ty,  ciebie przynajmniej ma kto odprowadzać."
        "Hania popatrzyła się na Anie i uśmiechnęła się"
        hh "A no tak. Może nakłonisz Taro,  by cię odprowadzał?"
        h "Co? Nie nie nie,  nie ma potrzeby,  żartuję sobie."
        "Popatrzyłem na nią ze smugiem na twarzy, "
        "albo czymś,  co miało przypominać smug,  bo wątpię,  że coś z tego wyszło."
        g "A jeśli sam będę chciał cię odprowadzić?"
        h "To zadzwonię na policję,  że jakiś zboczeniec mnie śledzi"
        "Outsmuged"
        "..."
        hide seba with dissolve
        pause 0.6
        hide ania with dissolve
        hide hania with dissolve
        hide hikaridefdef
        show hikaridefdef at c1 with dissolve
        "Przejechaliśmy stacje,  na której wysiadał Janusz,  a potem Ania i Hania."
        "Podoba mi się moja nowa klasa,  przynajmniej na tyle,  na ile ją poznałem."
        "Muszę jeszcze znaleść jakiegoś śmieszka i kogoś od kogoś będzie można ściągać prace domowe. Wtedy to ta klasa będzie idealna."
        h "Zgaduję również,  że nie wiesz nic o Panu Gronostaj Alberto."
        g "Nie,  a powinienem?"
        h "Otóż jest on legendą w tej szkole. Tak się ucieszyłam,  gdy dowiedziałam się,  że będzie mieć naszą klasę."
        h "Naucza angielskiego,  ale jak możesz zgadnąć po dzisiejszym spotkaniu z nim,  to nasze lekcje to nie będzie siedzenie w książkach i przepisywanie z tablicy."
        h "On naprawdę będzie gadał z nami przez całe lekcje,  i to nie zawsze na temat. Przynajmniej to usłyszałam od siostry."
        g "To jakim sposobem on jeszcze uczy w tej szkole,  jak,  tak naprawdę,  nie uczy?"
        h "Właśnie to jest naljepsze,  że jakimś sposobem jego klasy zdobywają najwyższe wyniki na sprawdzianach."
        h "Pan Alberto działa tak,  że pierwsze lekcje sobie gada z uczniami,  a potem przechodzi na angielski."
        h "I to nie jest nawet tak,  że możesz sobie siedzieć z tyłu klasy przez cały semestr,  a potem zrobisz jakąś pierdołe i masz piątkę."
        h "On wymęczy każdego,  nawet się nie zorientujesz,  że byłeś pytany."
        g "To brzmi… dziwnie strasznie."
        h "Tak jakby nikt w tej szkole nie mógłby być nudny."
        "Dojechaliśmy na moją stację."
        g "Dobra,  będę się zwijać,  do jutra!"
        h "Hej,  trzymaj się."
        
        
        
        
        jump boobcheck1end
        
        
    else:
        "Wystrzeliłem i ja."
        "Przecisnąłem się jakimś sposobem przez drzwi klasy. To było dziwne,  ale trochę zabawne."
        e "Hej,  Taro, gdzie idziesz?"
        show cmatekun at r2
        show justy at l2 with Dissolve(1.3)
        "Glutenian stał zaraz za drzwiami,  wraz z jakąś dziewczyną."
        "Czekał na mnie?"
        g "Na stacje,  a co?"
        e "To się przynajmniej trochę z nami przejdziesz,  to jest Justyna,  siedzi za mną."
        j "Miło poznać!"
        scene bcgfullroll
        "Znajdujemy swoją drogę do wyjścia pomiędzy tłumem uczniów. Jakoś."
        pause 1.3
        scene bcg2sroll
        show cmatekun at r2
        show justy at l2
        e "Wiesz,  że się okazało,  że Justyna mieszka dosłownie ulicę ode mnie?"
        e "Chodziła do tego samego gimnazjum. Właśnie wydawało mi się,  że kojarzę taką słodką twarzyczkę."
        j "Ej no,  bo jeszcze zaczniemy sobie historie z dzieciństwa wspominać i wyjdzie, "
        j " że jesteśmy jakiś dawno zaginionym rodzeństwem,  czy coś w tym stylu haha"
        e "Ale spróbować możemy kiedyś haha."
        e "A ty,  Taro,  masz kogoś znajomego w klasie?"
        g "Nie poznałem jeszcze wszystkich w klasie,  ale do gimnazjum chodziłem dosyć daleko stąd,  więc wątpię."
        g "Pewnie nawet jeśli ktoś by chodził do mnie do szkoły,  to bym go nie rozpoznał."
        e "Uuu,  czy to oznacza.... że jestem twoim jedynym znajomym z caaałej klasy?"
        g "Nie przedstawiaj tego tak dramatycznie"
        j "Proszę cię,  a ja?"
        j "Czekaj,  chyba jednak jak o tym pomyślę,  to lubię Taro bardziej,  niż ciebie,  Glutenian."
        e "Yyyy… Ładna pogoda,  co nie?"
        "Wybuchnęli śmiechem,  ja też się uśmiechnąłem."
        j "Poza tym,  jestem pewna,  że Hikari jest już z nim BFF."
        j "Ta dziewczyna ma w sobie coś takiego,  że nie można do niej się nie uśmiechnąć."
        
        if w02 == 4:
            "Ale już można się nie odezwać..."
        else:
            "Cóż..."
            
        e "Dokładnie,  ona jest taka,  że jeśli znajdzie kogoś,  kogokolwiek,  to się z nim zaprzyjaźni."
        e "Prawie jej tego zazdroszczę…"
        j "Nie wyszedłeś tak źle,  koniec końców."
        j "Znalazłeś Taro zanim jeszcze wpadliście do klasy,  i popatrz, dobry ziomek. I jeszcze mnie,  też dobry ziomek,  jeśli miałabym powiedzieć."
        e "Hmm,  ale chyba wolę jednak Taro,  ‘jak o tym pomyśle’.. Haha"
        j "Ale ale,  jak tam minął ci dzień,  Taro?"
        j "Wydaje mi się,  czy ciebie też nie było cię na ceremonii otwarcia?"
        g "Jakoś tak zaspałem,  a potem już nie chciało mi się biec"
        
        if w01 == 1:
            g "Właściwie,  to wychodząc ze stacji spotkałem taką dziewczynę,  z naszej szkoły."
            g "Zasłabła,  wyglądała przez chwilę jakby miała zamiar umierać,  to się zapytałem co z nią."
            e "I co,  rycerz w lśniącej zbroi przyszedł jej z ratunkiem? haha"
            g "Eh,  przesadzasz. Zatrzymałem się i jej pomogłem,  nic wielkiego."
            g "Poszliśmy razem do szkoły,  jest z klasy C"
            e "Chcesz mi powiedzieć,  że zacząłeś szybciej ode mnie?"
            j "Co miałby zacząć?"
            e "Um,  być przykładnym uczniem,  oczywiście."
            j "Jakoś omijanie ceremonii rozpoczęcia nie wydaje mi się przykładne."
        g "I tak jakoś to wszystko. Bez wybuchów."
        
        if w01 == 1:
            e "Co ty,  można powiedzieć,  że uratowałeś tą dziewczynę."
            e "Nie zdziw się jak jutro przyniesie ci pudełko czekoladek haha"
            j "Dziewczyn się tak łatwo nie zdobywa,  Glutenian"
            e "Oj,  ja bym przyniósł czekoladki jakby mnie ktoś uratował."
            "Uśmiechnąłem się na tą myśl"
        else:
            e "Zaraz się zrobi z ciebie dres,  Taro."
            e "Założe się,  że chowasz tam fajki w marynarce."
            g "Taak, w lewej kieszeni fajki,  a w prawej setkę,  tak,  żeby poprawić."
            e "Oj,  a teraz kto przesadza?"
            
        j "My tutaj skręcamy,  prawda,  Glutenian?"
        e "Oh,  tak,  do jutra Taro!"
        j "Do jutra!"
        g "Cześć"
        
        
        
    label boobcheck1end:
        scene black
        "Mój pierwszy dzień w nowej szkole nie minął nawet w połowie źle."
        "Wyszło,  że mam… ciekawego wychowawcę,  a ludzie w mojej klasie,  przynajmniej ci,  których poznałem,   są naprawdę spoko."
        "Jeśli będzie tak dalej to niedługo będę mógł sobie pogratulować szczęśliwego życia licealnego."
        
        show text "Z taką myślą kończe swój pierwszy dzień mojego licealnego życia" at truecenter with dissolve
        pause 3.0
        hide text with dissolve 
        pause 3.0
        
        jump ch1e