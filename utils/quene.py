import multiprocessing

# Erstelle die Queue
email_queue = multiprocessing.Queue()

# Funktion, um die Größe der Queue anzuzeigen
def get_queue_size():
    return email_queue.qsize()