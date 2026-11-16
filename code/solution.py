
# Bahareh Nojan - Assignment 4

def check_session(idle_minutes, max_idle=30):
    # TODO: Evaluate idle time against max_idle threshold
    # Note: Check the default parameter value above against the system requirement
    if idle_minutes >= max_idle:
        return "SESSION_EXPIRED"
    return "SESSION_ACTIVE"
