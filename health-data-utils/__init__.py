import csv

def load_libre_view(path):
    """Load a csv with CGM data, downloaded from LibreView"""
    all_data = []
    with open(path, newline='') as csvfile:
        glucose_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for i, row in enumerate(glucose_reader):

            if i in [0, 1]: # skip titles, they are unstructured
                continue

            # from each row, get the values we need
            measure_date = row[1].split(',')[-1]
            measure_time = row[2].split(',')[0]
            measure_qty = row[2].split(',')[2]

            # these are manually added notes, might need them
            notes = row[-1].split(',')
            notes = [n for n in notes if n.isalpha()]

            all_data.append([measure_date, measure_time, measure_qty, notes])

        return pd.DataFrame(all_data, columns=['date', 'time', 'glucose (mmol/L)', 'notes'])