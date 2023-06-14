# Guessing Game

The Guessing Game is a simple game where the computer randomly chooses a number between a specified range, and the player's objective is to guess that number. Here's how the game works:

At the beginning of the game, the computer displays the rules and prompts the player to make a choice.

If the player chooses to play, they can select from three difficulty levels: Easy, Medium, and Pro. Each level corresponds to a different range of numbers to guess from.

Once the player selects a level, the game begins. The computer generates a random number within the chosen range.

The player is prompted to enter their guess. If the input is not a valid number, they are asked to enter a valid number.

After each guess, the computer provides feedback to the player. If the guess is too low, the computer displays "Too low. Try again!" If the guess is too high, the computer displays "Too high. Try again!"

The player continues guessing until they guess the correct number. Once the correct number is guessed, the computer displays "Congratulations! You took X attempts," where X represents the number of attempts made by the player.

The game ends, and the player is given the option to play again or quit. If they choose to play again, they can select a new level. If they choose to quit, the game exits.

The game provides an interactive and challenging experience for the player, encouraging them to guess the correct number within the given range with as few attempts as possible.


![intro image](/assets/main.png)

## Demo

Welcome to [Guessing Game](https://ci-python.herokuapp.com/)

[GitHub Repo](https://github.com/CVilares/ci-python)

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
* [Credits](#credits)

- - - 
### User Experience UX

Let's break the user experience step by step:

1. The game starts with a friendly welcome message, clearly stating the name of the game and its objective.

2. The user is presented with a clean and organized menu, featuring three options: 'R' to read the rules, 'P' to play the game, and 'Q' to quit.

3. If the user selects 'R' to read the rules, the rules of the game are displayed using clear and concise language, ensuring they are easy to understand.

4. When the user chooses 'P' to play the game, the difficulty levels are presented with descriptive labels ('Easy,' 'Medium,' 'Pro') and their respective number ranges.

5. After selecting a difficulty level, a new game session starts, and the user receives a personalized message inviting them to guess a number within the specified range.

6. The input validation process is enhanced to provide immediate feedback when an invalid entry is made. Clear error messages guide the user to enter a valid numeric guess.

7. If the user's guess is outside the valid range, a specific error message notifies them of the valid range, prompting another guess.

8. Each time the user makes a guess, the feedback provided by the game ('Too low' or 'Too high') is displayed prominently, ensuring easy visibility.

9. The user is encouraged to continue guessing until they find the correct number, with the game keeping track of their attempts and providing a sense of progress.

10. Once the user successfully guesses the number, a celebratory message acknowledges their achievement, accompanied by the number of attempts taken.

11. A closing message signifies the end of the game, providing closure and thanking the user for their participation.

The Guessing Game creates a user-friendly experience that guides the player through the rules, offers clear instructions and feedback, and keeps them engaged and motivated to reach the correct solution.




- - - 
 ##  Technologies Used

-   [Git:](https://git-scm.com/) was used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
-   [GitHub:](https://github.com/) is used as the respository for the projects code after being pushed from Git.
-   [Herokuapp:](https://www.heroku.com/) for deployment.
- [Am I Responsive:](http://ami.responsivedesign.is) Checking the responsiveness.
- [W3Schools:](https://www.w3schools.com/) To learn , test and train.
-   [Code Institute](https://codeinstitute.net/global/) To learn and train
-   [Stack Overflow](https://stackoverflow.com/) To learn and train
-   [Python](https://pt.wikipedia.org/wiki/Python)
- - - 


### Features

1-Random Number Generation: The code uses the random.randint() function to generate a random number between 1 and 300. This random number is the target number that the player needs to guess.

![Reactions](/assets/randomnumber.png)

2-Game Loop: The code uses a while loop to keep the game running until the player guesses the correct number. The loop continues until the player's guess matches the target number.

![Reactions](/assets/feedback.png)

3-User Input: The code prompts the player to enter their guess using the input() function. The player's input is then validated to ensure it is a valid number between 1 and 300 depending on the choosen level.

![Reactions](/assets/validation.png)

4-Feedback: After each guess, the code provides feedback to the player. If the guess is too low, it displays the message "Too low. Try again!" If the guess is too high, it displays "Too high. Try again!"

![Reactions](/assets/gameover.png)

5-Attempts Count: The code keeps track of the number of attempts made by the player using the attempts variable. It increments the attempts variable after each guess.

![Reactions](/assets/feedback.png)

6-Game Over: When the player guesses the correct number, the code displays a congratulatory message along with the number of attempts it took. The game then ends.

![Reactions](/assets/over.png)

7-Game Menu: The code provides a simple menu for the player to choose options. The menu allows the player to read the game rules, start playing the game, or quit the game.

![Reactions](/assets/menu.png)

8-Rule Display: The code includes a function called display_rules() that prints the rules of the game when the player selects the option to read the rules.

![Reactions](/assets/rule.png)

9-User Experience: The code includes user-friendly messages to welcome the player, prompt for input, and provide instructions. It also handles invalid input gracefully and prompts the player to enter a valid number.

![Reactions](/assets/welcome.png)

10- Play Again Option: After each round of the game, when the user guesses the correct number or decides to quit the game, the program returns to the start menu. From the start menu, the user can choose to play the game again by selecting the "P" option.Once the user selects the "P" option, a new round of the game starts, and the user can continue guessing numbers to try and find the correct answer. This process can be repeated as many times as the user wants by selecting the "P" option from the start menu.

![Reactions](/assets/again.png)

11- Levels: The code offers three levels of difficulty for the player to choose from: Easy, Medium, and Pro. Each level has a different range of numbers to guess from, providing varying degrees of challenge.

![Reactions](/assets/level.png)
- - -

### Potential Implementations

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

5- Bellow Build and deployment and bellow SOURCE choose  Main from the drop list.

6- Choose which folder to deploy from, usually "/root".

7- Click "Save", then WAIT for it to be deployed. 

8- Your URL will be displayed above "Source

To deploy the website to Heroku, follow these steps:

1- Create or log in to your Heroku account.

2-Create a new app on Heroku with a unique name.

3-Set the buildpacks for the app in the correct order. In this case, set the buildpacks to Python and NodeJS.

4-Connect your app to the GitHub repository that contains your website's code.

5-Config variable for PORT with a value of 8000.

6-In the deployment tab of your Heroku app, you have the option to choose between automatic deployment or manual deployment. If you select automatic deployment, the app will automatically update with each new push to the repository.

7-If you prefer manual deployment, you can choose that option and manually trigger the deployment whenever you want, typically after making certain changes to the code.
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
### Other tests framework????


* Background and foreground colors have a sufficient contrast ratio.
* All pages and images are loaded without issues.
* All text is visable and appropriately positioned, text sizing and font are legible.
* When you hover over  buttons with your mouse, the color or opacity change to give a visual indication to the user.
* Hover on touch-sensitive devices, such as mobile devices, may not work in the same way as on devices with a mouse.
* Consistent Design: By specifying a specific font family, you can ensure that the text content on your website or application appears consistently across different devices and platforms.

- - -

### Credits 

- Code Institute
- A special thank you to my mentors, family,friends.
- Slack comunity

- - -
