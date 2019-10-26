# hiwhatsyourna.me

## Inspiration
One of the hardest things to do when a new school year starts is making friends. The best way to make friends is to talk to others in your dorm hall, but sometimes it can be difficult to start a conversation. hiwhatsyourna.me is a way to get an idea of what you and your neighbors have in common, which in turn allows you to "break the ice" easier and initiate a conversation!

## What it does
hiwhatsyourna.me is a web app that gets user input in the form of a name, age, gender, an 'about me' section, and social media handles. It then gives the user a QR code that they can print out and put on their door. Once someone scans the QR code, it directs them to an automatically generated 'mini-profile' of the user.

## How we built it
We wrote hiwhatsyourna.me in Python, using the Flask web framework combined with an SQL Alchemy database. The web app is hosted using Google Cloud's App Engine.

## How it works
Once the user inputs their information, we generate a hash value for the entry (we just used random()). This hash value is unique for each entry and is how we identify the entry when storing and retrieving the information from our database. We also use this hash value when we generate a QR code, where the QR code links to the dynamically created web page hiwhatsyourna.me/page/<hash value>. Once someone scans the QR code, we query the database for the information associated with the hash value and generate a user profile.

## Challenges we ran into
One challenge we ran into was how we would dynamically generate web pages, and how we would route them. We spent some time brainstorming ideas and we came up with the idea of generating a hash value of some sorts for each entry, and to use this hash value for routing a new web page.

## Accomplishments that we're proud of
We are proud of creating a web app that we can see being implemented on college campuses the next coming school year.

## What we learned
We learned how to implement a web app using Flask as well as how to implement a simple database using SQL Alchemy. We learned a lot about web app development in general, especially how painful it was to get our Google Cloud host working for the first time...
