def lambda_handler(event,context):
    """
    Lambda Handler function for the download_members module
    """
    print("IM ALIVE!! LAMBDA TRIGGERED BY EVENTBRIDGE")
    print('event: ', event)
    print('context: ', context)