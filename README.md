# **The Hangman Game**

A classic game of hangman written in Python and played in a terminal based window. The game is deployed to Code Institute's mock terminal on Heroku.   



User will only have six attempts to try and uncover the letters of the secret word - only hint is the length of the word.The words is randomly selected from a file with  
nearly 2500 words. The letters of the secret word is hidden by asterisk symbols and will uncover once the user guesses the correct letter. The secret word is revealed  
to user at the end of the game regardless of forfeit or win. If user manages to guess the word, 100 point is awarded and a total score is shown to the user as they  
descide to leave the game.
  
[Here is the live version of my project](https://hangman-gamee.herokuapp.com/)

<img width="1000" src="documentation/responsive.png">

---
## **Features** 

### **Navigation**  

 * The top of the page shows the studio name, a clickable link that takes user back to homepage.
 * To the right of the navigation user can find links to home, blog and gallery pages.
 * The navigation has a dark font and a lighter background for good contrast.
 * The studio name has a bigger font than the navigation bar to make a clear statement of the name of studio and webpage.

 <img width="1000" src="documentation/main.png">

### **The main section**

* The main section gives users a glimt of the studio through a large photo of two women training in serene enviroment.
* The main text is a short introduction of the yoga studio.
* Under the intriguing main text is a clickable read more button that takes users to about section further down the page.
* The previous colors from the header is switched up in the main section with headers background as font color and vice versa. 

<img width="1000" src="documentation/username.png">

### **The about section**
* The about section gives the users more information about the studio and location.
* This section provides user with information about the studio, what the goal of the studio is and and whom the yoga classes are for - everybody! 
* The same woman from the main section accours in this sections again to maintain a common tread.
* The colors from the header recur in this section.

<img width="1000" src="documentation/start-game.png">


### **Customer reviews**

* The customer reviews aim to increase the users need for a visit to the studio by showing three happy clients reviews.
* The goal is to reenforce the user that the studio is worth a visit.
* The colors from main section recurs here to create a good balance between sections.

<img width="1000" src="documentation/reviews.png">

### **The contact section**

* The contact section provides the user with location to join The Yoga Studio.
* This section also gives user contact information to call or email.
* The page matches the colors from about section with same box style.

<img width="1000" src="documentation/contact.png">

### **The footer section**
* The footer section is linked with all social media platforms the studio is connected to.
* The page links to facebook, instagram, twitter and youtube and opens i new tabs when clicked.
* The colors from the header at the top, matches the colors in this section at the bottom of page - to create a nice frame to page.

<img width="1000" src="documentation/social-media.png">

## **Blog page**

### **Blog preview**

* The blog navigation link from the home page redirects user to the blog page.
* In the blog main page a preview of three blog posts can be seen, the whole area round the previews is clickable and redirects users to the full blog posts in other pages.
* The blog preview page is arrenged to fit in with colors from the home page.
* The magnifying glas icon is used to hint to users that the area is a clickable link that will redirect them.

<img width="1000" src="documentation/blog-main.png">

### **Full blog post pages**

* The full blog post pages is color indentical to its parent blog page - the blog preview page.

<img width="1000" src="documentation/full-blog-post.png">

## **Gallery**

* Matching photos is combined in one page to give inspiration to users.
* The gallery is responsive and changes from 4 columns - to three - to two and lastly to one in small devices.

<img width="1000" src="documentation/gallery.png">

---

## **Testing**

* I tested that the page works in diffrent browsers such as Chrome, firefox and Microsoft Edge.
* I confirmed that this project is responsive, looks good and functions on all standard screen sizes using the devtools device toolbar.
* I confirmed that the header, navigation, main, about us, reviews, footer, gallery and blog pages text are all readable and easy to understand.
* I have confirmed that the links between diffrent pages work and are accessible.

## **Bugs**

* When I deployed my project to Github pages I discovered my project was broken, the links to the other files (CSS, blog and gallery) dit not work.
* I discovered this was because I had used aboulte file paths such as this in my code

![bug, wrong filepath](documentation/filepath.png)

* When I removed the / from the start of the path the problem was fixed.

---

## **Validator testing**

* HTML
3 errors occured since I used h1-headings on three occations i blog.html, when replaced code passed.
* CSS
No errors were found when passing through the official (Jigsaw) validator.
* Accessability
I confirmed that the colors and fonts chosen are easy to read and accessible by running it through lighthouse in devtools.

<img width="1000" src="documentation/lighthouse-score.png">

---

### **Unfixed Bugs**

* No unfixed bugs.

---

## **Deployment**

The site was deployed to GitHub pages. The steps to deploy are as follows:
* In the GitHub repository, navigate to the settings tab.
* From the source section drop-down menu, select the Master Branch.
* Once the master branch has been selected, the page provided the link to the completed website.

The live link can be found here - [The Yoga Studio](https://thereslundqvist.github.io/The-Yoga-Studio/)

---

## **Credits**

### **Content**

* The text for the about section is copied and translated from [Hot Yoga - Stockholm](https://www.hotyogasthlm.se/)
* The customer reviews was copied from [Trustpilot](https://www.trustpilot.com/review/www.yogabody.com)
* Icons for about, reviews, social media icons and blog headers are from [Font Awesome](https://fontawesome.com/)
* The blogposts are copied from [Mind Oasis](https://mindoasis.org/)

### **Media** 

* The images was all downloaded from [Pexels](https://www.pexels.com/sv-se/)
