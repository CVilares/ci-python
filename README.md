# Guessing Game

The computer selects a random number between a specified range. For example, it may choose a number between 1 and 100.

The player is then prompted to enter their guess for the chosen number.

After the player enters their guess, the computer provides feedback to help the player narrow down their guess. If the player's guess is lower than the chosen number, the computer will say "Too low." If the guess is higher, the computer will say "Too high." This feedback guides the player towards the correct number.

The player continues to guess and receive feedback until they guess the correct number.

Once the player guesses the correct number, the game ends, and the player is notified of their success. The game may also display the number of attempts it took the player to guess correctly.

The purpose of the game is for the player to use their logic and intuition to make educated guesses and eventually arrive at the correct number. The game can be repeated multiple times, allowing the player to improve their guessing skills and challenge themselves to guess the number in fewer attempts.

The code provided implements a basic version of the guessing number game, where the computer generates a random number, the player enters their guesses, and the computer provides feedback until the correct number is guessed.


![intro image](/assets/intro.png)

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
* [heroku](#heroku)  
* [Credits](#credits)

- - - 
### User Experience UX

Let's break down the user experience step by step:

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

-  Difficulty Levels: Add different difficulty levels to the game, where the range of numbers to guess from can vary. For example, you can have an easy mode with numbers between 1 and 50, a medium mode with numbers between 1 and 100, and a hard mode with numbers between 1 and 1000.

-  Limit the Number of Attempts: Set a limit on the number of attempts the player has to guess the number. If they exceed the limit without guessing correctly, they lose the game.

-  Score Tracking: Keep track of the player's scores or points based on the number of attempts they take to guess the number. Assign higher scores for fewer attempts to encourage replayability and competition.

-  Multiplayer Mode: Implement a multiplayer mode where multiple players can take turns guessing the number, and the player with the fewest attempts wins.

-  Time-Based Challenges: Add a time limit for each guess, challenging the player to make their guess within a specified time frame. If they fail to do so, they lose the game.

- - -

### Browser Compatibility in progress 

- This pages were successfully tested on Firefox and Google Chrome browsers.

### Validator Testing 

- https://pep8ci.herokuapp.com/#

No errors were returned when passing through the PEP8 linter validator.

![PEP](/assets/pep.png)
  
- - -

### Deployment 

1- Login or Sign Up to GitHub.
2- Go to project repository.
3- Select Settings
4- Click on "Pages" in the left side of the panel.
5- Bellow Build and deployment and bellow SOURCE choose  Main .
6- Choose which folder to deploy from, usually "/root".
7- Click "Save", then WAIT for it to be deployed. 
8- Your URL will be displayed above "Source

- - -

### Responsiveness 

The responsiveness was also tested successfully on :

- Desktop
  1600x992px scaled down to scale(0.3181)
- Laptop
  1280x802px scaled down to scale(0.277)
- Tablet
  768x1024px scaled down to scale(0.219)
- Mobile
  320x480px scaled down to scale(0.219)

  ![responsive image](/assets/responsive.png)

  
- - -
### Other tests 


* Background and foreground colors have a sufficient contrast ratio.
* All pages and images are loaded without issues.
* All text is visable and appropriately positioned, text sizing and font are legible.
* When you hover over  buttons with your mouse, the color or opacity change to give a visual indication to the user.
* Hover on touch-sensitive devices, such as mobile devices, may not work in the same way as on devices with a mouse.
* Consistent Design: By specifying a specific font family, you can ensure that the text content on your website or application appears consistently across different devices and platforms.


- - -
### heroku

To deploy the website to Heroku, follow these steps:

1- Create or log in to your Heroku account.
2-Create a new app on Heroku with a unique name.
3-Set the buildpacks for the app in the correct order. In this case, set the buildpacks to Python and NodeJS.
4-Connect your app to the GitHub repository that contains your website's code.
5-Config variable for PORT with a value of 8000.
6-In the deployment tab of your Heroku app, you have the option to choose between automatic deployment or manual deployment. If you select automatic deployment, the app will automatically update with each new push to the repository.
7-If you prefer manual deployment, you can choose that option and manually trigger the deployment whenever you want, typically after making certain changes to the code.

- - -

### Credits 

- Code Institute
- A special thank you to my mentors, family,friends.
- Slack comunity

- - -
