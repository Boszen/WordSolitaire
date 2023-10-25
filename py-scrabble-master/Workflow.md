# Development Workflow

1. Make a 2 player Scrabble game
    1. Word validity checker function
    2. Function for finding word score
    3. Move validity checker function
    4. Set up testing system for game functions
    5. Graphics and user interface
        1. Set up state-driven game
        2. Grab/Create graphics and aesthetics for game
        3. Design user interface and features
        4. Make interactive game board
        5. Make interactive "hand"
        6. Make interactive interface
        7. Route the flow of the game
    6. Route the flow of the 2 players
    7. Create a logging system
    8. Main menu
        1. Design main menu
        2. Grab/Create graphical elements
        3. Code callback-based system for user interface elements
        4. Route the flow of the main menu (decisions tree)
    9. Set up behaviour-driven tesing system
    10. Create more tests
    11. Pass said tests
2. Write the AI for 1 player Scrabble game
    1. Abstract out the AI portion (class from player)
    2. Create the first AI class skeleton (best play for most points)
        1. Function to find highest scoring word
        2. Function to find highest scoring move
    3. Create the rest of the AI classes (specializations)
        - Ladder style (based on short word length)
        - Front-and-back hook style (based on long, open hooks with bingoes)
        - Mixed conservative (puts weight on getting as many bingoes as
          possible, but also tries to reserve specific letters as prefixes)
    4. Write testing system for best move for all of them (based on board)
3. Combine and implement both game modes into the menu
