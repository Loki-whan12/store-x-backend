# Store-X Backend

The backend for Store-X, an online shopping store built with Flask (Python) for the API and PostgreSQL for the database. This backend handles users, sellers, products, and admin functionalities.

## Table of Contents

- [Technologies](#technologies)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Database Migrations](#database-migrations)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Technologies

- **Framework**: Flask (Python)
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy with Flask-Migrate for database migrations
- **CORS**: Flask-CORS for Cross-Origin Resource Sharing
- **Environment**: dotenv for environment variables
- **Security**: Werkzeug for password hashing

## Project Structure

```
storex_app/
│
├── app/
│   ├── __init__.py        # Initializes Flask app and extensions
│   ├── models/            # Database models (User, Product, Seller, etc.)
│   ├── routes/            # API routes for different entities
│   ├── utils/             # Utility functions, helpers
│   └── config.py          # Configuration settings for the app
│
├── migrations/            # Database migration scripts
├── run.py                 # Entry point for running the app
├── .env                   # Store environment variables
└── requirements.txt       # Python dependencies
```

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/store-x-backend.git
   cd store-x-backend
   ```

2. **Set up a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up PostgreSQL**:

   - Create a PostgreSQL database for the project.
   - Configure the connection settings in your `.env` file.

5. **Create and activate the `.env` file** with necessary environment variables:

   ```
   FLASK_APP=run.py
   FLASK_ENV=development
   SQLALCHEMY_DATABASE_URI=postgresql://username:password@localhost:5432/storex_db
   SECRET_KEY=your_secret_key
   CORS_ORIGINS=*
   ```

## Environment Variables

Ensure the following variables are set in your `.env` file:

- `FLASK_APP`: The Flask app entry point.
- `FLASK_ENV`: The environment (development/production).
- `SQLALCHEMY_DATABASE_URI`: PostgreSQL connection string.
- `SECRET_KEY`: Secret key for sessions and security.
- `CORS_ORIGINS`: Allowed origins for CORS.

## Database Migrations

After setting up your database and making sure your models are defined, follow these steps for database migrations:

1. **Initialize migrations**:

   ```bash
   flask db init
   ```

2. **Create a new migration**:

   ```bash
   flask db migrate -m "Initial migration"
   ```

3. **Apply the migration**:
   ```bash
   flask db upgrade
   ```

## API Endpoints

Here are some example endpoints:

### Users

- **GET** `/api/users/get-all-users`: Get all users.
- **POST** `/api/users`: Create a new user.
- **PUT** `/api/users/<user_id>`: Update a user by ID.
- **DELETE** `/api/users/<user_id>`: Delete a user by ID.

### Sellers

- **GET** `/api/sellers`: Get all sellers.
- **POST** `/api/sellers`: Create a new seller.
- **PUT** `/api/sellers/<seller_id>`: Update seller by ID.
- **DELETE** `/api/sellers/<seller_id>`: Delete a seller by ID.

### Products

- **GET** `/api/products`: Get all products.
- **POST** `/api/products`: Create a new product.
- **PUT** `/api/products/<product_id>`: Update product by ID.
- **DELETE** `/api/products/<product_id>`: Delete product by ID.

### Admins

- **GET** `/api/admins`: Get all admins.
- **POST** `/api/admins`: Create a new admin.
- **PUT** `/api/admins/<admin_id>`: Update admin by ID.
- **DELETE** `/api/admins/<admin_id>`: Delete admin by ID.

## Running the App

Start the Flask app using:

```bash
flask run
```

The app will be available at `http://127.0.0.1:5000`.

## Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature-branch-name`)
3. Commit changes (`git commit -am 'Add a feature'`)
4. Push to the branch (`git push origin feature-branch-name`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License.
