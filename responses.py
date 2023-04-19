def handle_response(message) -> str:
    mess = message.lower()
    
    if mess == 'check':
        return 'Initiating Ready Check'
    
    if mess == 'ready':
        return 'X is ready'
