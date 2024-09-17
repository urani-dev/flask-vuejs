# Flask & Vue.js (Vite) Project

This project uses Flask for the backend and Vue.js (with Vite) for the frontend. Below are the instructions to start development and production builds.

## Prerequisites

- Python 3.x
- Node.js (with npm)

## Getting Started

### 1. Backend Setup

1. Install the required Python packages:

    ```bash
    pip3 install -r requirements.txt
    ```

2. Run the Flask server in development mode:

    ```bash
    flask --debug run
    ```

### 2. Frontend Setup

1. Navigate to the `frontend` folder:

    ```bash
    cd frontend
    ```

2. Install the frontend dependencies:

    ```bash
    npm install
    ```

3. Start the frontend development server:

    ```bash
    npm run dev
    ```

    The frontend will now be served by Vite on its local development server.

## Production Build

### 1. Frontend

To build the frontend for production, run:

```bash
npm run build
```

This will generate the production files in the dist folder inside the frontend directory.

### 2. Backend

To run the Flask server in production mode:

```bash
flask run
```
