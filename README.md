# **Pandemic Simulation with Graphs**  

This project simulates the spread of an infectious disease within a population, considering various factors such as age, mask-wearing, family interactions, and daily activities. The simulation runs for 50 days and visualizes the results using **Matplotlib**.

## **Features**  
- Simulates disease spread among **1,000,000** individuals.  
- Categorizes individuals into **children, adults, and seniors** with different infection probabilities.  
- Factors in **mask-wearing** to reduce infection risk.  
- Simulates **family-based infections** and random social interactions.  
- Tracks **hospitalizations, recoveries, and deaths** over time.  
- **User input options** for enforcing mask-wearing and travel restrictions.  
- Generates **graphs** to visualize the spread of infection, hospitalizations, recoveries, and deaths over 50 days.  

## **Installation**  
To run this simulation, ensure you have **Python 3.x** installed along with the required dependencies.  

Install **Matplotlib** if you haven’t already:  
```bash
pip install matplotlib
```

## **Usage**  
1. Clone this repository:  
   ```bash
   git clone https://github.com/UdithaPJ/Pandemic-Simulation-with-Graphs.git
   cd Pandemic-Simulation-with-Graphs
   ```
2. Run the simulation:  
   ```bash
   python main.py
   ```
3. Follow the prompts to **enforce mask-wearing** and **apply travel restrictions**.  

## **Visualization**  
At the end of the simulation, graphs will be displayed to show trends over 50 days:  
- **Daily infections**  
- **Daily hospitalizations**  
- **Daily recoveries**  
- **Daily deaths**  

## **Code Structure**  
- **Person Class**: Represents an individual with age type, mask-wearing status, and infection probability.  
- **Family Class**: Groups individuals into families to simulate household infections.  
- **Population Class**: Manages the overall population, tracks statistics, and simulates disease spread.  
- **Graphing Functions**: Uses Matplotlib to visualize infection trends over time.  

## **Example Output**  
Sample statistics displayed during simulation:  
```
Day 10
Total Infected: 5000
Total Hospitalized: 3000
Total Recovered: 1200
Total Deaths: 200
```

## **License**  
This project is licensed under the MIT License.
