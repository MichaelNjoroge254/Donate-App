# Donate-App
An application that one can donate money to feed the street children and orphans 

## Author
- Michael Njoroge

## Live link
https://offer-donation.herokuapp.com/

## User Stories

- Sign in with the application to start using.
- Set up a profile about me and a general location and my neighborhood name.
- Find a list of different businesses in my neighborhood.
- Find Contact Information for the health department and Police authorities near my neighborhood.
- Create Posts that will be visible to everyone in my neighborhood.
- Change My neighborhood when I decide to move out.
- Only view details of a single neighborhood.

## Installation

### Requirements

- Python3.8 or a later version

#### Cloning

- Open the terminal/command prompt
- `git clone https://github.com/MichaelNjoroge254/Donate-App.git
- `cd Notify-Alerts`
- `code` or open through your preferred editor.

#### Running the application

1. Set Up the virtual environment
- `python3.8 -m venv --without-pip virtual` to install the virtual environment
- `source virtual/bin/activate` to activate virtual environment

2. Install all the required dependancies
- `python3.8 -m pip install -r requirements.txt`

3. Running the application
- `python3 manage.py runserver`

## Behavior Driven Development

|Behavior|Input|Output|
|--------|-----|------|
|User login|Clicks on the login button|Login form for an authenticated user|
|Register|Clicks on the register button|Register form for new users|
|Incorrect data input||Flash message indicating the errors|
|Add a neigborhood|Click on the neighbourhood link|A form with the input fields for adding a neighborhood|
|Add a business|Click on the business link|A form with the input fields for adding a business|

## Technologies Used

- Python/Django3
- PostgreSQL

## Known bugs

- The application does not have different role users. It's supposed to have an admin dashboard and user dashboard.

## Contact Information

Email: michael.njoroge@student.moringaschool.com

## License

MIT License
