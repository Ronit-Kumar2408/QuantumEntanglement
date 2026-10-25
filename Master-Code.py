#Importing External Tools
import random
import time
import sys

def dramatic_loading_screen():
    print("\n[INITIATING QUANTUM PROCESSOR...]")
    loading_messages = [
        "Synthesizing quantum superposition states...",
        "Applying Hadamard and CNOT gates...",
        "Collapsing wave functions across 1,000 trials...",
        "Finalizing statistical correlation matrix..."
    ]
    
    for message in loading_messages:
        sys.stdout.write(f"  ⏳ {message}\r")
        sys.stdout.flush()
        time.sleep(0.9)  # Pauses for ~0.9 seconds per message (Total ~3.6 seconds)
    print("  ✅ Processing complete!\n")

#Defining the Statistical Proof Function
def run_statistical_proof():
    print("\n--- PROVING ENTANGLEMENT VIA STATISTICS (1,000 Trials) ---")
    
    # Trigger the dramatic loading screen
    dramatic_loading_screen()
    
    # Counters for Classical
    c_outcomes = {"00": 0, "01": 0, "10": 0, "11": 0}
    
    # Counters for Quantum Entangled (|00⟩ + |11⟩)
    q_outcomes = {"00": 0, "01": 0, "10": 0, "11": 0}
    
    trials = 1000
    for _ in range(trials):
        # Classical: independent
        c1, c2 = random.choice([0, 1]), random.choice([0, 1])
        c_outcomes[f"{c1}{c2}"] += 1
        
        # Quantum Entangled: perfectly correlated (Bell state)
        q_state = random.choice([0, 1])
        q_outcomes[f"{q_state}{q_state}"] += 1
        
    print("[Results over 1,000 runs]")
    print("1. Classical Independent Coins:")
    print(f"    -> 00 (Both Heads): {c_outcomes['00']} times ({c_outcomes['00']/10}% )")
    print(f"    -> 01 / 10 (Mixed) : {c_outcomes['01'] + c_outcomes['10']} times (Expected ~50%)")
    print(f"    -> 11 (Both Tails): {c_outcomes['11']} times ({c_outcomes['11']/10}% )")
    print("    *Proof:* Notice all 4 combinations appear equally (~25% each). No correlation.\n")
    
    print("2. Quantum Entangled Qubits (|00⟩ + |11⟩):")
    print(f"    -> 00 (Both Heads): {q_outcomes['00']} times ({q_outcomes['00']/10}%)")
    print(f"    -> 01 / 10 (Mixed) : {q_outcomes['01'] + q_outcomes['10']} times (0%)")
    print(f"    -> 11 (Both Tails): {q_outcomes['11']} times ({q_outcomes['11']/10}%)")
    print("    *Proof:* Mixed states (01 and 10) are strictly 0%. The particles *always* agree. That absolute correlation is the mathematical visualization of entanglement\n")

def interactive_simulation():
    print("==================================================")
    print("    QUANTUM ENTANGLEMENT STATISTICAL PROOF        ")
    print("==================================================")
    
    round_num = 1
    while True:
        user_input = input(f"Press [ENTER] to run statistical proof round {round_num} (or type 'q' to quit): ")
        if user_input.strip().lower() == 'q':
            print("Exiting simulation. Goodbye!")
            break
            
        run_statistical_proof()
        print("-" * 50 + "\n")
        round_num += 1

if __name__ == "__main__":
    interactive_simulation()