import time
import random

# Simulate a Veltrix-like data store with potential for decay
class VeltrixDataStore:
    def __init__(self):
        self.data = {}

    def add_record(self, key, value):
        # Simulate adding a record with a timestamp
        self.data[key] = {
            'value': value,
            'timestamp': time.time()
        }
        print(f"Added record: {key} = {value}")

    def get_record(self, key):
        if key in self.data:
            return self.data[key]
        return None

    def simulate_decay(self, decay_probability=0.1, age_threshold=10):
        # Simulate data decay: records older than age_threshold have a chance to become 'corrupted'
        keys_to_remove = []
        for key, record in self.data.items():
            age = time.time() - record['timestamp']
            if age > age_threshold and random.random() < decay_probability:
                print(f"Simulating decay for record: {key} (age: {age:.2f}s)")
                # In a real scenario, this might involve data corruption, loss of integrity, etc.
                # Here, we'll simulate it by marking it for removal or alteration.
                self.data[key]['value'] = "<DECAYED>"
                # Or, for a more drastic simulation, remove it:
                # keys_to_remove.append(key)
        # for key in keys_to_remove:
        #     del self.data[key]

    def get_valid_records(self, max_age):
        # Strategy 1: Data Validation and Pruning
        # Periodically check and remove or flag records that are too old or corrupted.
        valid_data = {}
        current_time = time.time()
        for key, record in self.data.items():
            if record.get('value') != "<DECAYED>" and (current_time - record['timestamp']) < max_age:
                valid_data[key] = record['value']
        return valid_data

    def get_all_records(self):
        # For demonstration, show all records including potentially decayed ones
        return self.data

# --- Main Simulation ---

store = VeltrixDataStore()

# Add some initial data
store.add_record("user_session_123", "active")
store.add_record("config_setting_abc", "enabled")

time.sleep(2) # Wait a bit

# Simulate some data decay
print("\n--- Simulating Decay ---")
store.simulate_decay(decay_probability=0.5, age_threshold=1)

print("\n--- Current Data State ---")
print(store.get_all_records())

# Apply a data management strategy: Keep records younger than 5 seconds
print("\n--- Applying Data Validation Strategy (Max Age: 5s) ---")
valid_data = store.get_valid_records(max_age=5)
print("Valid Records:", valid_data)

# Add more data and let it age
print("\n--- Adding More Data and Waiting ---")
store.add_record("event_log_xyz", "processed")
time.sleep(6) # Wait for data to age

print("\n--- Re-applying Data Validation Strategy (Max Age: 5s) ---")
valid_data_after_wait = store.get_valid_records(max_age=5)
print("Valid Records After Wait:", valid_data_after_wait)

print("\n--- Final Data State (Including Decayed) ---")
print(store.get_all_records())
