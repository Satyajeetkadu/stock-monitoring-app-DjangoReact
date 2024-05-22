

This project is a full-stack web application for monitoring stock prices. It allows users to create and manage their own watchlists of stock symbols, view the latest stock values, and delete stocks or entire watchlists. The backend is built with Django and the frontend is built with React.

## Features

- User authentication (login/signup)
- Create and manage watchlists
- Add and delete stock symbols in watchlists
- View latest stock prices
- Responsive and user-friendly interface

## Installation Guidelines

### Backend (Django)

1. **Clone the repository:**
   \`\`\`
   git clone https://github.com/Satyajeetkadu/stock-monitoring-app-DjangoReact.git
   cd stock-monitoring-platform
   \`\`\`

2. **Create a virtual environment:**
   \`\`\`
   python3 -m venv venv
   source venv/bin/activate  # On Windows use \`venv\Scripts\activate\`
   \`\`\`

3. **Install dependencies:**
   \`\`\`
   pip install -r requirements.txt
   \`\`\`

4. **Run database migrations:**
   \`\`\`
   cd stock_monitor
   python3 manage.py migrate
   \`\`\`

5. **Run the Django development server:**
   \`\`\`
   python3 manage.py runserver
   \`\`\`

Keep the server running in this terminal.
### Frontend (React)

1. **Open a new terminal and navigate to the \`frontend\` directory:**
   \`\`\`
   cd frontend
   \`\`\`

2. **Install dependencies:**
   \`\`\`
   npm install
   \`\`\`

3. **Start the React development server:**
   \`\`\`
   npm start
   \`\`\`

### Access the Application

- Open your web browser and go to \`http://localhost:3000\` to view the application.

