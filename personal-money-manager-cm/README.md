# Personal Money Management App

This is a Personal Money Management App designed specifically for students and young professionals in Cameroon. The application aims to help users track their income and expenses, set savings goals, and gain insights into their financial habits.

## Features

- **Manual Income and Expense Tracking**: Users can easily log their income and expenses, categorizing them for better organization.
- **Categorization**: Transactions can be categorized into various types, making it easier to analyze spending habits.
- **Dashboards**: A user-friendly dashboard provides an overview of financial health, including total income, expenses, and balance.
- **Summaries**: Users can view summaries of their financial activities over different periods.
- **Savings Goals**: Users can set and track their savings goals, helping them to save for future needs.
- **Future Integration with MoMo APIs**: The app is designed to integrate with MoMo APIs for seamless transaction imports in the future.

## Project Structure

The project is divided into two main parts: the backend and the frontend.

### Backend

The backend is built using FastAPI and includes:

- API endpoints for managing transactions, users, and savings goals.
- Database models and schemas for transactions and users.
- CRUD operations for database interactions.
- Services for business logic and future integrations.

### Frontend

The frontend is built using React and TypeScript, featuring:

- A responsive user interface with pages for dashboard, transactions, adding transactions, and savings goals.
- Components for displaying transaction lists, forms, and summary cards.
- Services for making API calls to the backend.

## Getting Started

### Prerequisites

- Python 3.x
- Node.js and npm
- Docker (optional)

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd personal-money-manager-cm
   ```

2. Set up the backend:
   - Navigate to the `backend` directory.
   - Install the required Python packages:
     ```
     pip install -r requirements.txt
     ```

3. Set up the frontend:
   - Navigate to the `frontend` directory.
   - Install the required Node packages:
     ```
     npm install
     ```

4. Configure environment variables:
   - Copy `.env.example` to `.env` and update the values as needed.

5. Run the application:
   - For the backend:
     ```
     uvicorn app.main:app --reload
     ```
   - For the frontend:
     ```
     npm start
     ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.