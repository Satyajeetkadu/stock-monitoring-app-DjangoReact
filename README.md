

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


## If you want to Deploy here are the Steps

### Backend (Django) Deployment on Heroku

1. **Set up a Heroku account:**
   - Sign up for a free account at [Heroku](https://www.heroku.com/).

2. **Install the Heroku CLI:**
   - Follow the instructions at [Heroku CLI Installation](https://devcenter.heroku.com/articles/heroku-cli) to install the Heroku CLI on your system.

3. **Create a new Heroku app:**
   - Use the Heroku CLI to create a new app for your Django backend.

4. **Configure environment variables:**
   - Set environment variables such as `SECRET_KEY` and `DATABASE_URL` on Heroku.

5. **Add Heroku as a Git remote:**
   - Connect your local Git repository to the Heroku app.

6. **Deploy the app:**
   - Push your code to Heroku to deploy the Django backend.

7. **Run database migrations:**
   - Run the necessary Django management commands to apply database migrations on Heroku.

### Frontend (React) Deployment on Netlify

1. **Set up a Netlify account:**
   - Sign up for a free account at [Netlify](https://www.netlify.com/).

2. **Create a new site from Git:**
   - Connect your Git repository containing the React frontend to Netlify.

3. **Configure build settings:**
   - Set the build command to `npm run build` and the publish directory to `frontend/build`.

4. **Deploy the site:**
   - Trigger the deployment to build and host the React frontend on Netlify.

5. **Update API URLs:**
   - Ensure that the React app's API URLs point to the Heroku backend.

### Optional: Configure Custom Domain

1. **Set up a custom domain:**
   - Add a custom domain to your Netlify site via the "Domain settings" page.

2. **Update DNS settings:**
   - Configure your domain's DNS settings to point to Netlify, following the instructions provided by Netlify.

### Additional Notes

- **CORS Configuration:**
  - Ensure that your Django backend allows requests from your Netlify domain by configuring CORS settings.

- **Environment Variables:**
  - Make sure all necessary environment variables are set correctly on both Heroku and Netlify.

Follow these steps to deploy your full-stack web application, ensuring both the backend and frontend are properly set up and connected.

