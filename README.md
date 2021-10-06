# 2021 Python Assignments (September)

## 3.  All Roads Lead to One :heavy_check_mark: 
Γράψτε έναν κώδικα σε Python ο οποίος υπολογίζει πόσα βήματα χρειάζονται για να γίνει ένας αριθμός μονάδα κάνοντας την ακόλουθη διαδικασία: Αν ο αριθμός είναι ζυγός, τον διαιρεί με το 2, αν είναι μονός τον πολλαπλασιάζει με το 3 και προσθέτει ένα. Παράδειγμα: 7 → 3 * 7 + 1 = 22 → 11 → 3 * 11+ 1 = 34 → 17 → 17 * 3 + 1 = 52 → 26 → 13 → 13 * 3 + 1 → 40 → 20 → 10 → 5 → 3 * 5 + 1 → 16 → 8 → 4 → 2 → 1.

![output](https://github.com/vagman/Python-Intro-Projects/blob/master/2021%20September%20Assignments/img/all_roads_lead_to_one.jpg)
## 5. ANUOne :heavy_check_mark: 
Γράψτε έναν κώδικα σε Python ο οποίος παίρνει από τον κβαντικό υπολογιστή του [ANU](https://qrng.anu.edu.au/contact/api-documentation/) 1000 τυχαίους αριθμούς (0-255) και κρατάει τον κάθε ένα modulo 20. Εμφανίστε τα στατιστικά εμφάνισης του κάθε αριθμού.

![output](https://github.com/vagman/Python-Intro-Projects/blob/master/2021%20September%20Assignments/img/anu_one.jpg)

### Setup
* `pip install requests`

## 11. ANUTwo :heavy_check_mark: 
Γράψτε έναν κώδικα σε Python ο οποίος παίρνει από τον κβαντικό υπολογιστή του [ANU](https://qrng.anu.edu.au/contact/api-documentation/) 1000 τυχαίους αριθμούς (0-255). Στην συνέχεια, απεικονίζει τον κάθε αριθμό ως δυαδικό μήκους 8 και εμφανίζει α) το μεγαλύτερο μήκος συνεχόμενων μηδενικών και β) το μεγαλύτερο μήκος συνεχόμενων μονάδων.

![output](https://github.com/vagman/Python-Intro-Projects/blob/master/2021%20September%20Assignments/img/anu_two.jpg)

Note: Example was executed for length=10 for ease of understanding the concept.

### Setup
* `pip install requests`
* `pip install regex`

## 12. 0xPrinter :heavy_check_mark: 
Γράψτε έναν κώδικα σε Python ο οποίος διαβάζει ένα αρχείο που δηλώνει ο χρήστης (δεν είναι απαραίτητα κειμένου) και εμφανίζει το περιεχόμενό του σε γραμμές μήκους 16 χαρακτήρων. Αν ο χαρακτήρας είναι λειτουργικός τον εμφανίζετε ως κενό (space), αν είναι γράμμα εμφανίζετε τον χαρακτήρα A, αν είναι ψηφίο εμφανίζετε τον χαρακτήρα 1, αν είναι μέχρι το 128, εμφανίζετε το χαρακτήρα p, διαφορετικά, εμφανίζετε τον χαρακτήρα ?

Given input was `test.txt` file containing: 3a[भारतtesta3333333333333

![output](https://github.com/vagman/Python-Intro-Projects/blob/master/2021%20September%20Assignments/img/0xprinter.jpg)

# 2021 Python Assignments (June)

## 9. ASCII Prime :heavy_check_mark: 

Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει σαν είσοδο ένα αρχείο ASCII κειμένου και μετατρέπει τον κάθε χαρακτήρα στον αντίστοιχο αριθμό ASCII και κρατάει τους μονούς. Εμφανίστε τα στατιστικά εμφάνισης του κάθε γράμματος με “μπάρες” χρησιμοποιώντας το χαρακτήρα *, όπου κάθε * αντιστοιχεί σε 1%. Η στρογγυλοποίηση θα γίνει προς τα πάνω.

A: **********

C: ***

E: **************

G: **

### Setup
* Run as `python3 main.py`.

## 6. Twitter API :heavy_check_mark: 

Γράψτε ένα κώδικα σε Python ο οποίος συνδέεται στο twitter (χρησιμοποιείστε το tweepy) και επιλέξτε τα 10 τελευταία tweets του χρήστη που θα σας δηλώσει ο χρήστης. Εμφανίστε τις 5 μεγαλύτερες λέξεις και τις 5 μικρότερες λέξεις του.

### Setup

* Go to config.ini file and enter your own **consumer keys** and **access tokens** from [Twitter Developers](https://developer.twitter.com/en/portal/projects/).
* Run as `python3 main.py`.

# Genral Info
Python version: 3.9.X
