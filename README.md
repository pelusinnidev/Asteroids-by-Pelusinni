# 🎮 Asteroids - A Modern Take on a Classic

Welcome to my reimagined version of the classic Asteroids game! This project was developed as part of my coursework at La Salle Gràcia, where I took the timeless arcade game and gave it a modern twist with enhanced graphics, smooth controls, and exciting new features.

## 🌟 About This Project

This game was born in the classrooms of La Salle Gràcia and has been polished with additional features to make it more enjoyable for everyone. It's not just a school project anymore - it's a labor of love that I want to share with the gaming community. Feel free to play, modify, and improve it!

<div align="center">
  <a href="https://pelusinnidev.craft.me/AsteroidsGame">📝 Development Documentation (Available in Catalan)</a>
</div>

## 🚀 Quick Start

The easiest way to get started is using our setup script:

```bash
# Clone the repository
git clone https://github.com/pelusinnidev/Asteroids-by-Pelusinni.git
cd Asteroids-by-Pelusinni

# Run the setup script
python3 setup.py
```

That's it! The script will automatically:
- Create a virtual environment
- Install all dependencies
- Launch the game

## 💾 MongoDB Configuration (Optional)

The game supports storing high scores in MongoDB. To enable this feature:

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` with your MongoDB settings:
   - For MongoDB Atlas:
     ```
     MONGODB_URI=mongodb+srv://your_username:your_password@your_cluster.mongodb.net/
     MONGODB_DB_NAME=asteroids
     ```
   - For local MongoDB:
     ```
     MONGODB_URI=mongodb://localhost:27017
     MONGODB_DB_NAME=asteroids
     ```

Note: The game will work without MongoDB configuration, storing scores locally for the current session.

## 🎮 Features

- **✨ Smooth Vector Graphics**: Crisp visuals at any resolution, ensuring your spaceship and asteroids look sharp and stylish!
- **🛠 Physics-Based Movement**: Experience realistic momentum and ship controls that make flying an immersive experience.
- **📈 Progressive Difficulty**: Each round ramps up the challenge with more asteroids and faster speeds. Can you keep up?
- **🔢 Round System**: Track your progression with the current round displayed prominently on the screen.
- **🎵 Dynamic Sound System**:
  - 🎶 **Menu Music**: Groove to the beats while navigating the main menu.
  - 🎮 **Game Music**: Intense tracks that keep you pumped during gameplay.
  - 💀 **Game Over Effects**: Hear the sounds of defeat when things get tough.
- **🕹 Multiple Game States**:
  - 🏠 **Main Menu**
  - 🎮 **Gameplay**
  - ⏸ **Pause Menu**
  - 🛑 **Game Over Screen**
  - 🏆 **High Scores Entry**
  
## 🎮 Controls

Take command of your spaceship with ease! Whether you prefer arrow keys or WASD, mastering the controls is a breeze:

- **Movement**: Arrow keys or WASD
  - UP/W: Thrust forward
  - DOWN/S: Thrust backward
  - LEFT/A & RIGHT/D: Rotate ship
- **Actions**:
  - SPACE: Fire
  - ESC: Pause game
  - F11: Toggle fullscreen

## 🎨 Visual Elements

- **🚀 Spaceship**: Sleek vector-based design with a cool thrust animation.
- **🪨 Asteroids**: Procedurally generated with three distinct sizes:
  - **Large**: 40 radius
  - **Medium**: 20 radius
  - **Small**: 10 radius
- **💫 Projectiles**: Light-based shooting effects that leave a trail.
- **🖥 UI Elements**: Clean, arcade-style interface that keeps you informed without clutter.
- **📽 Intro Slides**: Flashing developer and partner logos with smooth fade transitions.

## 🏆 Scoring System

Rack up points by destroying asteroids! Here's how it breaks down:

- **Large Asteroid**: 🥉 20 points
- **Medium Asteroid**: 🥈 50 points
- **Small Asteroid**: 🥇 100 points

## 🔄 Round System

Survive and thrive through multiple rounds, each more challenging than the last!

- **Round Display**: Current round shown on the top-right corner.
- **Asteroid Count**: Increases by 1 each round.
- **Asteroid Speed**: Accelerates by 10% each round, capped at 2x the base speed.
  
**Example Progression**:
- **Round 1**: 3 asteroids at normal speed.
- **Round 5**: 7 asteroids at 1.4x speed.
- **Round 10**: 12 asteroids at 2x speed.
- **Round 15+**: Asteroid count continues to rise while speed remains capped.

## 🛠 Setup and Installation

Get ready to blast off! Follow these simple steps to set up the game on your machine:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/pelusinnidev/Pols-Asteroids.git
    cd Pols-Asteroids
    ```
2. **Create a Virtual Environment**:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```
3. **Install Dependencies**:
    ```bash
    pip3 install -r requirements.txt
    ```
4. **Run the Game**:
    ```bash
    python3 src/main.py
    ```

## 🤝 Contributing

This project is open for improvements! Whether you're fixing bugs, adding new features, or suggesting improvements, your contributions are welcome. Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📫 Contact & Support

- **GitHub Issues**: For bug reports and feature requests
- **Email**: [your.email@example.com](mailto:your.email@example.com)

## 🎓 Academic Context

This project was developed at La Salle Gràcia as part of the programming curriculum. It demonstrates practical applications of:
- Object-Oriented Programming
- Game Development Principles
- Physics Simulation
- User Interface Design

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Created with ❤️ by PelusinniDev**  
**La Salle Gràcia - 2023**

</div>

Check out the project on [GitHub](https://github.com/pelusinnidev/Pols-Asteroids) for more details and updates!