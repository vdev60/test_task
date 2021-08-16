import application
data = application.get_data()
current_element = application.return_current_element(data)

def lambda_handler(event, context):
    return f"{next(current_element)}"
