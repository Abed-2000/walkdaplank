<h1 align="center">Man Overboard</h1>

<p align="center">
  <em>Advanced tech for cruise ship safety, rapid detection, and crew alerts in critical situations.</em>
</p>

## 🚀 Quick Start

To get Man Overboard up and running, follow these steps:

### On Swarm Devices

1. Clone this repository on each swarm device.
2. Install the required libraries using `pip install -r libraries.txt`.
3. Configure the settings in the `.env` file for each device.
4. Run the swarm component using `python3 swarm_main.py`.

### On the Crew's Machine (Control Center)

1. Clone this repository on the crew's machine.
2. Install the required libraries using `pip install -r libraries.txt`.
3. Configure the settings in the `.env` file.
4. Run the control center component using `python3 controlCenter.py`.

Now, you can effectively monitor the ship's surroundings in real-time and receive alerts from the swarm!

## 🌊 Inspiration

Man Overboard was inspired by the need to address overboard incidents on cruise ships, a risk to human lives that demanded a swift and effective response. The project aims to ensure passenger and crew safety at sea by providing real-time alerts.

## 🛠️ What it does

Man Overboard continuously monitors the ship's surroundings using computer vision. It detects and tracks potential overboard situations and instantly alerts the ship's crew through real-time communication. The system is versatile and adaptable for various security and safety scenarios.

## 🚧 Challenges Faced

During development, obtaining a live video feed from the swarm of devices and relaying it to the ship's crew in real-time proved to be a significant challenge. Due to time constraints, this challenge couldn't be fully addressed as comprehensively as desired. Future development will focus on enhancing real-time monitoring capabilities.

## 🏆 Accomplishments

- A highly effective overboard detection system.
- A scalable architecture for coordinated swarm configurations.
- A versatile system adaptable for various security and safety applications.

## 🎓 What We Learned

The development of Man Overboard expanded our knowledge in computer vision, real-time communication, and secure configuration management. The project emphasized the importance of adaptability and scalability in safety systems.

## 🔮 What's Next for Man Overboard

The next order of business for Man Overboard is to enable remote live video feed to the crew from the swarm, improving real-time monitoring capabilities. Future plans include:

## 🛠️ Built with

- OpenCV: Real-time image and video processing.
- RabbitMQ: Real-time message queuing for crew alerts.
- dotenv: Secure configuration management.
- Python: The primary programming language for system development.
- ZeroTier: Network virtualization for secure communication.

<hr>

<p align="center">
  <em>⚓️ Safe Seas, Happy Journeys ⚓️</em>
</p>
