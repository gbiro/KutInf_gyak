# A kutatómunka információs eszközei - gyakorlat

## 2018.02.22.

---

### Szoftverek

Néhány eszköz, amiket fogunk használni a félév során:

* [git](https://git-scm.com/downloads/guis)
* [vscode](https://code.visualstudio.com/)
* [Visual Studio Community](https://www.visualstudio.com/vs/community/)
* [cmake](https://cmake.org/download/)
* [MiKTeX](https://miktex.org/download) (latex Windows alá)
* [Python](https://www.python.org/downloads/release/python-2714/)

#### Telepítés Linux alól:

```bash
sudo apt-get install gcc g++ cmake git texlive-full python3-pip python3-setuptools python3-tk
(sudo pip install --upgrade pip)
sudo pip3 install matplotlib
```

A VS Code alapból nincs benne az Ubuntu és tsai szoftverközpontjában, így azt a fenti linkről kell letölteni.

#### Telepítés Windows alól:

*Klikk-klikk-install-kész* módon, vagy `PowerShell` használatával (ld. részletesebben [itt](https://chocolatey.org/packages) illetve a következő órákon). 

```powershell
choco install git cmake python ...
```

---

Az alábbiakban az óra összefoglalója található.

---

### Markdown

Könnyen olvasható és írható nyelv, gyakran használják README fájlokhoz (mint amilyen ez is), fórumokhoz vagy akár Wiki oldalakhoz.

Linkek:

* https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
* https://en.wikipedia.org/wiki/Markdown
* https://pandoc.org/MANUAL.html (ez egy program amivel mindenből mindenbe lehet konvertálni, pl. markdown-ból latex-ba vagy pdf-be)

---

### Git

Idézve a https://git-scm.com/ oldalról: *Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.*

Használata kis projektek esetén is hasznos, de nagyobb, többemberes projektek esetén kifizetődő igazán. Számos érv szól mellette, a teljesség igénye nélkül:

* rendkívül hatékony verziókövetés: minden változás egyszerűen nyomon követhető, szükség esetén visszafordítható;
* tetszőlegesen konfigurálható elágazások (branching) a különböző feature/bug/patch fejlesztésekhez;
* *distributed file system* aka többszörös biztonsági mentés: a projektről annyi másolat létezik, ahányan klónozzák a repository-t és mindegyik teljesen egyenértékű, tehát bármelyik alkalmas a központi szerver példányának a lecserélésére. Ilyen központi szerver a https://github.com, de pl. a https://about.gitlab.com/ vagy https://git.zx2c4.com/cgit/ projektek segítségével bárki létrehozhatja a saját, otthoni szerverét (akár egy [málnás mini-PC-n](https://www.raspberrypi.org/) is);
* óriási közösség: git-tel kapcsolatos kérdésed van, a kutatásodhoz van szükséged egy speciális programra, valami sokak számára hasznosat készítettél vagy épp valaki más projektjéhez van egy sokak számára hasznos hozzájárulásod - jó eséllyel a github-on fogsz kikötni. Mindenki értékeli, ha akár csak visszajelzésekkel is aktív vagy - akár még állásajánlatot is kaphatsz (ma már a CV-ben is elég gyakori a github profilhoz mutató link).

> A gyakorlathoz készítsetek egy github accountot (ha még nem tettétek meg) és legalább egy saját repository-t, hogy tudjátok próbálgatni a parancsokat.
> Új repot létre tudtok hozni a webes felületen keresztül vagy lokálisan is, pl. [ez](https://git-scm.com/docs/git-init) alapján.

Ahhoz hogy a github tudjon azonosítani Titeket, amikor fel akarjátok tölteni a munkátokat, vagy minden egyes alkalommal meg kell adnotok a felhasználó neveteket/jelszavatokat, vagy a https://github.com-on a profilotoknál az *SSH and GPG keys* pontban adjatok hozzá egy [SSH](https://hu.wikipedia.org/wiki/Secure_Shell) kulcsot (erről egyelőre bőven elég annyit ismernetek ami a Wikipedia oldalon is van). Linux alatt:

```bash
ssh-keygen -t rsa
```

A létrehozott *.pub* végződésű kulcs teljes tartalmát kell bemásolni. Első alkalommal a gépeteken lévő git-et is fel kell konfigurálni:

```bash
git config --global user.name "Példa Béla"
git config --global user.email pelda@bela.hu
```

Számos más dolgot is konfigurálhattok, pl. [ez alapján](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup).

Ha a webes felületről hoztátok létre a repot, azt klónozni kell a saját gépetekre. A projekt főoldalán a *Clone or download* gombra kattintva másoljátok ki az elérési címet (megj.: a projekt URL címe is jó), majd egy terminálból (vagy az adott grafikus program megfelelő menüjéből) klónozzátok a repot:

```bash
git clone git@github.com:gbiro/KutInf_gyak.git
```

> **Fork**: a repo teljes egészéről készít egy másolatot a saját felhasználótok alá. Végeredményben ezt is ugyanúgy le kell klónozni a saját gépetekre, de pl. ha az eredeti projektbe akartok majd kontributálni (*pull request*, ld. később) akkor ezt érdemes.

Néhány a legfontosabb parancsokból:

```bash
git status
```

* kiírja melyik branch-on vagy, melyek azok a fájlok amik módosultak vagy éppen confict-ot okoznak.

```bash
git branch
git checkout [name_of_the_branch]
```

* előbbi kilistázza a lokális branch-okat (*-a* kapcsolóval a szerver oldaliakat is), míg utóbbival másik branch-ra lehet váltani. Ugyanez a *-b* kapcsolóval kiegészítve új branch-ot hoz létre (lokálisan).

```bash
git pull
```

* az aktuális lokális branch-ot szinkronizálja a szerveroldalival.

```bash
git add .
git commit -m "A really meaningful message"
git push origin [name_of_branch]
```

* első lépésben a mappa összes megváltozott fájlját hozzáadja az indexelési listához, a másodikban rögzítjük ezeket a változásokat a lokális repoban, végül a harmadikban a szerver oldali repot szinkronizáljuk a lokálissal.

> **Conflict**: előfordulhat, hogy egy fájlnál az időbélyegek sorrendje ,,megkeveredik'' (pl. akkor is, ha a laptopodon elfelejted push-olni a munkádat, az otthoni gépeden csinálsz valami változást, majd a laptopodon kiadsz egy pull-t...), ilyenkor jól behatárolt *conflict* keletkezik. [Ezen a linken](https://help.github.com/articles/resolving-a-merge-conflict-using-the-command-line/) találtok egy jó leírást, hogy hogyan kell ezeket feloldani.

A továbbiakban szeretnénk majd csapatmunkát, úgyhogy szerveződjetek 2-5 fős csapatokba és hozzatok létre közös repot. Ezt a legegyszerűbben úgy tudjátok megtenni, ha a repo tulajdonosa annak a beállításainál a *Collaborators* pontban hozzáadja a többieket.

---

### Python

A fenti csomagok telepítése elég ahhoz, hogy a `quickhistogram.py` működjön, azonban ha a későbbiekben valamiről kiderül hogy még nincs telepítve, akkor a `pip install [package]` parancs gyorsan orvosolja a problémát. Aki Jupyter-ben szeretne dolgozni, annak a https://try.jupyter.org/ oldalon van erre lehetősége (ha a korábbi ELTÉs Jupyter-hez még van hozzáférésetek akkor természetesen az is jó), de akár saját magatoknak is telepíthetitek [innen](http://jupyter.org/install.html) (megj.: az Anaconda telepítését én nem javaslom). Végül de nem utolsó sorban a jó öreg terminálra mindig lehet számítani:

```bash
python3 quickhistogram.py [other arguments]
VAGY
chmod +x quickhistogram.py
./quickhistogram.py [other arguments]
```

A mellékelt program a 3 adatfájlt (argumentumként írandók) egyszerűen betölti majd (ahol van) hibával plotolja. Jó kiindulási alap lehet későbbi feladatokhoz.

---

### Latex

A `latex` mappában találtok egy elég sok mindenre kiterjedő sablont, melyben igyekeztem rámutatni sok lehetséges hibaforrásra is. Hivatkozásjegyzéket `bibtex` segítségével készíti el, ami egy elterjedt (de nem az egyetlen) módja a hivatkozások rendszerezésének. A `lazy.sh` egy egyszerű shell szkript ami elvégzi helyettünk a tex fájl lefordításának rendkívül fáradtságos műveletét.

> Ez is (és még megannyi minden más is) teljes egészében automatizálható pl. a VS Code pluginjei révén.

A `cv` mappában egy latex CV-re láthattok egy példát, ami egy külső (nem a rendszerrel együtt telepített) `cls` stílusfájl alapján készül. Ehhez (és bármi máshoz is) léteznek előre elkészített stílusfájlok, pl. [itt](https://www.latextemplates.com/cat/curricula-vitae) vagy [itt](https://www.sharelatex.com/templates/thesis).

---

### C++, cmake

Hamarosan!

---

# Házi feladat

1. saját git repo létrehozása, az alap parancsok begyakorlása
2. néhány fős csoportoként közös git repo létrehozása

> A repo linkjét küldjétek el a biro.gabor@wigner.mta.hu és nagy-egri.mate@wigner.mta.hu címekre!

3. Tetszőleges sablon alapján és tetszőleges tartalommal feltöltött CV írása és feltöltése a **közös** git repoba