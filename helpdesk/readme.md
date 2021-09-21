**Helpdesk bot with data retrival from different database as per the query of the user and can connect to telegram bot for the result**

**File Structure:**


  - Data/nly.yml : Contains data for intent classfication.
  - Data/stories.yml : Contains stories so as to make action according to it
  - Data/rules.yml : Rule for execution as per the intents
 
Actions:
  - action.py : Used to do modular tasks like retriving data from database or other api, filling forms
 
Models:
  - models : Containes model files after training
  
endpoints.yml : contains the webhook configuration for the custom actions
 


**Connecting to Telegram Bot :**
 We need to modify the credential file and provide the details as per the bot features.
 More details can be found [here](https://rasa.com/docs/rasa/connectors/telegram/).

Here is the link to make bot using [telegram](https://core.telegram.org/bots).
