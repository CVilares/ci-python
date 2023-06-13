# Guessing number game

The computer selects a random number between a specified range. For example, it may choose a number between 1 and 100.

The player is then prompted to enter their guess for the chosen number.

After the player enters their guess, the computer provides feedback to help the player narrow down their guess. If the player's guess is lower than the chosen number, the computer will say "Too low." If the guess is higher, the computer will say "Too high." This feedback guides the player towards the correct number.

The player continues to guess and receive feedback until they guess the correct number.

Once the player guesses the correct number, the game ends, and the player is notified of their success. The game may also display the number of attempts it took the player to guess correctly.

The purpose of the game is for the player to use their logic and intuition to make educated guesses and eventually arrive at the correct number. The game can be repeated multiple times, allowing the player to improve their guessing skills and challenge themselves to guess the number in fewer attempts.

The code provided implements a basic version of the guessing number game, where the computer generates a random number, the player enters their guesses, and the computer provides feedback until the correct number is guessed.






![responsive image](/assets/images/rsp.png)


## Demo

Welcome to [Sporting Quiz](https://cvilares.github.io/quizJavascript/)

- - -

# Contents
* [User Experience](#user-experience-ux)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Potential Implementations](#potential-implementations) 
* [Browser Compability](#browser-compatibility)  
* [Validator Testing](#validator-testing)
* [Color Scheme ](#color-scheme)
* [Typography](#typography)
* [Deployment](#deployment)  
* [Responsiveness](#responsiveness)
* [Other tests](#Other-tests)
* [Fork and Clone](#fork-and-clone)  
* [Credits](#credits)

- - - 
### User Experience UX

The provided code offers a simple and straightforward user experience for the guessing game. Let's break down the user experience step by step:

1-The game starts with a welcome message, introducing the user to the Guessing Game.

2-The user is presented with three options: 'R' to read the rules, 'P' to play the game, and 'Q' to quit the game.

3-If the user selects 'R' to read the rules, the rules of the game are displayed on the screen, providing clear instructions on how to play.

4-If the user selects 'P' to play the game, the game begins. The user is prompted to enter their guess for the chosen number.

5-The user's input is validated to ensure it is a valid number. If the input is invalid, an error message is displayed, and the user is asked to enter a valid number.

6-If the input is a valid number, the game checks if the guess is within the valid range of 1-100. If the guess is outside the range, an error message is displayed, and the user is asked to guess again within the valid range.

7-If the guess is within the valid range, the game provides feedback to the user. If the guess is lower than the chosen number, the message "Too low. Try again!" is displayed. If the guess is higher, the message "Too high. Try again!" is displayed.

8-The user continues to guess and receive feedback until they guess the correct number. Once the correct number is guessed, a congratulatory message is displayed, informing the user of the number of attempts it took them to guess correctly.

9-After the game ends, the user is informed that the game is over.

The code structure and user experience provided in the code ensure that the user can easily understand and interact with the game. The game offers clear instructions, validates user input, and provides appropriate feedback to guide the user towards the correct guess.


### Interactive Quiz Experience

Navigation: The user can navigate through the quiz using the provided options and buttons. They can progress to the next question, submit their answers, and receive feedback on their performance.

Question Display: The quiz displays questions one at a time, allowing the user to focus on each question individually. This approach helps prevent overwhelming the user with too much information at once.

Answer Selection: The user can select their answer from the provided options. This allows for easy interaction and ensures that the user understands the available choices.

Immediate Feedback: After the user selects an answer, the quiz provides immediate feedback. 

Scoring and Progress Tracking: The quiz keeps track of the user's score. The user can see their current score, allowing them to track their progress throughout the quiz.

Random Quotes: The inclusion of random quotes adds an extra element of interest and variety to the quiz. It provides an opportunity to engage the user with quotes related to the quiz's theme.

Success and Failure Pages: The quiz incorporates separate pages for success (congratulations) and failure (disappointment) scenarios. If the user achieves a high score, they are redirected to the success page, acknowledging their achievement. Conversely, if the user fails to answer correctly within the given attempts, they are redirected to the failure page, providing closure to their quiz experience.

- - - 
 ##  Technologies Used

-   [Google Fonts:](https://fonts.google.com/) 
-   [Git:](https://git-scm.com/) was used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
-   [GitHub:](https://github.com/) is used as the respository for the projects code after being pushed from Git.
- [Am I Responsive:](http://ami.responsivedesign.is) Checking the responsiveness.
- [W3Schools:](https://www.w3schools.com/) To learn , test and train.
-   [Code Institute](https://codeinstitute.net/global/) To learn and train
-   [Stack Overflow](https://stackoverflow.com/) To learn and train
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

- - - 


### Features

- Displaying Questions:

The displayQuestion function retrieves the current question from the questions array and displays it on the screen.

- Handling User Answers:

The checkAnswer function is called when the user selects an answer. It compares the user's answer with the correct answer for the current question and updates the score accordingly.
If the user's answer is correct, the score is incremented, and a message is logged to the console.
If the user's answer is wrong, the wrong answer count is incremented. If the count reaches 3, the showDisappointment function is called to redirect the user to the "end.html" page.
The score display is updated using the updateScore function.

- Moving to the Next Question:

The nextQuestion function increments the currentPos variable to move to the next question. If the end of the questions array is reached, it wraps around to the first question.

- Checking Total Score:

The checkTotalScore function checks if the user's total score reaches 5. If it does, the showCongratulations function is called to redirect the user to the "congratulations.html" page.

- Updating Score Display:

The updateScore function retrieves the score element from the HTML document and updates its content with the current score.

![Reactions](/assets/images/sum.png)
![Reactions](/assets/images/sdois.png)

- Displaying Random Quote:

The displayRandomQuote function selects a random quote from the quotes array and displays it on the screen. It includes a random quote and the corresponding character.

![Random Quote](/assets/images/random.png)

- Setting Up Answer Listeners:

The setupAnswerListeners function adds event listeners to the answer elements. When an answer is clicked, the checkAnswer function is called with the corresponding answer index.

- Starting the Quiz:

The startQuiz function is called initially to begin the quiz. It displays the first question, sets up the answer listeners, and displays a random quote.

- Showing Congratulations and Disappointment Pages with a Try Again button that leads you to the start main page.

The showCongratulations function redirects the user to the "congratulations.html" page when the total score reaches 5.
The showDisappointment function redirects the user to the "end.html" page when the wrong answer count reaches 3.
![Reactions](/assets/images/congs.png)
![Reactions](/assets/images/end.png)



- Rules button that leads you to the quiz rules and to start game button.
![Reactions](/assets/images/rules.png)
![Reactions](/assets/images/ruless.png)

- - -

### Potential Implementations



-  Timer: Implement a timer to add a time constraint for answering each question. This adds an element of urgency and can make the quiz more challenging.


- Progress Bar: Add a visual progress bar to indicate how far the user is in the quiz. It helps provide a sense of completion and motivates users to continue.

- High Scores: Implement a high score feature where users can save their scores and compare them with other players. This can encourage competition and replayability.

-  Score Multipliers: Assign score multipliers for consecutive correct answers. For example, if the user answers two questions correctly in a row, their score for the third question could be doubled.

- Hint System: Provide users with the option to request hints for difficult questions. You can display additional information or eliminate one or more incorrect answer choices.

- Share Results: Enable users to share their quiz results on social media platforms or via email. This can encourage others to take the quiz and increase its reach.

- - -

### Browser Compatibility in progress 

- This pages were successfully tested on Safari ,Firefox and Google Chrome browsers.

### Validator Testing 
HTML

- All HTML tested separeted,no errors were returned when passing through the official W3C validator.

![HTML Page](/assets/images/htlmvalidation.png)
  

CSS
No errors were found when passing through the official (Jigsaw) validator

  * CSS Page
![CSS Page](/assets/images/cssvalid.png)

Javascript
- No errors were returned when passing through the JSHint validator.
![JavaScript Page](/assets/images/javas.png)
- - -

### Color Scheme 

- The color scheme chosen for this quiz is inspired by the football club's main colors, predominantly green and white, with hints of yellow. These colors reflect the club's identity and serve as the main theme throughout the quiz. The use of green symbolizes the club's vitality, growth, and connection with nature, while white represents purity, clarity, and the club's commitment to fair play. The subtle touches of yellow add a vibrant and energetic element, complementing the overall design and enhancing the visual appeal. This color combination creates a visually pleasing and cohesive experience, immersing users in the spirit of the football club as they engage with the quiz.

## Typography
The font roboto was used for the entire quiz.

- - -
### Deployment 

1. Login or Sign Up to GitHub.
2. Go to project repository.
3. Select Settings
4. Click on "Pages" in the left side of the panel.
5. Bellow Build and deployment and bellow SOURCE choose  Main .
6. Choose which folder to deploy from, usually "/root".
7. Click "Save", then WAIT for it to be deployed. 
8. Your URL will be displayed above "Source

- - -

### Responsiveness 

Chrome developer tool have been used to check successfully the responsivness in multiple kind of devices.

The responsiveness was also tested successfully on :

- Desktop
  1600x992px scaled down to scale(0.3181)
- Laptop
  1280x802px scaled down to scale(0.277)
- Tablet
  768x1024px scaled down to scale(0.219)
- Mobile
  320x480px scaled down to scale(0.219)

  
- - -
### Other tests 


* Background and foreground colors have a sufficient contrast ratio.
* All pages and images are loaded without issues.
* All text is visable and appropriately positioned, text sizing and font are legible.
* When you hover over  buttons with your mouse, the color or opacity change to give a visual indication to the user.
* Hover on touch-sensitive devices, such as mobile devices, may not work in the same way as on devices with a mouse.
* Consistent Design: By specifying a specific font family, you can ensure that the text content on your website or application appears consistently across different devices and platforms.


- - -
### Fork and Clone 
**Fork**
1. Login or Sign Up to GitHub.
2. Open the project [repository](https://github.com/CVilares/quizJavascript).
3. Click the Fork button in the top right corner.

**Clone**
1. Login or Sign Up to GitHub.
2. Open the project [repository](https://github.com/CVilares/quizJavascript).
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in the code editor of your choice and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.

- - -

### Credits 

- This project was inspired on https://github.com/jamesqquick/Build-A-Quiz-App-With-HTML-CSS-and-JavaScript
- A special thank you to my mentors, family,friends.
- Slack comunity

- - -
