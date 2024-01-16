# Flask-Based Twitter Clone with Live chatting 

## Description

This project is a web-based social media and chat application built using Flask, a Python web framework, and Flask-SocketIO for real-time communications. It provides a platform for users to sign in, create and view tweets, and engage in live chat sessions. The application integrates social media functionalities with real-time chat capabilities to offer a comprehensive user experience.

## Key Features

1. **User Authentication**: Supports user sign-in and sign-up with credential verification and account creation.
2. **Session Management**: Utilizes session handling for security and enhanced user experience.
3. **Tweet Generation and Display**: Allows users to create and view tweets, with a `tweet_generator` module for tweet management.
4. **Real-Time Chat**: Implements Flask-SocketIO for live chat functionalities, including joining chat rooms and sending messages.
5. **Profile and Content Management**: Manages user profiles and content, displaying user-generated tweets on an explore page.
6. **Dynamic Web Pages**: Uses Flask's `render_template` for serving dynamic web content.

## Technical Stack

- **Flask**: Python web application framework.
- **Flask-SocketIO**: For real-time communications between web clients and servers.
- **Python**: Backend programming language.
- **HTML/CSS**: Frontend development and design.
- **JavaScript**: Enhances frontend interactivity, particularly for real-time chat.

## Modules

- `db`: Handles database operations, including user authentication and data retrieval.
- `tweet_generator`: Generates and manages tweet content.

## Setup and Running

- Utilizes a secret key from `keys/app_secret_key.txt` for session management.
- Configured with debug mode on for development.
- Runs using SocketIO to support real-time web sockets.

## Usage

Ideal for users interested in social media and real-time chatting, and as a learning resource for integrating Flask with technologies like SocketIO. Suitable for developers building a social media platform prototype.

#### Enhanced Visual Experience


# Images of website live 
<img width="1300" alt="Screen Shot 2024-01-15 at 7 11 13 PM" src="https://github.com/esohel30/TwitterClone/assets/90656205/0f38cd3e-7614-4183-94c8-8f59894ad87f">
<img width="1300" alt="Screen Shot 2024-01-15 at 6 25 49 PM" src="https://github.com/esohel30/TwitterClone/assets/90656205/7a4adbbf-e0cd-4783-b3b0-fcf6fe0a825e">
<img width="1300" alt="Screen Shot 2024-01-15 at 6 40 28 PM" src="https://github.com/esohel30/TwitterClone/assets/90656205/639d12f9-6193-4e79-9241-4a51df931a16">

#### Installation Guide

1. Clone the Repository: 
   `git clone git@github.com:esohel30/Twitter_clone.git`
2. Navigate to the Project: 
   `cd FinalProjectSoftDev`
3. Install Dependencies: 
   `pip install -r requirements.txt`
4. Enter the Application Directory: 
   `cd app`
5. Launch the Application: 
   `python3 __init.py__`

Project for Stuyvesant Software development Class 
