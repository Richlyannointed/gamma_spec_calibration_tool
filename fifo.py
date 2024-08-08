"""
file io manager
"""

class USX_Data:
    def __init__(self, filepath):
        self.file = filepath
        self.elapsed_time = None
        self.live_time = None
        self.real_time = None
        self.dead_time = None
        self.counts = None

    pass

def read_usx_csv(filepath):
    """
    populates USX_Data class
    """
    elapsed_time = extract_elapsed_live_time(filename) # For count rate conversion
    if elapsed_time is None:
        return None
    
    skip_rows = 22 # USX Header
    data = []
    with open(filepath, 'r') as file:
        csv_reader = csv.reader(file)
        for _ in range(skip_rows):
            next(csv_reader)  # Skip rows
        for row in csv_reader:
        # Skip the middle column (assuming the array has 3 columns)
            channel = float(row[0]) if row[0] else None
            counts_per_sec = float(row[2]) / elapsed_time if row[2] else None  
            u_counts_per_sec = np.sqrt(counts_per_sec) / elapsed_time if counts_per_sec else None
            data.append((channel, counts_per_sec, u_counts_per_sec))
        
    # Convert list to NumPy array
    try:
        numpy_array = np.array(data).astype(float)
    except TypeError:
        print('Failed to cast data to float')
        return None
    return numpy_array, elapsed_time
    
    pass