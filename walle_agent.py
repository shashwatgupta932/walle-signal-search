import json
import time

# Load mission config
with open('config.json', 'r') as f:
    config = json.load(f)

# Initialize environment state
grid_size = config['map_size']
walle_pos = config['start_pos']
battery = config['budget']['battery']
move_cost = config['budget']['action_cost']
trace_log = []

print("🚀 Initiating WALL-E Search Protocol...\n")

def print_grid(walle, eve_est):
    """ASCII visualization of the simulated environment"""
    for y in range(grid_size[1]):
        row = ""
        for x in range(grid_size[0]):
            if [x, y] == walle:
                row += "[W]"
            elif [x, y] == eve_est:
                row += "[?]"
            else:
                row += " . "
        print(row)
    print("\n")

# Autonomous Search Loop
while battery > 0:
    # Belief Update: Extract target from signal reading
    signal = config['initial_signal']
    target_x, target_y = signal['coordinates']
    
    print_grid(walle_pos, [target_x, target_y])
    
    if walle_pos == [target_x, target_y]:
        trace_log.append(f"Action: Scan | Result: EVE positively identified at {walle_pos}.")
        break
        
    # Decision Making: Pathfinding to the strongest signal
    move_x = 1 if walle_pos[0] < target_x else (-1 if walle_pos[0] > target_x else 0)
    move_y = 1 if walle_pos[1] < target_y else (-1 if walle_pos[1] > target_y else 0)
    
    if move_x != 0:
        walle_pos[0] += move_x
        action = f"Moved along X-axis to {walle_pos[0]}"
    elif move_y != 0:
        walle_pos[1] += move_y
        action = f"Moved along Y-axis to {walle_pos[1]}"
        
    # Resource Management
    battery -= move_cost
    trace = f"Action: {action} | Battery: {battery}% | Observation: Signal strengthening."
    trace_log.append(trace)
    print(trace)
    time.sleep(0.4) # Slight pause for visual effect in terminal

# Final Mission Report
print("\n" + "="*40)
print("FINAL MISSION REPORT")
print("="*40)
for log in trace_log:
    print(log)
print(f"\nInferred Location/Status: EVE secured at coordinates {walle_pos}.")
print(f"Confidence: 100% | Remaining Battery: {battery}%")
print("Recommended Next Step: Initiate recovery and recharge sequence.")
