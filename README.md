# TomBworld Adventure

Welcome to 'Tombworld Adventure' a text-based adventure game that plunges you into the grim and foreboding universe of Warhammer 40,000. You're a miner on a desolate planet, working diligently until a mysterious blackout transports you to the heart of a Necron tomb world. Navigate treacherous catacombs, decipher ancient hieroglyphs, and battle unspeakable horrors in your quest for survival and escape. Can you overcome the malevolent forces of the Necrons and find your way back to the world you once knew?



[View TomBworld Adventure live project here](https://tombworld-adventure-26cae5d127df.herokuapp.com/)


![Am I Responsive](assets\images\README_Am_I_Responsive.png)

### Table of Contents

- [User Experience](#user-experience)
- [User Stories](#user-stories)
- [Features](#features)
- [Existing Features](#existing-features)
- [Features Left to Implement](#features-left-to-implement)
- [Challenges Faced](#challenges-faced)
- [Testing](#testing)
- [Deployment and local development](#deployment-and-local-development)
- [Design](#design)
- [Technologies Used](#technologies-used)
- [Sites & Programs Used](#sites--programs-used)
- [Credits](#credits)

---

### User Experience

#### Game Objective 
- Survival: Navigate through the treacherous Necron tomb world, making choices that maximize your chances of staying alive.

- Escape: Uncover the mysteries of the tomb and find a way to escape back to your world.

- Confrontation: Encounter and engage with the malevolent forces of the Necrons, including solving puzzles and making decisions in the face of danger.

- Exploration: Explore the eerie catacombs, decipher ancient hieroglyphs, and piece together the secrets of this grim universe.

- Choices: Make critical decisions that impact the outcome of the story, leading to different endings.

#### Controls 
- You navigate the maze by selecting a number that corresponds to the available choices in each room.

#### Enjoy the Challenge 
- Embrace the challenge and immerse yourself in the intriguing world of Tombworld Adventure. Confront the mysteries of the Necron tomb world, decipher ancient hieroglyphs, and make life-or-death decisions in a gripping text-based journey. Are you ready to test your wits and determination in this thrilling adventure?

---

### User Stories

#### For First-time Visitors
- When starting your journey in the Tombworld Adventure game, you'll find yourself immediately drawn into the immersive world. A compelling representation of the game's setting and a prominently placed 'Run Game' button will eagerly invite you to embark on your adventure.
#### For Returning Visitors
- For those returning to the Tombworld Adventure, welcome back to the ever-engaging world of mystery and decision-making. The 'Run Game' button stands ready, inviting you to resume your journey into the depths of the Necron tomb world, where new challenges and secrets await.
#### For Frequent Users
- For those who frequently play the game, my goal is to continually improve and strive to find a way out.

---

### Features

- Immersive Narrative: Explore a captivating storyline set in the Warhammer 40,000 universe.
- Choices and Consequences: Make decisions that impact the narrative and lead to various outcomes.
- Exploration: Journey through eerie catacombs, decipher ancient hieroglyphs, and unveil Necron secrets.
- Combat Encounters: Engage in strategic battles against malevolent foes with randomized results.
- Inventory Management: Collect and utilize items to aid in your survival and progress.
- Challenging Puzzles: Solve cryptic puzzles that test your wit and resourcefulness.
- Revisit Choices: Rewind to explore different paths and uncover all the game's secrets.
- Evolving Storyline: Frequent updates and new content to keep the adventure fresh and exciting.

---

### Existing Features

#### Text-Based Immersion
- Dive into a nostalgic text-based adventure experience that focuses on storytelling and decision-making.

<img src="assets\images\README_console_screen.png" alt="Picture of Console Screen" width= 600px>

#### Rich Storytelling
- Enjoy a well-crafted narrative that keeps you engaged.

<img src="assets\images\README_storytelling.png" alt="Picture of Story" width= 600px>

#### Interactive Exploration
- Interact with the game world by making choices, uncovering secrets, and encountering various characters.

<img src="assets\images\README_decision_making.png" alt="Picture of Decisions" width= 600px>

---

### Features Left to Implement

#### Persistent Player Health
- In future add in persistent player health that will allow the engagement of multiple foes, this would allow an adjustment in navigation options and open new ways to try to finish the game.

#### New Rooms

- Currently there are 13 rooms, each with their on story elements, this could be expanded on to allow a more immersive experience.

---

### Challenges Faced

#### Understanding Game Mechanics 
- Overseeing the process of making critical decisions and guiding your path through the intricate maze of choices, leading you through the intricacies of the game world.

#### Combat System
- Introducing a combat system that simulates a D6 dice roll with a random number generator in the range of 1 to 6, where a successful hit is dependent on the outcome of this roll.

#### Story telling
- Crafting a captivating narrative within the Warhammer 40,000 universe, designed to resonate with both newcomers and seasoned veterans of the franchise. The story aims to provide an engaging experience for a diverse audience.

#### Implementing different printing speeds
- I thought it was important to have multiple printing speeds to assist the story telling but also not impact gameplay too much. I settled on 3 different speed options.

---

### Testing 

<details>
<summary>PEP8 Linter - PASS</summary>

- run.py

    <img src="assets\images\README_PEP8_linter_run.png" alt="Picture of Story" width= 600px>

- game_stories.py

    <img src="assets\images\README_PEP8_linter_game_stories.png" alt="Picture of Story" width= 600px>

- gameplay.py

    <img src="assets\images\README_PEP8_linter_gameplay.png" alt="Picture of Story" width= 600px>


- [PEP8 Code Institute](https://pep8ci.herokuapp.com/)

</details>

<details>
<summary>Lighthouse  -  PASS</summary>

- Desktop

    <img src="assets\images\README_lighthouse.png" alt="Description" width="550" height="150">

</details>

#### Manual Testing

- Narrative Cohesion Test: Ensure that the storyline remains consistent and coherent as players progress through different paths and choices. Test whether all narrative branches lead to logical outcomes and maintain the immersion.

- Game Mechanics Stress Test: Evaluate how well the game mechanics handle complex scenarios. Create test cases that involve multiple interactions, combat situations, and inventory management to assess the system's stability.

- Player Decision Impact Test: Assess how player decisions affect the story's direction and outcomes. Test various choices to confirm that they result in meaningful consequences and multiple story branches.

- Bug and Error Testing: Conduct thorough testing to identify and address any bugs, glitches, or errors in the game, including graphical glitches, incorrect text, or gameplay issues.

#### Bug Fixes and Improvements

- Infinite Loop with user_input: The issue where the input loop was causing an infinite loop when an invalid entry was made has been fixed by using a while loop and appropriate if conditions to handle different user inputs.

- Validation for Picking Up Mining Laser: A validation check has been added to the weapon_1() function to ensure that the player cannot pick up multiple Mining Lasers if it's already in the WEAPON_TYPE list.

- Returning Text from main_story(): The main_story() function has been modified to return the story text as a string, enabling it to be used with the slow_print() function.

- Handling Comments Exceeding 79 Characters: When comments exceed 79 characters, they have been split into multiple lines or reformatted to adhere to the recommended line length limits.

- New Line Before Input: New lines have been added before input prompts to enhance readability and user experience.

---

### Deployment and local development

#### GitHub Pages

GitHub Pages used to deploy live version of the website.
1. Log in to GitHub and locate [GitHub Repository Snake](https://github.com/barryCFlynn/tombworld_adventure)
2. At the top of the Repository(not the main navigation) locate "Settings" button on the menu.
3. Scroll down the Settings page until you locate "GitHub Pages".
4. Under "Source", click the dropdown menu "None" and select "Main" and click "Save".
5. The page will automatically refresh.
6. Scroll back to locate the now-published site [link](https://barrycflynn.github.io/Snake/) in the "GitHub Pages" section.

#### Heroku App hosting

Heroku use to host the Python app
1. Log In: Log in to your Heroku account using your credentials.
2. Create a New App: From your Heroku dashboard, click the "New" button.
Select "Create new app."
Provide a unique app name (it will become part of your app's URL) and choose a region. Click the "Create App" button.
3. Deployment Method: On your app's dashboard, you'll find a section labeled "Deployment method."
Choose the deployment method that matches your code repository. Options include Heroku Git, GitHub, and other integrations.
4. Connect to Your Repository: Depending on the chosen deployment method, you will need to connect your app to your code repository.
For example, if you choose GitHub, you will need to connect your GitHub account and select the repository containing your app's code.
5. Configure and Deploy: After connecting to your repository, you can configure deployment settings.
This might include specifying the branch to deploy, enabling automatic deploys, or configuring environment variables.
6. Manual Deploy (if not using automatic deploys): If you're not using automatic deploys, you can manually trigger a deployment from the Heroku Dashboard.
Go to the "Deploy" tab and click the "Deploy Branch" button.
7. Open Your App:Once the deployment is successful, you can open your app by clicking the "Open App" button on your app's dashboard.

---

### Design

#### Maze layout - Lucid Charts
- Used lucid charts to design the maze and some of the options from each room

    <img src="assets\images\README_lucid_chart.png" alt="Picture of Story" width= 600px>

#### Colour Scheme
- I opted to go with a very simple colour scheme to go with the background image used.
    - Primary Background Colour

        ![#04120a](https://placehold.it/150x40/04120a/FFFFFF?text=04120a)

    - Primary Text and Screen Colour
    
        ![#10ab13](https://placehold.it/150x40/10ab13/FFFFFF?text=10ab13)

    - Contrast Grid - Only AA and AAA options used.

        <img src="assets\images\README_contrast_grid.png" alt="Description" width= 300px>
            
#### Layout
- To have the main background image showing I opted to keep the Consoled screen and button in the default position form the Code Institute template for the project.
---

### Technologies Used

 - HTML
 - CSS
 - Python
 - App hosting
 - ChatGPT

---

### Sites & Programs Used

- [VS Code](https://code.visualstudio.com/)
    - Code editor.
- [Git](https://git-scm.com/)
    - To manage version control and push updates to GitHub.
- [Github](https://github.com/)
    - File Storage and Hosting the website.
- [Chat GPT](https://openai.com/blog/chatgpt)
    - Only used for troubleshooting and story telling elements.
- [Am I Responsive](https://ui.dev/amiresponsive)
    - Mockup picture for the README file.
- [8 Shapes Contrast Grid](contrast-grid.eightshapes.com)
    - Used to make sure colours are compliant.
- [Adobe Color](https://color.adobe.com/create/color-wheel)
    - Used to select colours on the site
- [Heroku](https://www.heroku.com/)
    - Used to host the Python app for the project
- [TextKool](https://textkool.com/)
    - for ASCII art generator - used for game title

---

### Credits

- My mentor Mitko Bachvarov for his help in guiding me through this project
- Background art was taken form the Warhammer Community site


