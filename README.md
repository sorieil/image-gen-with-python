# Generate Image: Nature Scene Drawing

This project generates a simple nature scene using Python's `matplotlib` library. The scene includes mountains, a sun, a tree, and a cloud, all drawn using geometric shapes.

## Features

- Draws a nature scene with:
  - Two mountains
  - A sun
  - A tree (trunk and leaves)
  - A cloud
- Uses `matplotlib` for visualization.
- Customizable styles and layout.

## Prerequisites

- Python 3.7 or higher
- `matplotlib` and other dependencies listed in `requirements.txt`

## Setup Instructions

1. Clone the repository or download the project files.
2. Open a terminal and navigate to the project directory.
3. Run the setup script to create a virtual environment and install dependencies:

   ```bash
   bash setup_env.sh
   ```

## Running the Project

1. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

2. Run the main script to generate the nature scene:

   ```bash
   python main.py
   ```

3. The script will display the nature scene in a pop-up window.

## Project Structure

- `main.py`: Contains the code to draw the nature scene.
- `setup_env.sh`: Script to set up the virtual environment and install dependencies.
- `requirements.txt`: Lists the required Python packages and their versions.

## Example Output

The generated nature scene includes:

- Two triangular mountains
- A circular sun
- A rectangular tree trunk with triangular leaves
- An elliptical cloud

## Notes

- Ensure that `matplotlib` is installed correctly to avoid runtime errors.
- You can modify the shapes and styles in `main.py` to customize the scene.
