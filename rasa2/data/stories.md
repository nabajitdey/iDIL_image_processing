 ## happy path
* greet
  - utter_how_can_i_help
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## search check happy path
* greet
  - utter_how_can_i_help
* search_provider{"check":"pool"}  
  - action_check_search
* thanks
  - utter_goodbye

## list checks happy path
* greet
  - utter_how_can_i_help
* search_provider{"food_group":"food menu"}  
  - action_check_search
* thanks
  - utter_goodbye


## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
