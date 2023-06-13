# Guessing Game

The computer selects a random number between a specified range. For example, it may choose a number between 1 and 100.

The player is then prompted to enter their guess for the chosen number.

After the player enters their guess, the computer provides feedback to help the player narrow down their guess. If the player's guess is lower than the chosen number, the computer will say "Too low." If the guess is higher, the computer will say "Too high." This feedback guides the player towards the correct number.

The player continues to guess and receive feedback until they guess the correct number.

Once the player guesses the correct number, the game ends, and the player is notified of their success. The game may also display the number of attempts it took the player to guess correctly.

The purpose of the game is for the player to use their logic and intuition to make educated guesses and eventually arrive at the correct number. The game can be repeated multiple times, allowing the player to improve their guessing skills and challenge themselves to guess the number in fewer attempts.

The code provided implements a basic version of the guessing number game, where the computer generates a random number, the player enters their guesses, and the computer provides feedback until the correct number is guessed.






![responsive image](/assets/responsive.png)


## Demo

Welcome to [Guessing Game](https://ci-python.herokuapp.com/)

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




- - - 
 ##  Technologies Used

-   [Git:](https://git-scm.com/) was used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
-   [GitHub:](https://github.com/) is used as the respository for the projects code after being pushed from Git.
-   [Herokuapp:] for deployment.
- [Am I Responsive:](http://ami.responsivedesign.is) Checking the responsiveness.
- [W3Schools:](https://www.w3schools.com/) To learn , test and train.
-   [Code Institute](https://codeinstitute.net/global/) To learn and train
-   [Stack Overflow](https://stackoverflow.com/) To learn and train
-   [Python](https://pt.wikipedia.org/wiki/Python)
- - - 


### Features

1-Random Number Generation: The code uses the random.randint() function to generate a random number between 1 and 100. This random number is the target number that the player needs to guess.

![Reactions](/assets/images/ruless.png)

2-Game Loop: The code uses a while loop to keep the game running until the player guesses the correct number. The loop continues until the player's guess matches the target number.

![Reactions](/assets/images/ruless.png)

3-User Input: The code prompts the player to enter their guess using the input() function. The player's input is then validated to ensure it is a valid number between 1 and 100.

![Reactions](/assets/images/ruless.png)

4-Feedback: After each guess, the code provides feedback to the player. If the guess is too low, it displays the message "Too low. Try again!" If the guess is too high, it displays "Too high. Try again!"

![Reactions](/assets/images/ruless.png)

5-Attempts Count: The code keeps track of the number of attempts made by the player using the attempts variable. It increments the attempts variable after each guess.

![Reactions](/assets/images/ruless.png)

6-Game Over: When the player guesses the correct number, the code displays a congratulatory message along with the number of attempts it took. The game then ends.

![Reactions](/assets/images/ruless.png)

7-Game Menu: The code provides a simple menu for the player to choose options. The menu allows the player to read the game rules, start playing the game, or quit the game.

![Reactions](/assets/images/ruless.png)

8-Rule Display: The code includes a function called display_rules() that prints the rules of the game when the player selects the option to read the rules.

![Reactions](/assets/images/ruless.png)

9-User Experience: The code includes user-friendly messages to welcome the player, prompt for input, and provide instructions. It also handles invalid input gracefully and prompts the player to enter a valid number.

![Reactions](/assets/images/rules.png)


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
