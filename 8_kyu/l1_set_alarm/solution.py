def set_alarm(employed, vacation):
    if employed and vacation:
        return False
    elif employed and not vacation:
        return True
    elif not employed and vacation:
        return False
    else:
        return False