# NATABOARDS - Final Project CS50

## Video Demo: https://youtu.be/bQwpvN5TBos

## Description

**NataBoards** is a web-based task management application inspired by tools like Padlet and Trello. It allows users to create personalized boards, organize them into columns (categories), and add cards (items) containing either text or images.

### Key Features:

* **Dynamic Boards**: Create and delete multiple boards from a central dashboard.
* **Horizontal Layout**: Columns are organized horizontally with a custom scrollbar for better navigation.
* **Rich Content**: Items support **Markdown** formatting for text (bold, lists, links) and can display images via URLs.
* **Full CRUD**: Users can Create, Read, Update, and Delete boards, columns, and items.

---

## Files and Structure

### `app.py`

The heart of the application. It manages Flask routes and database interactions. It is organized into clear sections:

* **Configuration**: Initializing Flask, SQLite3, and Markdown filters.
* **Navigation**: Routes for the index and specific board views.
* **Management**: Specialized routes for adding, updating, and removing data.

### `nataboards.db`

A SQLite database containing three main tables:

1. `boards`: Stores the name and ID of each project.
2. `columns`: Stores column names, IDs, numerical `position`, color, and the parent `board_id`.
3. `items`: Stores content (text/URL), titles, position, color, type (text/image), and the parent `column_id`.

### `static/styles.css`

Contains all custom styling. Key implementations include:

* **Flexbox & Grid**: Used for the board layout and horizontal column scrolling.
* **Sticky Footer**: Ensures the footer stays at the bottom regardless of content length.
* **Custom Scrollbar**: Tailored to match the application's color palette for a cohesive UI.

### Templates (`templates/`)

* `layout.html`: The base template containing the navbar and footer.
* `index.html`: The dashboard displaying all available boards.
* `board.html`: The main workspace displaying columns and items for a specific board.

---

## Roadmap / Soon...

* **Multi-user integration**: User accounts and private boards.
* **Drag & Drop**: Ability to modify the position of elements manually.
* **Enhanced Styling**: UI to modify the color of elements directly from the interface.
* **Customization**: More personalization options!

## Installation

To run this project locally:

1. Install dependencies:
`pip install flask cs50 markdown`
2. Run the Flask app:
`flask run`

---

© 2025 Nathan | Built for CS50 Final Project.

**GitHub**: [NathanSNB68](https://www.google.com/search?q=https://github.com/NathanSNB68)

**Contact**: natsnb68@gmail.com

*Thanks to the CS50 staff for this amazing experience. I learned a lot and I am excited to keep learning!*
