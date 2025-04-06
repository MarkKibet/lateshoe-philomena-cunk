# The Late Night Show by Philomena Cunk

Welcome to **The Late Night Show by Philomena Cunk**, the web app that gives you all the excitement of a talk show without the inconvenience of actual celebrities refusing to attend. Here, you can manage and explore guests, episodes, and appearances, with just the right amount of chaos and charm.
 
## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [File Structure](#file-structure)
- [Key Functionalities](#key-functionalities)
- [Future Improvements](#future-improvements)

---

## Features
1. **Dynamic Guest List**:
   - View all the guests and their details dynamically.
   - Clicking on a guest leads to their personal details, including a humorous reason for their participation.

2. **Episode Management**:
   - List all episodes and their details, with plans to extend functionality to include CRUD (Create, Read, Update, Delete) operations.

3. **Appearances**:
   - Track appearances of guests on episodes with ratings.

4. **Humorous Guest Details**:
   - A fun twist where each guest's profile includes a funny reason explaining why they are part of the meeting.

5. **Background Video and Stylish Design**:
   - Features a background video on the landing page and an elegant user interface with a smooth, curved design for the hero section.

---

## Technologies Used
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS (with Google Fonts)
- **Database**: SQLite (managed via SQLAlchemy)
- **Video and Media**: MP4 and WebM for background videos
- **Other Libraries**:
  - Flask-Migrate for database migrations
  - SQLAlchemy ORM for database management

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  

```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up the Database
Run the `seed.py` file to populate the database with initial data (guests, episodes, and appearances):
```bash
python seed.py
```

### 5. Start the Flask Application
```bash
python app.py
```
By default, the app will run on `http://localhost:5555`.

### 6. Test in the Browser
Open your browser and visit `http://localhost:5555` to explore the app.

---

## File Structure
```
late-show-codechallenge/
├── app.py                 
├── models.py            
├── seed.py                
├── templates/
│   ├── index.html         
│   ├── guests.html       
│   ├── guest_details.html 
├── static/
│   ├── css/
│   │   └── styles.css     
│   ├── videos/
│   │   └── background.mp4 
│   ├── js/
│       └── scripts.js         
└── README.md             
```

---

## Key Functionalities

### 1. Landing Page
The homepage features:
- A sleek design with a **background video**.
- A button to navigate to the **Guest List**.

### 2. Guest List
- Displays a list of all guests with their names and occupations.
- Clicking a guest's name links to their detailed page.

### 3. Guest Details
- Provides detailed information about a guest, including:
  - Their name and occupation.
  - A reason for their attendance.

### 4. Episodes and Appearances
- View and manage episodes and guest appearances, complete with ratings.

---

## Future Improvements
- **Search and Filter**:
  - Enable searching for guests or filtering by occupation or ratings.
---
