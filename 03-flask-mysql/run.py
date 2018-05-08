from app import app

# function to be called first
if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )