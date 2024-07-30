import multiprocessing

# Erstelle die Queue
email_queue = multiprocessing.Queue()

# Funktion, um die Größe der Queue anzuzeigen
def get_email_queue_size():
    return email_queue.qsize()

# Erstelle die Queue
search_obj_queue = multiprocessing.Queue()

# Funktion, um die Größe der Queue anzuzeigen
def get_search_obj_queue_size():
    return search_obj_queue.qsize()

# Erstelle die Queue
question_vector_queue = multiprocessing.Queue()

# Funktion, um die Größe der Queue anzuzeigen
def get_question_vector_queue_size():
    return question_vector_queue.qsize()